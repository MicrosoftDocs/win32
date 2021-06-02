---
description: Provides feedback to the quality manager about playback quality.
ms.assetid: 1b4b6a2d-411e-42d1-a44b-bb1928e1c063
title: MEQualityNotify event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEQualityNotify event

Provides feedback to the quality manager about playback quality.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE           | Description                         |
|-------------------|-------------------------------------|
| VT\_I8<br/> | See Remarks.<br/> <br/> |



## Remarks

This event is raised by some pipeline components. The Media Session forwards the event to the quality manager by calling the [**IMFQualityManager::NotifyQualityEvent**](/windows/desktop/api/mfidl/nf-mfidl-imfqualitymanager-notifyqualityevent) method.

The event's extended type indicates the meaning of the event data.



| Extended type                            | Event data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MF\_QUALITY\_NOTIFY\_PROCESSING\_LATENCY | Approximate processing latency introduced by the component, in 100-nanosecond units.<br/> Processing latency is the amount of latency that a component introduces into the pipeline by processing a sample. In some cases, the latency cannot be derived simply by looking at the calls to [**IMFQualityManager::NotifyProcessInput**](/windows/desktop/api/mfidl/nf-mfidl-imfqualitymanager-notifyprocessinput) and [**IMFQualityManager::NotifyProcessOutput**](/windows/desktop/api/mfidl/nf-mfidl-imfqualitymanager-notifyprocessoutput). For example, there may not be a one-to-one correspondence between input samples and output samples. In this case, the component might send an MEQualityNotify event with the processing latency. If the processing latency changes, the component can send a new event at any time during streaming.<br/> |
| MF\_QUALITY\_NOTIFY\_SAMPLE\_LAG         | Lag time for the sample, in 100-nanosecond units. If the value is positive, the sample was late. If the value is negative, the sample was early.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |



 

To get the extended type, call [**IMFMediaEvent::GetExtendedType**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getextendedtype).

Pipeline components are not required to send this event.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IMFQualityManager**](/windows/desktop/api/mfidl/nn-mfidl-imfqualitymanager)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




