-- Restrição de Integridade (RI-1)
-- Stored Procedure: Check Employee Age
ALTER TABLE employee
    ADD CONSTRAINT check_employee_age
        CHECK (DATE_PART('YEAR', CURRENT_DATE) - DATE_PART('YEAR', bdate) >= 18);

-- MUDARRRRRRR
-- Restrição de Integridade (RI-2)
-- Stored Procedure: Check Workplace Type Constraint
CREATE OR REPLACE FUNCTION check_workplace_type()
RETURNS TRIGGER AS $$
DECLARE
    office_count INTEGER;
    warehouse_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO office_count FROM office WHERE address = NEW.address;
    SELECT COUNT(*) INTO warehouse_count FROM warehouse WHERE address = NEW.address;

    IF (office_count > 0 AND warehouse_count > 0) THEN
        RAISE EXCEPTION 'A workplace cannot be both an office and a warehouse.';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger: Enforce Workplace Type Constraint for Office table
DROP TRIGGER IF EXISTS enforce_workplace_type ON office;
CREATE TRIGGER enforce_workplace_type
BEFORE INSERT OR UPDATE ON office
FOR EACH ROW
EXECUTE FUNCTION check_workplace_type();

-- Trigger: Enforce Workplace Type Constraint for Warehouse table
DROP TRIGGER IF EXISTS enforce_workplace_type ON warehouse;
CREATE TRIGGER enforce_workplace_type
BEFORE INSERT OR UPDATE ON warehouse
FOR EACH ROW
EXECUTE FUNCTION check_workplace_type();

-- Restrição de Integridade (RI-3)
-- Stored Procedure: Check Order in Contains Constraint
CREATE OR REPLACE FUNCTION check_order_in_contains()
RETURNS TRIGGER AS $$
BEGIN
  IF NOT EXISTS(SELECT 1 FROM contains WHERE order_no = NEW.order_no) THEN
    RAISE EXCEPTION 'An order must appear in the Contains table.';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger: Enforce Order in Contains Constraint
DROP TRIGGER IF EXISTS enforce_order_in_contains ON orders;
CREATE CONSTRAINT TRIGGER enforce_order_in_contains
AFTER INSERT OR UPDATE ON orders DEFERRABLE
FOR EACH ROW
EXECUTE FUNCTION check_order_in_contains();
