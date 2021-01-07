---
description: Retrieves all instances that are associated with a particular source instance.
ms.assetid: d6bd9643-523d-4d81-8bf1-da52ccc7524d
ms.tgt_platform: multiple
title: ASSOCIATORS OF Statement
ms.topic: article
ms.date: 05/31/2018
---

# ASSOCIATORS OF Statement

The ASSOCIATORS OF statement retrieves all instances that are associated with a particular source instance. The instances that are retrieved are referred to as the endpoints. Each endpoint is returned as many times as there are associations between it and the source object. For example, assume there are instances A, B, X, and Y. Two association instances exist, one that links A and X and another that links B and Y. The following query returns the single endpoint X:


```sql
ASSOCIATORS OF {A}
```



However, if there is another association linking A and X, the above query returns two X endpoints.

The basic syntax for the ASSOCIATORS OF statement is:

``` syntax
ASSOCIATORS OF {ObjectPath}
```

Note that the braces are part of the syntax. Any valid object path can be used for ObjectPath. The tokens within the object path cannot contain any white space. For example, the query in the following list returns instances that are associated with the specified logical disk:

<dl> <dt>

<span id="Query_"></span><span id="query_"></span><span id="QUERY_"></span>Query:
</dt> <dd>


```sql
ASSOCIATORS OF {Win32_LogicalDisk.DeviceID="C:"}
```



</dd> <dt>

<span id="Results_"></span><span id="results_"></span><span id="RESULTS_"></span>Results:
</dt> <dd>

``` syntax
Win32_Directory.Name="C:\\"
```

``` syntax
Win32_ComputerSystem.Name="mycomputer"
Win32_DiskPartition.DeviceID="Disk #0, Partition #0"
```

</dd> </dl>

As with the [SELECT statement](select-statement-for-data-queries.md), an ASSOCIATORS OF statement can include a [WHERE clause](where-clause.md), but the WHERE clause for an ASSOCIATORS OF statement is very different from the SELECT statementWHERE clause.

The [WHERE clause](where-clause.md) of the ASSOCIATORS OF statement can include one or more of the following predefined keywords and their values:


```sql
ASSOCIATORS OF {ObjectPath} WHERE
    AssocClass = AssocClassName
    ClassDefsOnly
    RequiredAssocQualifier = QualifierName
    RequiredQualifier = QualifierName
    ResultClass = ClassName
    ResultRole = PropertyName
    Role = PropertyName
```



Note that the optional subclauses are not separated by commas.

The **AssocClass** keyword indicates that the returned endpoints must be associated with the source through the specified class or one of its derived classes. For example, the query in the following list returns only endpoints that are associated with the source through the [**Win32\_SystemDevices**](/windows/desktop/CIMWin32Prov/win32-systemdevices) association class or any of its derived classes:

<dl> <dt>

<span id="Query_"></span><span id="query_"></span><span id="QUERY_"></span>Query:
</dt> <dd>


```sql
ASSOCIATORS OF {Win32_LogicalDisk.DeviceID="C:"} WHERE AssocClass = Win32_SystemDevices
```



</dd> <dt>

<span id="Results_"></span><span id="results_"></span><span id="RESULTS_"></span>Results:
</dt> <dd>

``` syntax
Win32_ComputerSystem.Name="mycomputer"
```

</dd> </dl>

The **ClassDefsOnly** keyword indicates that the clause returns a result set of class definition objects rather than actual instances of the classes. These objects are the definitions of classes to which the endpoint instances belong. For example, the query in the following list returns definitions for the [**Win32\_Directory**](/windows/desktop/CIMWin32Prov/win32-directory) and [**Win32\_ComputerSystem**](/windows/desktop/CIMWin32Prov/win32-computersystem) classes:

<dl> <dt>

<span id="Query_"></span><span id="query_"></span><span id="QUERY_"></span>Query:
</dt> <dd>


```sql
ASSOCIATORS OF {Win32_LogicalDisk.DeviceID="C:"} WHERE ClassDefsOnly
```



</dd> <dt>

<span id="Results_"></span><span id="results_"></span><span id="RESULTS_"></span>Results:
</dt> <dd>

``` syntax
Win32_Directory
```

``` syntax
Win32_ComputerSystem
Win32_DiskPartition
```

</dd> </dl>

The **ClassDefsOnly** and **ResultClass** keywords are mutually exclusive. Using them together causes an invalid query error.

The **RequiredAssocQualifier** keyword indicates that the returned endpoints must be associated with the source object through an association class that includes the specified qualifier. This type of filtering is used to eliminate broad ranges of endpoints unless the endpoints are associated with the target through a particular set of tagged association classes. For example, the query in the following list returns endpoint instances if the association class includes a qualifier called **Association**.

<dl> <dt>

<span id="Query_"></span><span id="query_"></span><span id="QUERY_"></span>Query:
</dt> <dd>


```sql
ASSOCIATORS OF {Win32_LogicalDisk.DeviceID="C:"}
   WHERE RequiredAssocQualifier = Association
```



</dd> <dt>

<span id="Results_"></span><span id="results_"></span><span id="RESULTS_"></span>Results:
</dt> <dd>

``` syntax
Win32_Directory.Name="C:\\"
```

``` syntax
Win32_ComputerSystem.Name="mycomputer"
Win32_DiskPartition.DeviceID="Disk #0, Partition #0"
```

</dd> </dl>

The **RequiredQualifier** keyword indicates that the returned endpoints associated with the source object must include the specified qualifier. The **RequiredQualifier** keyword can be used to include particular types of instances in the result set. For example, the query in the following list returns endpoint instances that include a qualifier called [**Locale**](swbemobjectpath-locale.md).

<dl> <dt>

<span id="Query_"></span><span id="query_"></span><span id="QUERY_"></span>Query:
</dt> <dd>


```sql
ASSOCIATORS OF {Win32_LogicalDisk.DeviceID="C:"} WHERE RequiredQualifier = Locale
```



</dd> <dt>

<span id="Results_"></span><span id="results_"></span><span id="RESULTS_"></span>Results:
</dt> <dd>

``` syntax
Win32_Directory.Name="C:\\"
```

``` syntax
Win32_ComputerSystem.Name="mycomputer"
Win32_DiskPartition.DeviceID="Disk #0, Partition #0"
```

</dd> </dl>

The **ResultClass** keyword indicates that the returned endpoints associated with the source object must belong to or be derived from the specified class. For example, the query in the following list returns endpoint instances that are derived from the [**CIM\_Directory**](/windows/desktop/CIMWin32Prov/cim-directory) class:

<dl> <dt>

<span id="Query_"></span><span id="query_"></span><span id="QUERY_"></span>Query:
</dt> <dd>


```sql
ASSOCIATORS OF {Win32_LogicalDisk.DeviceID="C:"} WHERE ResultClass = Cim_Directory
```



</dd> <dt>

<span id="Results_"></span><span id="results_"></span><span id="RESULTS_"></span>Results:
</dt> <dd>

``` syntax
Win32_Directory.Name="C:\\"
```

</dd> </dl>

The **ClassDefsOnly** and **ResultClass** keywords are mutually exclusive. Using them together causes an invalid query error.

The **ResultRole** keyword indicates that the returned endpoints must play a particular role in their association with the source object. The role is defined by the specified property, a reference property of type [ref](references.md). For example, the **ResultRole** keyword can be used to retrieve all endpoints that have the **GroupComponent** property in their association with a source object, as the following query illustrates.

<dl> <dt>

<span id="Query_"></span><span id="query_"></span><span id="QUERY_"></span>Query:
</dt> <dd>


```sql
ASSOCIATORS OF {Win32_LogicalDisk.DeviceID="C:"} WHERE ResultRole = GroupComponent
```



</dd> <dt>

<span id="Results_"></span><span id="results_"></span><span id="RESULTS_"></span>Results:
</dt> <dd>

``` syntax
Win32_ComputerSystem.Name="mycomputer"
```

</dd> </dl>

The **Role** keyword indicates that the returned endpoints participate in an association with the source object where the source object plays a particular role. The role is defined by the specified property, a reference property of type **ref**. For example, the **Role** keyword can be used to retrieve all endpoints associated with a source object that have the **GroupComponent** property, as the following query illustrates.

<dl> <dt>

<span id="Query_"></span><span id="query_"></span><span id="QUERY_"></span>Query:
</dt> <dd>


```sql
ASSOCIATORS OF {Win32_LogicalDisk.DeviceID="C:"}
   WHERE Role = GroupComponent
```



</dd> <dt>

<span id="Results_"></span><span id="results_"></span><span id="RESULTS_"></span>Results:
</dt> <dd>

``` syntax
Win32_Directory.Name="C:\\"
```

</dd> </dl>

> [!Note]  
> Complex queries cannot use "And" or "Or" to separate keywords for ASSOCIATORS OF and [REFERENCES OF](references-of-statement.md) statements. Furthermore, the equal sign is the only valid operator that can be used in such queries. For example, the following query is valid:

 


```sql
ASSOCIATORS OF {win32_LogicalDisk="C:"} WHERE resultClass = Win32_Directory requiredQualifier = Dynamic
```



> [!Note]  
> The next examples are not valid. The first example does not use the equal sign and the second example erroneously attempts to use the **AND** keyword.

 

``` syntax
Associators of {win32_LogicalDisk="C:"} where resultClass = Win32_Directory requiredQualifier <> Dynamic

Associators of {win32_LogicalDisk="C:"} where resultClass = Win32_Directory AND requiredQualifier = Dynamic
```

 

 
