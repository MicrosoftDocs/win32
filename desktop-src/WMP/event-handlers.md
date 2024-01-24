---
title: Event Handlers
description: Event Handlers
ms.assetid: 'abb5f123-b838-46fb-ab11-cee70cc76a38'
keywords:
- Windows Media Player skins,event handlers in JScript
- skins,event handlers in JScript
- events,JScript
- JScript files for skins,event handlers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Event Handlers

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Microsoft JScript is used to process events in the skin definition file. See [Handling Events](handling-events.md) for more information about event handlers.

You can have more than one line of code in an event handler, but care must be taken not to exceed the line length that JScript permits. Separate the lines by semicolons.


```C++
onclick = "JScript: player.URL = 'https://proseware.com/cool.wma' ; myText.value = 'Playing'; "

```



## Related topics

<dl> <dt>

[**Using JScript**](using-jscript.md)
</dt> </dl>

 

 




