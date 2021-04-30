---
description: Sent to the CPlApplet function of a Control Panel application to retrieve the number of dialog boxes supported by the application.
title: CPL_GETCOUNT message (Cpl.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 6b88b56c-aad7-4144-ab95-15d7eef21861
api_name: 
 - CPL_GETCOUNT
api_type: 
 - HeaderDef
api_location: 
 - Cpl.h
topic_type: 
 - APIRef
 - kbSyntax

---

# CPL\_GETCOUNT message

Sent to the [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function of a Control Panel application to retrieve the number of dialog boxes supported by the application.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

The [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function returns the number of dialog boxes that the Control Panel application supports.

## Remarks

This message is sent immediately after the [**CPL\_INIT**](cpl-init.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Cpl.h</dt> </dl> |



 

 
