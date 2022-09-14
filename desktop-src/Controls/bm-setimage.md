---
title: BM_SETIMAGE message (Winuser.h)
description: Associates a new image (icon or bitmap) with the button.
ms.assetid: bf05e684-63d0-4583-960b-f329edafb151
keywords:
- BM_SETIMAGE message Windows Controls
topic_type:
- apiref
api_name:
- BM_SETIMAGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BM\_SETIMAGE message

Associates a new image (icon or bitmap) with the button.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The type of image to associate with the button. This parameter can be one of the following values:

-   IMAGE\_BITMAP
-   IMAGE\_ICON

</dd> <dt>

*lParam* 
</dt> <dd>

A handle (**HICON** or **HBITMAP**) to the image to associate with the button.

</dd> </dl>

## Return value

The return value is a handle to the image previously associated with the button, if any; otherwise, it is **NULL**.

## Remarks

The appearance of text, an icon, or both on a button control depends on the [**BS\_ICON**](button-styles.md) and [**BS\_BITMAP**](button-styles.md) styles, and whether the **BM\_SETIMAGE** message is called. The possible results are as follows:



| BS\_ICON or BS\_BITMAP Set? | BM\_SETIMAGE Called? | Result              |
|-----------------------------|----------------------|---------------------|
| Yes                         | Yes                  | Show icon only.     |
| No                          | Yes                  | Show icon and text. |
| Yes                         | No                   | Show text only.     |
| No                          | No                   | Show text only      |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**BM\_GETIMAGE**](bm-getimage.md)
</dt> </dl>

 

 





