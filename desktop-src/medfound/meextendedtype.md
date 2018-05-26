---
Description: Custom event type.
ms.assetid: a54a446c-0e96-467b-90f6-0f64a7c1727d
title: MEExtendedType event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEExtendedType event

Custom event type. You can use this event type to define custom events for your component. Use the extended event type to identify the event. The extended event type is a GUID value associated with the event. For more information, see [**IMFMediaEvent::GetExtendedType**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getextendedtype?branch=master).

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




