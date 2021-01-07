---
description: Enables low-latency processing in the Microsoft Media Foundation pipeline.
ms.assetid: 4D11B4D6-8CFF-4850-BF8F-9019A1F79153
title: MF_LOW_LATENCY attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_LOW\_LATENCY attribute

Enables low-latency processing in the Microsoft Media Foundation pipeline.

## Data type

**BOOL** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

Low latency is defined as the smallest possible delay from when the media data is generated (or received) to when it is rendered. Low latency is desirable for real-time communication scenarios. For other scenarios, such as local playback or transcoding, you typically should not enable low-latency mode, because it can affect quality.

> [!Note]  
> The GUID value of this attribute is identical to the [CODECAPI\_AVLowLatencyMode](codecapi-avlowlatencymode.md) property defined for the [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) interface.

 

Set this attribute on pipeline components as follows:

-   Media source: Use the [**IMFMediaSourceEx::GetSourceAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasourceex-getsourceattributes) method.
-   Media Foundation transform (MFT): Use the [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) method. For encoders, the encoder might support low latency through the [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) interface.
-   Media sink: Query the media sink for the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface.

Applications typically do not set this attribute directly on the pipeline components, but instead set the attribute on one of the following objects:

-   [Media Session](media-session.md): Use the *pConfiguation* parameter of the [**MFCreateMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatemediasession) or [**MFCreatePMPMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatepmpmediasession) function, or else set the attribute on the topology.
-   [Source Reader](source-reader.md): Set the attribute with the configuration properties when you create the Source Reader. For more information, see [Source Reader Attributes](source-reader-attributes.md).
-   [Sink Writer](sink-writer.md): Set the attribute with the configuration properties when you create the Sink Writer. For more information, see [Sink Writer Attributes](sink-writer-attributes.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sink Writer Attributes](sink-writer-attributes.md)
</dt> <dt>

[Source Reader Attributes](source-reader-attributes.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 
