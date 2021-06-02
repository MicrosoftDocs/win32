---
title: StringFileInfo structure
description: Represents the organization of data in a file-version resource. It contains version information that can be displayed for a particular language and code page.
ms.assetid: dda38fee-e8ea-4e58-b5ee-72e4cdb08f42
keywords:
- StringFileInfo structure Menus and Other Resources
topic_type:
- apiref
api_name:
- StringFileInfo
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StringFileInfo structure

Represents the organization of data in a file-version resource. It contains version information that can be displayed for a particular language and code page.

## Syntax


```C++
typedef struct {
  WORD        wLength;
  WORD        wValueLength;
  WORD        wType;
  WCHAR       szKey;
  WORD        Padding;
  StringTable Children;
} StringFileInfo;
```



## Members

<dl> <dt>

**wLength**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The length, in bytes, of the entire **StringFileInfo** block, including all structures indicated by the **Children** member.

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

The Unicode string L"StringFileInfo".

</dd> <dt>

**Padding**
</dt> <dd>

Type: **WORD**

</dd> <dd>

As many zero words as necessary to align the **Children** member on a 32-bit boundary.

</dd> <dt>

**Children**
</dt> <dd>

Type: **[**StringTable**](stringtable.md)**

</dd> <dd>

An array of one or more [**StringTable**](stringtable.md) structures. Each **StringTable** structure's **szKey** member indicates the appropriate language and code page for displaying the text in that **StringTable** structure.

</dd> </dl>

## Remarks

This structure is not a true C-language structure because it contains variable-length members. This structure was created solely to depict the organization of data in a version resource and does not appear in any of the header files shipped with the Windows Software Development Kit (SDK).

The **Children** member of the [**VS\_VERSIONINFO**](vs-versioninfo.md) structure may contain zero or more **StringFileInfo** structures.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**StringTable**](stringtable.md)
</dt> <dt>

[**String**](string-str.md)
</dt> <dt>

[**VS\_VERSIONINFO**](vs-versioninfo.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Version Information](version-information.md)
</dt> </dl>

 

 





