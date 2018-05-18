---
Description: 'Raised by the network source when it starts opening a URL.'
ms.assetid: '0844ac10-cc5b-4e7f-92df-3a5901c72148'
title: MEConnectStart event
---

# MEConnectStart event

Raised by the network source when it starts opening a URL.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

The network source sends this event directly to the application through the application's [**IMFSourceOpenMonitor::OnSourceEvent**](imfsourceopenmonitor-onsourceevent.md) method, not through the usual [**IMFMediaEventGenerator**](imfmediaeventgenerator.md) interface.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IMFSourceOpenMonitor**](imfsourceopenmonitor.md)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




