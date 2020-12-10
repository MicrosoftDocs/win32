---
title: VS_VERSIONINFO structure
description: Represents the organization of data in a file-version resource. It is the root structure that contains all other file-version information structures.
ms.assetid: 7864510f-1894-4f17-bf7b-fd5bc1ba4aae
keywords:
- VS_VERSIONINFO structure Menus and Other Resources
topic_type:
- apiref
api_name:
- VS_VERSIONINFO
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# VS\_VERSIONINFO structure

Represents the organization of data in a file-version resource. It is the root structure that contains all other file-version information structures.

## Syntax


```C++
typedef struct {
  WORD             wLength;
  WORD             wValueLength;
  WORD             wType;
  WCHAR            szKey;
  WORD             Padding1;
  VS_FIXEDFILEINFO Value;
  WORD             Padding2;
  WORD             Children;
} VS_VERSIONINFO;
```



## Members

<dl> <dt>

**wLength**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The length, in bytes, of the **VS\_VERSIONINFO** structure. This length does not include any padding that aligns any subsequent version resource data on a 32-bit boundary.

</dd> <dt>

**wValueLength**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The length, in bytes, of the **Value** member. This value is zero if there is no **Value** member associated with the current version structure.

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

The Unicode string L"VS\_VERSION\_INFO".

</dd> <dt>

**Padding1**
</dt> <dd>

Type: **WORD**

</dd> <dd>

Contains as many zero words as necessary to align the **Value** member on a 32-bit boundary.

</dd> <dt>

**Value**
</dt> <dd>

Type: **[**VS\_FIXEDFILEINFO**](/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo)**

</dd> <dd>

Arbitrary data associated with this **VS\_VERSIONINFO** structure. The **wValueLength** member specifies the length of this member; if **wValueLength** is zero, this member does not exist.

</dd> <dt>

**Padding2**
</dt> <dd>

Type: **WORD**

</dd> <dd>

As many zero words as necessary to align the **Children** member on a 32-bit boundary. These bytes are not included in **wValueLength**. This member is optional.

</dd> <dt>

**Children**
</dt> <dd>

Type: **WORD**

</dd> <dd>

An array of zero or one [**StringFileInfo**](stringfileinfo.md) structures, and zero or one [**VarFileInfo**](varfileinfo.md) structures that are children of the current **VS\_VERSIONINFO** structure.

</dd> </dl>

## Remarks

This structure is not a true C-language structure because it contains variable-length members. This structure was created solely to depict the organization of data in a version resource and does not appear in any of the header files shipped with the Windows Software Development Kit (SDK).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**StringFileInfo**](stringfileinfo.md)
</dt> <dt>

[**VerQueryValue**](/windows/desktop/api/Winver/nf-winver-verqueryvaluea)
</dt> <dt>

[**VarFileInfo**](varfileinfo.md)
</dt> <dt>

[**VS\_FIXEDFILEINFO**](/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Version Information](version-information.md)
</dt> </dl>

 

 





