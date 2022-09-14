---
description: Structure used by the SfcGetFiles function.
ms.assetid: 958167e3-3eb3-406a-85bf-ffe2851a95a1
title: PPROTECT_FILE_ENTRY structure (Sfcfiles.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PPROTECT_FILE_ENTRY
api_type: 
- HeaderDef
api_location: 
- Sfcfiles.h
---

# PPROTECT\_FILE\_ENTRY structure

\[This structure is available for use in the operating systems specified in the Requirements section. Support for this structure was removed in Windows Vista and Windows Server 2008. Use the supported functions listed in [WRP Functions](wfp-functions.md) instead.\]

Structure used by the [**SfcGetFiles**](sfcgetfiles.md) function.

## Syntax


```C++
typedef struct _PPROTECT_FILE_ENTRY {
  PWSTR SourceFileName;
  PWSTR FileName;
  PWSTR InfName;
} PPROTECT_FILE_ENTRY, *PPPROTECT_FILE_ENTRY;
```



## Members

<dl> <dt>

**SourceFileName**
</dt> <dd>

Pointer to a string value containing the filename of the source file. This will be **NULL** if the file is not renamed on installation.

</dd> <dt>

**FileName**
</dt> <dd>

Pointer to string value containing the destination filename plus the full path to the file.

</dd> <dt>

**InfName**
</dt> <dd>

Pointer to string value containing the filename of the INF file which provides layout information. This parameter may be **NULL** when using the default layout.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Header<br/>                   | <dl> <dt>Sfcfiles.h</dt> </dl> |



## See also

<dl> <dt>

[**SfcGetFiles**](sfcgetfiles.md)
</dt> </dl>

 

 




