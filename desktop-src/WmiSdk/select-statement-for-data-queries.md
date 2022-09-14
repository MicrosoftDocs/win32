---
description: Describe the SELECT statement for a data query.
ms.assetid: 9c1a164e-4728-4fbe-8a49-b571005a46ec
ms.tgt_platform: multiple
title: SELECT Statement for Data Queries
ms.topic: article
ms.date: 05/31/2018
---

# SELECT Statement for Data Queries

You can use a variety of SELECT statements to query for information. The statements can be basic statements or they can be more restrictive to narrow the result set that is returned from the query.

The following example is a basic SELECT statement that is used to query for data.


```sql
SELECT * FROM Class
```



This statement returns instances of the specified class and any of its subclasses. All of the system and user-defined properties for the classes are included. If a system property is not relevant for a particular query, it contains **NULL**.

You can use several techniques to reduce the bandwidth required to retrieve the result set, if the execution of the query results in too much overhead and the user is only interested in a subset of the properties. First, queries can replace the asterisk with the desired properties.

The following example shows how to query for specific properties.


```sql
SELECT property_1, property_2, property_3 FROM class
```



The result set includes all system properties and the specified nonsystem properties.

Another technique for narrowing the scope of a query's result set is to use the [**\_\_CLASS**](wmi-system-properties.md) system property. Queries by default return all instances of the specified class and its subclasses. You can use the **\_\_CLASS** system property to request only instances of the specified class, excluding its subclasses.

The following example shows how to use the [**\_\_CLASS**](wmi-system-properties.md) system property in a WHERE clause.


```sql
SELECT * FROM Device WHERE __CLASS = "Device"
```



You can also use the [**\_\_CLASS**](wmi-system-properties.md) system property to restrict the result set to instances of particular subclasses.

The following example shows how to restrict the result set to instances of particular subclasses.


```sql
SELECT * FROM Device WHERE __CLASS = "Modem" OR __CLASS = "Keyboard"
```



> [!Note]  
> If you construct a query with an invalid path for an embedded object, your query does not return an error or any results.

 

The following example returns an instance of **MainClass**, assuming that an instance of **MainClass** exists containing the embedded object **EmbedObj** with a property **P\_Uint32** that is equal to "70011".


```sql
SELECT * FROM MainClass WHERE EmbedObj.P_Uint32 = 70011
```



The following example returns no results and does not return an error, assuming that the embedded object **EmbedObj** in the instance of **MainClass** does not have a property **INVALID**.


```sql
SELECT * FROM MainClass WHERE StrongEmbedObj.INVALID = 70011
```



 

 



