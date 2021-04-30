---
description: Specifies the amount of content, in milliseconds, that can fit into the model buffer.
ms.assetid: da959bef-1e87-4638-9a77-4135c31a3d27
title: MFPKEY_VIDEOWINDOW Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_VIDEOWINDOW Property

Specifies the amount of content, in milliseconds, that can fit into the model buffer.

## Constant for IPropertyBag

g\_wszWMVCVideoWIndow

## Data Type

VT\_I4

## Default Value

3000

## Remarks

The buffer window is one of the "leaky bucket" model parameters used in the codec rate control.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Configuring Video Encoding](configuringvideoencoding.md)
</dt> <dt>

[The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md)
</dt> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




