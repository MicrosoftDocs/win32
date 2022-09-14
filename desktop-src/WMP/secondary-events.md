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
ms.date: 05/31/2018
---

# Secondary Events

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

 

 




