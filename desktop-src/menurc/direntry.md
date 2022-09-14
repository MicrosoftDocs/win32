---
title: DIRENTRY structure
description: Contains a unique ordinal that identifies an individual font in the font resource group. The structure definition provided here is for explanation only; it is not present in any standard header file.
ms.assetid: 4afc561e-bc98-4968-9a00-5002870b0c5e
keywords:
- DIRENTRY structure Menus and Other Resources
topic_type:
- apiref
api_name:
- DIRENTRY
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DIRENTRY structure

Contains a unique ordinal that identifies an individual font in the font resource group. The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  WORD fontOrdinal;
} DIRENTRY;
```



## Members

<dl> <dt>

**fontOrdinal**
</dt> <dd>

Type: **WORD**

</dd> <dd>

A unique ordinal identifier for an individual font in a font resource group.

</dd> </dl>

## Remarks

The [**FONTDIRENTRY**](fontdirentry.md) structure for the specified font directly follows the **DIRENTRY** structure for that font.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**FONTDIRENTRY**](fontdirentry.md)
</dt> <dt>

[**FONTGROUPHDR**](fontgrouphdr.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> </dl>

 

 





