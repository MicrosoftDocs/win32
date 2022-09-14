---
title: ARIA Container Role Error
description: ARIA Container Role Error
ms.assetid: AF207293-1172-43D0-B92C-C3070876DF54
keywords:
- AriaContainerRoleErrorId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Container Role Error

## Text

Element with **active-descendant** defined does not have a container role (**combobox**, **grid**, **listbox**, **menu**, **menubar**, **radiogroup**, **tree**, **treegrid**, **tablist**, **row**).

## Type

Error

## Description

This error applies to elements that have the **aria-activedescendant** attribute.

An element appears to be a container that has the **aria-activedescendant** attribute set, but the element's role attribute doesn’t have a value that is valid for a container.

To fix this error, set the **role** attribute to a Web Accessibility Initiative - Accessible Rich Internet Applications (WAI-ARIA) role value that is valid for a container element: **combobox**, **grid**, **listbox**, **menu**, **menubar**, **radiogroup**, **tablist**, **tree**, or **treegrid**.

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

[ARIA Role Error](aria-role-invalid.md)
</dt> </dl>

 

 




