---
title: RB\_GETRECT message
description: Retrieves the bounding rectangle for a given band in a rebar control.
ms.assetid: 'e272b090-1e4d-4cff-87f0-557ad8116e7e'
keywords: ["RB_GETRECT message Windows Controls"]
topic_type:
- apiref
api_name:
- RB_GETRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# RB\_GETRECT message

Retrieves the bounding rectangle for a given band in a rebar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of a band in the rebar control.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure that will receive the bounds of the rebar band.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





