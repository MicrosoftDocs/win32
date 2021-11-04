---
description: The Windows Media Video 9 decoder decodes video streams that were encoded by the Windows Media Video Encoder.
ms.assetid: 08f68d1c-c226-4bf6-abd0-fce0f9ddbc05
title: Windows Media Video 9 Decoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Media Video 9 Decoder

The Windows Media Video 9 decoder decodes video streams that were encoded by the [**Windows Media Video Encoder**](windowsmediavideo9encoder.md). The encoder and decoder support the following four categories of encoded video.

-   Windows Media Video 9 Simple Profile
-   Windows Media Video 9 Main Profile
-   Windows Media Video 9 Advanced Profile
-   Windows Media Video 9.1 Image

## Class Identifier

The class identifier (CLSID) for the Windows Media Video decoder is represented by the constant **CLSID\_CWMVDecMediaObject**. You can create an instance of the video decoder by calling **CoCreateInstance**.

## Interfaces

A video decoder object exposes the [**IMediaObject**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobject) interface so that the object can be used as a DirectX Media Object (DMO), and it exposes the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface so that the object can be used as a Media Foundation Transform (MFT).

A video decoder behaves as a DMO or an MFT depending on which interfaces you obtain and which version of Windows is running. The following table shows the conditions under which a video decoder behaves as a DMO or an MFT.



| Operating system            | Decoder behavior                                                                                                                                                      |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows XP                  | A Windows Media video decoder always behaves as a DMO.                                                                                                                |
| Windows Vista and Windows 7 | By default, a Windows Media video decoder behaves as a DMO. If you obtain an [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface on a video decoder, it behaves as an MFT. |



 

Beginning with Windows 7, the Windows Media Video decoder implements the [**IDMOQualityControl**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-idmoqualitycontrol) interface.

## Input Formats

The following table shows the four-character codes (FOURCCs) that correspond to the categories of encoded input that are supported by the Windows Media Video decoder.



| Category                               | FOURCC                                   |
|----------------------------------------|------------------------------------------|
| Windows Media Video 9 Simple Profile   | "WMV3"                                   |
| Windows Media Video 9 Main Profile     | "WMV3"                                   |
| Windows Media Video 9 Advanced Profile | "WVC1"                                   |
| Windows Media Video 9.1 Image          | "WMVP" for 9.1, "WVP2" for 9.1 version 2 |



 

## Output Formats

The Windows Media Video decoder supports the following output media subtypes when it is acting as a DMO.

-   MEDIASUBTYPE\_NV12
-   MEDIASUBTYPE\_YV12
-   MEDIASUBTYPE\_YUY2
-   MEDIASUBTYPE\_UYVY
-   MEDIASUBTYPE\_YVYU
-   MEDIASUBTYPE\_NV11
-   MEDIASUBTYPE\_RGB32
-   MEDIASUBTYPE\_RGB24
-   MEDIASUBTYPE\_RGB565
-   MEDIASUBTYPE\_RGB555
-   MEDIASUBTYPE\_RGB8

The Windows Media Video decoder supports the following output media subtypes when it is acting as an MFT.

-   MFVideoFormat\_NV12
-   MFVideoFormat\_YV12
-   MFVideoFormat\_YUY2
-   MFVideoFormat\_UYVY
-   MFVideoFormat\_YVYU
-   MFVideoFormat\_NV11
-   MFVideoFormat\_RGB32
-   MFVideoFormat\_RGB24
-   MFVideoFormat\_RGB565
-   MFVideoFormat\_RGB555
-   MFVideoFormat\_RGB8

## Properties

The Windows Media Video decoder supports the following properties.




| Property | Description | 
|----------|-------------|
| <a href="mfpkey-decoder-deinterlacingproperty.md">MFPKEY_DECODER_DEINTERLACING</a> | Specifies whether the codec decodes interlaced video frames from the compressed stream as progressive frames.<br /><dl> Windows XP and later.<br />Simple Profile, Main Profile, Advanced Profile.<br />Read/write.<br /></dl> | 
| <a href="mfpkey-dxva-enabledproperty.md">MFPKEY_DXVA_ENABLED</a> | Specifies whether the decoder will use DirectX video acceleration hardware, if available.<br /><dl> Windows XP and later.<br />Simple Profile, Main Profile, Advanced Profile.<br />Write-only.<br /></dl> | 
| <a href="mfpkey-avdecvideoswpowerlevelproperty.md">MFPKEY_AVDecVideoSWPowerLevel</a> | Specifies the power level for the decoder.<br /><dl> Windows 7.<br />Simple Profile, Main Profile, Advanced Profile, Image.<br />Read/write.<br /></dl> | 
| <a href="mfpkey-fi-enabledproperty.md">MFPKEY_FI_ENABLED</a> | Specifies whether the decoder should use frame interpolation.<br /><dl> Windows XP and later.<br />Simple Profile, Main Profile, Advanced Profile, Image.<br />Write-only.<br /></dl> | 
| <a href="mfpkey-fi-supportedproperty.md">MFPKEY_FI_SUPPORTED</a> | Specifies whether the decoder supports frame interpolation.<br /><dl> Windows XP and later.<br />Simple Profile, Main Profile, Advanced Profile, Image<br />Read-only.<br /></dl> | 
| <a href="mfpkey-numthreadsdecproperty.md">MFPKEY_NUMTHREADSDEC</a> | Specifies the number of threads that the decoder will use.<br /><dl> Windows Vista and later.<br />Simple Profile, Main Profile, Advanced Profile, Image.<br />Read/write.<br /></dl> | 
| <a href="mfpkey-postprocessmodeproperty.md">MFPKEY_POSTPROCESSMODE</a> | Specifies the post processing mode for the decoder.<br /><dl> Windows Vista and later.<br />Simple Profile, Main Profile, Advanced Profile, Image.<br />Write-only.<br /></dl> | 
| <strong>g_wszWMVCNeedsDrain</strong> | Specifies whether the decoder should be drained.<br /><dl> Windows 8<br />Read-only.<br /></dl> This property is used by the Windows Media Format runtime. The property type is <strong>VARIANT_BOOL</strong>. If the value is <strong>VARIANT_TRUE</strong>, the decoder should be drained after a discontinuity. For more information about draining an MFT, see <a href="basic-mft-processing-model.md">Basic MFT Processing Model</a>.<br /><blockquote>[!Note]<br />To query this property, use the <a href="/windows/desktop/com/ipropertybag-and-ipersistpropertybag"><strong>IPropertyBag</strong></a> interface.</blockquote><br /> | 




 

## Remarks

The maximum resolution allowed by the Windows Media Video 9 decoder is 4096x4096.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows XP, Windows Vista or Windows 7<br/>                                       |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Wmvdecod.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Codec Implementation](codecimplementation.md)
</dt> </dl>

 

 
