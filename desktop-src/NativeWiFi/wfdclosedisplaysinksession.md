---
description: Cleans up the state for the session being opened, or the currently open session.
ms.assetid: 8247AFA9-F471-4CCD-972D-D0C827E86880
title: WFDDisplaySinkCloseSession function (Wfdsink.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WFDCloseDisplaySinkSession
api_type: 
- DllExport
api_location: 
- wifidisplay.dll
---

# WFDDisplaySinkCloseSession function

Cleans up the state for the session being opened, or the currently open session.

## Syntax


```C++
DWORD WINAPI WFDCloseDisplaySinkSession(
  _In_ HANDLE hSessionHandle
);
```



## Parameters

<dl> <dt>

*hSessionHandle* \[in\]
</dt> <dd>

The handle received via the most recent [**WFD\_DISPLAY\_SINK\_NOTIFICATION\_CALLBACK**](wfd-display-sink-notification-callback.md) invocation that included one.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

## Remarks

Your app can call this function to terminate the Miracast session for any reason. Your app is not required to call it when it receives the **DisconnectedNotification** type in its callback.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows 10<br/>                                                                      |
| End of server support<br/>    | Windows Server 2016<br/>                                                             |
| Header<br/>                   | <dl> <dt>Wfdsink.h</dt> </dl>       |
| Library<br/>                  | <dl> <dt>Wifidisplay.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wifidisplay.dll</dt> </dl> |



## See also

<dl> <dt>

[**WFD\_DISPLAY\_SINK\_NOTIFICATION\_CALLBACK**](wfd-display-sink-notification-callback.md)
</dt> </dl>

 

 




