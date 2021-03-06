-- create staging table for full load
CREATE TABLE stg_full_covid (
	id SERIAL PRIMARY KEY,
	csv_row BIGINT,
	data_as_of TIMESTAMP,
	start_date TIMESTAMP,
	end_date TIMESTAMP,
	data_group VARCHAR(8),
	us_state VARCHAR(13),
	sex VARCHAR(9),
	age_group VARCHAR(17),
	covid_19_deaths BIGINT NULL,
	total_deaths BIGINT NULL,
	pneumonia_deaths BIGINT NULL,
	pneumonia_and_covid_19_deaths BIGINT NULL,
	influenza_deaths BIGINT NULL,
	pneumonia_influenza_or_covid BIGINT NULL,
	footnote TEXT NULL,
	case_year INT NULL,
	case_month INT NULL
);
