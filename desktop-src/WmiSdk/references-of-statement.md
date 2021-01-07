---
description: The REFERENCES OF statement retrieves all association instances that refer to a particular source instance.
ms.assetid: 674be546-e7fd-4150-9d7c-2888d24bf1b3
ms.tgt_platform: multiple
title: REFERENCES OF Statement
ms.topic: article
ms.date: 05/31/2018
---

# REFERENCES OF Statement

The REFERENCES OF statement retrieves all association instances that refer to a particular source instance. The REFERENCES OF statement is similar to the ASSOCIATORS OF statement in its syntax. However, rather than retrieving endpoint instances, it retrieves the intervening association instances.

The REFERENCES OF WHERE clause can include one or more of the following predefined keywords and their values:


```sql
REFERENCES OF {SourceObject} WHERE 
    ClassDefsOnly
    RequiredQualifier = QualifierName
    ResultClass = ClassName
    Role = PropertyName
```



To specify a source object, use any valid object path for SourceObject. As with the SELECT statement, the WHERE clause is optional and is used to further define the query. That is, the following statement is perfectly valid:


```sql
REFERENCES OF {Adapter="AHA-294X"}
```



The **ClassDefsOnly** keyword indicates that the statement returns a result set of class definition objects rather than actual instances of the association classes. These objects contain definitions of classes to which the instances that reference the source object belong. For example, the following statement returns definitions for the **AdapterDriver** and **AdapterProtocol** classes:


```sql
REFERENCES OF {Adapter="AHA-294X"} WHERE ClassDefsOnly
```



The **RequiredQualifier** keyword indicates that the returned association objects must include the specified qualifier. The **RequiredQualifier** keyword can be used to include particular instances of associations in the result set. For example, the following statement returns association instances that include a qualifier called **AdapterTag**:


```sql
REFERENCES OF {Adapter="AHA-294X"}  WHERE RequiredQualifier = AdapterTag
```



The **ResultClass** keyword indicates that the returned association objects must belong to or be derived from the specified class. For example, the following statement returns associations of the **AdapterDriver** class or subclasses of **AdapterDriver**:


```sql
REFERENCES OF {Adapter="AHA-294X"} WHERE ResultClass = AdapterDriver
```



The **ClassDefsOnly** and **ResultClass** keywords are mutually exclusive. Using them together causes an invalid query error.

The **Role** keyword indicates that the returned associations are only those in which the source object plays a particular role. The role is defined by the specified property, a reference property of type [ref](references.md). The **Role** keyword is useful in associations where a certain object can play one role in some cases and another role in others, such as in hierarchical associations. The **Role** keyword can be used to retrieve all of the associations in which the source object plays the role of parent, for example. The following statement illustrates the syntax for retrieving associations that have a **parent** property referencing the source object as the parent:


```sql
REFERENCES OF {Adapter="AHA-294X"} WHERE Role = parent
```



> [!Note]  
> Complex queries cannot use "And" or "Or" to separate keywords for ASSOCIATORS OF and REFERENCES OF statements. Furthermore, the equal sign is the only valid operator that can be used with the keywords in these queries. For example, the following query is valid:

 


```sql
"REFERENCES OF {Win32_NetworkAdapter.DeviceID="0"} " +
    "WHERE resultclass = Win32_NetworkAdapterSetting " +
    "requiredQualifier = Dynamic"
```



> [!Note]  
> The next examples are not valid. The first example does not use the equal sign and the second example erroneously attempts to use the **AND** keyword:

 


```sql
"REFERENCES OF {Win32_NetworkAdapter.DeviceID="0"} " +
    "WHERE resultclass = Win32_NetworkAdapterSetting " +
    "requiredQualifier <> Dynamic"

"REFERENCES OF {Win32_NetworkAdapter.DeviceID="0"} " +
"WHERE resultclass = Win32_NetworkAdapterSetting " +
"AND requiredQualifier = Dynamic"
```



 

 



