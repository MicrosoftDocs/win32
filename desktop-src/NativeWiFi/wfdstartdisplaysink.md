---
description: Performs the necessary initialization to allow the calling app to become a Miracast display sink.
ms.assetid: D87B427B-0B7F-44BB-BC34-726FDF87CCCC
title: WFDDisplaySinkStart function (Wfdsink.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WFDStartDisplaySink
api_type: 
- DllExport
api_location: 
- wifidisplay.dll
---

# WFDDisplaySinkStart function

Performs the necessary initialization to allow the calling app to become a Miracast display sink. Your app should call this once on startup.

## Syntax


```C++
DWORD WINAPI WFDStartDisplaySink(
  _In_     USHORT                                 uDeviceCategory,
  _In_     USHORT                                 uSubCategory,
  _In_opt_ PVOID                                  pCallbackContext,
  _In_     WFD_DISPLAY_SINK_NOTIFICATION_CALLBACK *pfnCallback
);
```



## Parameters

<dl> <dt>

*uDeviceCategory* \[in\]
</dt> <dd>

The device category.

</dd> <dt>

*uSubCategory* \[in\]
</dt> <dd>

The device subcategory.

</dd> <dt>

*pCallbackContext* \[in, optional\]
</dt> <dd>

An optional context pointer which is passed to the callback function specified in the *pfnCallback* parameter.

</dd> <dt>

*pfnCallback* \[in\]
</dt> <dd>

A pointer to the callback function to be called whenever there is a notification for the app. Notifications that can be sent are described in [**WFD\_DISPLAY\_SINK\_NOTIFICATION\_CALLBACK**](wfd-display-sink-notification-callback.md).

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value may be one of the following return codes.



| Return code                                                                                          | Description                                                    |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>**ERROR\_NOT\_SUPPORTED**</dt> </dl> | The display sink is not supported on this hardware.<br/> |



 

## Remarks

This function performs the following tasks:

-   Makes the PC discoverable
-   Sets the P2P device info to reflect the category and sub category specified
-   Sets the Miracast IEs on all Wi-Fi Direct frames with the device type as the sink
-   Registers the specified callback to be invoked whenever there is an incoming connection

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

 

 




