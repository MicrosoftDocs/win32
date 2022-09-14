---
title: Attributes with Multiple Values (Windows Media Format 11 SDK)
description: Learn about attributes with multiple values in the Windows Media Format 11 SDK. Some media item attributes can have multiple values.
ms.assetid: 2e65c5d0-6f5e-45a4-8e13-9e49da007145
keywords:
- Windows Media Format SDK,attributes
- Advanced Systems Format (ASF),attributes
- ASF (Advanced Systems Format),attributes
- attributes,multiple values
ms.topic: article
ms.date: 05/31/2018
---

# Attributes with Multiple Values (Windows Media Format 11 SDK)

Some of the predefined attributes can have multiple values assigned to them. For example, **Artist** is an attribute that can have multiple values. You can call [**IWMHeaderInfo3::AddAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-addattribute) multiple times to add as many **Artist** values as you require. If you make multiple calls to **AddAttribute** for attributes that do not support multiple values, the method may return an error code, or simply ignore your request.

The following table lists the attributes that support multiple values. Some attributes can have multiple values only in ASF files, while others can have multiple values in both ASF and MP3 files.



| Attribute                                                 | Support for multiple values |
|-----------------------------------------------------------|-----------------------------|
| [**Author**](author.md)                                  | ASF, MP3                    |
| [**WM/AlbumArtist**](wm-albumartist.md)                  | ASF                         |
| [**WM/AlbumCoverURL**](wm-albumcoverurl.md)              | ASF                         |
| [**WM/Category**](wm-category.md)                        | ASF                         |
| [**WM/Composer**](wm-composer.md)                        | ASF, MP3                    |
| [**WM/Conductor**](wm-conductor.md)                      | ASF                         |
| [**WM/Director**](wm-director.md)                        | ASF                         |
| [**WM/Genre**](wm-genre.md)                              | ASF                         |
| [**WM/GenreID**](wm-genreid.md)                          | ASF                         |
| [**WM/Language**](wm-language.md)                        | ASF, MP3                    |
| [**WM/Lyrics\_Synchronised**](wm-lyrics-synchronised.md) | ASF, MP3                    |
| [**WM/Mood**](wm-mood.md)                                | ASF, MP3                    |
| [**WM/Picture**](wmpicture.md)                           | ASF, MP3                    |
| [**WM/Producer**](wm-producer.md)                        | ASF                         |
| [**WM/PromotionURL**](wm-promotionurl.md)                | ASF                         |
| [**WM/UserWebURL**](wm-userweburl.md)                    | ASF, MP3                    |
| [**WM/Writer**](wm-writer.md)                            | ASF, MP3                    |



 

## Related topics

<dl> <dt>

[**Attributes**](attributes.md)
</dt> </dl>

 

 




