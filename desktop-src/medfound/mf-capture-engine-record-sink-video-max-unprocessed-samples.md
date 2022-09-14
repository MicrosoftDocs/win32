---
description: Sets the maximum number of unprocessed samples that can be buffered for processing in the record sink video path.
ms.assetid: B3B5C547-1F06-45B1-BFCB-513AD7B6A9B6
title: MF_CAPTURE_ENGINE_RECORD_SINK_VIDEO_MAX_UNPROCESSED_SAMPLES attribute (Mfcaptureengine.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_VIDEO\_MAX\_UNPROCESSED\_SAMPLES attribute

Sets the maximum number of unprocessed samples that can be buffered for processing in the record sink video path.

## Data type

**UINT64**

## Remarks

To configure this attribute on the capture engine, add it to the *pAttributes* parameter when you call [**IMFCaptureEngine::Initialize**](/windows/desktop/api/mfcaptureengine/nf-mfcaptureengine-imfcaptureengine-initialize).

The maximum value for this attribute is 17.

Once the record has buffered the maximum number of unprocessed samples, specified by MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_VIDEO\_MAX\_UNPROCESSED\_SAMPLES, it drops the frame rate by dropping samples.

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

[Capture Engine Attributes](capture-engine-attributes.md)
</dt> <dt>

[**IMFCaptureEngine::Initialize**](/windows/desktop/api/mfcaptureengine/nf-mfcaptureengine-imfcaptureengine-initialize)
</dt> </dl>

 

 




