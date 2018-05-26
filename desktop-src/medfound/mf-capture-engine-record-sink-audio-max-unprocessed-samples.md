---
Description: Sets the maximum number of unprocessed samples that can be buffered for processing in the record sink audio path.
ms.assetid: C959ED58-77EB-47EC-8D5D-BBFA9342295D
title: MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_AUDIO\_MAX\_UNPROCESSED\_SAMPLES attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_AUDIO\_MAX\_UNPROCESSED\_SAMPLES attribute

Sets the maximum number of unprocessed samples that can be buffered for processing in the record sink audio path.

## Data type

**UINT64**

## Remarks

To configure this attribute on the capture engine, add it to the *pAttributes* parameter when you call [**IMFCaptureEngine::Initialize**](/windows/win32/mfcaptureengine/nf-mfcaptureengine-imfcaptureengine-initialize?branch=master).

The maximum value for this attribute is 100.

Once the record has buffered the maximum number of unprocessed samples, specified by MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_AUDIO\_MAX\_UNPROCESSED\_SAMPLES, it drops the frame rate by dropping samples.

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

[**IMFCaptureEngine::Initialize**](/windows/win32/mfcaptureengine/nf-mfcaptureengine-imfcaptureengine-initialize?branch=master)
</dt> </dl>

 

 




