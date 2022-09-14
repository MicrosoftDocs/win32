---
description: The FORM_INFO_1 structure contains information about a print form. The information includes the print forms origin, its name, its dimensions, and the dimensions of its printable area.
ms.assetid: 1c42ea6c-82cf-463c-bc67-44a8d8c4a1e7
title: FORM_INFO_1 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FORM_INFO_1
- _FORM_INFO_1A
- _FORM_INFO_1W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# FORM_INFO_1 structure

The **FORM_INFO_1** structure contains information about a print form. The information includes the print form's origin, its name, its dimensions, and the dimensions of its printable area.

## Syntax


```C++
typedef struct _FORM_INFO_1 {
  DWORD  Flags;
  LPTSTR pName;
  SIZEL  Size;
  RECTL  ImageableArea;
} FORM_INFO_1, *PFORM_INFO_1;
```



## Members

<dl> <dt>

**Flags**
</dt> <dd>

The form properties. The following values are defined.



| Value         | Meaning                                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------------------------|
| FORM_USER    | If this bit flag is set, the form has been defined by the user. Forms with this flag set are defined in the registry.        |
| FORM_BUILTIN | If this bit-flag is set, the form is part of the spooler. Form definitions with this flag set do not appear in the registry. |
| FORM_PRINTER | If this bit flag is set, the form is associated with a certain printer, and its definition appears in the registry.          |



 

</dd> <dt>

**pName**
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the form. The form name cannot exceed 31 characters.

</dd> <dt>

**Size**
</dt> <dd>

The width and height, in thousandths of millimeters, of the form.

</dd> <dt>

**ImageableArea**
</dt> <dd>

The width and height, in thousandths of millimeters, of the form.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **_FORM_INFO_1W** (Unicode) and **_FORM_INFO_1A** (ANSI)<br/>                                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**AddForm**](addform.md)
</dt> <dt>

[**GetForm**](getform.md)
</dt> <dt>

[**SetForm**](setform.md)
</dt> </dl>

 

 




