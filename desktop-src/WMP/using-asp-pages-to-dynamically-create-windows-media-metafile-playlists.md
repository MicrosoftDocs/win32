---
title: Using ASP Pages to Dynamically Create Windows Media Metafile Playlists
description: Using ASP Pages to Dynamically Create Windows Media Metafile Playlists
ms.assetid: 9abf04a4-33b9-4502-aaf3-e40de06c7b41
keywords:
- Windows Media metafile playlists,creating
- metafile playlists,creating
- playlists,creating
- Windows Media metafile playlists,dynamically creating
- metafile playlists,dynamically creating
- playlists,dynamically creating
- Windows Media metafile playlists,ASP pages
- metafile playlists,ASP pages
- playlists,ASP pages
- creating Windows Media metafile playlists
- dynamically creating Windows Media metafile playlists
- ASP pages
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Using ASP Pages to Dynamically Create Windows Media Metafile Playlists

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use Active Server Pages (ASP, or .asp files) to dynamically generate playlists based on information provided by users. An ASP page is a dynamic webpage used in conjunction with Microsoft Internet Information Services (IIS). ASP is an environment in which you can combine HTML, scripts, and reusable ActiveX server components to create dynamic and powerful Web-based business solutions. ASP pages enable server-side scripting for IIS with native support for both Microsoft Visual Basic Scripting Edition (VBScript) and Microsoft JScript. This discussion assumes that you are familiar with ASP and defining variables.

All header information must be contained on the first line of the ASP page string returned to Windows Media Player.

When you use ASP pages to generate playlists, you must specify values for the **Response** object's **ContentType** and **expires** properties in the ASP page because of latency issues with Windows Media Player. The **Response.ContentType** value must be a valid file name extension for Windows Media metafiles. Acceptable values include wma, wax, wmv, wvx, asf, and asx.

The **Response.expires** property specifies the length of time, in seconds, that Windows Media Player caches the playlist file. Specifying a value of zero results in Windows Media Player requesting a new playlist from the server each time the user refreshes the page.

See the Platform SDK for details about using the **Response** object in Active Server Pages.

The following code is an example of an ASP page used to generate a Windows Media metafile playlist.


```XML
<%Response.ContentType = "video/x-ms-wma"%><%Response.expires=0 %>
<ASX VERSION="3.0">
    <TITLE>Your title here</TITLE>
    <ENTRY>
        <REF HREF ="mms://adventure-works.com/pubpt/filename.wma" />
    </ENTRY>
</ASX>

```



## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> </dl>

 

 




