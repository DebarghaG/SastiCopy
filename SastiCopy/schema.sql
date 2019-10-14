DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS product;

CREATE TABLE user(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
);

CREATE TABLE product(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  category INTEGER NOT NULL,
  code TEXT NOT NULL,
  name TEXT NOT NULL,
  image TEXT NOT NULL,
  describe TEXT NOT NULL,
  price INTEGER
);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (1, 'ITEM_01', 0,'Men_prod1', 'product-images/men_1.jpg', 'SampleDescription', 1200);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (2,  'ITEM_02' , 0,  'Men_prod2' ,  'product-images/men_2.jpg',  'Sample description' , 5000);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (3,  'ITEM_03' , 0,  'Men_prod3' , 'product-images/men_3.jpg',  'Sample description' , 1000);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (4,  'ITEM_04' , 1,  'Women_prod1' , 'product-images/women_1.jpg',  'Sample description' , 80000);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (5,  'ITEM_05' , 1,  'Women_prod2' , 'product-images/women_2.jpg',  'Sample description' , 150000);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (6,  'ITEM_06' , 1,  'Women_prod3' , 'product-images/women_3.jpg',  'Sample description' , 3000);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (7,  'ITEM_07' , 2,  'Acc_prod1' , 'product-images/acc_1.jpg',  'Sample description' , 3000);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (8,  'ITEM_08' , 2,  'Acc_prod2' , 'product-images/acc_2.jpg',  'Sample description' , 400);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (9,  'ITEM_09' , 2,  'Acc_prod3' , 'product-images/acc_3.jpg',  'Sample description' , 500);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (10,  'ITEM_10' , 2,  'Acc_prod4' , 'product-images/acc_4.jpg',  'Sample description', 500);
