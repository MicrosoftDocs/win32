---
description: Specifies whether the application requires Microsoft Direct3D support in the Source Reader or Sink Writer.
ms.assetid: 3844ED7B-E1E5-4CD7-B080-FE7EC7B28AC5
title: MF_READWRITE_D3D_OPTIONAL attribute (Mfreadwrite.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_READWRITE\_D3D\_OPTIONAL attribute

Specifies whether the application requires Microsoft Direct3D support in the [Source Reader](source-reader.md) or [Sink Writer](sink-writer.md).

## Data type

**BOOL** stored as **UINT32**

## Remarks

This attribute applies only if the application enables Direct3D support using the [MF\_SOURCE\_READER\_D3D\_MANAGER](mf-source-reader-d3d-manager.md) or [MF\_SINK\_WRITER\_D3D\_MANAGER](mf-sink-writer-d3d-manager.md) attribute.

If the application enables Direct3D support, the Source Reader and Sink Writer will both try to allocate Direct3D surfaces for video. If this fails, and the MF\_READWRITE\_D3D\_OPTIONAL attribute is **TRUE**, the Source Reader/Sink Writer will fall back to allocating video surfaces in system memory. Otherwise, if Direct3D surfaces cannot be allocated and MF\_READWRITE\_D3D\_OPTIONAL is **FALSE**, an error occurs during processing.

If the application does not enable Direct3D support, the Source Reader/Sink Writer uses system memory, and ignores the value of MF\_READWRITE\_D3D\_OPTIONAL.

This attribute is optional. The default value is **FALSE**. Set the attribute when you create the Source Reader or Sink Writer.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sink Writer Attributes](sink-writer-attributes.md)
</dt> <dt>

[Source Reader Attributes](source-reader-attributes.md)
</dt> </dl>

 

 




