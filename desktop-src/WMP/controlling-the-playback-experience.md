---
title: Controlling the Playback Experience
description: Controlling the Playback Experience
ms.assetid: f130eee1-10ef-4cbe-b6ac-8ad24e1f0f34
keywords:
- Windows Media metafile playlists,controlling playback
- playlists,controlling playback
- metafile playlists,controlling playback
- Windows Media metafile playlists,playback issues
- playlists,playback issues
- metafile playlists,playback issues
- controlling playback
- Windows Media Player,controlling playback
- Windows Media Player,playback issues
- HTMLView,playback issues
- HTMLView,controlling playback
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Controlling the Playback Experience

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section discusses some of the playback issues you may encounter when using the HTMLView feature.

## Requiring the user to view Web-based content

You may decide that you only want users to be able to enjoy your digital media content when the HTMLView Web-based content is also displayed. You can include script code in your HTMLView webpage that stops playback of the digital media content if the user switches away from the **Now Playing** feature. To do this, you can specify an event handler for the **unload** event as part of the **BODY** element, as the following HTML code demonstrates:


```XML
<BODY onunload = "UnloadMe();">

```



Then you can include script code in your event handler function to close the file in the Player. The following example code does this:


```XML
function UnloadMe()
{
   Player.close();
}

```



When the user switches away from **Now Playing** by clicking a button to open another Windows Media Player feature, such as the library, the Player closes the embedded browser. This causes the **onunload** event to occur, running the script in the function named **UnloadMe**. The [Player.close](player-close.md) method stops playback and unloads the current digital media file. To view the content again, the user must reopen the original .asx file. This technique also stops playback when the user navigates away from the HTMLView webpage. Note that this technique cannot prevent the user from viewing the digital media content when he or she switches to skin mode.

You will recall that the HTMLView parameter can be applied to each **ENTRY** element in an .asx file. You can take advantage of this feature to ensure that your HTMLView content is displayed each time a new digital media file starts. To do this, associate a **PARAM** element for HTMLView with each entry in your .asx playlist. When each entry plays, the Player returns to full mode and displays the HTMLView content you specified in the playlist.

## URL and FILE script command types are disabled by default

Windows Media Player 9 Series or later provides settings that enable the user to specify whether URL and FILE type script commands are able to run. By default, both of these script command types do not run. If you use custom script command types, they will continue to run, regardless of the user setting. If you must use URL and FILE type script commands, you must prompt the user to change the settings. To change the settings, click **Tools**, then **Options**, and then **Security**.

## Reopening an HTMLView does not reload the webpage

When the user opens an .asx file that includes an HTMLView parameter and subsequently reopens the same file, Windows Media Player does not refresh the HTMLView webpage. This also means that if you have allowed users to navigate away from your HTMLView webpage, the Player does not return the embedded browser to the initial HTMLView webpage.

## Hiding the content location

You might decide that you don't want Windows Media Player to display the location of your digital media content while it is playing an .asx file. Usually, Windows Media Player only shows information about the playlist itself when streaming content from the Internet. However, there are further steps you can take to prevent users from determining the location of your content. For example, one way to ensure that the Player does not display the path to your content is to stream your content using Windows Media Services server-side playlists. That way, when the user views the properties for the content, he or she sees the URL of the server and not the URL of your content.

## Related topics

<dl> <dt>

[**Displaying Web Pages in Windows Media Player**](displaying-web-pages-in-windows-media-player.md)
</dt> <dt>

[**PARAM Element**](param-element.md)
</dt> </dl>

 

 




