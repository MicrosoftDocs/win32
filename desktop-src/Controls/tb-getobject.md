---
title: TB_GETOBJECT message (Commctrl.h)
description: Retrieves the IDropTarget for a toolbar control.
ms.assetid: b26394ea-6f0f-4084-956d-f9166cc54b76
keywords:
- TB_GETOBJECT message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETOBJECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETOBJECT message

Retrieves the [**IDropTarget**](/windows/desktop/api/oleidl/nn-oleidl-idroptarget) for a toolbar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Identifier of the interface being requested. This value must point to **IID\_IDropTarget**.

</dd> <dt>

*lParam* 
</dt> <dd>

Address that receives the interface pointer. If an error occurs, a **NULL** pointer is placed in this address.

</dd> </dl>

## Return value

Returns an **HRESULT** value indicating success or failure of the operation.

## Remarks

The toolbar's [**IDropTarget**](/windows/desktop/api/oleidl/nn-oleidl-idroptarget) is used by the toolbar when objects are dragged over or dropped onto it.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

