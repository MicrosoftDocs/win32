---
title: StringTable structure
description: Represents the organization of data in a file-version resource. It contains language and code page formatting information for the strings specified by the Children member. A code page is an ordered character set.
ms.assetid: e8e9d654-b515-434c-ac38-79d333a8d7cb
keywords:
- StringTable structure Menus and Other Resources
topic_type:
- apiref
api_name:
- StringTable
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StringTable structure

Represents the organization of data in a file-version resource. It contains language and code page formatting information for the strings specified by the **Children** member. A code page is an ordered character set.

## Syntax


```C++
typedef struct {
  WORD   wLength;
  WORD   wValueLength;
  WORD   wType;
  WCHAR  szKey;
  WORD   Padding;
  String Children;
} StringTable;
```



## Members

<dl> <dt>

**wLength**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The length, in bytes, of this **StringTable** structure, including all structures indicated by the **Children** member.

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

An 8-digit hexadecimal number stored as a Unicode string. The four most significant digits represent the language identifier. The four least significant digits represent the code page for which the data is formatted. Each Microsoft Standard Language identifier contains two parts: the low-order 10 bits specify the major language, and the high-order 6 bits specify the sublanguage. For a table of valid identifiers see .

</dd> <dt>

**Padding**
</dt> <dd>

Type: **WORD**

</dd> <dd>

As many zero words as necessary to align the **Children** member on a 32-bit boundary.

</dd> <dt>

**Children**
</dt> <dd>

Type: **[**String**](string-str.md)**

</dd> <dd>

An array of one or more [**String**](string-str.md) structures.

</dd> </dl>

## Remarks

This structure is not a true C-language structure because it contains variable-length members. This structure was created solely to depict the organization of data in a version resource and does not appear in any of the header files shipped with the Windows Software Development Kit (SDK).

The **Children** member of the [**StringFileInfo**](stringfileinfo.md) structure contains at least one **StringTable** structure.

Set the code page portion of the **szKey** member to the hexadecimal value 0x04b0 to indicate the Unicode code page, or to the hexadecimal value of the code page that is appropriate for the language component. After you choose the value for the code page you should continue to use the same value in later revisions to the file.

An executable file or DLL that supports multiple languages should have a version resource for each language, rather than a single version resource that contains strings in several languages. However, if you use the [**Var**](var-str.md) structure to list the languages that your application supports, the number of **StringTable** structures in the version resource is directly related to the number of language/code page identifier pairs in the **Value** member of the **Var** structure.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**String**](string-str.md)
</dt> <dt>

[**StringFileInfo**](stringfileinfo.md)
</dt> <dt>

[**Var**](var-str.md)
</dt> <dt>

[**VarFileInfo**](varfileinfo.md)
</dt> <dt>

[**VS\_VERSIONINFO**](vs-versioninfo.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Version Information](version-information.md)
</dt> </dl>

 

 





