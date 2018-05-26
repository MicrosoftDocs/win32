---
Description: Opens the specified Apphelp details database.
ms.assetid: c3b07c00-a3c6-419c-94c6-34c573a04d6d
title: SdbOpenApphelpDetailsDatabase function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SdbOpenApphelpDetailsDatabase function

Opens the specified Apphelp details database.

## Syntax


```C++
PDB WINAPI SdbOpenApphelpDetailsDatabase(
  _In_opt_ LPCWSTR pwsDetailsDatabasePath
);
```



## Parameters

<dl> <dt>

*pwsDetailsDatabasePath* \[in, optional\]
</dt> <dd>

The database path. If this parameter is **NULL**, the local system database is opened.

</dd> </dl>

## Return value

The function returns a handle to the Apphelp details database.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



 

 




