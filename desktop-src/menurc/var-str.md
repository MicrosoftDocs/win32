---
title: Var structure
description: Represents the organization of data in a file-version resource. It typically contains a list of language and code page identifier pairs that the version of the application or DLL supports.
ms.assetid: edd2f2e5-100c-49c2-841f-f75e2909460a
keywords:
- Var structure Menus and Other Resources
topic_type:
- apiref
api_name:
- Var
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Var structure

Represents the organization of data in a file-version resource. It typically contains a list of language and code page identifier pairs that the version of the application or DLL supports.

## Syntax


```C++
typedef struct {
  WORD  wLength;
  WORD  wValueLength;
  WORD  wType;
  WCHAR szKey;
  WORD  Padding;
  DWORD Value;
} Var;
```



## Members

<dl> <dt>

**wLength**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The length, in bytes, of the **Var** structure.

</dd> <dt>

**wValueLength**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The length, in bytes, of the **Value** member.

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

The Unicode string L"Translation".

</dd> <dt>

**Padding**
</dt> <dd>

Type: **WORD**

</dd> <dd>

As many zero words as necessary to align the **Value** member on a 32-bit boundary.

</dd> <dt>

**Value**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

An array of one or more values that are language and code page identifier pairs. For additional information, see the following Remarks section.

</dd> </dl>

## Remarks

This structure is not a true C-language structure because it contains variable-length members. This structure was created solely to depict the organization of data in a version resource and does not appear in any of the header files shipped with the Windows Software Development Kit (SDK).

If you use the **Var** structure to list the languages your application or DLL supports instead of using multiple version resources, use the **Value** member to contain an array of **DWORD** values indicating the language and code page combinations supported by this file. The low-order word of each **DWORD** must contain a Microsoft language identifier, and the high-order word must contain the IBM code page number. Either high-order or low-order word can be zero, indicating that the file is language or code page independent. If the **Var** structure is omitted, the file will be interpreted as both language and code page independent.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**VarFileInfo**](varfileinfo.md)
</dt> <dt>

[**StringFileInfo**](stringfileinfo.md)
</dt> <dt>

[**StringTable**](stringtable.md)
</dt> <dt>

[**VS\_VERSIONINFO**](vs-versioninfo.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Version Information](version-information.md)
</dt> </dl>

 

 





