---
title: Internal Events
description: Internal Events
ms.assetid: d99e84ec-41db-42e7-ab26-5ca6a3ba610b
keywords:
- Windows Media Player skins,internal events
- skins,internal events
- events,internal
- writing code for skins,internal events
- internal events
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Internal Events

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can detect changes that occur in Windows Media Player or changes in your own skin. These can be changes in Windows Media Player object properties or methods, changes in skin attributes, and so on.

## Windows Media Player Property Changes

You can process changes in Windows Media Player by using the wmpprop listener. You must set up the listener as a value of an attribute. Put the value in double quotes, and start with the word "wmpprop" followed by a colon. Then you include the property you want to listen to. When the property changes, the value of the attribute will change also. For example, to have a slider element value change whenever the value of the **currentPosition** attribute changes, type the following:


```C++
<SLIDER id="mySlider" value="wmpprop:player.Controls.currentPosition" />
```



-   **Important** Do not use wmpprop on Windows Media Player methods. Unexpected results may occur.

## Windows Media Player Method Changes

You can make your skin respond to the availability of methods on Windows Media Player using wmpenabled and wmpdisabled. These are used similarly to the wmpprop listener except that you can only use these on methods of the **Control** object that are supported by the **isAvailable** method.

For example, you could enable a button only when the **Play** method is enabled, using code like this:


```C++
<BUTTON ... enabled="wmpenabled:player.Controls.Play();" />

```



-   **Important** Do not use wmpenabled or wmpdisabled on Windows Media Player properties. Unexpected results may occur.

## Skin Attribute Changes

You can respond to changes in your skin attributes in one of two ways, by using wmpprop or the **\_onchange** event.

You can use wmpprop to listen for changes in your own skin. For example, to show the Slider value in a text box, you could type the following:


```C++
<TEXT ... value="wmpprop:mySlider.value">

```



You can use the **\_onchange** event to process events inside an element. You must attach the name of the attribute you want to track to **\_onchange**. For example, if you want to track the value of a text box, you would type:


```C++
value_onchange

```



You would then assign a JScript string that you want to run when the value changes. For example, to respond to a change in the value of a text box that can be used to adjust the volume of Windows Media Player, type the following inside your **TEXT** element as an attribute:


```C++
value_onchange = "JScript: player.Settings.Volume = myText.value"

```



## Related topics

<dl> <dt>

[**Handling Events**](handling-events.md)
</dt> </dl>

 

 




