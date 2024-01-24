---
description: Determines whether the specified database is one of the standard databases (Sysmain, Apphelp, Drvmain, or Msimain).
ms.assetid: 7d7e3ca7-535e-40b3-b635-299eff8abea5
title: SdbIsStandardDatabase function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbIsStandardDatabase
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbIsStandardDatabase function

Determines whether the specified database is one of the standard databases (Sysmain, Apphelp, Drvmain, or Msimain).

## Syntax


```C++
BOOL WINAPI SdbIsStandardDatabase(
  _In_ GUID GuidDB
);
```



## Parameters

<dl> <dt>

*GuidDB* \[in\]
</dt> <dd>

The GUID for the database.

</dd> </dl>

## Return value

The function returns **TRUE** if the GUID represents a standard database or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



 

 




