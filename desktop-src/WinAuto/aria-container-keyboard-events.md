---
title: ARIA Container Role Keyboard Accessibility Error
description: ARIA Container Role Keyboard Accessibility Error
ms.assetid: 364F26D7-7B65-418B-9DA5-F3B7B59284F7
keywords:
- AriaContainerKeyboardAccessibilityErrorId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Container Role Keyboard Accessibility Error

## Text

Element is a container with active descendant and custom mouse functionality but without the corresponding keyboard functionality: JavaScript event handlers for **OnKeyDown** or **OnKeyPress**.

## Type

Error

## Description

This error applies to elements that have the **aria-activedescendant** attribute. These elements have one or more mouse event handlers (**mousemove**, **mousedown** or **mouseup**), but are missing the equivalent keyboard event handlers (**keydown**, **keyup** or **keypress**). The keyboard event handlers are needed to ensure that the user can invoke the element's functionality by using the keyboard, and to ensure that the element maintains the **aria-activedescendant** attribute.

To fix this error, implement one of the keyboard event handlers.

## Example


```HTML
<div role="listbox" id="listbox1" tabindex="0" aria-activedescendant="listbox1-1"> 
  <div role="option" id="listbox1-1" class="selected">Item 1</div>
  <div role="option" id="listbox1-2">Item 2</div>
  <div role="option" id="listbox1-3">Item 3</div>
</div>

<script>

   ...

  listbox1.addEventListener('keyup', function(e) {
    var itm = document.getElementById(this.getAttribute('aria-activedescendant'));
    var prev = itm.previousElementSibling;
    var next = itm.nextElementSibling;
    
    if ( e.keyCode  38 && prev ) {
      // Arrow up to move active descendant to the previous item
      itm.removeAttribute('class’);
      prev.setAttribute("class", "selected");
      this.setAttribute ('aria-activedescendant', prev.id)
    } 

    else if ( e.keyCode == 40 && next) {
      // Arrow down to move focus to the next item
      itm.removeAttribute('class’);
      next.setAttribute("class", "selected");
      this.setAttribute ('aria-activedescendant', next.id)
    }
  });      

</script>
```



## Related topics

<dl> <dt>

[ARIA Container Role (without active descendant) Keyboard Accessibility Error](aria-container--no-active-descendants--keyboard-events.md)
</dt> </dl>

 

 




