---
description: The Audio Resampler performs one or both of the following actions on an audio stream.Change the sampling rate.Change the number of channels.
ms.assetid: bee755c4-0585-40fb-aa4d-4e964f5144a3
title: 'Audio Resampler DSP (Wmcodecdsp.h)'
ms.topic: reference
ms.date: 05/31/2018
---

# Audio Resampler DSP

The Audio Resampler performs one or both of the following actions on an audio stream.

-   Change the sampling rate.
-   Change the number of channels.

## CLSID

CLSID\_CResamplerMediaObject

## Interfaces

-   [**IMediaObject**](/previous-versions/ms785953(v=vs.85))
-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)
-   [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore)
-   [**IWMResamplerProps**](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmresamplerprops)

## Formats

PCM or IEEE floating-point

The media type must specify an uncompressed PCM or floating-point audio format.

-   For the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface, initialize the media type as described in [Uncompressed Audio Media Types](uncompressed-audio-media-types.md).
-   For the [**IMediaObject**](/previous-versions/ms785953%28v%3dvs.85%29) interface, the media type must be a **FORMAT\_WaveFormatEx** type. For more information, see [**DMO\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/mediaobj/ns-mediaobj-dmo_media_type).

## Properties

-   [MFPKEY\_WMRESAMP\_FILTERQUALITY](mfpkey-wmresamp-filterquality.md)
-   [MFPKEY\_WMRESAMP\_CHANNELMTX](mfpkey-wmresamp-channelmtx.md)
-   [MFPKEY\_WMRESAMP\_LOWPASS\_BANDWIDTH](mfpkey-wmresamp-lowpass-bandwidth.md)

## Required Attributes

The resampler requires the following attributes to be set on it:

-   [MF\_MT\_AUDIO\_CHANNEL\_MASK](mf-mt-audio-channel-mask-attribute.md)
-   [MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND](mf-mt-audio-avg-bytes-per-second-attribute.md)
-   [MF\_MT\_AUDIO\_BLOCK\_ALIGNMENT](mf-mt-audio-block-alignment-attribute.md)

## Custom Channel Mapping

The audio resampler maps the input audio channels to the output audio channels, based on the following information:

-   The number of channels. This is given in the [MF\_MT\_AUDIO\_NUM\_CHANNELS](mf-mt-audio-num-channels-attribute.md) attribute of the media type, or the **nChannels** member of the [WAVEFORMATEX](mf-mt-audio-prefer-waveformatex-attribute.md) structure.
-   The channel mask, which assigns channels to speaker position. The channel mask is given in the MF\_MT\_AUDIO\_CHANNEL\_MASK attribute of the media type, or the **dwChannelMask** member of the [**WAVEFORMATEXTENSIBLE**](/windows/desktop/api/mmreg/ns-mmreg-waveformatextensible) structure.
-   A matrix of mapping weights.

The matrix contains a series of weights, such that each output channel is a weighted average of the input channels.

You can specify a custom matrix for channel mapping by calling [**IWMResamplerProps::SetUserChannelMtx**](/windows/desktop/api/wmcodecdsp/nf-wmcodecdsp-iwmresamplerprops-setuserchannelmtx) or by setting the [**MFPKEY\_WMRESAMP\_CHANNELMTX**](mfpkey-wmresamp-channelmtx.md) property. If a custom matrix is not provided, the Audio Resampler uses a set of default matrices.

## Default Channel Mapping

If you do not specify a custom matrix, the Audio Resampler DSP uses default values for channel mapping.

In the tables that follow, the channels are abbreviated:

-   L: Left
-   R: Right
-   C: Center
-   LFE: Low Frequence Effects
-   BL: Back Left
-   BR: Back Right
-   SL: Surround Left
-   SR: Surround Right

The following table shows the default coefficients for mapping 6 channels (mask 0x3F) to 2 channels.



|     | L     | R     | C     | LFE   | BL    | BR    |
|-----|-------|-------|-------|-------|-------|-------|
| **L**   | 0.314 | 0     | 0.222 | 0.031 | 0.268 | 0.164 |
| **R**   | 0     | 0.314 | 0.222 | 0.031 | 0.164 | 0.268 |



 

The following table shows the default coefficients for mapping 6 channels (mask 0x60F) to 2 channels.



|     | L     | R     | C     | LFE   | SL    | SR    |
|-----|-------|-------|-------|-------|-------|-------|
| **L**   | 0.320 | 0     | 0.226 | 0.032 | 0.292 | 0.130 |
| **R**   | 0     | 0.320 | 0.226 | 0.032 | 0.130 | 0.292 |



 

The following table shows the default coefficients for mapping 6 (mask 0x3F or 0x60F) channels to 1 channel.



|     | L     | R     | C     | LFE   | BL(SL) | BR(SR) |
|-----|-------|-------|-------|-------|--------|--------|
| **C**   | 0.192 | 0.192 | 0.192 | 0.038 | 0.192  | 0.192  |



 

The following table shows the default coefficients for mapping 8 channels (mask 0x63F) to 2 channels.



|     | L     | R     | C     | LFE   | BL    | BR    | SL    | SR    |
|-----|-------|-------|-------|-------|-------|-------|-------|-------|
| **L**   | 0.222 | 0     | 0.157 | 0.022 | 0.189 | 0.116 | 0.203 | 0.090 |
| **R**   | 0     | 0.222 | 0.157 | 0.022 | 0.116 | 0.189 | 0.090 | 0.203 |



 

The following table shows the default coefficients for mapping 8 channels (mask 0x63F) to 1 channel.



|     | L     | R     | C     | LFE   | BL    | BR    | SL    | SR    |
|-----|-------|-------|-------|-------|-------|-------|-------|-------|
| **C**   | 0.139 | 0.139 | 0.139 | 0.028 | 0.139 | 0.139 | 0.139 | 0.139 |



 

The following table shows the default coefficients for mapping 8 channels (mask 0x63F) to 6 channels (mask 0x3F).



|     | L     | R     | C     | LFE   | BL    | BR    | SL    | SR    |
|-----|-------|-------|-------|-------|-------|-------|-------|-------|
| **L**   | 0.518 | 0     | 0     | 0     | 0     | 0     | 0.189 | 0     |
| **R**   | 0     | 0.518 | 0     | 0     | 0     | 0     | 0     | 0.189 |
| **C**   | 0     | 0     | 0.518 | 0     | 0     | 0     | 0     | 0     |
| **LFE** | 0     | 0     | 0     | 0.518 | 0     | 0     | 0     | 0     |
| **BL**  | 0     | 0     | 0     | 0     | 0.518 | 0     | 0.482 | 0     |
| **BR**  | 0     | 0     | 0     | 0     | 0     | 0.518 | 0     | 0.482 |



 

The following table shows the default coefficients for mapping 8 channels (mask 0x63F) to 6 channels (mask 0x60F).



|     | L     | R     | C     | LFE   | BL    | BR    | SL    | SR    |
|-----|-------|-------|-------|-------|-------|-------|-------|-------|
| **L**   | 0.447 | 0     | 0     | 0     | 0     | 0     | 0     | 0     |
| **R**   | 0     | 0.447 | 0     | 0     | 0     | 0     | 0     | 0     |
| **C**   | 0     | 0     | 0.447 | 0     | 0     | 0     | 0     | 0     |
| **LFE** | 0     | 0     | 0     | 0.447 | 0     | 0     | 0     | 0     |
| **SL**  | 0     | 0     | 0     | 0     | 0.429 | 0.124 | 0.447 | 0     |
| **SR**  | 0     | 0     | 0     | 0     | 0.124 | 0.429 | 0     | 0.447 |



 

To understand how to interpret the tables of coefficients, consider the first table, which maps 6 channels to 2. The first row of the table (0.314, 0, 0.222, 0.031, 0.268, 0.164) is a vector of weights that specifies how heavily each input channel contributes to the left channel of the output. The second row of the table (0, 0.314, 0.222, 0.031, 0.164, 0.268) is a vector of weights that specifies how heavily each input channel contributes to the right channel of the output.

The following formulas show how the output channels are calculated.

``` syntax
L_out = L*0.314 + C*0.222 + LFE*0.031 + BL*0.268 + BR*0.164 
R_out = R*0.314 + C*0.222 + LFE*0.031 + BL*0.164 + BR*0.268
```

> [!Note]  
> If you use the Audio Resampler DSP to increase the number of channels, the added channels will be assigned values of 0.

 

## Output Quality

You can specify the output quality of the Audio Resampler DSP by calling [**IWMResamplerProps::SetHalfFilterLength**](/windows/desktop/api/wmcodecdsp/nf-wmcodecdsp-iwmresamplerprops-sethalffilterlength) or by setting the [**MFPKEY\_WMRESAMP\_FILTERQUALITY**](mfpkey-wmresamp-filterquality.md) property. If you do not specify the output quality, the Audio Resampler DSP uses a default quality value of 30.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Resampledmo.dll</dt> </dl> |



## See also

[Digital Signal Processors](windowsmediadigitalsignalprocessors.md)
