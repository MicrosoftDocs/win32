---
description: Contains information about a selected file in the active File Manager window (the directory window or the Search Results window).
title: FMS_GETFILESEL structure (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FMS_GETFILESEL
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: d8339f87-ba05-40bf-b7d1-a9de29eb15a4
api_name: 
 - FMS_GETFILESEL
api_type: 
 - HeaderDef
api_location: 
 - Wfext.h
topic_type: 
 - APIRef
 - kbSyntax

---

# FMS\_GETFILESEL structure

Contains information about a selected file in the active File Manager window (the directory window or the Search Results window).

## Syntax


```C++
typedef struct _FMS_GETFILESEL {
  FILETIME ftTime;
  DWORD    dwSize;
  BYTE     bAttr;
  TCHAR    szName;
} FMS_GETFILESEL;
```



## Members

<dl> <dt>

**ftTime**
</dt> <dd>

Type: **FILETIME**

</dd> <dd>

The time and date the file was created.

</dd> <dt>

**dwSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The size, in bytes, of the file.

</dd> <dt>

**bAttr**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The attributes of the file.

</dd> <dt>

**szName**
</dt> <dd>

Type: **TCHAR**

</dd> <dd>

The null-terminated full path and file name of the selected file.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMExtensionProc**](fmextensionproc.md)
</dt> </dl>

 

 




