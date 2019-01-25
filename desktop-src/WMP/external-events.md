---
title: External Events
description: External Events
ms.assetid: d3fd8af6-8d7e-43b8-88fd-a59cf0cef609
keywords:
- Windows Media Player skins,external events
- skins,external events
- events,external
- writing code for skins,external events
- external events
ms.topic: article
ms.date: 05/31/2018
---

# External Events

When users click a button or press a key, you can respond to their input with event handlers. An event handler is a section of code that runs whenever the event is triggered.

The following events are supported by skin elements:

-   **load**
-   **close**
-   **resize**
-   **timer**
-   **click**
-   **dblclick**
-   **error**
-   **mousedown**
-   **mouseup**
-   **mousemove**
-   **mouseover**
-   **mouseout**
-   **keypress**
-   **keydown**
-   **keyup**

See the [Skin Programming Reference](skin-programming-reference.md) for more details about specific events.

A typical external event handler would name the event and define the code that will run. For example, if you want to create code to start Windows Media Player when the user clicks on a button, you would put the following line in your button code.


```C++
onclick = "JScript: player.URL = 'https://proseware.com/laure.wma' ; "

```



This will play the file named laure.wma. Note that you add the word "on" to specific events.

## Related topics

<dl> <dt>

[**Handling Events**](handling-events.md)
</dt> </dl>

 

 




