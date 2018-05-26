---
Description: Sets the maximum number of processed samples that can be buffered in the record sink video path.
ms.assetid: 5AFA197E-5A7F-402E-A62B-4F624A5DD917
title: MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_VIDEO\_MAX\_PROCESSED\_SAMPLES attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_VIDEO\_MAX\_PROCESSED\_SAMPLES attribute

Sets the maximum number of processed samples that can be buffered in the record sink video path.

## Data type

**UINT32**

## Remarks

To configure this attribute on the capture engine, add it to the *pAttributes* parameter when you call [**IMFCaptureEngine::Initialize**](/windows/win32/mfcaptureengine/nf-mfcaptureengine-imfcaptureengine-initialize?branch=master).

The maximum value for this attribute is 17.

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

 

 




