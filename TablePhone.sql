CREATE TABLE `heroku_d1afa11f42e01ce`.`phones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `phone` VARCHAR(10) NOT NULL,
  `random` VARCHAR(10) NOT NULL,
  `datetime` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `phone_UNIQUE` (`phone` ASC),
  UNIQUE INDEX `random_UNIQUE` (`random` ASC));