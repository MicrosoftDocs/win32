---
title: Windows Media Metafile Elements Reference
description: Windows Media Metafile Elements Reference
ms.assetid: 6f85e488-53f6-4fb0-ba48-55c3d7e59f1c
keywords:
- Windows Media metafiles,reference
- metafiles,reference
- reference for Windows Media metafiles
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Windows Media Metafile Elements Reference

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section contains reference documentation for all Windows Media metafile elements for client-side applications. Reference entries include definitions of the elements, their attributes and values, and special conditions related to each element.

The following metafile elements are supported for client-side applications.



| Element                                           | Description                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [ABSTRACT](abstract-element.md)                  | Contains text that describes the associated **ASX**, **BANNER**, or **ENTRY** element.                                 |
| [ASX](asx-element.md)                            | Defines a file as a Windows Media metafile.                                                                            |
| [AUTHOR](author-element.md)                      | Contains the name of the author of a media clip or a Windows Media metafile.                                           |
| [BANNER](banner-element.md)                      | Specifies a URL for a graphic that appears in the display panel of Windows Media Player.                               |
| [BASE](base-element.md)                          | Specifies a string that is appended to the front of URLs sent to Windows Media Player.                                 |
| [Comments](comments.md)                          | Specifies the XML syntax for comments ( <!--...--> ).                                                            |
| [COPYRIGHT](copyright-element.md)                | Contains the copyright information for an **ASX** or **ENTRY** element.                                                |
| [DURATION](duration-element.md)                  | Specifies the length of time Windows Media Player renders a stream.                                                    |
| [ENDMARKER](endmarker-element.md)                | Specifies a marker at which Windows Media Player stops rendering the stream.                                           |
| [ENTRY](entry-element.md)                        | Specifies the path for a media clip.                                                                                   |
| [ENTRYREF](entryref-element.md)                  | Links to the **ENTRY** elements in an external Windows Media metafile that has an .asx, .wax, .wvx, or .wmx extension. |
| [EVENT](event-element.md)                        | Defines a behavior or action taken by Windows Media Player when it receives a script command labeled as an event.      |
| [LOGURL](logurl-element.md)                      | Instructs Windows Media Player to submit any log data to the specified URL.                                            |
| [MOREINFO](moreinfo-element.md)                  | Specifies a URL for a website, email address, or script command associated with a show, clip, or banner.               |
| [PARAM](param-element.md)                        | Specifies the value of a custom parameter associated with a playlist or an element of a playlist.                      |
| [PREVIEWDURATION](previewduration-element.md)    | Specifies the length of time a clip is played in preview mode.                                                         |
| [REF](ref-element.md)                            | Specifies a URL for a piece of digital media content.                                                                  |
| [REPEAT](repeat-element.md)                      | Specifies the number of times Windows Media Player repeats one or more **ENTRY** or **ENTRYREF** elements.             |
| [SKIN (deprecated)](skin-element--deprecated.md) | Specifies a URL to an embedded skin.                                                                                   |
| [STARTMARKER](startmarker-element.md)            | Specifies a marker at which Windows Media Player starts rendering the stream.                                          |
| [STARTTIME](starttime-element.md)                | Specifies a time at which Windows Media Player will start rendering the stream.                                        |
| [TITLE](title-element--metafile.md)              | Contains the title of an **ASX** or **ENTRY** element.                                                                 |



 

 

 




