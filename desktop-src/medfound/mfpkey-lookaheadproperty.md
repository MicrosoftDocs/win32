---
description: Specifies the number of frames after the current frame that the codec will evaluate before encoding the current frame.
ms.assetid: e5cdd066-e25a-4107-9523-5611bd792372
title: MFPKEY_LOOKAHEAD Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_LOOKAHEAD Property

Specifies the number of frames after the current frame that the codec will evaluate before encoding the current frame.

## Constant for IPropertyBag

g\_wszWMVCLookAhead

## Data Type

VT\_I4

## Default Value

0

## Remarks

When the codec uses lookahead, it can encode the video more efficiently.

The writer object of the Windows Media Format SDK expects the codec to encode each sample immediately. As a result, this feature does not work properly in software that uses the writer object (including Windows Media Encoder and Windows Media Player). Any data unit extensions associated with video frames will be attached to the wrong output frame. The number of frames by which the data unit extensions are misplaced is equal to the number of frames of lookahead that are used.

Valid lookahead values range from 0 to 16 frames. The recommended value is 16.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




