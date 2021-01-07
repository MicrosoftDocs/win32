---
description: The ISA operator is a WQL-specific operator that can be used in data, event, and schema queries.
ms.assetid: 0520470c-ebfc-4c45-8a1f-47fd66bf8414
ms.tgt_platform: multiple
title: ISA Operator for Schema Queries
ms.topic: article
ms.date: 05/31/2018
---

# ISA Operator for Schema Queries

The ISA operator is a WQL-specific operator that can be used in data, event, and schema queries.

When ISA is included in the [WHERE clause](where-clause.md) of an schema query, it requests that the query be applied to all subclasses of the class you specify.

For example, the following statement requests notification every 10 minutes of instance modification events for all instances that are members of any class deriving from the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class.


```sql
SELECT * FROM __InstanceModificationEvent WITHIN 600
WHERE TargetInstance ISA "Win32_LogicalDisk"
```



The following query returns the definition for the [**CIM\_Processor**](/windows/desktop/CIMWin32Prov/cim-processor) class and definitions for all of its subclasses.


```sql
SELECT * FROM meta_class WHERE __this ISA "CIM_Processor"
```



The class **meta\_class** identifies this as a schema query, the property called **\_\_this** identifies the target class of the query, and the ISA operator requests definitions for the subclasses of the target class.

 

 
