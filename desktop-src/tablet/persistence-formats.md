---
description: An application should be able to produce and consume data from multiple formats.
ms.assetid: bf60fab7-866b-4659-8316-653509ac5112
title: Persistence Formats
ms.topic: article
ms.date: 05/31/2018
---

# Persistence Formats

An application should be able to produce and consume data from multiple formats. These often include proprietary binary formats and should also include some standard formats, such as Rich Text Format (RTF) or HTML.

The following table lists some formats that can contain ink.



| Format                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Binary<br/>                           | Applications should use ink serialized format (ISF) to encode ink into their binary formats.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| HTML<br/>                             | A HTML format is highly recommended for the representation of heterogeneous content. Applications should use fortified Graphics Interchange Format (GIF) to encode ink into their HTML documents. For more information about fortified GIFs, see [Building Blocks](building-blocks.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Image<br/>                            | For applications for which there is no other intersection of compatibility, an ink-enabled application should move bitmap and metafile formatted images to the Clipboard.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Ink Serialized Format (ISF)<br/>      | ISF is the most compact persistent representation of ink. Although it often contains only ink data, ISF is extensible. Applications can set custom attributes (identified by a globally unique identifier (GUID)) on an [**Ink**](inkdisp-class.md) object, ink stroke, or ink point. This allows you to store any kind of data or metadata as an attribute in an ISF stream. For Clipboard interoperability, ink can be placed into a standard Clipboard slot for ISF that is defined in the software development kit (SDK) header files.<br/> ISF is a format specific to Microsoft Tablet PC Technology, and is supported only in the [**Ink**](inkdisp-class.md) object's [**Load**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-load) and [**Save**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-save) methods.<br/> |
| RTF<br/>                              | It is possible to generate an RTF Clipboard format and encode ink in the RTF as OLE objects. This allows the ink to be pasted into an OLE container, such as Microsoft Word or a RichEdit-based application.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Extensible Markup Language (XML)<br/> | Applications can use either one of the ink formats that are base-64 encoded to store ink in an XML file format. An XML format is useful for entering ink content into a database, as in the case of a signature field, or even as an applications primary file format. This alleviates the need for writing a parser.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                        |



 

 

 




