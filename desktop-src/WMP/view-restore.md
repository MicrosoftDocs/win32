---
title: VIEW.restore
description: The restore method restores the VIEW.
ms.assetid: 8005c14e-771b-4f20-8039-fc09869dc726
keywords:
- VIEW.restore Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.restore
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# VIEW.restore

The **restore** method restores the **VIEW**.

``` syntax
        elementID.restore()
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
        onclick="jscript:View1.restore()">
    </BUTTON>
  </VIEW>
</THEME>
```



## Requirements



|                    |                                                      |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> </dl>

 

 





