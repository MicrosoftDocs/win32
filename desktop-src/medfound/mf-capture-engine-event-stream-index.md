---
description: Identifies which stream generated a capture event.
ms.assetid: A15B334A-716A-467E-AEA5-C13710FFE109
title: MF_CAPTURE_ENGINE_EVENT_STREAM_INDEX attribute (Mfcaptureengine.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_CAPTURE\_ENGINE\_EVENT\_STREAM\_INDEX attribute

Identifies which stream generated a capture event.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

## Remarks

This attribute appears on some events from the capture engine. To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32) on the event object. The event object is passed to the application through the [**IMFCaptureEngineOnEventCallback::OnEvent**](/windows/desktop/api/mfcaptureengine/nf-mfcaptureengine-imfcaptureengineoneventcallback-onevent) method.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>Mfcaptureengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFCaptureEngineOnEventCallback::OnEvent**](/windows/desktop/api/mfcaptureengine/nf-mfcaptureengine-imfcaptureengineoneventcallback-onevent)
</dt> </dl>

 

 




