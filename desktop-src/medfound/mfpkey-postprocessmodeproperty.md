---
description: Specifies the post processing mode for the decoder.
ms.assetid: c6dab7f6-4a3e-45bb-b81c-5f4c39f9e954
title: MFPKEY_POSTPROCESSMODE Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_POSTPROCESSMODE Property

Specifies the post processing mode for the decoder.

## Constant for IPropertyBag

**g\_wszWMVCForcePostProcessMode**

## Data Type

**VT\_I4**

## Remarks

Set this property to one of the following values.



| Value | Meaning                                                                                |
|-------|----------------------------------------------------------------------------------------|
| -1    | The decoder sets the post processing mode adaptively based on available CPU resources. |
| 0     | The decoder performs no post processing.                                               |
| 1     | fThe decoder performs fast deblocking.                                                 |
| 2     | The decoder performs full deblocking.                                                  |
| 3     | The decoder performs fast deblocking and deringing.                                    |
| 4     | The decoder performs full deblocking and deringing.                                    |



 

As the value of this property goes from 0 to 4, the decoding complexity, use of CPU resources, and picture quality all increase.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows Vista or Windows 7<br/>                                                   |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




