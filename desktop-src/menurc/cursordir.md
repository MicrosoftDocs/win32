---
title: CURSORDIR structure
description: Contains the dimensions of an individual cursor image in a resource group. The structure definition provided here is for explanation only; it is not present in any standard header file.
ms.assetid: bc826fd6-74a2-470b-8d19-437cdeb0727d
keywords:
- CURSORDIR structure Menus and Other Resources
topic_type:
- apiref
api_name:
- CURSORDIR
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# CURSORDIR structure

Contains the dimensions of an individual cursor image in a resource group.

The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax

```C++
typedef struct {
  WORD Width;
  WORD Height;
} CURSORDIR;
```

## Members

<dl> <dt>

**Width**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The width of the cursor, in pixels.

The value 0 is accepted as representing a width of 256.

</dd> <dt>

**Height**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The height of the cursor, in pixels.

The value 0 is accepted as representing a height of 256.

</dd> </dl>

## Remarks

The **CURSORDIR** structure is passed in the [**RESDIR**](resdir.md) structure if the **RESDIR** structure describes a cursor.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**RESDIR**](resdir.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> </dl>

 

 





