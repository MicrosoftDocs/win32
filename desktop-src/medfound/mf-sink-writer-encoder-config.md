---
Description: Contains a pointer to a property store with encoding properties.
ms.assetid: 28AC864C-C63C-4BD4-9770-B7B48A2815C6
title: MF\_SINK\_WRITER\_ENCODER\_CONFIG attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SINK\_WRITER\_ENCODER\_CONFIG attribute

Contains a pointer to a property store with encoding properties.

## Data type

**IUnknown\***

## Remarks

The value of this attribute is an [**IPropertyStore**](properties.IPropertyStore) pointer.

This attribute enables an application to set encoding properties when using the [Sink Writer](sink-writer.md). To set this attribute, perform the following steps:

1.  Call [**PSCreateMemoryPropertyStore**](properties.PSCreateMemoryPropertyStore) to create a new property store.
2.  Set encoder properties on the property store. The available properties depends on the encoder. For more information, see [Codec Objects](codecobjects.md).
3.  Call [**MFCreateAttributes**](/windows/win32/mfapi/nf-mfapi-mfcreateattributes?branch=master) to create a new attribute store.
4.  Call [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master) to set the [**IPropertyStore**](properties.IPropertyStore) pointer on the attribute store.
5.  Create a new instance of the Sink Writer. Pass the [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) pointer to the creation function. For more information, see [Sink Writer Attributes](sink-writer-attributes.md).

The Sink Writer sets the properties on the encoder before setting the media types.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFSinkWriter**](/windows/win32/mfreadwrite/nn-mfreadwrite-imfsinkwriter?branch=master)
</dt> <dt>

[Sink Writer Attributes](sink-writer-attributes.md)
</dt> </dl>

 

 




