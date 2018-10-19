-- Exported from QuickDBD: https://www.quickdatatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/schema/T7EDFUogV0qy-0k9LrXWUA
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).
CREATE SCHEMA organizer_fiuba
CREATE DATABASE


CREATE TABLE "course" (
    "id" int   NOT NULL,
    "name" varchar(256)   NOT NULL,
    "professor_id" int   NOT NULL,
    "subject_id" int   NOT NULL,
    "classroom" varchar(256)   NULL,
    "day" varchar(256)   NOT NULL,
    "time" int   NOT NULL,
    "type" varchar(256)   NOT NULL,
    CONSTRAINT "pk_course" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "professor" (
    "id" int   NOT NULL,
    "name" money   NOT NULL,
    CONSTRAINT "pk_professor" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "subject" (
    "id" int   NOT NULL,
    "code" int   NOT NULL,
    "name" varchar(256)   NOT NULL,
    CONSTRAINT "pk_subject" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "course" ADD CONSTRAINT "fk_course_professor_id" FOREIGN KEY("professor_id")
REFERENCES "professor" ("id");

ALTER TABLE "course" ADD CONSTRAINT "fk_course_subject_id" FOREIGN KEY("subject_id")
REFERENCES "subject" ("id");

CREATE INDEX "idx_course_name"
ON "course" ("name");


