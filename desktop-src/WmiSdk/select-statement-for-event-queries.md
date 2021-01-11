---
description: Describes the basic syntax of a SELECT statement for event queries.
ms.assetid: 8882fdcb-3768-41e3-82ab-3006d903f3a0
ms.tgt_platform: multiple
title: SELECT Statement for Event Queries
ms.topic: article
ms.date: 05/31/2018
---

# SELECT Statement for Event Queries

You can use a variety of SELECT statements to query for event information. The statements can be basic statements or they can be more restrictive to narrow the result set that is returned from the query.

The following example is a basic SELECT statement that is used to query for event information.


```sql
SELECT * FROM EventClass
```



When a consumer submits a query, it is a request to be notified of all occurrences of the event represented by **EventClass**. This request includes a request for notification about all of the event system and nonsystem properties. When an event provider submits a query, it registers support for generating notifications when an event represented by **EventClass** occurs.

Consumers can specify individual properties instead of the asterisk (\*) in the SELECT statement.

The following example shows how to query for specific properties.


```sql
SELECT property_1, property_2, property_3 FROM MyEventClass
```



However, all of the properties of an embedded object are returned, even if the query specifies embedded object properties.

The following example shows two queries that return the same data.


```sql
SELECT targetInstance FROM __InstanceCreationEvent within 2
    WHERE targetinstance isa "Win32_Process"
```




```sql
SELECT targetInstance.Name FROM __InstanceCreationEvent within 2
    WHERE targetinstance isa "Win32_Process"
```



If a system property is not relevant for a specific query, it contains **NULL**. For example, the value of the **\_\_RELPATH** system property is **NULL** for all event queries.

The following system properties contain **NULL** for event queries:

<dl> \_\_Namespace  
\_\_Path  
\_\_RelPath  
\_\_Server  
</dl>

For more information, see [WMI System Property Reference](wmi-system-properties.md).

All event queries can include an optional [WHERE clause](where-clause.md), but WHERE clauses are primarily used by consumers to specify additional filtering. It is strongly recommended that consumers always specify a WHERE clause. The cost of a complex query is minimal compared to the cost of delivering and processing unneeded notifications.

The following example shows a query that requests notifications of all instance modification events that affect the hypothetical class **EmailEvent**.


```sql
SELECT * FROM EmailEvent
```



If events associated with **EmailEvent** occur frequently, the consumer is flooded with events. A better query requests events only when specific conditions use properties of the class specified, such as when the importance level is high.

The following example shows the query you can use if **EmailImportance** is a property of the class **EmailEvent**.


```sql
SELECT * FROM EmailEvent WHERE EmailImportance > 3
```



Note that WMI can reject a query for a number of reasons. For example, the query can be too complex or resource-intensive for evaluation. When this occurs, WMI returns specific error codes, such as **WBEM\_E\_INVALID\_QUERY**.

Properties of embedded objects can be used in the WHERE clause.

The following example shows how to query for objects where the **TargetInstance** property of the [**\_\_InstanceModificationEvent**](--instancemodificationevent.md) system class is an embedded [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) object and **FreeSpace** is a property of **Win32\_LogicalDisk**.


```sql
SELECT * FROM __InstanceModificationEvent WITHIN 600
    WHERE TargetInstance ISA "Win32_LogicalDisk" 
    AND   TargetInstance.FreeSpace < 1000000
```



## Examples

The [Monitor creation event for specific process name](https://Gallery.TechNet.Microsoft.Com/52716121-f386-49de-86cd-46ca54d1714f) VBScript sample on TechNet uses the SELECT statement to monitor WMI instance creation events for Win32\_Process, filtering for a specific process name.

 

 
