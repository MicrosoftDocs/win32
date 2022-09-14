---
title: Order of Precedence
description: Order of Precedence
ms.assetid: 3865ea8a-2489-4714-9a05-d1082589841f
keywords:
- Windows Media metafiles,order of precedence
- Windows Media metafiles,precedence
- metafiles,order of precedence
- metafiles,precedence
- Windows Media,metafiles
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Order of Precedence

Not all metafile element attributes are created equal. Some metafile element attributes override other element attributes. Element attributes can be overridden by similar element attributes depending on position and order. Any attributes of a metafile playlist override those contained in a referenced Windows Media file. An attribute that overrides another has higher precedence.

The hierarchy, highest precedence to lowest, is shown in the following table. The highest precedence item is never overridden.



| Scope                    | Hierarchy                                   |
|--------------------------|---------------------------------------------|
| "Signed DRM content"     | Never overridden.                           |
| **REF** element scope    | Only overridden by signed DRM content.      |
| **ENTRY** element scope  | Overrides elements of the categories below. |
| **ASX** scope            | Overrides media file elements.              |
| Windows Media file scope | Overridden by all of the above.             |



 

-   "Signed DRM content" - Digital signature object.

    Attributes of Signed DRM content will override all others. For example, the Copyright information of "Signed DRM content" will not be overridden. It will always be streamed and presented.

-   **REF** element scope

    Attributes of the **REF** element will override other element attributes, but not signed DRM content.

-   **ENTRY** scope

    Attributes of the **ENTRY** element will be overridden by the **REF** element attribute but will override other element attributes. **TITLE** metadata from the **ENTRY** element is displayed instead of the title information from the media file.

-   **ASX** scope

    Any properties that are entered in the metafile override those contained in the Windows Media file. Attributes of the **ENTRY** element override **ASX** element attributes. While the **ENTRY** element's referenced media clip is playing, **TITLE** metadata from the **ENTRY** element is displayed instead of title information from the **ASX** element.

-   Windows Media file scope

    Attributes of the Windows Media file are overridden by any metafile attributes. Media file metadata is displayed only if there is no metadata defined for that element in the metafile.

## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 




