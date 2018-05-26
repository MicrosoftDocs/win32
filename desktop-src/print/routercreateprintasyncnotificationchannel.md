---
Description: The RouterCreatePrintAsyncNotificationChannel function creates an asynchronous notification channel that is associated with a printer or print server.
ms.assetid: 11f9a438-861f-42ef-b4f5-f64b0b9d658a
title: RouterCreatePrintAsyncNotificationChannel function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RouterCreatePrintAsyncNotificationChannel function

The `RouterCreatePrintAsyncNotificationChannel` function creates an asynchronous notification channel that is associated with a printer or print server.

## Syntax


```C++
HRESULT RouterCreatePrintAsyncNotificationChannel(
  _In_  PCWSTR                            pName,
  _In_  PrintAsyncNotificationType        *pNotificationType,
  _In_  PrintAsyncNotifyUserFilter        eNotificationFilter,
  _In_  PrintAsyncNotifyConversationStyle eConversationStyle,
  _In_  IPrintAsyncNotifyCallback         *pCallback,
  _Out_ IPrintAsyncNotifyChannel          **ppIAsyncNotification
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the printer or print server.

</dd> <dt>

*pNotificationType* \[in\]
</dt> <dd>

A pointer to a GUID that represents the type of notifications sent through this channel.

</dd> <dt>

*eNotificationFilter* \[in\]
</dt> <dd>

A filter for the session or user that receives the notifications.

</dd> <dt>

*eConversationStyle* \[in\]
</dt> <dd>

The type of communication: unidirectional or bidirectional.

</dd> <dt>

*pCallback* \[in\]
</dt> <dd>

A pointer to the callback function that is called to deliver the response notifications, when bidirectional communication is in effect. This parameter is ignored when unidirectional communication is in effect.

</dd> <dt>

*ppIAsyncNotification* \[out\]
</dt> <dd>

A pointer to a variable that receives the address of the interface object that represents the notification channel.

</dd> </dl>

## Return value

`RouterCreatePrintAsyncNotificationChannel` returns S\_OK on success and returns a standard COM error code otherwise.

## Remarks

In some cases, you must release the channel that you created with the `RouterCreatePrintAsyncNotificationChannel` function by calling **Release** on IPrintAsyncNotifyChannel. For information about when to release a channel, see [Notification Channel](print.notification_channel).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prnasntp.h (include Prnasntp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Spoolss.lib</dt> </dl>                     |
| DLL<br/>             | <dl> <dt>Spoolss.dll</dt> </dl>                     |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20RouterCreatePrintAsyncNotificationChannel%20%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




