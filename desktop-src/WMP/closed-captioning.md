---
title: Closed Captioning
description: Closed Captioning
ms.assetid: a5d4d591-4b4d-49c5-b7da-01d7ee303ffd
keywords:
- Windows Media Player,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player object model,Synchronized Accessible Media Interchange (SAMI)
- object model,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player Mobile,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player ActiveX control,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player Mobile ActiveX control,Synchronized Accessible Media Interchange (SAMI)
- ActiveX control,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player,migrating closed captions
- Windows Media Player object model,Smigrating closed captions
- object model,migrating closed captions
- Windows Media Player Mobile,migrating closed captions
- Windows Media Player ActiveX control,migrating closed captions
- Windows Media Player Mobile ActiveX control,migrating closed captions
- ActiveX control,migrating closed captions
- Synchronized Accessible Media Interchange (SAMI),migrating closed captions
- SAMI (Synchronized Accessible Media Interchange),migrating closed captions
- migration guide,Synchronized Accessible Media Interchange (SAMI)
- migration guide,closed captioning
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Closed Captioning

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Player 6.4 ActiveX control includes an integrated closed caption display panel that, when made visible, enables Synchronized Accessible Media Interchange (SAMI) closed captions and displays the closed caption text. The Windows Media Player 7 or later control enables SAMI closed caption display by using an HTML **<DIV>** element. For example:


```C++
<DIV  ID = "CCDiv"></DIV>

```



This technique provides you with complete flexibility, since you can design your webpage to display closed captions in a customized manner; the closed caption display is no longer required to be in a fixed location adjacent to the Windows Media Player user interface.

Once you have created an area to display closed captions, use the *ClosedCaption*.**captioningID** property to specify the location where Windows Media Player renders the closed caption text.


```C++
Player.closedCaption.captioningID = "CCDiv";

```



The Windows Media Player Software Development Kit (SDK) contains a working sample of an embedded Player that displays closed caption text. To get the SDK samples, download and install the complete Windows Media Player SDK from the Microsoft Web Site. For more information about closed captions and SAMI, see the [Microsoft Accessibility website](https://www.microsoft.com/enable/).

## Related topics

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> <dt>

[**ClosedCaption Object**](closedcaption-object.md)
</dt> <dt>

[**Object Model Migration Guide**](object-model-migration-guide.md)
</dt> </dl>

 

 




