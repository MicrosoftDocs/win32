---
title: Metadata Editor Object
description: Metadata Editor Object
ms.assetid: 224eea1c-1d0d-47ac-9d99-c13674284f6d
keywords:
- Windows Media Format SDK,metadata editor objects
- Advanced Systems Format (ASF),metadata editor objects
- ASF (Advanced Systems Format),metadata editor objects
- objects,metadata editor objects
- metadata editor objects,about
- metadata,editor objects
ms.topic: article
ms.date: 05/31/2018
---

# Metadata Editor Object

The metadata editor object is used to edit information stored in the header section of ASF files. The most common things manipulated by this object are metadata attributes. Additionally, the metadata editor deals with [*markers*](wmformat-glossary.md) and script commands. The only time you need to use the metadata editor is when you want to edit the header of an existing file without playing it.

The metadata editor object is created by the function [**WMCreateEditor**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateeditor), which sets a pointer to an **IWMMetadataEditor** interface. The other interfaces of the metadata editor object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the metadata editor object.



| Interface                                        | Description                                                                                                                                                                                            |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMDRMEditor**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmeditor)             | Enables editing applications to examine the [*DRM*](wmformat-glossary.md) properties of an ASF file without having any rights to play the protected content. |
| [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo)           | Manipulates attributes, markers, and script commands in the header.                                                                                                                                    |
| [**IWMHeaderInfo2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo2)         | Retrieves codec information. Inherits all of the methods of **IWMHeaderInfo**.                                                                                                                         |
| [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3)         | Provides advanced support for attributes, including large attributes, multiple languages, and duplicate attribute names. Inherits all of the methods of **IWMHeaderInfo** and **IWMHeaderInfo2**.      |
| [**IWMMetadataEditor**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmetadataeditor)   | Opens, closes, and saves changes to the header of an ASF file.                                                                                                                                         |
| [**IWMMetadataEditor2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmetadataeditor2) | Opens an ASF file for header editing with multiple file access and sharing options. Inherits all of the methods of **IWMMetadataEditor**.                                                              |



 

## Related topics

<dl> <dt>

[**Markers**](markers.md)
</dt> <dt>

[**Metadata**](metadata.md)
</dt> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Script Commands**](script-commands.md)
</dt> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




