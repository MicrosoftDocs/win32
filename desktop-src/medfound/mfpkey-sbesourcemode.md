---
description: Sets the stream configuration for the WTV media source.
ms.assetid: 2181723A-C6E8-42BD-979C-5C26FE3986C4
title: MFPKEY_SBESourceMode property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_SBESourceMode property

Sets the stream configuration for the WTV media source.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**INT**

VT\_INT

**intVal**



## Remarks

Use this property to configure the WTV media source. To set the property, pass an [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

The WTV media source reads Windows Recorded TV Show (.wtv and .ms-drv) files.

This property must have one of the following values.

-   1: Map available audio streams to a single output, based on the system local. This mode is appropriate for playback. (Default.)
-   2. All audio streams and substreams (such as caption and data streams) are selected. This mode is appropriate for remuxing or transcoding.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 
