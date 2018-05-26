---
Description: A stream-control start command has taken effect.
ms.assetid: e2f8d9a2-c96c-457c-8a88-7c86d4405928
title: EC\_STREAM\_CONTROL\_STARTED
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EC\_STREAM\_CONTROL\_STARTED

A stream-control start command has taken effect.

## Parameters

<dl> <dt>

<span id="pSender"></span><span id="psender"></span><span id="PSENDER"></span>*pSender*
</dt> <dd>

(**IUnknown**\*) Pointer to the [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master) interface of the pin that started the stream.

</dd> <dt>

<span id="dwCookie"></span><span id="dwcookie"></span><span id="DWCOOKIE"></span>*dwCookie*
</dt> <dd>

(**DWORD**) User-defined value.

</dd> </dl>

## Default Action

None.

## Remarks

Filters send this event in response to the [**IAMStreamControl::StartAt**](/windows/win32/Strmif/nf-strmif-iamstreamcontrol-startat?branch=master) method. This method specifies a reference time for a pin to begin streaming. When streaming does begin, the filter sends this event.

The *pSender* parameter specifies the pin that executes the start command. Depending on the implementation, it might not be the pin that received the [**StartAt**](/windows/win32/Strmif/nf-strmif-iamstreamcontrol-startat?branch=master) call.

The *dwCookie* parameter is specified by the application in the [**StartAt**](/windows/win32/Strmif/nf-strmif-iamstreamcontrol-startat?branch=master) method. This parameter enables the application to track multiple calls to the method.

## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 




