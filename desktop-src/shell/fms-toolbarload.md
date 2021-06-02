---
description: Contains information about custom buttons to be added to the File Manager toolbar. The buttons are provided by a File Manager extension DLL.
title: FMS_TOOLBARLOAD structure (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FMS_TOOLBARLOAD
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: 7185f9e5-10c6-43cc-b85b-cd077378338f

---

# FMS\_TOOLBARLOAD structure

Contains information about custom buttons to be added to the File Manager toolbar. The buttons are provided by a File Manager extension DLL.

## Syntax


```C++
typedef struct _FMS_TOOLBARLOAD {
  DWORD        dwSize;
  LPEXT_BUTTON lpButtons;
  WORD         cButtons;
  WORD         cBitmaps;
  WORD         idBitmap;
  HBITMAP      hBitmap;
} FMS_TOOLBARLOAD;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The size, in bytes, of the structure. File Manager sets the size before calling the extension and checks the size after the extension procedure returns.

</dd> <dt>

**lpButtons**
</dt> <dd>

Type: **LPEXT\_BUTTON**

</dd> <dd>

The address of an array of [**EXT\_BUTTON**](ext-button.md) structures.

</dd> <dt>

**cButtons**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The number of [**EXT\_BUTTON**](ext-button.md) structures in the array pointed to by the **lpButtons** member. This number equals the number of buttons and separators to add to the toolbar.

</dd> <dt>

**cBitmaps**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The number of buttons represented by the given bitmap.

</dd> <dt>

**idBitmap**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The identifier of a bitmap resource in the executable file for the extension DLL. The bitmap resource contains images for the number of buttons specified by **cBitmaps**. File Manager loads the bitmap resource and then uses it to display the buttons.

</dd> <dt>

**hBitmap**
</dt> <dd>

Type: **HBITMAP**

</dd> <dd>

A handle to a bitmap that File Manager will use to obtain and display button images if **idBitmap** is 0.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMEVENT\_TOOLBARLOAD**](fmevent-toolbarload.md)
</dt> </dl>

 

 




