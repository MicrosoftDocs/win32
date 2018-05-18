---
title: File Management Data Types
description: Used as a function parameter type.
ms.assetid: 'ee199501-2f22-483b-8cab-f48921ecc40e'
keywords: ["PFILE_RESTORE_CONTEXT"]
---

# File Management Data Types

The data type for File Management is used as a function parameter type.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 


```C++
typedef PVOID PFILE_RESTORE_CONTEXT;
```



<dl> <dt>

**PFILE\_RESTORE\_CONTEXT**
</dt> <dd>

A pointer to a file restore context.

</dd> </dl>

## Remarks

Note that there is no associated header file for this data type.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





