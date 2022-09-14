---
description: Schema data queries use the SELECT statement with a syntax similar to that for data queries.
ms.assetid: e7150aaa-5829-4d64-a13b-39f83adc5b98
ms.tgt_platform: multiple
title: SELECT Statement for Schema Queries
ms.topic: article
ms.date: 05/31/2018
---

# SELECT Statement for Schema Queries

Schema data queries use the SELECT statement with a syntax similar to that for [data queries](select-statement-for-data-queries.md). The difference is the use of a special class called "meta\_class", which identifies the query as a schema query.

The following example requests all class definitions that are within the current namespace.


```sql
SELECT * FROM meta_class
```



Schema queries only support "\*". To narrow the scope of the definitions returned, a provider can add a WHERE clause that specifies a particular class.

The following example shows how to add a WHERE clause to specify a particular class.


```sql
SELECT * FROM meta_class WHERE __this ISA "Win32_LogicalDisk"
```



The special property called **\_\_this** identifies the target class for a schema query. Note that the ISA operator must be used with the **\_\_this** property to request definitions for the subclasses of the target class. The preceding query returns the definition for the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class and definitions for all of its subclasses.

The following example shows how to request a class definition for a single class by using the **\_\_Class** system property.


```sql
SELECT * FROM meta_class WHERE __Class = "Win32_LogicalDisk"
```



This query is equivalent to calling the [**IWbemServices::GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) or the [**IWbemServices::GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync) method with the object path parameter set to "Win32\_LogicalDisk".

The following VBScript code sample retrieves all child classes of a top level WMI class. The \_\_Dynasty WMI system property holds the name of the top-level class from which a class is derived, which you can use to retrieve all classes in a namespace derived from a top level class, including that class.


```VB
' Retrieve immediate child classes for Cim_DataFile

Set objWmi = GetObject ("winmgmts:root\cimv2")

Set colClasses = objWmi.ExecQuery _ 
    ("Select * From meta_class " _
    & "Where __Dynasty = 'Win32_CurrentTime'")

For Each objClass In colClasses 
    WScript.Echo objClass.SystemProperties_("__Class")
Next
```



The following VBScript retrieves an immediate child classes for a WMI class.


```VB
' Retrieve immediate child classes for Cim_DataFile

Set objWmi = GetObject ("winmgmts:root\cimv2")

Set colClasses = objWmi.ExecQuery _ 
    ("Select * From meta_class " _
    & "Where __Superclass = 'Cim_DataFile'")

For Each objClass In colClasses 
    WScript.Echo objClass.SystemProperties_("__Class")
Next
```



The following VBScript retrieves top level classes. For all the top level classes in a WMI namespace, the \_\_Superclass system property is Null. Therefore, it is possible to retrieve the top level classes by searching for a Null superclass.


```VB
 Retrieve top level classes in root\cimv2

Set objWmi = GetObject ("winmgmts:root\cimv2")

Set colClasses = objWmi.ExecQuery _
    ("Select * From meta_class Where __Superclass Is Null")

For Each objClass In colClasses
    WScript.Echo objClass.SystemProperties_("__Class")

```



 

 
