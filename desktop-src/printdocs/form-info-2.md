---
description: Contains information about a localizable print form.
ms.assetid: 5cc11a77-2b9d-44a4-88de-6ed0b7460bc8
title: FORM_INFO_2 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FORM_INFO_2
- _FORM_INFO_2A
- _FORM_INFO_2W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# FORM\_INFO\_2 structure

Contains information about a localizable print form.

## Syntax


```C++
typedef struct _FORM_INFO_2 {
  DWORD   Flags;
  LPTSTR  pName;
  SIZEL   Size;
  RECTL   ImageableArea;
  LPCSTR  pKeyword;
  DWORD   StringType;
  LPCTSTR pMuiDll;
  DWORD   dwResourceId;
  LPCTSTR pDisplayName;
  LANGID  wLangId;
} FORM_INFO_2, *PFORM_INFO_2;
```



## Members

<dl> <dt>

**Flags**
</dt> <dd>

The form properties. The following values are defined, but only one can be set. When the **FORM\_INFO\_2** is returned by [**GetForm**](getform.md) or [**EnumForms**](enumforms.md), **Flags** is set to the current value in the forms database.



| Value         | Meaning                                                                                                                                                                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FORM\_USER    | If this bit flag is set, the form has been defined by the user. Forms with this flag set are defined in the registry.                                                                                                                                                                    |
| FORM\_BUILTIN | If this bit-flag is set, the form is part of the spooler. Form definitions with this flag set do not appear in the registry. Built-in forms cannot be modified, so this flag should not be set when the structure is passed to [**AddForm**](addform.md) or [**SetForm**](setform.md). |
| FORM\_PRINTER | If this bit flag is set, the form is associated with a certain printer, and its definition appears in the registry.                                                                                                                                                                      |



 

</dd> <dt>

**pName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the form. The form name cannot exceed 31 characters.

</dd> <dt>

**Size**
</dt> <dd>

The width and height of the form in thousandths of millimeters.

</dd> <dt>

**ImageableArea**
</dt> <dd>

The width and height, in thousandths of millimeters, of the area of the page on which the printer can print.

</dd> <dt>

**pKeyword**
</dt> <dd>

A pointer to a non-localizable string identifier of the form. When passed to [**AddForm**](addform.md) or [**SetForm**](setform.md), this gives the caller a means of identifying the form in all locales.

</dd> <dt>

**StringType**
</dt> <dd>

Specifies how a localized display name for the form is obtained at runtime. The following values are defined. Only one can be set in any given call to [**AddForm**](addform.md) or [**SetForm**](setform.md). Both STRING\_MUIDLL and STRING\_LANGPAIR can be set in the **FORM\_INFO\_2** (s) returned by [**GetForm**](getform.md) or [**EnumForms**](enumforms.md). See Remarks.



| Value            | Meaning                                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STRING\_NONE     | There is no localized display name.                                                                                                                                                            |
| STRING\_MUIDLL   | The display name is extracted from the [Multilingual User Interface](/windows/desktop/Intl/mui-resource-management) localized resources DLL specified in **pMuiDll**. The ID is in the **dwResourceId** member. |
| STRING\_LANGPAIR | The display name and language ID are provided directly by **pDisplayName** and the language is specified by **wLangId**.                                                                       |



 

</dd> <dt>

**pMuiDll**
</dt> <dd>

The [Multilingual User Interface](/windows/desktop/Intl/mui-resource-management) localized resource DLL that contains the localized display name.

</dd> <dt>

**dwResourceId**
</dt> <dd>

The resource ID of the form's display name in **pMuiDll**.

</dd> <dt>

**pDisplayName**
</dt> <dd>

The form's display name in the language specified by **wLangId**.

</dd> <dt>

**wLangId**
</dt> <dd>

The language of the **pDisplayName**.

</dd> </dl>

## Remarks

On a call to [**AddForm**](addform.md) or [**SetForm**](setform.md):

-   If **StringType** is STRING\_NONE, both **pMuiDll** and **pDisplayName** must be **NULL** and both **dwResourceId** and **wLangId** must be 0.
-   If **StringType** is STRING\_MUIDLL, **pDisplayName** must be **NULL** and **wLangId** must be 0.
-   If **StringType** is STRING\_LANGPAIR, **pMuiDll** must be **NULL** and **dwResourceId** must be 0.

For a **FORM\_INFO\_2** returned by a call to [**GetForm**](getform.md) or [**EnumForms**](enumforms.md):

-   If **StringType** is both STRING\_MUIDLL and STRING\_LANGPAIR, **pMuiDll**, **pDisplayName**, **dwResourceId**, and **wLangId** will all have valid values.
-   If **StringType** is STRING\_MUIDLL only, **pMuiDll** and **dwResourceId** will have valid values. **pDisplayName** will be **NULL** and **wLangId** will be 0.
-   If **StringType** is STRING\_LANGPAIR only, **pDisplayName** and **wLangId** will have valid values. **pMuiDll** will be **NULL** and **dwResourceId** will be 0.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_FORM\_INFO\_2W** (Unicode) and **\_FORM\_INFO\_2A** (ANSI)<br/>                                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[Multilingual User Interface](/windows/desktop/Intl/mui-resource-management)
</dt> <dt>

[**AddForm**](addform.md)
</dt> <dt>

[**GetForm**](getform.md)
</dt> <dt>

[**EnumForms**](enumforms.md)
</dt> <dt>

[**SetForm**](setform.md)
</dt> </dl>

 

