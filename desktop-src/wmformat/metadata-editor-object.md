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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Metadata Editor Object

The metadata editor object is used to edit information stored in the header section of ASF files. The most common things manipulated by this object are metadata attributes. Additionally, the metadata editor deals with [*markers*](wmformat-glossary.md#wmformat-marker) and script commands. The only time you need to use the metadata editor is when you want to edit the header of an existing file without playing it.

The metadata editor object is created by the function [**WMCreateEditor**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateeditor?branch=master), which sets a pointer to an **IWMMetadataEditor** interface. The other interfaces of the metadata editor object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the metadata editor object.



| Interface                                        | Description                                                                                                                                                                                            |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMDRMEditor**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmdrmeditor?branch=master)             | Enables editing applications to examine the [*DRM*](wmformat-glossary.md#wmformat-digital-rights-management--drm-) properties of an ASF file without having any rights to play the protected content. |
| [**IWMHeaderInfo**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmheaderinfo?branch=master)           | Manipulates attributes, markers, and script commands in the header.                                                                                                                                    |
| [**IWMHeaderInfo2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmheaderinfo2?branch=master)         | Retrieves codec information. Inherits all of the methods of **IWMHeaderInfo**.                                                                                                                         |
| [**IWMHeaderInfo3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3?branch=master)         | Provides advanced support for attributes, including large attributes, multiple languages, and duplicate attribute names. Inherits all of the methods of **IWMHeaderInfo** and **IWMHeaderInfo2**.      |
| [**IWMMetadataEditor**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmmetadataeditor?branch=master)   | Opens, closes, and saves changes to the header of an ASF file.                                                                                                                                         |
| [**IWMMetadataEditor2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmmetadataeditor2?branch=master) | Opens an ASF file for header editing with multiple file access and sharing options. Inherits all of the methods of **IWMMetadataEditor**.                                                              |



 

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

 

 




