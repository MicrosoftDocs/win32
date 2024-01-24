---
title: Ensuring that Windows Media Player Opens the HTMLView Content
description: Ensuring that Windows Media Player Opens the HTMLView Content
ms.assetid: 4ec4e027-4f9c-4a86-9f70-b4014971c070
keywords:
- Windows Media metafile playlists,Windows Media Player opening HTMLView content
- playlists,Windows Media Player opening HTMLView content
- metafile playlists,Windows Media Player opening HTMLView content
- Windows Media metafile playlists,opening HTMLView content
- playlists,opening HTMLView content
- metafile playlists,opening HTMLView content
- opening HTMLView content
- Windows Media Player,opening HTMLView content
- Windows Media Player,HTMLView content
- HTMLView,opening content
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Ensuring that Windows Media Player Opens the HTMLView Content

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Currently, Windows Media Player 9 Series and Windows Media Player 10 are the only players that support the *HTMLView* parameter in .asx files. This means you should take steps to ensure that your HTMLView content plays back in these versions of Windows Media Player.

You must first determine whether Windows Media Player 9 Series or Windows Media Player 10 is installed on the user's computer. The Windows Media Player SDK includes a comprehensive sample that demonstrates how to detect different versions of Windows Media Player in different Web browsers. Although a complete analysis of the detection sample is beyond the scope of this section, there are some basic steps you can take to determine which version of Windows Media Player the user's computer is running.

In its simplest form, detecting Windows Media Player involves embedding the Player control in the webpage that links to your HTMLView content and then inspecting the value retrieved by the *Player*.**versionInfo** property. Once you have verified that the user has Windows Media Player 9 Series or Windows Media Player 10 installed, you can use the [Player.openPlayer](player-openplayer.md) method to open the content in the full-mode Player. The **openPlayer** method ensures that your content is initially displayed in the **Now Playing** feature of the full-mode Player, rather than in a skin, in mini Player mode, or in another player that has registered itself as the default program for files with an .asx file name extension, but doesn't support HTMLView. Once the content is displayed, however, the user has complete control of Windows Media Player, meaning that he or she can choose to display a feature other than **Now Playing**, switch to skin mode, or even quit the Player.

The following example code creates a webpage for Internet Explorer. This page opens an .asx file, which specifies an HTMLView webpage that appears in the full-mode Player when Windows Media Player 9 Series or later is installed.


```XML
<HTML>
<BODY>

<!-- This code embeds the Player object in invisible mode. -->
<OBJECT id = "Player" 
    CLASSID = "CLSID:6BF52A52-394A-11d3-B153-00C04F79FAA6" height = 0 width = 0> 
        <PARAM Name = "AutoStart"  Value = "True">
        <PARAM Name = "uiMode" Value = "invisible">
</OBJECT>

<!-- Create a button to open the content. -->
<INPUT Type = "Button"  ID = "btnPlay"  Value = "Play ASX"  onClick = "PlayASX();"/>

<SCRIPT Language = "JScript">

// This function tests the Player version. If it is Windows Media 
// Player 9 Series or later, the script opens the .asx file in the full-mode 
// Player. Otherwise, the script makes the embedded control visible to 
// the user and opens the .asx file in the webpage. 

function PlayASX()
{
    if(parseInt(Player.versionInfo) >= 9)
        {
            // Open the full-mode Player to show HTMLView.
            Player.openPlayer("https://www.proseware.com/MyHTMLView.asx");
        }
        else
        {
            // Open the .asx file in the embedded Player.
            Player.uiMode = "full";
            Player.height = 200;
            Player.width = 200;
            Player.URL = "https://www.proseware.com/MyHTMLView.asx";
        }
}
</SCRIPT>

</BODY>
</HTML>

```



The code in the preceding example embeds the Windows Media Player control with the **uiMode** property set to "invisible" and the Player height and width attributes set to zero. This is because the webpage does not require the Player control user interface to be displayed initially—it only requires access to the Player object model. The page also displays an input button that enables the user to play the .asx file.

When the user clicks the Play ASX button, the Microsoft JScript function PlayASX runs. This function first retrieves the value for the Player **versionInfo** property, using the JScript **parseInt** method to inspect the numerical value of the string retrieved. If the numerical value is greater than or equal to 9 (meaning that the user has Windows Media Player 9 Series installed), the script code calls the **openPlayer** method, passing the URL of the .asx file that contains the HTMLView parameter. This method opens the .asx file using Windows Media Player in full mode, plays the digital media content in the .asx playlist, and displays the HTMLView Web-based content in the **Now Playing** feature.

If the numerical value of the version string is not greater than or equal to 9 (meaning that the user does not have Windows Media Player 9 Series or later installed on his or her computer), the script code changes the **uiMode** of the Player control to "full", sets a new width and height for the control, and then opens the .asx file in the embedded Player by specifying a value for the **URL** property. When this happens, the digital media content plays in the webpage, but any HTMLView values specified in the .asx file are ignored.

How content is played back when the user does not have Windows Media Player 9 Series or Windows Media Player 10 installed is up to you. The preceding example shows how to specify that the content play in the webpage instead of the full-mode Player, ignoring any HTMLView content in the process. There are other approaches you might take. For example, you could prompt the user to install a newer version of Windows Media Player, making that version of the Player a requirement for playing back your digital media content.

## Related topics

<dl> <dt>

[**Displaying Web Pages in Windows Media Player**](displaying-web-pages-in-windows-media-player.md)
</dt> <dt>

[**Player.uiMode**](player-uimode.md)
</dt> <dt>

[**Player.URL**](player-url.md)
</dt> </dl>

 

 




