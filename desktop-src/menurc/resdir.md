---
title: RESDIR structure
description: Contains information about an individual icon or cursor component in a resource group. There is one RESDIR structure for each group component. The structure definition provided here is for explanation only; it is not present in any standard header file.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\resources\introductiontoresources\resourcereference\resourcestructures\resdir.htm'
keywords:
- RESDIR structure Menus and Other Resources
topic_type:
- apiref
api_name:
- RESDIR
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RESDIR structure

Contains information about an individual icon or cursor component in a resource group. There is one **RESDIR** structure for each group component. The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  union
  {
      ICONRESDIR   Icon;
      CURSORDIR    Cursor;
  };
  WORD       Planes;
  WORD       BitCount;
  DWORD      BytesInRes;
  WORD       IconCursorId;
} RESDIR;
```



## Members

<dl> <dt>

**Icon**
</dt> <dd>

Type: **[**ICONRESDIR**](iconresdir.md)**

</dd> <dd>

The width, height, and color count of the indicated icon.

</dd> <dt>

**Cursor**
</dt> <dd>

Type: **[**CURSORDIR**](cursordir.md)**

</dd> <dd>

The width and height of the indicated cursor.

</dd> <dt>

**Planes**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The number of color planes in the icon or cursor bitmap.

</dd> <dt>

**BitCount**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The number of bits per pixel in the icon or cursor bitmap.

</dd> <dt>

**BytesInRes**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The size of the resource, in bytes.

</dd> <dt>

**IconCursorId**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The icon or cursor with a unique ordinal identifier.

</dd> </dl>

## Remarks

One or more **RESDIR** structures immediately follow the [**NEWHEADER**](newheader.md) structure in the .res file. The **ResCount** member of the **NEWHEADER** structure specifies the number of **RESDIR** structures. Note that the **RESDIR** structure consists of either an [**ICONRESDIR**](iconresdir.md) structure or a [**CURSORDIR**](cursordir.md) structure followed by the **Planes**, **BitCount**, **BytesInRes**, and **IconCursorId** members. If the **RESDIR** structure contains information about a cursor, the first two **WORD**s the resource compiler writes to the [RT\_CURSOR](/windows/desktop/menurc/resource-types) resource are the **xHotSpot** and **yHotSpot** members of the [**LOCALHEADER**](localheader.md) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CURSORDIR**](cursordir.md)
</dt> <dt>

[**ICONRESDIR**](iconresdir.md)
</dt> <dt>

[**LOCALHEADER**](localheader.md)
</dt> <dt>

[**NEWHEADER**](newheader.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> </dl>

 

