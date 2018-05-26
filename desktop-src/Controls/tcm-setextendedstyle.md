---
title: TCM\_SETEXTENDEDSTYLE message
description: Sets the extended styles that the tab control will use. You can send this message explicitly or by using the TabCtrl\_SetExtendedStyle macro.
ms.assetid: 96ccebe1-2836-4198-8cd7-858401562c21
keywords:
- TCM_SETEXTENDEDSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- TCM_SETEXTENDEDSTYLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TCM\_SETEXTENDEDSTYLE message

Sets the extended styles that the tab control will use. You can send this message explicitly or by using the [**TabCtrl\_SetExtendedStyle**](/windows/win32/Commctrl/nf-commctrl-tabctrl_setextendedstyle?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A **DWORD** value that indicates which styles in *lParam* are to be affected. Only the extended styles in *wParam* will be changed. All other styles will be maintained as they are. If this parameter is zero, then all of the styles in *lParam* will be affected.

</dd> <dt>

*lParam* 
</dt> <dd>

Value specifying the extended tab control styles. This value is a combination of tab control [extended styles](tab-control-extended-styles.md).

</dd> </dl>

## Return value

Returns a **DWORD** value that contains the previous tab control extended styles.

## Remarks

The *wParam* parameter allows you to modify one or more extended styles without having to retrieve the existing styles first. For example, if you pass [**TCS\_EX\_FLATSEPARATORS**](tab-control-extended-styles.md#tcs-ex-flatseparators) for *wParam* and 0 for *lParam*, the **TCS\_EX\_FLATSEPARATORS** style will be cleared, but all other styles will remain the same.

For backward compatibility reasons, the [**TabCtrl\_SetExtendedStyle**](/windows/win32/Commctrl/nf-commctrl-tabctrl_setextendedstyle?branch=master) macro has not been updated to use *dwExMask*.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TCM\_GETEXTENDEDSTYLE**](tcm-getextendedstyle.md)
</dt> </dl>

 

 





