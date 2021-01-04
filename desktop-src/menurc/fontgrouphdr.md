---
title: FONTGROUPHDR structure
description: Contains the information necessary for an application to access a specific font. The structure definition provided here is for explanation only; it is not present in any standard header file.
ms.assetid: 180b3dfd-3f20-4100-b45b-2f253b7c0582
keywords:
- FONTGROUPHDR structure Menus and Other Resources
topic_type:
- apiref
api_name:
- FONTGROUPHDR
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# FONTGROUPHDR structure

Contains the information necessary for an application to access a specific font. The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  WORD     NumberOfFonts;
  DIRENTRY DE;
} FONTGROUPHDR;
```



## Members

<dl> <dt>

**NumberOfFonts**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The number of individual fonts associated with this resource.

</dd> <dt>

**DE**
</dt> <dd>

Type: **[**DIRENTRY**](direntry.md)**

</dd> <dd>

A structure that contains a unique ordinal identifier for each font in the resource. The **DE** member is a placeholder for the variable-length array of [**DIRENTRY**](direntry.md) structures.

</dd> </dl>

## Remarks

The **FONTGROUPHDR** structure follows the data for the individual fonts in the .Res file. The resource compiler automatically adds the **FONTGROUPHDR** structure, generally as the last entry in the file.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DIRENTRY**](direntry.md)
</dt> <dt>

[**FONTDIRENTRY**](fontdirentry.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> </dl>

 

 





