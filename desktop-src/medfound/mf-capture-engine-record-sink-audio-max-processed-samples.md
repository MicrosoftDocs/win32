---
Description: 'Sets the maximum number of processed samples that can be buffered in the record sink audio path.'
ms.assetid: '216886DB-B206-4944-925A-C2106331F1CB'
title: 'MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_AUDIO\_MAX\_PROCESSED\_SAMPLES attribute'
---

# MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_AUDIO\_MAX\_PROCESSED\_SAMPLES attribute

Sets the maximum number of processed samples that can be buffered in the record sink audio path.

## Data type

**UINT32**

## Remarks

To configure this attribute on the capture engine, add it to the *pAttributes* parameter when you call [**IMFCaptureEngine::Initialize**](imfcaptureengine-initialize.md).

The maximum value for this attribute is 100.

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

 

 




