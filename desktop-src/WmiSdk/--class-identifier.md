---
description: The well-known identifier \_\_CLASS refers to a pseudo-property on every WMI object that indicates the class of the current object.
ms.assetid: a1d0e934-c5b5-4554-9d6e-3881064419ca
ms.tgt_platform: multiple
title: '__CLASS Identifier'
ms.topic: article
ms.date: 05/31/2018
---

# \_\_CLASS Identifier

The well-known identifier \_\_CLASS refers to a pseudo-property on every WMI object that indicates the class of the current object.

Use \_\_CLASS in a [WHERE](where-clause.md) clause to filter out any objects of derived classes from your result set. For example, the result set of the following query contains not only objects whose class is [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk), but also objects whose class is derived from **Win32\_LogicalDisk**.


```sql
SELECT * FROM Win32_LogicalDisk
```



In the following example, the use of \_\_CLASS in the **WHERE** clause filters out all objects of classes derived from [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) because their class is not **Win32\_LogicalDisk**.


```sql
SELECT * FROM Win32_LogicalDisk   WHERE __CLASS = "Win32_LogicalDisk"
```



Use \_\_CLASS in providers that are asked to provide instances of a specific class, irrespective of any subclasses.

 

 
