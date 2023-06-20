---
title: THEME.openViewRelative
description: The openViewRelative method opens a VIEW in a new window at a specified initial position relative to the upper-left corner of the skin.
ms.assetid: fc31a1ce-e6b9-4084-b244-28fad486f485
keywords:
- THEME.openViewRelative Windows Media Player
topic_type:
- apiref
api_name:
- THEME.openViewRelative
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# THEME.openViewRelative

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **openViewRelative** method opens a **VIEW** in a new window at a specified initial position relative to the upper-left corner of the skin.

``` syntax
        theme.openView(view, left, top)
```

## Parameters

<dl> <dt>

<span id="view"></span><span id="VIEW"></span>*view*
</dt> <dd>

A **String** specifying the **id** of the **VIEW** to open.

</dd> <dt>

<span id="left"></span><span id="LEFT"></span>*left*
</dt> <dd>

A **Number** (**long**) specifying the initial distance in pixels of the left border of the **VIEW** from the left border of the skin. A negative value indicates an initial position to the left of the skin border.

</dd> <dt>

<span id="top"></span><span id="TOP"></span>*top*
</dt> <dd>

A **Number** (**long**) specifying the initial position of the top border of the **VIEW** relative to the top border of the skin. A negative values indicates an initial position above the skin border.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

The position specified for the **VIEW** is used the first time this method is called, after which the user can drag the **VIEW** to another location. The new position is saved, and on subsequent calls, the most recent position is used.

## Examples


```JScript
<THEME>
  <VIEW>
    <TEXT value="open" 
        onclick="jscript:theme.openViewRelative('newView', 50, 50)"/>
    <TEXT top="30" value="close" 
        onclick="jscript:theme.closeView('newView')"/>
  </VIEW>
  <VIEW id="newView"/>
</THEME>
```



## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**THEME Element**](theme-element.md)
</dt> <dt>

[**THEME.closeView**](theme-closeview.md)
</dt> <dt>

[**THEME.openView**](theme-openview.md)
</dt> </dl>

 

 





