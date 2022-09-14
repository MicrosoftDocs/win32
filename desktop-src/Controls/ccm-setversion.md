---
title: CCM_SETVERSION message (Commctrl.h)
description: This message is used to inform the control that you are expecting a behavior associated with a particular version.
ms.assetid: f87b20bc-0139-4d0a-b38c-32c75743d6f6
keywords:
- CCM_SETVERSION message Windows Controls
topic_type:
- apiref
api_name:
- CCM_SETVERSION
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CCM\_SETVERSION message

This message is used to inform the control that you are expecting a behavior associated with a particular version.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The version number.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the version specified in the previous **CCM\_SETVERSION** message. If *wParam* is set to a value greater than the current DLL version, it returns -1.

## Remarks

In a few cases, a control may behave differently, depending on the version. This primarily applies to bugs that were fixed in later versions. The **CCM\_SETVERSION** message enables you to inform the control which behavior is expected. You can determine which version you have specified by sending a [**CCM\_GETVERSION**](ccm-getversion.md) message. For an example of how to use this message, see [Custom Draw With List-View and Tree-View Controls](custom-draw.md).

If you have ComCtl32.dll version 6 installed, regardless of what value you set in *wParam*, the **CCM\_SETVERSION** message returns version 6.

> [!Note]  
> This message only sets the version number for the control to which it is sent.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





