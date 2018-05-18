---
Description: 'Disables the use of hardware-based Media Foundation transforms (MFTs) in the capture engine.'
ms.assetid: '1C687FEC-276D-4759-A3B8-9A2A31CB0DE1'
title: 'MF\_CAPTURE\_ENGINE\_DISABLE\_HARDWARE\_TRANSFORMS attribute'
---

# MF\_CAPTURE\_ENGINE\_DISABLE\_HARDWARE\_TRANSFORMS attribute

Disables the use of hardware-based Media Foundation transforms (MFTs) in the capture engine.

## Data type

**BOOL** stored as **UINT32**

## Remarks

By default, the capture engine uses hardware decoders or encoders. To disable the use of hardware MFTs, set this attribute to **TRUE** when you create the capture engine.

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

 

 




