---
Description: 'Identifies which stream generated a capture event.'
ms.assetid: 'A15B334A-716A-467E-AEA5-C13710FFE109'
title: 'MF\_CAPTURE\_ENGINE\_EVENT\_STREAM\_INDEX attribute'
---

# MF\_CAPTURE\_ENGINE\_EVENT\_STREAM\_INDEX attribute

Identifies which stream generated a capture event.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

## Remarks

This attribute appears on some events from the capture engine. To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md) on the event object. The event object is passed to the application through the [**IMFCaptureEngineOnEventCallback::OnEvent**](imfcaptureengineoneventcallback-onevent.md) method.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>Mfcaptureengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFCaptureEngineOnEventCallback::OnEvent**](imfcaptureengineoneventcallback-onevent.md)
</dt> </dl>

 

 




