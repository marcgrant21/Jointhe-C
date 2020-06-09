-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema jointh-C
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema jointh-C
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `jointh-C` DEFAULT CHARACTER SET utf8 ;
USE `jointh-C` ;

-- -----------------------------------------------------
-- Table `jointh-C`.`Parents`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `jointh-C`.`Parents` (
  `Parents_id` INT NOT NULL,
  `Parents_FirstName` VARCHAR(45) NULL,
  `Parents_LastName` VARCHAR(45) NULL,
  `Parents_Address1` VARCHAR(45) NULL,
  `Parents_Address2` VARCHAR(45) NULL,
  `Parents_Telephone` INT NULL,
  `Parents_Email` VARCHAR(45) NULL,
  PRIMARY KEY (`Parents_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `jointh-C`.`Event`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `jointh-C`.`Event` (
  `Event_id` INT NOT NULL,
  `Event_Name` VARCHAR(45) NULL,
  `Event_time` VARCHAR(45) NULL,
  `Event_Date` DATETIME NULL,
  PRIMARY KEY (`Event_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `jointh-C`.`Children`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `jointh-C`.`Children` (
  `Children_id` INT NOT NULL,
  `Parents_Id` INT NULL,
  `Event_Id` INT NULL,
  `Children_FirstName` VARCHAR(45) NULL,
  `Children_DOB` DATETIME NULL,
  `Children_Attend` INT NULL,
  `Children_sex` VARCHAR(45) NULL,
  PRIMARY KEY (`Children_id`),
  INDEX `fk_Children_Parents_idx` (`Parents_Id` ASC) VISIBLE,
  INDEX `fk_Children_Event1_idx` (`Event_Id` ASC) VISIBLE,
  CONSTRAINT `fk_Children_Parents`
    FOREIGN KEY (`Parents_Id`)
    REFERENCES `jointh-C`.`Parents` (`Parents_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Children_Event1`
    FOREIGN KEY (`Event_Id`)
    REFERENCES `jointh-C`.`Event` (`Event_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `jointh-C`.`Employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `jointh-C`.`Employee` (
  `Employee_id` INT NOT NULL,
  `Event_Event_id` INT NOT NULL,
  `Child_Id` INT NULL,
  `Employee_FirstName` VARCHAR(45) NULL,
  `Employee_LastName` VARCHAR(45) NULL,
  `Employee_Address1` VARCHAR(45) NULL,
  `Employee_Address2` VARCHAR(45) NULL,
  `Employee_Telephone` INT NULL,
  `Employee_Email` VARCHAR(45) NULL,
  PRIMARY KEY (`Employee_id`, `Event_Event_id`),
  INDEX `fk_Employee_Event1_idx` (`Event_Event_id` ASC) VISIBLE,
  INDEX `fk_Employee_Children1_idx` (`Child_Id` ASC) VISIBLE,
  CONSTRAINT `fk_Employee_Event1`
    FOREIGN KEY (`Event_Event_id`)
    REFERENCES `jointh-C`.`Event` (`Event_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Employee_Children1`
    FOREIGN KEY (`Child_Id`)
    REFERENCES `jointh-C`.`Children` (`Children_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `jointh-C`.`Saving`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `jointh-C`.`Saving` (
  `Saving_id` INT NOT NULL,
  `Children_Children_id` INT NOT NULL,
  `Saving_Amount` INT NULL,
  PRIMARY KEY (`Saving_id`, `Children_Children_id`),
  INDEX `fk_Saving_Children1_idx` (`Children_Children_id` ASC) VISIBLE,
  CONSTRAINT `fk_Saving_Children1`
    FOREIGN KEY (`Children_Children_id`)
    REFERENCES `jointh-C`.`Children` (`Children_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
