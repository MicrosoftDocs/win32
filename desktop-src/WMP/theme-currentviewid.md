---
title: THEME.currentViewID
description: The currentViewID attribute specifies or retrieves the currently displayed VIEW.
ms.assetid: 94f23da9-cfda-4dc4-9804-b7daff5ebb8f
keywords:
- THEME.currentViewID Windows Media Player
topic_type:
- apiref
api_name:
- THEME.currentViewID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# THEME.currentViewID

The **currentViewID** attribute specifies or retrieves the currently displayed **VIEW**.

``` syntax
theme.currentViewID
```

## Possible Values

This attribute is a read/write **String** specifying the **id** of the current **VIEW**. It has no default value.

## Remarks

Specifying **currentViewID** automatically closes the existing **currentView** (pointed to by the **view** global attribute) and opens the specified **VIEW**.

## Examples


```C++
<THEME currentViewID="startView">
  <VIEW>
    <TEXT value="this would have been the default view"/>
  </VIEW>
  <VIEW id="startView">
    <TEXT value="go to new view"
        onclick="jscript:theme.currentViewID='newView'"/>
  </VIEW>
  <VIEW id="newView">
    <TEXT value="new view"/>
  </VIEW>
</THEME>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**THEME Element**](theme-element.md)
</dt> </dl>

 

 





