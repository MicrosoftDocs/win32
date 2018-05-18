---
Description: 'A device error has occurred in an audio renderer filter.'
ms.assetid: '60e36476-f553-468d-a28d-351fdf4a02f1'
title: 'EC\_SNDDEV\_OUT\_ERROR'
---

# EC\_SNDDEV\_OUT\_ERROR

A device error has occurred in an audio renderer filter.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

DWORD value from the [**SNDDEV\_ERR**](snddev-err.md) enumerated type, indicating how the device was being accessed when the failure occurred.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

DWORD value indicating the error returned from the sound device call.

</dd> </dl>

## Default Action

None.

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

 

 




