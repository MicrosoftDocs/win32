---
Description: Signals the progress of a content enabler object. Objects that expose the IMFContentEnabler interface can raise this event to notify the application about the progress of the content enablers actions.
ms.assetid: ec14ba9b-cfb6-4e32-870e-2436e11c308b
title: MEEnablerProgress event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEEnablerProgress event

Signals the progress of a content enabler object. Objects that expose the [**IMFContentEnabler**](/windows/win32/mfidl/nn-mfidl-imfcontentenabler?branch=master) interface can raise this event to notify the application about the progress of the content enabler's actions.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE               | Description                                                               |
|-----------------------|---------------------------------------------------------------------------|
| VT\_LPWSTR<br/> | Wide-character string that describes the progress.<br/> <br/> |



## Remarks

To receive this event, query the [**IMFContentEnabler**](/windows/win32/mfidl/nn-mfidl-imfcontentenabler?branch=master) interface for the [**IMFMediaEventGenerator**](/windows/win32/mfobjects/nn-mfobjects-imfmediaeventgenerator?branch=master) interface. Then call [**IMFMediaEventGenerator::BeginGetEvent**](/windows/win32/mfobjects/nf-mfobjects-imfmediaeventgenerator-begingetevent?branch=master), as described in the topic [Media Event Generators](media-event-generators.md).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IMFContentEnabler**](/windows/win32/mfidl/nn-mfidl-imfcontentenabler?branch=master)
</dt> <dt>

[Media Event Generators](media-event-generators.md)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




