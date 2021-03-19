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
ms.date: 05/31/2018
api_location: 
---

# THEME.openViewRelative

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

 

 





