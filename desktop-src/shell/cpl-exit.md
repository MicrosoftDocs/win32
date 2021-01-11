---
description: Sent once to the CPlApplet function of a Control Panel application before the DLL containing the Control Panel application is released.
ms.assetid: 1afcb0d3-41a7-4fd8-9561-d96e1e8f0ddb
title: CPL_EXIT message (Cpl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CPL\_EXIT message

Sent once to the [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function of a Control Panel application before the DLL containing the Control Panel application is released.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

If the [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function processes this message successfully, it should return zero.

## Remarks

This message is sent after the last [**CPL\_STOP**](cpl-stop.md) message is sent.

In response to this message, a Control Panel application must free any memory that it has allocated and perform global-level cleanup.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Cpl.h</dt> </dl> |



## See also

<dl> <dt>

[**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary)
</dt> </dl>

 

 
