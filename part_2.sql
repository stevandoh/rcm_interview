
-- Find all customers in Berlin
SELECT * FROM Customers where city = 'Berlin';

-- Find all customers in Mexico City
SELECT * FROM Customers WHERE City LIKE 'México%';

-- Find avg price of all products
SELECT AVG (Price) FROM Products;

-- Find number of products that Have price = 18
SELECT * FROM Products where Price =18;

-- Find orders between 1996-08-01 and 1996-09-06
SELECT * FROM [Orders] where OrderDate BETWEEN '1996-08-01' AND '1996-09-06';

-- Find customers with more than 3 orders
 SELECT customers.*,  COUNT(*) AS OrderCount
    FROM customers INNER JOIN orders
               ON customers.customerid=orders.customerid
    GROUP BY customers.customerid having  OrderCount > 3;

-- Find all customers that are from the same city
SELECT distinct city, group_concat('{'|| 'id: '|| c.customerId ||
                                   ', name: '||c.CustomerName  ||
                                   ', address: '||c.address ||
                                   ', contactName: '||c.contactName ||
                                   ', postalCode: '||c.postalCode ||
                                   ', country: '||c.country ||
                                   '}') as customerList  FROM  Customers c group by city;
