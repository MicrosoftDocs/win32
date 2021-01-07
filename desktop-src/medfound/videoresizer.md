---
description: Resizes a video stream.
ms.assetid: 4acd6366-1abf-43f3-b6c9-4ea17a335cec
title: Video Resizer DSP (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Video Resizer DSP

Resizes a video stream.

## CLSID

CLSID\_CResizerDMO

## Interfaces

-   [**IMediaObject**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobject)
-   [**IMFRealTimeClient**](/windows/desktop/api/mfidl/nn-mfidl-imfrealtimeclient)
-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)
-   [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore)
-   [**IWMResizerProps**](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmresizerprops)

## Formats

The Video Resizer DSP supports the following input/output media subtypes when it is acting as a DirectX Media Object (DMO).

-   MEDIASUBTYPE\_IYUV
-   MEDIASUBTYPE\_YUY2
-   MEDIASUBTYPE\_UYVY
-   MEDIASUBTYPE\_I420
-   MEDIASUBTYPE\_RGB32
-   MEDIASUBTYPE\_RGB24
-   MEDIASUBTYPE\_RGB565
-   MEDIASUBTYPE\_RGB8
-   MEDIASUBTYPE\_RGB555
-   MEDIASUBTYPE\_AYUV
-   MEDIASUBTYPE\_V216
-   MEDIASUBTYPE\_YV12

The Video Resizer DSP supports the following input/output media subtypes when it is acting as a Media Foundation Transform (MFT).

-   MFVideoFormat\_IYUV
-   MFVideoFormat\_YUY2
-   MFVideoFormat\_UYVY
-   MFVideoFormat\_I420
-   MFVideoFormat\_RGB32
-   MFVideoFormat\_RGB24
-   MFVideoFormat\_RGB565
-   MFVideoFormat\_RGB8
-   MFVideoFormat\_RGB555
-   MFVideoFormat\_AYUV
-   MFVideoFormat\_V216
-   MFVideoFormat\_YV12

## Properties

-   [MFPKEY\_RESIZE\_SRC\_LEFT](mfpkey-resize-src-left.md)
-   [MFPKEY\_RESIZE\_SRC\_TOP](mfpkey-resize-src-top.md)
-   [MFPKEY\_RESIZE\_SRC\_WIDTH](mfpkey-resize-src-width.md)
-   [MFPKEY\_RESIZE\_SRC\_HEIGHT](mfpkey-resize-src-height.md)
-   [MFPKEY\_RESIZE\_DST\_LEFT](mfpkey-resize-dst-left.md)
-   [MFPKEY\_RESIZE\_DST\_TOP](mfpkey-resize-dst-top.md)
-   [MFPKEY\_RESIZE\_DST\_WIDTH](mfpkey-resize-dst-width.md)
-   [MFPKEY\_RESIZE\_DST\_HEIGHT](mfpkey-resize-dst-height.md)
-   [MFPKEY\_RESIZE\_QUALITY](mfpkey-resize-quality.md)
-   [MFPKEY\_RESIZE\_INTERLACE](mfpkey-resize-interlace.md)
-   [MFPKEY\_RESIZE\_GEOMAPX](mfpkey-resize-geomapx.md)
-   [MFPKEY\_RESIZE\_GEOMAPY](mfpkey-resize-geomapy.md)
-   [MFPKEY\_RESIZE\_GEOMAPWIDTH](mfpkey-resize-geomapwidth.md)
-   [MFPKEY\_RESIZE\_GEOMAPHEIGHT](mfpkey-resize-geomapheight.md)
-   [MFPKEY\_RESIZE\_MINAPX](mfpkey-resize-minapx.md)
-   [MFPKEY\_RESIZE\_MINAPY](mfpkey-resize-minapy.md)
-   [MFPKEY\_RESIZE\_MINAPWIDTH](mfpkey-resize-minapwidth.md)
-   [MFPKEY\_RESIZE\_MINAPHEIGHT](mfpkey-resize-minapheight.md)
-   [MFPKEY\_RESIZE\_PANSCANAPX](mfpkey-resize-panscanapx.md)
-   [MFPKEY\_RESIZE\_PANSCANAPY](mfpkey-resize-panscanapy.md)
-   [MFPKEY\_RESIZE\_PANSCANAPWIDTH](mfpkey-resize-panscanapwidth.md)
-   [MFPKEY\_RESIZE\_PANSCANAPHEIGHT](mfpkey-resize-panscanapheight.md)
-   [MFPKEY\_PIXELASPECTRATIO](mfpkey-pixelaspectratio.md)

## Remarks

The Video Resizer DSP is implemented as a COM object that can act as a DMO or an MFT. The object has a single class identifier (CLSID) regardless of whether it acts as a DMO or an MFT. For information about when a DSP acts as a DMO or an MFT, see [Digital Signal Processors](windowsmediadigitalsignalprocessors.md).

The globally unique identifiers (GUIDs) for RGB media subtypes differ depending on whether a DSP is acting as a DMO or an MFT. The GUIDs for non-RGB media subtypes are the same, regardless of whether a DSP is acting as a DMO or an MFT. For information about the GUIDs that represent media subtypes, see [Video Subtype GUIDs](video-subtype-guids.md).

This DSP can perform both cropping and scaling on the video image. The format of the output type must match the format of the input type. The DSP does not perform color-space conversions.

Before setting the output type, you can define any of the following regions by using the properties listed in this table.



| Region                   | Properties                                                                                                                                                       |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Source rectangle         | MFPKEY\_RESIZE\_SRC\_LEFT<br/> MFPKEY\_RESIZE\_SRC\_TOP<br/> MFPKEY\_RESIZE\_SRC\_WIDTH<br/> MFPKEY\_RESIZE\_SRC\_HEIGHT<br/>            |
| Destination rectangle    | MFPKEY\_RESIZE\_DST\_LEFT<br/> MFPKEY\_RESIZE\_DST\_TOP<br/> MFPKEY\_RESIZE\_DST\_WIDTH<br/> MFPKEY\_RESIZE\_DST\_HEIGHT<br/>            |
| Geometric aperture       | MFPKEY\_RESIZE\_GEOMAPX<br/> MFPKEY\_RESIZE\_GEOMAPY<br/> MFPKEY\_RESIZE\_GEOMAPWIDTH<br/> MFPKEY\_RESIZE\_GEOMAPHEIGHT<br/>             |
| Minimum display aperture | MFPKEY\_RESIZE\_MINAPX<br/> MFPKEY\_RESIZE\_MINAPY<br/> MFPKEY\_RESIZE\_MINAPWIDTH<br/> MFPKEY\_RESIZE\_MINAPHEIGHT<br/>                 |
| Pan/scan region          | MFPKEY\_RESIZE\_PANSCANAPX<br/> MFPKEY\_RESIZE\_PANSCANAPY<br/> MFPKEY\_RESIZE\_PANSCANAPWIDTH<br/> MFPKEY\_RESIZE\_PANSCANAPHEIGHT<br/> |



 

In each case, you must set all of the associated properties for the setting to take effect.

The DSP copies the portion of the source image defined by source rectangle, and stretches or compresses it onto the destination rectangle on the output buffer. The source and destination rectangles do not need to be the same size. The frame size in the output media type must be large enough to hold the destination rectangle.

The geometric aperture, minimum display aperture, and pan/scan region do not affect how the DSP resizes the video. However, they might affect how the downstream component interprets the video frame. In particular, the enhanced video renderer (EVR) uses these values when it calculates the picture aspect ratio and the display area.

If you are using Media Foundation media types, you can set the geometric aperture, minimum display aperture, and pan/scan regions directly in the output media type. Otherwise, if you are using DMO media types, set them using the properties.

For more information, see the following topics:

-   [**MF\_MT\_GEOMETRIC\_APERTURE**](mf-mt-geometric-aperture-attribute.md)
-   [**MF\_MT\_MINIMUM\_DISPLAY\_APERTURE**](mf-mt-minimum-display-aperture-attribute.md)
-   [**MF\_MT\_PAN\_SCAN\_APERTURE**](mf-mt-pan-scan-aperture-attribute.md)

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vidreszr.dll</dt> </dl> |



## See also

<dl> <dt>

[Digital Signal Processors](windowsmediadigitalsignalprocessors.md)
</dt> </dl>

 

 
