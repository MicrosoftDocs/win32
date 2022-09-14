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
ms.date: 05/31/2018
---

# Writing Event Code

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

 

 




