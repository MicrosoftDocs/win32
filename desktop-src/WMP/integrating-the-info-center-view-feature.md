---
title: Integrating the Info Center View Feature
description: Integrating the Info Center View Feature
ms.assetid: ce6692d2-a780-4aab-809f-c63236edd912
keywords:
- Windows Media Player online stores,integrating Info Center View
- online stores,integrating Info Center View
- type 1 online stores,integrating Info Center View
- type 2 online stores,integrating Info Center View
- Windows Media Player online stores,Info Center View
- online stores,Info Center View
- type 1 online stores,Info Center View
- type 2 online stores,Info Center View
- integrating Info Center View
- Info Center View
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Integrating the Info Center View Feature

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player enables users to open and close the Info Center View feature. Info Center View is the feature where users expect to find rich, extended information about specific digital media content. When the user chooses to open Info Center View, Windows Media Player calls on the current music store to display the Info Center View webpage specified by the **URL** attribute of the **InfoCenter** element of the ServiceInfo document.

To retrieve information about the currently playing digital media content, you must embed an instance of the Windows Media Player control in your webpage and use the Player object model. For example, to retrieve the title, you could use the following JScript code:


```C++
// The control was created with ID = "Player"
var title = Player.currentMedia.getItemInfoByType("Title", "", 0);
```



## Guidelines for Info Center View

When creating your **Info Center View** webpage, use the following guidelines:

-   The page must clearly identify the online store providing the information. You can do this by prominently displaying your logo, for example.
-   The page must include a link to your company's privacy statement.
-   Avoid page navigation within the Info Center View feature whenever possible. You should navigate to your online store for most activities.
-   It is best to provide valuable information without requiring the user to install programs or log in to your online store.

## Related topics

<dl> <dt>

[**External.NavigateTaskPaneURL**](external-navigatetaskpaneurl.md)
</dt> <dt>

[**InfoCenter Element**](infocenter-element.md)
</dt> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**Using the Windows Media Player Control in a Web Page**](using-the-windows-media-player-control-in-a-web-page.md)
</dt> </dl>

 

 




