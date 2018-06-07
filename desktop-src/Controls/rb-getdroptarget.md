---
title: RB\_GETDROPTARGET message
description: Retrieves a rebar control's IDropTarget interface pointer.
ms.assetid: f429c5d1-406b-47f0-a654-47cabccc1d0e
keywords:
- RB_GETDROPTARGET message Windows Controls
topic_type:
- apiref
api_name:
- RB_GETDROPTARGET
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

# RB\_GETDROPTARGET message

Retrieves a rebar control's [**IDropTarget**](https://msdn.microsoft.com/library/windows/desktop/ms679679) interface pointer.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**IDropTarget**](https://msdn.microsoft.com/library/windows/desktop/ms679679) pointer that receives the interface pointer. It is the caller's responsibility to call [**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) on this pointer when it is no longer needed.

</dd> </dl>

## Return value

The return value for this message is not used.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





