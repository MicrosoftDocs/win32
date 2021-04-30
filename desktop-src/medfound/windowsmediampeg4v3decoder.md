---
description: The Windows Media MPEG-4 V3 decoder decodes MPEG-4 V3 video streams.
ms.assetid: 5143b0cc-c171-46af-8d7f-4d029af71fb4
title: Windows Media MPEG-4 V3 Decoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Media MPEG-4 V3 Decoder

The Windows Media MPEG-4 V3 decoder decodes MPEG-4 V3 video streams.

## Class Identifier

The class identifier (CLSID) for the Windows MPEG-4 V3 decoder is represented by the constant **CLSID\_CMpeg43DecMediaObject**. You can create an instance of the MPEG-4 V3 decoder by calling **CoCreateInstance**.

## Formats

The Windows Media MPEG-4 V3 decoder supports the following input media types.

-   MEDIASUBTYPE\_MP43
-   MEDIASUBTYPE\_mp43

The Windows Media MPEG-4 V3 decoder supports the following output media subtypes when it is acting as a DirectX Media Object (DMO).

-   MEDIASUBTYPE\_YUY2
-   MEDIASUBTYPE\_UYVY
-   MEDIASUBTYPE\_RGB32
-   MEDIASUBTYPE\_RGB24
-   MEDIASUBTYPE\_RGB565
-   MEDIASUBTYPE\_RGB8
-   MEDIASUBTYPE\_RGB555

The Windows Media MPEG-4 V3 decoder supports the following output media subtypes when it is acting as a Media Foundation Transform (MFT).

-   MFVideoFormat\_YUY2
-   MFVideoFormat\_UYVY
-   MFVideoFormat\_RGB32
-   MFVideoFormat\_RGB24
-   MFVideoFormat\_RGB565
-   MFVideoFormat\_RGB8
-   MFVideoFormat\_RGB555

## Remarks

The Windows Media MPEG-4 V3 decoder object exposes the [**IMediaObject**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobject) interface so that the object can be used as a DirectX Media Object (DMO), and it exposes the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface so that the object can be used as a Media Foundation Transform (MFT). The object has the same class identifier (CLSID) regardless of whether it acts as a DMO or an MFT.

The MPEG-4 V3 decoder behaves as a DMO or an MFT depending on which interfaces you obtain and which version of Windows is running. The following table shows the conditions under which an MPEG-4 V3 decoder behaves as a DMO or an MFT.



| Operating system            | Decoder behavior                                                                                                                                                    |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows XP                  | The MPEG-4 V3 decoder always behaves as a DMO.                                                                                                                      |
| Windows Vista and Windows 7 | By default, the MPEG-4 V3 decoder behaves as a DMO. If you obtain an [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface on the MPEG-4 V3 decoder, it behaves as an MFT. |



 

The globally unique identifiers (GUIDs) for RGB media subtypes differ depending on whether a decoder is acting as a DMO or an MFT. The GUIDs for non-RGB media subtypes are the same, regardless of whether a decoder is acting as a DMO or an MFT. For information about the GUIDs that represent media subtypes, see [Video Subtype GUIDs](video-subtype-guids.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MP43DECD.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> </dl>

 

 
