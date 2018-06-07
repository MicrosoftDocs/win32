---
title: TB\_SETPADDING message
description: Sets the padding for a toolbar control.
ms.assetid: a18c4efb-1140-4149-8dce-dfc1f03bb61a
keywords:
- TB_SETPADDING message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETPADDING
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TB\_SETPADDING message

Sets the padding for a toolbar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) specifies the horizontal padding, in pixels. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the vertical padding, in pixels.

</dd> </dl>

## Return value

Returns a **DWORD** value that contains the previous horizontal padding in the [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) and the previous vertical padding in the [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657), in pixels.

## Remarks

The padding values are used to create a blank area between the edge of the button and the button's image and/or text. Where and how much padding is actually applied depends on the type of the button and whether it has an image. The horizontal padding is applied to both the right and left of the button, and the vertical padding is applied to both the top and bottom of the button. Padding is only applied to buttons that have the [**TBSTYLE\_AUTOSIZE**](toolbar-control-and-button-styles.md) style.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TB\_GETPADDING**](tb-getpadding.md)
</dt> </dl>

 

 





