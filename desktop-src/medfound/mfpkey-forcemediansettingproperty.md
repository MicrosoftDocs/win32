---
description: Specifies whether the codec should use median filtering during encoding.
ms.assetid: adfca033-4679-4f36-a802-6dd5df7100c8
title: MFPKEY_FORCEMEDIANSETTING Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_FORCEMEDIANSETTING Property

Specifies whether the codec should use median filtering during encoding.

## Constant for IPropertyBag

g\_wszWMVCForceMedianSetting

## Data Type

VT\_BOOL

## Default Value

FALSE

## Remarks

Median filtering tells the codec to ignore noise and grain when calculating motion between frames. This can improve the quality of very noisy video, but can lead to motion trails (also known as trailing artifacts) when applied to clean source video.

By default, the codec uses internal logic to determine whether median filtering should be used. If you set this property, that logic will be overridden.

> [!Note]  
> This filter is not the same as median blur filters found in many video editing and post-processing applications.

 

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

 

 




