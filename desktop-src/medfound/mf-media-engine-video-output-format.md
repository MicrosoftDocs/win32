---
description: Sets the render-target format for the Media Engine.
ms.assetid: 70FFDD44-9FDE-4D86-AD65-60019AC4A2BC
title: MF_MEDIA_ENGINE_VIDEO_OUTPUT_FORMAT attribute (Mfmediaengine.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MEDIA\_ENGINE\_VIDEO\_OUTPUT\_FORMAT attribute

Sets the render-target format for the Media Engine.

## Data type

**DXGI\_FORMAT** stored as **UINT32**

## Remarks

Set this attribute if you create the Media Engine in frame-server mode. For more information, see [**IMFMediaEngineClassFactory::CreateInstance**](/windows/desktop/api/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance). The value of the attribute is a [DXGI\_FORMAT](../direct3d9/d3dformat.md) value.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmediaengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 
