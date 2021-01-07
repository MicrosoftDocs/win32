---
description: Setting an Output Type for a WMA Encoder
ms.assetid: 0a1a22bb-460f-4ac2-be76-4249997441de
title: Setting an Output Type for a WMA Encoder
ms.topic: article
ms.date: 05/31/2018
---

# Setting an Output Type for a WMA Encoder

To create a valid output type for a Windows Media Audio (WMA) encoder, you must have the following information:

-   The audio subtype that repesents the encoded WMA format. See [Audio Subtype GUIDs](audio-subtype-guids.md).
-   The configuration properties to set on the encoder.

    The configuration properties are documented in the Windows Media Audio and Video Codec and DSP APIs documentation. For more information, see "Audio Stream Properties" in [Encoding Properties](configuring-the-encoder.md).

### Windows Vista or Later

To get a valid output type for the encoder, perform the following steps.

1.  Use the [**MFTEnum**](/windows/desktop/api/mfapi/nf-mfapi-mftenum) or [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) function to create an instance of the encoder.
2.  Query the encoder for the **IPropertyStore** interface.
3.  Use the **IPropertyStore** interface to configure the encoder.
4.  Retrieve the supported output types by calling [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype) in a loop until the encoder returns **MF\_E\_NO\_MORE\_TYPES** and you choose the target media type. I
5.  Call [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype) to set the compression media type on the encoder.

### Windows 7

To get a valid output type for the encoder in Windows 7, Media Foundation provides the [**MFTranscodeGetAudioOutputAvailableTypes**](/windows/desktop/api/mfidl/nf-mfidl-mftranscodegetaudiooutputavailabletypes) function. An application must pass required the audio subtype that repesents the encoded WMA and the encoding properties. The properties are required because the encoder changes the supported output types depending upon the mode set.

> [!Note]  
> [**MFTranscodeGetAudioOutputAvailableTypes**](/windows/desktop/api/mfidl/nf-mfidl-mftranscodegetaudiooutputavailabletypes)is only supported for [Constant Bit Rate Encoding](constant-bit-rate-encoding.md).

 

If the call succeeds, the application receives a list of IUnknown pointers of the supported output media types in an [**IMFCollection**](/windows/desktop/api/mfobjects/nn-mfobjects-imfcollection) object. To set the output media type, find the one that matches your target type and call [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype) to set the compression media type on the encoder.

## Related topics

<dl> <dt>

[Instantiating an Encoder MFT](instantiating-the-encoder-mft.md)
</dt> <dt>

[Windows Media Encoders](windows-media-encoders.md)
</dt> </dl>

 

 



