---
title: Secondary Events
description: Secondary Events
ms.assetid: cc9eb382-82ca-4416-a04e-1572e4c69c90
keywords:
- Windows Media Player skins,secondary events
- skins,secondary events
- events,secondary
- writing code for skins,secondary events
- secondary events
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Secondary Events

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can determine what other events are taking place when a specific event is triggered. For example, when a mouse button is clicked, you may want to know whether the ALT key was down at the same time.

## Event Attributes

The following event attributes are supported for skins:

-   **altKey**
-   **button**
-   **clientX**
-   **clientY**
-   **ctrlKey**
-   **fromElement**
-   **offsetX**
-   **offsetY**
-   **screenX**
-   **screenY**
-   **shiftKey**
-   **srcElement**
-   **toElement**
-   **x**
-   **y**
-   **keyCode**

For more information about these attributes, see the [Skin Programming Reference](skin-programming-reference.md).

## Using Secondary Events

You can only process event attributes in JScript code. You must use the following syntax:


```C++
event.eventattributename
```



*eventattributename* is the name of the event attribute. For example, to determine whether the ALT key was pressed during a click event, you could use the following lines in your JScript code:


```C++
wasAlt = event.altKey ;
if (wasAlt = true)
{
   // Do something here.
}
```



## Related topics

<dl> <dt>

[**Handling Events**](handling-events.md)
</dt> </dl>

 

 




