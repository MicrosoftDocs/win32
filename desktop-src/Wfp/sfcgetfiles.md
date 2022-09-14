---
description: Lists protected files.
ms.assetid: 46a1ff83-afed-4ce3-bb62-551446efdb78
title: SfcGetFiles function (Sfcfiles.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SfcGetFiles
api_type: 
- DllExport
api_location: 
- Sfcfiles.dll
---

# SfcGetFiles function

\[This function is available for use in the operating systems specified in the Requirements section. Support for this function was removed in Windows Vista and Windows Server 2008. Use the supported functions listed in [WRP Functions](wfp-functions.md) instead.\]

Lists protected files.

## Syntax


```C++
NTSTATUS WINAPI SfcGetFiles(
  _Out_ PPROTECT_FILE_ENTRY ProtFileData,
  _Out_ PULONG              FileCount
);
```



## Parameters

<dl> <dt>

*ProtFileData* \[out\]
</dt> <dd>

A pointer to a [**PPROTECT\_FILE\_ENTRY**](pprotect-file-entry.md) structure that contains the protected files list.

</dd> <dt>

*FileCount* \[out\]
</dt> <dd>

A pointer to a location containing a ULONG value that is the number of protected files.

</dd> </dl>

## Return value

If the function succeeds, the return value is STATUS\_SUCCESS. If the function fails, it returns the appropriate NTSTATUS error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Sfcfiles.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Sfcfiles.dll</dt> </dl> |



## See also

<dl> <dt>

[**PPROTECT\_FILE\_ENTRY**](pprotect-file-entry.md)
</dt> </dl>

 

 




