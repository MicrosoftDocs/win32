---
title: VIEW.minimize
description: The minimize method minimizes the VIEW.
ms.assetid: 97c257fa-aa4f-4e6f-bc49-fa54db63b59b
keywords:
- VIEW.minimize Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.minimize
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# VIEW.minimize

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **minimize** method minimizes the **VIEW**.

``` syntax
        elementID.minimize()
```

## Parameters

This method has no parameters.

## Return Value

This method does not return a value.

## Examples


```JScript
<THEME>
  <VIEW id="View1">
    <BUTTON id="Open" image="Open.png" 
        onclick="jscript:View1.minimize()">
    </BUTTON>
  </VIEW>
</THEME>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> <dt>

[**VIEW.maximize**](view-maximize.md)
</dt> </dl>

 

 





