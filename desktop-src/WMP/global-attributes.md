---
title: Global Attributes (Windows Media Player SDK)
description: Global Attributes
ms.assetid: 2ed09506-990e-4da2-89d6-6ff77dc43eb2
keywords:
- Windows Media Player skins,global attributes
- skins,global attributes
- reference for skins,global attributes
- global attributes
- attributes,global
ms.topic: article
ms.date: 05/31/2018
---

# Global Attributes

Global attributes are attributes that provide easy access to certain player elements or objects from anywhere within a skin.

The **player** global attribute is a reference to the [Player](player-object.md) object, and is used to access the primary functionality of Windows Media Player. The following example uses **player** to begin digital media playback.


```C++
<BUTTON
  onclick="jscript:player.controls.play();"
/>

```



The **theme** global attribute is a reference to the [THEME](theme-element.md) element. This is the proper way to access **THEME** attributes, rather than by specifying an ID within the **THEME** element. The following example uses **theme** to open a new view.


```C++
<TEXT 
  value="open" 
  onclick="jscript:theme.openView('newView');"
/>

```



The **view** global attribute is a reference to the current [VIEW](view-element.md). This can be used instead of the ID specified within the various **VIEW** elements. The following example uses **view** to close the current view.


```C++
<BUTTON 
  id="quitbutton"
  onclick="jscript:view.close();"
/>

```



The **event** global attribute is used to access ambient event attributes from within event handlers. The following example uses **event** to determine whether the ALT key is pressed when a button is clicked.


```C++
<BUTTON
  onclick="jscript:if (event.altKey == true) myText.value='ALT';"
/>

```



The **playerApplication** global attribute is a reference to the [PlayerApplication](playerapplication-object.md) object, and is used by skin files provided as custom user interfaces for remoted Player controls. The Player control can be embedded in remote mode only in C++ programs that implement the **IWMPRemoteMediaServices** interface. The following example uses **playerApplication** to switch to the full mode of the Player.


```C++
<BUTTON
  onclick="jscript:playerApplication.switchToPlayerApplication();"
/>

```



For more information, see [Ambient Event Attributes](ambient-event-attributes.md).

## Related topics

<dl> <dt>

[**Miscellaneous**](miscellaneous.md)
</dt> </dl>

 

 




