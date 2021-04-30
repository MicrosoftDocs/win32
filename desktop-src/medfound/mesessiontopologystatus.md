---
description: Raised by the Media Session when the status of a topology changes.
ms.assetid: b45fd598-ab1e-4b12-8d82-c88c96d1f770
title: MESessionTopologyStatus event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESessionTopologyStatus event

Raised by the Media Session when the status of a topology changes.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE                | Description                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFTopology**](/windows/desktop/api/mfidl/nn-mfidl-imftopology) interface of the topology.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                            | Description                                                      |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**MF\_EVENT\_TOPOLOGY\_STATUS**](mf-event-topology-status-attribute.md)<br/> | Specifies the new status of the topology.<br/> <br/> |



## Remarks

For a code example that retrieves the [**IMFTopology**](/windows/desktop/api/mfidl/nn-mfidl-imftopology) pointer from the event, see [MESessionTopologySet](mesessiontopologyset.md) event.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




