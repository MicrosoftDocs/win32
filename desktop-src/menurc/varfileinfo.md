---
title: VarFileInfo structure
description: Represents the organization of data in a file-version resource. It contains version information not dependent on a particular language and code page combination.
ms.assetid: 3b667778-fb08-4195-a88e-ac04baf45fee
keywords:
- VarFileInfo structure Menus and Other Resources
topic_type:
- apiref
api_name:
- VarFileInfo
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# VarFileInfo structure

Represents the organization of data in a file-version resource. It contains version information not dependent on a particular language and code page combination.

## Syntax


```C++
typedef struct {
  WORD  wLength;
  WORD  wValueLength;
  WORD  wType;
  WCHAR szKey;
  WORD  Padding;
  Var   Children;
} VarFileInfo;
```



## Members

<dl> <dt>

**wLength**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The length, in bytes, of the entire **VarFileInfo** block, including all structures indicated by the **Children** member.

</dd> <dt>

**wValueLength**
</dt> <dd>

Type: **WORD**

</dd> <dd>

This member is always equal to zero.

</dd> <dt>

**wType**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The type of data in the version resource. This member is 1 if the version resource contains text data and 0 if the version resource contains binary data.

</dd> <dt>

**szKey**
</dt> <dd>

Type: **WCHAR**

</dd> <dd>

The Unicode string L"VarFileInfo".

</dd> <dt>

**Padding**
</dt> <dd>

Type: **WORD**

</dd> <dd>

As many zero words as necessary to align the **Children** member on a 32-bit boundary.

</dd> <dt>

**Children**
</dt> <dd>

Type: **[**Var**](var-str.md)**

</dd> <dd>

Typically contains a list of languages that the application or DLL supports.

</dd> </dl>

## Remarks

This structure is not a true C-language structure because it contains variable-length members. This structure was created solely to depict the organization of data in a version resource and does not appear in any of the header files shipped with the Windows Software Development Kit (SDK).

The **Children** member of the [**VS\_VERSIONINFO**](vs-versioninfo.md) structure may contain zero or one **VarFileInfo** structures.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**Var**](var-str.md)
</dt> <dt>

[**VS\_VERSIONINFO**](vs-versioninfo.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Version Information](version-information.md)
</dt> </dl>

 

 





