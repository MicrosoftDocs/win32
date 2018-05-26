---
title: TB\_BUTTONSTRUCTSIZE message
description: Specifies the size of the TBBUTTON structure.
ms.assetid: 4e63a075-4191-44c1-8df6-38fce51d4be5
keywords:
- TB_BUTTONSTRUCTSIZE message Windows Controls
topic_type:
- apiref
api_name:
- TB_BUTTONSTRUCTSIZE
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

# TB\_BUTTONSTRUCTSIZE message

Specifies the size of the [**TBBUTTON**](/windows/win32/Commctrl/ns-commctrl-_tbbutton?branch=master) structure.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Size, in bytes, of the [**TBBUTTON**](/windows/win32/Commctrl/ns-commctrl-_tbbutton?branch=master) structure.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

No return value.

## Remarks

The system uses the size to determine which version of the common control dynamic-link library (DLL) is being used.

If an application uses the [**CreateWindowEx**](https://msdn.microsoft.com/library/windows/desktop/ms632680) function to create the toolbar, the application must send this message to the toolbar before sending the [**TB\_ADDBITMAP**](tb-addbitmap.md) or [**TB\_ADDBUTTONS**](tb-addbuttons.md) message. The [**CreateToolbarEx**](/windows/win32/Commctrl/nf-commctrl-createtoolbarex?branch=master) function automatically sends **TB\_BUTTONSTRUCTSIZE**, and the size of the [**TBBUTTON**](/windows/win32/Commctrl/ns-commctrl-_tbbutton?branch=master) structure is a parameter of the function.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





