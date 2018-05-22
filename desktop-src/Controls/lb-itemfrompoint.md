---
title: LB\_ITEMFROMPOINT message
description: Gets the zero-based index of the item nearest the specified point in a list box.
ms.assetid: '5739eccb-e708-4ddb-ac97-d3e6c6120842'
keywords: ["LB_ITEMFROMPOINT message Windows Controls"]
topic_type:
- apiref
api_name:
- LB_ITEMFROMPOINT
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# LB\_ITEMFROMPOINT message

Gets the zero-based index of the item nearest the specified point in a list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) specifies the x-coordinate of a point, relative to the upper-left corner of the client area of the list box.

The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the y-coordinate of a point, relative to the upper-left corner of the client area of the list box.

</dd> </dl>

## Return value

The return value contains the index of the nearest item in the [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659). The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) is zero if the specified point is in the client area of the list box, or one if it is outside the client area.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**MAKELPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632661)
</dt> </dl>

 

 





