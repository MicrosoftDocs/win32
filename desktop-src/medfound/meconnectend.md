---
Description: Raised by the network source when it finishes opening a URL.
ms.assetid: 737aec32-24f4-4825-ad34-8d2fc889bc09
title: MEConnectEnd event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEConnectEnd event

Raised by the network source when it finishes opening a URL.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

The network source sends this event directly to the application through the application's [**IMFSourceOpenMonitor::OnSourceEvent**](/windows/win32/mfidl/nf-mfidl-imfsourceopenmonitor-onsourceevent?branch=master) method, not through the usual [**IMFMediaEventGenerator**](/windows/win32/mfobjects/nn-mfobjects-imfmediaeventgenerator?branch=master) interface.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IMFSourceOpenMonitor**](/windows/win32/mfidl/nn-mfidl-imfsourceopenmonitor?branch=master)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




