---
title: Writing Event Code
description: Writing Event Code
ms.assetid: ce29aa81-1db8-4aea-a3bd-86c6b559fff7
keywords:
- Windows Media Player skins,writing code
- skins,writing code
- events,writing code
- writing code for skins,about
- Windows Media Player skins,events
- skins,events
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writing Event Code

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Events are treated similarly to attributes. You must give the event a value, and the value is the code you want to run when the event happens. The word "on" is added to the front of the event name; for example, the click event will become **onclick**.

The event value is in double quotes and starts with the word JScript followed by a colon. The code you want to run comes next, followed by a semicolon and the closing double quotes. For example, to stop playing when the user clicks on a button, type the following as an attribute in your **BUTTON** element code:


```C++
onclick = "JScript: player.Controls.Stop() ; "
```



If you have a code that requires quotes, use single quotes. Care must be taken when using quotation marks so that they are balanced properly. Here is an example of using both types:


```C++
onclick = "JScript: player.URL = 'https://proseware.com/laure.wma' ; "
```



You can also change attributes of your skin when handling an external event. For example, to close a view named myView, you could type:


```C++
onclick = "JScript: myView.close() ;"
```



## Related topics

<dl> <dt>

[**Handling Events**](handling-events.md)
</dt> </dl>

 

 




