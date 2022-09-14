---
title: Advantages of Using HTMLView
description: Advantages of Using HTMLView
ms.assetid: bbec9471-87f1-4c41-a322-f11e9e1dec37
keywords:
- Windows Media metafile playlists,HTMLView advantages
- playlists,HTMLView advantages
- metafile playlists,HTMLView advantages
- Windows Media metafile playlists,advantages of HTMLView
- playlists,advantages of HTMLView
- metafile playlists,advantages of HTMLView
- advantages of HTMLView
- Windows Media Player,advantages of HTMLView
- Windows Media Player,HTMLView advantages
- HTMLView,advantages
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Advantages of Using HTMLView

The HTMLView feature makes it easy to create an integrated Web-based user experience that plays back digital media content by using the familiar look of the Web. When you combine Web-based content with digital media content in the Windows Media Player user interface (UI), the result can have a greater impact on the user than when the elements are viewed separately. The digital media content is enhanced by interesting related information, while the webpage can provide links to similar content, thereby creating new business opportunities.

## HTMLView provides a better user experience

Users want and enjoy accessing the information that can be offered with digital media content, but they don't want to deal with a seemingly endless series of pop-up advertisements. Using pop-up browser windows to display advertising on the Web has become so commonplace that there is now software that prevents these windows from opening. This software can have the unwanted side effect of preventing legitimate webpages from being displayed, sometimes suppressing an entire digital media presentation.

When you use the HTMLView feature, users no longer have to deal with pop-up windows. Instead of having to open a separate browser window to provide additional information to the user, you can display custom, Web-based content in the **Now Playing** feature of the Windows Media Player UI while the Player plays the audio or video content the user wants. Users can control playback by using the Windows Media Player controls. Since your content plays in the full-mode Player, software designed to prevent pop-up ads won't stop users from enjoying the content.

## HTMLView content is easy to create

As the feature name implies, you create Web-based content displayed using the HTMLView feature by using Hypertext Markup Language (HTML). If you already create content for the Web, this means that you don't need to learn a new programming language to create rich content easily with the HTMLView feature. If you already have webpages with an embedded Windows Media Player ActiveX control, you can have these pages appear in the Player UI by simply pointing to these webpages from a Windows Media metafile (.asx file) by using a special parameter.

Windows Media Player uses an embedded instance of Microsoft Internet Explorer to display HTMLView content. This means that you don't have to consider different Internet browsers, multiple scripting models, or different scripting languages when creating your webpages. Even if the user doesn't use Internet Explorer as his or her default browser, your webpage is still displayed properly in the Player.

It is possible that a program other than Windows Media Player may register itself as the default program for opening .asx files. The Windows Media Player 9 Series or later object model includes a new method, **openPlayer**, that enables you to specify a Uniform Resource Locator (URL) for the content you want to play. When you use the **openPlayer** method, Windows Media Player always opens in full mode to play the specified content. Using this method, you can ensure that your HTMLView content is displayed in Windows Media Player, rather than some other application that has taken over the .asx file type association.

## Related topics

<dl> <dt>

[**Displaying Web Pages in Windows Media Player**](displaying-web-pages-in-windows-media-player.md)
</dt> <dt>

[**Player.openPlayer**](player-openplayer.md)
</dt> </dl>

 

 




