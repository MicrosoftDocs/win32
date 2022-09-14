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
ms.date: 05/31/2018
---

# Event Handlers

Microsoft JScript is used to process events in the skin definition file. See [Handling Events](handling-events.md) for more information about event handlers.

You can have more than one line of code in an event handler, but care must be taken not to exceed the line length that JScript permits. Separate the lines by semicolons.


```C++
onclick = "JScript: player.URL = 'https://proseware.com/cool.wma' ; myText.value = 'Playing'; "

```



## Related topics

<dl> <dt>

[**Using JScript**](using-jscript.md)
</dt> </dl>

 

 




