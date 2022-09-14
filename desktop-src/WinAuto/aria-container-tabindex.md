---
title: ARIA Container Tabindex Error
description: ARIA Container Tabindex Error
ms.assetid: CCEA9490-903D-423D-B9FD-641E8B7D3E0B
keywords:
- AriaContainerTabIndexErrorId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Container Tabindex Error

## Text

Element is a focusable container with active descendants defined but without **tabindex** value greater or equal to 0.

## Type

Error

## Description

This error applies to elements that have the **aria-activedescendant** attribute, are not disabled, and do not have the **tabindex** attribute set to a value that is greater than or equal to 0. These elements must be in tab order because they are responsible for handling keyboard events for their child elements.

To fix this error, set the **tabindex** attribute to a value that is greater than or equal to 0.

## Example


```HTML
<div role="listbox" id="listbox1" tabindex="0" aria-activedescendant="listbox1-1"> 
       <div role="option" id="listbox1-1" class="selected">Item 1</div> 
       <div role="option" id="listbox1-2">Item 2</div> 

       <div role="option" id="listbox1-3">Item 3</div>
      ... 
<div>
```



## Related topics

<dl> <dt>

[ARIA Container Role (without active descendant) Tabindex Error](aria-container--no-active-descendant--tabindex.md)
</dt> </dl>

 

 




