---
title: Event Handlers
description: Event Handlers
ms.assetid: ec806b92-a66d-499d-9bb3-cea7e82676bb
keywords:
- Windows Media Player skins,event handlers in JScript
- skins,event handlers in JScript
- events,JScript
- JScript files for skins,event handlers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Event Handlers

Microsoft JScript is used to process events in the skin definition file. See [Handling Events](handling-events.md) for more information about event handlers.

You can have more than one line of code in an event handler, but care must be taken not to exceed the line length that JScript permits. Separate the lines by semicolons.


```C++
onclick = "JScript: player.URL = 'http://proseware.com/cool.wma' ; myText.value = 'Playing'; "

```



## Related topics

<dl> <dt>

[**Using JScript**](using-jscript.md)
</dt> </dl>

 

 




