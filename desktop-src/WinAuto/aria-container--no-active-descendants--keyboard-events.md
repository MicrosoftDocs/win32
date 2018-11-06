---
title: ARIA Container Role (without active descendant) Keyboard Accessibility Error
description: ARIA Container Role (without active descendant) Keyboard Accessibility Error
ms.assetid: 15EDD3CC-FC2A-42FC-95DD-B04D9AF3515E
keywords:
- AriaContainerWithoutActiveDescendantKeyboardAccessiblityId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Container Role (without active descendant) Keyboard Accessibility Error

## Text

Element is a focusable container without active descendant defined and without **OnKeyDown**/**OnKeyPress**/**OnKeyUp** event handlers (neither on container nor on one of child elements).

## Type

Error

## Description

This error applies to elements that have a container role, do not have an **aria-activedescendant** attribute, and are not disabled. These elements implement keyboard navigation among child elements by using the concept known as *roving index*. In this concept, the **tabindex** attributes of child elements are maintained dynamically, ensuring that at all times only one child element is in tab order.

This error indicates that a container element that does not have the **aria-activedescendant** attribute, and that is not disabled, is not accessible to keyboard users. The problem exists because the container does not have the needed keyboard event handlers (**keydown**, **keyup**, or **keypress**), and neither do any of the container's child elements.

To fix this error, define a **keydown**, **keyup**, or **keypress** event handler for the container or one of its child elements.

## Example


```HTML
<div role="listbox" id="listbox1" >
  <div role="option" id="listbox1-1" tabindex="0" class="selected">Item 1</div>
  <div role="option" id="listbox1-2">Item 2</div>
  <div role="option" id="listbox1-3">Item 3</div>
  ...
<div>

<script>

  ...

  listbox1.addEventListener('keyup', function(e) {
    var itm = e.srcElement;
    var prev = itm.previousElementSibling;
    var next = itm.nextElementSibling;

    if (e.keyCode == 38 && prev) {
      // On arrow up move focus to the previous item.
      itm.setAttribute('tabindex', '-1');
      prev.setAttribute('tabindex','0');
      prev.focus();
    }

    else if (e.keyCode == 40 && next) {
      // On arrow down move focus to the next item.
      itm.setAttribute('tabindex', '-1');
      next.setAttribute('tabindex','0');
      next.focus();
    }
  });

</script>
```



## Related topics

<dl> <dt>

[ARIA Container Role Keyboard Accessibility Error](aria-container-keyboard-events.md)
</dt> </dl>

 

 




