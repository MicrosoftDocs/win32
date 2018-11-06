---
title: Windows Media Metafile Reference
description: Windows Media Metafile Reference
ms.assetid: 03dadba3-0143-46f0-990a-108196eb58ab
keywords:
- Windows Media metafiles,reference
- metafiles,reference
- reference for Windows Media metafiles
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Windows Media Metafile Reference

This reference documents elements and file name extensions for Windows Media metafiles. The reference is divided into the following sections.



| Section                                                                                    | Description                                                                                                                      |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [Windows Media Metafile Elements Reference](windows-media-metafile-elements-reference.md) | Documents metafile elements, including definitions, attributes and their values, and special conditions related to each element. |
| [File Name Extensions](file-name-extensions.md)                                           | Documents metafile file name extensions with rules and guidelines on their use.                                                  |



 

Windows Media metafiles are text files that provide information about a file stream and its presentation. The metafiles are based on the Extensible Markup Language (XML) syntax, and are made up of various XML-like elements with their tags and attributes. Each element defines a setting or action for streaming media.

There are two sets of element tags available for metafiles. Client-side metafiles have one set of elements, and server-side metafiles have another set of elements.

If an element tag does not have any child elements (those that modify or are contained within another element), a single slash character (/) can be used at the end of the opening tag in place of a closing tag. If child elements do not appear between the opening and closing tag for an element, they are not child elements for that element, and are ignored or cause an error in the syntax of the metafile.

## Related topics

<dl> <dt>

[**About Windows Media Metafiles**](about-windows-media-metafiles.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> <dt>

[**Windows Media Metafiles**](windows-media-metafiles.md)
</dt> </dl>

 

 




