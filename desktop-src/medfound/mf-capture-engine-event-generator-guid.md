---
Description: 'Identifies the component that generated a capture event.'
ms.assetid: 'DCCF3054-AF14-44C7-84C0-B03E35B5D90A'
title: 'MF\_CAPTURE\_ENGINE\_EVENT\_GENERATOR\_GUID attribute'
---

# MF\_CAPTURE\_ENGINE\_EVENT\_GENERATOR\_GUID attribute

Identifies the component that generated a capture event.

## Data type

**GUID**

## Remarks

This attribute appears on some events from the capture engine. To get this attribute, call [**IMFAttributes::GetGUID**](imfattributes-getguid.md) on the event object. The event object is passed to the application through the [**IMFCaptureEngineOnEventCallback::OnEvent**](imfcaptureengineoneventcallback-onevent.md) method.

The value is an interface identifier for the component that generated the event. For example, the value **IID\_IMFCapturePreviewSink** indicates the preview sink ([**IMFCapturePreviewSink**](imfcapturepreviewsink.md)). Not every capture event contains this attribute.

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

[Capture Engine Attributes](capture-engine-attributes.md)
</dt> <dt>

[**IMFCaptureEngine::Initialize**](imfcaptureengine-initialize.md)
</dt> </dl>

 

 




