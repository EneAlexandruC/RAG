CREATE TABLE "Users" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "email" varchar,
  "password" varchar
);

CREATE TABLE "Documents" (
  "user_id" integer,
  "title" varchar,
  "path" varchar,
  "category" varchar
);

CREATE TABLE "Conversations" (
  "user_id" integer,
  "document_ids" varchar,
  "question" varchar,
  "answer" varchar,
  "timestamp" varchar
);

ALTER TABLE "Documents" ADD FOREIGN KEY ("user_id") REFERENCES "Users" ("id");

ALTER TABLE "Conversations" ADD FOREIGN KEY ("user_id") REFERENCES "Users" ("id");
