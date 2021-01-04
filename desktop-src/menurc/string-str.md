---
title: String structure
description: Represents the organization of data in a file-version resource. It contains a string that describes a specific aspect of a file, for example, a file's version, its copyright notices, or its trademarks.
ms.assetid: fcc5ac68-4aec-4a3b-aa92-96fc50cc4ca2
keywords:
- String structure Menus and Other Resources
topic_type:
- apiref
api_name:
- String
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# String structure

Represents the organization of data in a file-version resource. It contains a string that describes a specific aspect of a file, for example, a file's version, its copyright notices, or its trademarks.

## Syntax


```C++
typedef struct {
  WORD  wLength;
  WORD  wValueLength;
  WORD  wType;
  WCHAR szKey;
  WORD  Padding;
  WORD  Value;
} String;
```



## Members

<dl> <dt>

**wLength**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The length, in bytes, of this **String** structure.

</dd> <dt>

**wValueLength**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The size, in words, of the **Value** member.

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

An arbitrary Unicode string. The **szKey** member can be one or more of the following values. These values are guidelines only.

<dt>

<span id="Comments"></span><span id="comments"></span><span id="COMMENTS"></span>

<span id="Comments"></span><span id="comments"></span><span id="COMMENTS"></span>**Comments**


</dt> <dd>

The **Value** member contains any additional information that should be displayed for diagnostic purposes. This string can be an arbitrary length.

</dd> <dt>

<span id="CompanyName"></span><span id="companyname"></span><span id="COMPANYNAME"></span>

<span id="CompanyName"></span><span id="companyname"></span><span id="COMPANYNAME"></span>**CompanyName**


</dt> <dd>

The **Value** member identifies the company that produced the file. For example, "Microsoft Corporation" or "Standard Microsystems Corporation, Inc."

</dd> <dt>

<span id="FileDescription"></span><span id="filedescription"></span><span id="FILEDESCRIPTION"></span>

<span id="FileDescription"></span><span id="filedescription"></span><span id="FILEDESCRIPTION"></span>**FileDescription**


</dt> <dd>

The **Value** member describes the file in such a way that it can be presented to users. This string may be presented in a list box when the user is choosing files to install. For example, "Keyboard driver for AT-style keyboards" or "Microsoft Word for Windows".

</dd> <dt>

<span id="FileVersion"></span><span id="fileversion"></span><span id="FILEVERSION"></span>

<span id="FileVersion"></span><span id="fileversion"></span><span id="FILEVERSION"></span>**FileVersion**


</dt> <dd>

The **Value** member identifies the version of this file. For example, **Value** could be "3.00A" or "5.00.RC2".

</dd> <dt>

<span id="InternalName"></span><span id="internalname"></span><span id="INTERNALNAME"></span>

<span id="InternalName"></span><span id="internalname"></span><span id="INTERNALNAME"></span>**InternalName**


</dt> <dd>

The **Value** member identifies the file's internal name, if one exists. For example, this string could contain the module name for a DLL, a virtual device name for a Windows virtual device, or a device name for a MS-DOS device driver.

</dd> <dt>

<span id="LegalCopyright"></span><span id="legalcopyright"></span><span id="LEGALCOPYRIGHT"></span>

<span id="LegalCopyright"></span><span id="legalcopyright"></span><span id="LEGALCOPYRIGHT"></span>**LegalCopyright**


</dt> <dd>

The **Value** member describes all copyright notices, trademarks, and registered trademarks that apply to the file. This should include the full text of all notices, legal symbols, copyright dates, trademark numbers, and so on. In English, this string should be in the format "Copyright Microsoft Corp. 1990  1994".

</dd> <dt>

<span id="LegalTrademarks"></span><span id="legaltrademarks"></span><span id="LEGALTRADEMARKS"></span>

<span id="LegalTrademarks"></span><span id="legaltrademarks"></span><span id="LEGALTRADEMARKS"></span>**LegalTrademarks**


</dt> <dd>

The **Value** member describes all trademarks and registered trademarks that apply to the file. This should include the full text of all notices, legal symbols, trademark numbers, and so on. In English, this string should be in the format "Windows is a trademark of Microsoft Corporation".

</dd> <dt>

<span id="OriginalFilename"></span><span id="originalfilename"></span><span id="ORIGINALFILENAME"></span>

<span id="OriginalFilename"></span><span id="originalfilename"></span><span id="ORIGINALFILENAME"></span>**OriginalFilename**


</dt> <dd>

The **Value** member identifies the original name of the file, not including a path. This enables an application to determine whether a file has been renamed by a user. This name may not be MS-DOS 8.3-format if the file is specific to a non-FAT file system.

</dd> <dt>

<span id="PrivateBuild"></span><span id="privatebuild"></span><span id="PRIVATEBUILD"></span>

<span id="PrivateBuild"></span><span id="privatebuild"></span><span id="PRIVATEBUILD"></span>**PrivateBuild**


</dt> <dd>

The **Value** member describes by whom, where, and why this private version of the file was built. This string should only be present if the **VS\_FF\_PRIVATEBUILD** flag is set in the **dwFileFlags** member of the [**VS\_FIXEDFILEINFO**](/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo) structure. For example, **Value** could be "Built by OSCAR on \\OSCAR2".

</dd> <dt>

<span id="ProductName"></span><span id="productname"></span><span id="PRODUCTNAME"></span>

<span id="ProductName"></span><span id="productname"></span><span id="PRODUCTNAME"></span>**ProductName**


</dt> <dd>

The **Value** member identifies the name of the product with which this file is distributed. For example, this string could be "Microsoft Windows".

</dd> <dt>

<span id="ProductVersion"></span><span id="productversion"></span><span id="PRODUCTVERSION"></span>

<span id="ProductVersion"></span><span id="productversion"></span><span id="PRODUCTVERSION"></span>**ProductVersion**


</dt> <dd>

The **Value** member identifies the version of the product with which this file is distributed. For example, **Value** could be "3.00A" or "5.00.RC2".

</dd> <dt>

<span id="SpecialBuild"></span><span id="specialbuild"></span><span id="SPECIALBUILD"></span>

<span id="SpecialBuild"></span><span id="specialbuild"></span><span id="SPECIALBUILD"></span>**SpecialBuild**


</dt> <dd>

The **Value** member describes how this version of the file differs from the normal version. This entry should only be present if the **VS\_FF\_SPECIALBUILD** flag is set in the **dwFileFlags** member of the [**VS\_FIXEDFILEINFO**](/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo) structure. For example, **Value** could be "Private build for Olivetti solving mouse problems on M250 and M250E computers".

</dd> </dl> </dd> <dt>

**Padding**
</dt> <dd>

Type: **WORD**

</dd> <dd>

As many zero words as necessary to align the **Value** member on a 32-bit boundary.

</dd> <dt>

**Value**
</dt> <dd>

Type: **WORD**

</dd> <dd>

A zero-terminated string. See the **szKey** member description for more information.

</dd> </dl>

## Remarks

This structure is not a true C-language structure because it contains variable-length members. This structure was created solely to depict the organization of data in a version resource and does not appear in any of the header files shipped with the Windows Software Development Kit (SDK).

A **String** structure may have an **szKey** value of, for example, "CompanyName" and a **Value** of "Microsoft Corporation". Another **String** structure with the same **szKey** value could contain a **Value** of "Microsoft GmbH". This might occur if the second **String** structure were associated with a [**StringTable**](stringtable.md) structure whose **szKey** value is 040704b0   that is, German/Unicode.

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

[**VS\_FIXEDFILEINFO**](/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo)
</dt> <dt>

[**StringFileInfo**](stringfileinfo.md)
</dt> <dt>

[**VS\_VERSIONINFO**](vs-versioninfo.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Version Information](version-information.md)
</dt> </dl>

 

 





