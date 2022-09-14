---
title: ARIA Container Role (without active descendant) Tabindex Error
description: ARIA Container Role (without active descendant) Tabindex Error
ms.assetid: E3CCA500-7104-4163-927C-94EA8F1E89D8
keywords:
- AriaContainerWithoutActiveDescendantTabIndexErrorId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Container Role (without active descendant) Tabindex Error

## Text

Element is a focusable container without active descendant defined, but no child element has **tabindex** greater or equal to 0.

## Type

Error

## Description

This error applies to elements that have a container role, do not have an **aria-activedescendant** attribute, and are not disabled. These elements implement keyboard navigation among child elements by using the concept known as *roving index*. In this concept, the **tabindex** attributes of child elements are maintained dynamically, ensuring that at all times only one child element is in tab order.

To fix this error, set the **tabindex** attribute of one of the child elements to a value equal to or greater than 0.

## Example


```HTML
<div id="listbox" role="listbox1">
  <div role="option" id="listbox1-1" tabindex="0" class="selected">Item 1</div>
  <div role="option" id="listbox1-2">Item 2</div>
  <div role="option" id="listbox1-3">Item 3</div>
</div>

<script>

  ...

  listbox1.addEventListener('keyup', function(e) {
    var itm = e.srcElement;
    var prev = itm.previousElementSibling;
    var next = itm.nextElementSibling;

    if (e.keyCode == 38 && prev) {
      // Arrow up to move focus to the previous item.
      itm.setAttribute('tabindex', '-1');
      prev.setAttribute('tabindex','0');
      prev.focus();
    } 

    else if (e.keyCode == 40 && next) {
      // Arrow down to move focus to the next item.
      itm.setAttribute('tabindex', '-1');
      next.setAttribute('tabindex','0');
      next.focus();
    }
  });

</script>
```



## Related topics

<dl> <dt>

[ARIA Container Tabindex Error](aria-container-tabindex.md)
</dt> </dl>

 

 




