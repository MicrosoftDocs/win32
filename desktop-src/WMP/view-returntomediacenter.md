---
title: VIEW.returnToMediaCenter
description: The returnToMediaCenter method returns the user to the full mode of Windows Media Player.
ms.assetid: eebf0679-5704-498c-8eb3-f7710e0cb1fe
keywords:
- VIEW.returnToMediaCenter Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.returnToMediaCenter
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# VIEW.returnToMediaCenter

The **returnToMediaCenter** method returns the user to the full mode of Windows Media Player.

``` syntax
        elementID.returnToMediaCenter()
```

## Parameters

This method has no parameters.

## Return Value

This method does not return a value.

## Examples


```JScript
<THEME>
  <VIEW id="View1" backgroundImage="greenstone.bmp">
    <BUTTON id="Open" image="Open.png" 
        onclick="jscript:View1.returnToMediaCenter()">
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
</dt> </dl>

 

 





