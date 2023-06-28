---
title: THEME.openView
description: The openView method opens a VIEW in a new window.
ms.assetid: 2aa63c29-dafe-4942-a010-076f1503862b
keywords:
- THEME.openView Windows Media Player
topic_type:
- apiref
api_name:
- THEME.openView
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# THEME.openView

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **openView** method opens a **VIEW** in a new window.

``` syntax
        theme.openView(view)
```

## Parameters

<dl> <dt>

<span id="view"></span><span id="VIEW"></span>*view*
</dt> <dd>

A **String** specifying the **id** of the **VIEW** to open.

</dd> </dl>

## Return Value

This method does not return a value.

## Examples


```JScript
<THEME>
  <VIEW>
    <TEXT value="open" 
        onclick="jscript:theme.openView('newView')"/>
    <TEXT top="30" value="close" 
        onclick="jscript:theme.closeView('newView')"/>
  </VIEW>
  <VIEW id="newView"/>
</THEME>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**THEME Element**](theme-element.md)
</dt> <dt>

[**THEME.closeView**](theme-closeview.md)
</dt> <dt>

[**THEME.openViewRelative**](theme-openviewrelative.md)
</dt> </dl>

 

 





