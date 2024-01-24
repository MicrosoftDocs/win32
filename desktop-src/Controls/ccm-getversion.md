---
title: CCM_GETVERSION message (Commctrl.h)
description: Gets the version number for a control set by the most recent CCM\_SETVERSION message.
ms.assetid: c4b401d7-bba0-430c-b368-c363d49b3411
keywords:
- CCM_GETVERSION message Windows Controls
topic_type:
- apiref
api_name:
- CCM_GETVERSION
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CCM\_GETVERSION message

Gets the version number for a control set by the most recent [**CCM\_SETVERSION**](ccm-setversion.md) message.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the version number set by the most recent [**CCM\_SETVERSION**](ccm-setversion.md) message. If no such message has been sent, it returns zero.

## Remarks

This message does not return the DLL version. See [Shell Versions](common-control-versions.md) for a discussion of how to use [**DllGetVersion**](/windows/desktop/api/shlwapi/nc-shlwapi-dllgetversionproc) to retrieve the current DLL version.

> [!Note]  
> The version number is set on a control by control basis, and may not be the same for all controls.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

