---
description: The Windows Media Video 9 Screen decoder decodes streams that were encoded by the Windows Media Video 9 Screen Encoder.
ms.assetid: 6688a830-7a54-4f58-947e-26013e191b5f
title: Windows Media Video 9 Screen Decoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Media Video 9 Screen Decoder

The Windows Media Video 9 Screen decoder decodes streams that were encoded by the [**Windows Media Video 9 Screen Encoder**](windowsmediavideo9screenencoder.md).

## Class Identifier

The class identifier (CLSID) for the Windows Media Video 9 Screen decoder is represented by the constant **CLSID\_CMSSCDecMediaObject**. You can create an instance of the decoder by calling **CoCreateInstance**.

## Input Types

The four-character code (FOURCC) for Windows Media Video Screen Version 9 encoded content is "MSS2".

The following input types are supported by the Version 9 Screen decoder.

-   MEDIASUBTYPE\_MSS2

## Output Types

The following output types are supported by the Version 9 Screen decoder when it is being used as a DirectX Media Object (DMO).

-   MEDIASUBTYPE\_RGB24
-   MEDIASUBTYPE\_RGB32
-   MEDIASUBTYPE\_ARGB32
-   MEDIASUBTYPE\_RGB565
-   MEDIASUBTYPE\_RGB555
-   MEDIASUBTYPE\_RGB8

The following output types are supported by the Version 9 Screen decoder when it is being used as a Media Foundation Transform (MFT).

-   MFVideoFormat\_RGB24
-   MFVideoFormat\_RGB32
-   MFVideoFormat\_ARGB32
-   MFVideoFormat\_RGB565
-   MFVideoFormat\_RGB555
-   MFVideoFormat\_RGB8

## Remarks

A screen decoder object exposes the [**IMediaObject**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobject) interface so that the object can be used as a DirectX Media Object (DMO), and it exposes the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface so that the object can be used as a Media Foundation Transform (MFT).

A screen decoder behaves as a DMO or an MFT depending on which interfaces you obtain and which version of Windows is running. The following table shows the conditions under which a screen decoder behaves as a DMO or an MFT.



| Operating system            | Decoder behavior                                                                                                                                                        |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows XP                  | A Windows Media Screen decoder always behaves as a DMO.                                                                                                                 |
| Windows Vista and Windows 7 | By default, a Windows Media Screen decoder behaves as a DMO. If you obtain an [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface on a screen decoder, it behaves as an MFT. |



 

You can use the same CLSID (CLSID\_CMSSCDecMediaObject) to create the Version 7 Screen decoder and the Version 9 Screen decoder. The FOURCC for Windows Media Video Screen Version 7 encoded content is "MSS1". The Version 7 Screen decoder supports the MEDIASUBTYPE\_MSS1 input type.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows XP, Windows Vista or Windows 7<br/>                                       |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Wmvsdecd.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Codec Implementation](codecimplementation.md)
</dt> <dt>

[Using the Windows Media Video 9 Screen Codec](usingthewindowsmediavideo9screencodec.md)
</dt> <dt>

[Windows Media Video 9 Screen Encoder](windowsmediavideo9screenencoder.md)
</dt> </dl>

 

 
