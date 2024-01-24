---
title: ICONRESDIR structure
description: Contains the dimensions and color format of an individual icon image in a resource group. The structure definition provided here is for explanation only; it is not present in any standard header file.
ms.assetid: 4c727369-2e90-40ad-85af-96d7e060b97a
keywords:
- ICONRESDIR structure Menus and Other Resources
topic_type:
- apiref
api_name:
- ICONRESDIR
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ICONRESDIR structure

Contains the dimensions and color format of an individual icon image in a resource group.

The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  BYTE Width;
  BYTE Height;
  BYTE ColorCount;
  BYTE reserved;
} ICONRESDIR;
```

## Members

<dl> <dt>

**Width**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The width of the icon, in pixels.
  
The value 0 is accepted as representing a width of 256.

</dd> <dt>

**Height**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The height of the icon, in pixels.
  
The value 0 is accepted as representing a height of 256.

</dd> <dt>

**ColorCount**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The number of colors in the icon.
  
Acceptable values are 2, 8, and 16. The value 0 means that the number of colors deduced from **BitCount** and **Planes** in the [**RESDIR**](resdir.md) structure.

</dd> <dt>

**reserved**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

Reserved; must be set to the same value as that of the reserved field in the icon file header.

</dd> </dl>

## Remarks

The **ICONRESDIR** structure is passed in the [**RESDIR**](resdir.md) structure if the **RESDIR** structure describes an icon.

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

 

 





