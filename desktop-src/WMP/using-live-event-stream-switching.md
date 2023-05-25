---
title: Using Live Event Stream Switching
description: Using Live Event Stream Switching
ms.assetid: fa8af007-2db6-438f-9551-8e748bb79ef4
keywords:
- Windows Media metafile playlists,live event stream switching
- playlists,live event stream switching
- metafile playlists,live event stream switching
- Windows Media metafile playlists,event stream switching
- playlists,event stream switching
- metafile playlists,event stream switching
- Windows Media metafile playlists,ad insertion
- playlists,ad insertion
- metafile playlists,ad insertion
- Windows Media Player,live event stream switching
- Windows Media Player,event stream switching
- Windows Media Player,ad insertion
- live event stream switching
- event stream switching
- ad insertion
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Using Live Event Stream Switching

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Streaming media can also be controlled by the interaction of script commands embedded in a media stream with Windows Media metafile elements in a metafile playlist.

An event is a particular type of script command embedded in a media stream or media file. When the Windows Media Player control receives the script command, it processes the event as defined by the **EVENT** element in the metafile playlist. Windows Media Player switches from the current stream it is rendering and renders the content referenced in the metafile playlist **EVENT** element. The **EVENT** element is usually used in live production.

An **EVENT** element looks similar to an **ENTRY** element, but each handles the playback of streams and media files differently. The **ENTRY** element is used to create playlists. A stream or media file referenced in an **ENTRY** element starts playing when the stream or media file referenced in the previous **ENTRY** finishes. A stream referenced in an **EVENT** plays only when a specific script command is received. For example, when Windows Media Player receives a script command with type string "EVENT" and the command string "Adlink", it searches the playlist for the following elements.


```XML
<EVENT NAME="Adlink" WHENDONE="RESUME"> 
    <ENTRY HREF=mms://www.proseware.com/adlink.wma />
</EVENT>

```



Windows Media Player then switches from the live stream to play the stream or media file contained in the **EVENT**, in this case Adlink.wma. The code `WHENDONE="RESUME"` instructs Windows Media Player to resume playing the previous stream when Adlink.wma is finished.

> [!Note]  
> Failure to handle every event embedded in a media stream or media file may yield unexpected results.

 

If you want to use live event stream switching, you must include one **EVENT** element in your playlist to handle each event script command embedded in the media streams or media files in your playlist. Before you create your playlist, you must know the details about which script commands are embedded in your digital media content. If there is an event script command that you want Windows Media Player to ignore, include an **EVENT** element in your playlist to handle the event, but reference a dummy URL in the event handler.

## Ad Insertion

This technique can be used for ad insertion. For example, during a live Internet broadcast of a ball game, a command can be sent at the beginning of every commercial break that instructs each client (Windows Media Player) to play commercials listed in its playlist. When clients finish playing the commercials, the playlist instructs each client to cut back to the live broadcast. The **EVENT** media content will be rendered only when the streaming media being accessed broadcasts embedded scripting with the matching **EVENT** name.

The possibilities inherent in **EVENT** switching are best appreciated by contrasting how ads reach viewers through standard, over-the-air broadcasting with how ads can reach viewers using Windows Media Technologies. Historically, broadcast ads could only be roughly targeted at viewers, using ratings data as the primary criteria. Ads sent using Windows Media Technologies can be aimed directly at the target user because **EVENTs** and playlists can be built on the fly based on user input. For more information, see [Personalizing Media Delivery](personalizing-media-delivery.md).

You can also use metafile playlists to display customized graphics, audio and text for advertising. You can use the **BANNER** element as a child element of an **EVENT** to display an advertising message graphic. The **BANNER** element provides the path and file containing the graphics for your advertising banner. You can also provide a link to a site or file using the **MOREINFO** child element. The URL in the **MOREINFO** element can provide a link to even more advertisements on the Web. The following example demonstrates using these elements.

Example Code


```XML
<BANNER HREF="SomePath\2.gif">
    <ABSTRACT>Read This Ad and Buy.</ABSTRACT>
    <MOREINFO HREF="https://www.proseware.com" />
</BANNER>

```



The following example inserts the ad Advert.wma into the broadcast unicast stream BallGame when a client receives a script command **EVENT** with the **NAME** attribute set to "Time-Out". **CLIENTSKIP** is set to NO to prevent the streamed ad from being skipped. In this example, the streamed ad must be played before returning to the original stream. When the ad is finished, the client resumes playing the original stream.

Example Code


```XML
<ASX VERSION="3.0">
    <ENTRY>
        <REF HREF="mms://proseware.com/BallGame" />
    </ENTRY>
    <EVENT NAME="Time-Out" WHENDONE="RESUME">
        <ENTRY>
            <REF HREF = "mms://proseware.com/Advert.wma" 
                CLIENTSKIP = "NO" />
       </ENTRY>
    </EVENT>
</ASX>

```



## Related topics

<dl> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Using Metafile Playlists**](using-metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 




