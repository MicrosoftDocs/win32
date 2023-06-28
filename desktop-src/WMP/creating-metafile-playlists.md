---
title: Creating Metafile Playlists
description: Creating Metafile Playlists
ms.assetid: 0afe3aaa-bcd1-4060-8772-add50f3b6bac
keywords:
- Windows Media metafile playlists,creating
- playlists,creating
- metafile playlists,creating
- creating Windows Media metafile playlists
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Creating Metafile Playlists

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can create a playlist using any text editor, such as Microsoft Notepad. Open your text editor. Type the script entries you want to implement. After you have finished typing into Notepad, save the file with an appropriate file name and file name extension. For more information about extensions, see [Metafile Extension Guidelines](metafile-extension-guidelines.md). Typically the file name is the name of the Windows Media file or stream followed by an extension of .wax, .wvx, or .asx. For example, if your media content is a Windows Media audio file that has a .wma extension, use the .wax extension when naming the playlist. Playlists must not include any formatting codes from a word processor, such as Microsoft Word. To be sure no formatting codes are included in the playlist, save the file as a plain text or ASCII file.

> [!Note]  
> Elements and attributes are not case sensitive. The text used in the playlist to define an element or attribute can be either uppercase or lowercase, or a mixture of both.

 

If an element does not have any child elements (those that modify or are contained within another element), a single slash character (/) can be used at the end of the opening tag, just before the '>', in place of a closing tag. Child elements of an element must appear between the opening and closing tag for that element; otherwise they are not child elements for that element, and are ignored or cause an error in the syntax of the playlist.

The first four characters of a playlist must be "&lt;ASX". The **ASX** element is used in all playlists whether their extension is .wax, .wvx, or .asx. There must be only one **ASX** element per playlist. This element identifies the file as a Windows Media metafile playlist. It does not specify the type of playlist.

The **ASX** element has three possible attributes:

**VERSION**

The **VERSION** attribute is required and must follow immediately after the **ASX** element, for example "<ASX version = "3.0"&gt;". The current version number is 3.0. Windows Media Player supports all previous versions. Acceptable values for the **VERSION** attribute include both 3.0 and 3 (with no decimal point).

**PREVIEWMODE**

The **PREVIEWMODE** attribute is optional. It provides another mechanism for specifying how long to render a clip. If the value of the **PREVIEWMODE** attribute is YES, Windows Media Player will render each clip for the duration specified by the element **PREVIEWDURATION**. Each clip can have a **PREVIEWDURATION** specified.

**BANNERBAR**

The optional **BANNERBAR** attribute defines whether the Windows Media Player control reserves space for a banner graphic. (Use the **BANNER** element to specify the graphic to display.) If the value of **BANNERBAR** is FIXED, Windows Media Player reserves banner space for the show and for every clip, whether the metafile playlist specifies a banner for the show or clip. This will keep the size of the Windows Media Player window the same (except when the video size changes) regardless of the absence or presence of a banner graphic. If the show or clip does not have a banner associated with it, the space reserved for one is black. If the value of the **BANNERBAR** attribute is AUTO, Windows Media Player reserves space for the banner only when the show or clip includes one.


```XML
<ASX version="3.0" BANNERBAR="AUTO" >

```



For more information about the three attributes of the **ASX** element, see the reference entry for the [ASX Element](asx-element.md).

An **ASX** element contains **ENTRY** child elements that define information about the media files to be accessed. Each **ENTRY** element must contain a **REF** element that specifies the path to the media file to be streamed. There must be at least one **ENTRY** or **ENTRYREF** element within an **ASX** element.

Other elements defined within the scope of the **ASX** element, such as **TITLE** and **AUTHOR**, are associated with the metadata displayed by Windows Media Player.

The simplest playlists are created by adding multiple **ENTRY** elements with a single **REF** element to a metafile. Each **ENTRY** element in a metafile playlist is rendered in the order it appears in the file as though the user had manually opened each clip.

Example Code


```XML
<ASX version = "3.0">
<!--A simple playlist with entries to be played in sequence.-->
    <Title>The Show Title</Title>
    <Entry>
        <Ref href = "mms://adventure-works.com/Path/title1.wma" />
    </Entry>
    <Entry>
        <Ref href = "mms://adventure-works.com/Path/title2.wma" />
    </Entry>
    <Entry>
        <Ref href = "mms://adventure-works.com/Path/title3.wma" />
    </Entry>
</ASX>

```



Be sure that the playlist is working by double-clicking it in Windows Explorer. Windows Media Player should open and start streaming the media content. After you have confirmed that the playlist works, save it to your web server along with your webpages, and link to it by means of an **HREF** element, or embed it in a webpage using the Windows Media Player **OBJECT** element.

The following sections contain more information:

-   [Nesting Metafiles](nesting-metafiles.md)
-   [Using ASP Pages to Dynamically Create Windows Media Metafile Playlists](using-asp-pages-to-dynamically-create-windows-media-metafile-playlists.md)

## Related topics

<dl> <dt>

[**BANNER Element**](banner-element.md)
</dt> <dt>

[**Example Playlists**](example-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 




