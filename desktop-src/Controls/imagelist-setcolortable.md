---
title: ImageList_SetColorTable function
description: Sets the color table for an image list.
ms.assetid: 1b62f468-cbc4-479b-b9f8-5553c2bd8c79
keywords:
- ImageList_SetColorTable function Windows Controls
topic_type:
- apiref
api_name:
- ImageList_SetColorTable
api_location:
- Comctl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ImageList\_SetColorTable function

Sets the color table for an image list.

## Syntax


```C++
int ImageList_SetColorTable(
  _In_ HIMAGELIST himl,
  _In_ int        start,
  _In_ int        len,
  _In_ RGBQUAD    *prgb
);
```



## Parameters

<dl> <dt>

*himl* \[in\]
</dt> <dd>

Type: **HIMAGELIST**

A handle to the image list.

</dd> <dt>

*start* \[in\]
</dt> <dd>

Type: **int**

A zero-based color table index that specifies the first color table entry to set.

</dd> <dt>

*len* \[in\]
</dt> <dd>

Type: **int**

The number of color table entries to set.

</dd> <dt>

*prgb* \[in\]
</dt> <dd>

Type: **[**RGBQUAD**](/windows/win32/api/wingdi/ns-wingdi-rgbquad)\***

A pointer to an array of *len* [**RGBQUAD**](/windows/win32/api/wingdi/ns-wingdi-rgbquad) structures containing new color information for the color table of the DIB.

</dd> </dl>

## Return value

Type: **int**

If the function succeeds, it returns the number of color table entries set by the function. If the function fails, the return value is less than or equal to zero.

## Remarks

Only image lists created with the [**ILC\_COLOR4**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_create) or [**ILC\_COLOR8**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_create) flag have color tables. The color table of such an image list is typically set automatically by copying the color table of the first image added to the list (for example, through the [**ImageList\_Add**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_add) function) if that image is a DIB. If the first image added to the image list is not a DIB, then the color table of the halftone palette is used for **ILC\_COLOR8** image lists and the VGA color table is used for **ILC\_COLOR4**.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                            |
| DLL<br/>                      | <dl> <dt>Comctl32.dll (version 3.51 or later)</dt> </dl> |



## See also

<dl> <dt>

[Color Table](https://msdn.microsoft.com/library/ms531197(v=VS.85).aspx)
</dt> </dl>

 

