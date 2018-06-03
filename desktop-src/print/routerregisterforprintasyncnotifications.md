---
Description: The RouterRegisterForPrintAsyncNotifications function registers for asynchronous notifications associated with a printer or print server.
ms.assetid: 87966827-72b2-4be7-859a-628c1accca48
title: RouterRegisterForPrintAsyncNotifications function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RouterRegisterForPrintAsyncNotifications function

The `RouterRegisterForPrintAsyncNotifications` function registers for asynchronous notifications associated with a printer or print server.

## Syntax


```C++
HRESULT RouterRegisterForPrintAsyncNotifications(
  _In_  PCWSTR                            pName,
  _In_  PrintAsyncNotificationType        *pNotificationType,
  _In_  PrintAsyncNotifyUserFilter        eNotifyFilter,
  _In_  PrintAsyncNotifyConversationStyle eConversationStyle,
  _In_  IPrintAsyncNotifyCallback         *pCallback,
  _Out_ HANDLE                            *phNotify
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

A pointer to the GUID that represents the type of notifications of interest to the caller.

</dd> <dt>

*eNotifyFilter* \[in\]
</dt> <dd>

The filter for the session or user of interest to the caller when receiving notifications.

</dd> <dt>

*eConversationStyle* \[in\]
</dt> <dd>

The type of communication: unidirectional or bidirectional.

</dd> <dt>

*pCallback* \[in\]
</dt> <dd>

A pointer to the callback that is used deliver the notifications.

</dd> <dt>

*phNotify* \[out\]
</dt> <dd>

A pointer to an opaque handle. The caller can use this handle to discontinue receiving notifications.

</dd> </dl>

## Return value

This function returns S\_OK on success, and a standard COM error code otherwise.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prnasntp.h (include Prnasntp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Spoolss.lib</dt> </dl>                     |
| DLL<br/>             | <dl> <dt>Spoolss.dll</dt> </dl>                     |



## See also

<dl> <dt>

[**RouterUnregisterForPrintAsyncNotifications**](routerunregisterforprintasyncnotifications.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20RouterRegisterForPrintAsyncNotifications%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





