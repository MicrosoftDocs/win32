---
title: ARIA Role Error for elements with event handlers
description: ARIA Role Error for elements with event handlers
ms.assetid: 20BB874A-874B-4266-9C7B-49C07D4146DA
keywords:
- AriaContainerRoleErrorMessage
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Role Error for elements with event handlers

## Text

Element has an event handler but valid WAI-ARIA role is not defined.

## Type

Error

## Description

This error applies to elements that do not have an implicit Web Accessibility Initiative - Accessible Rich Internet Applications (WAI-ARIA) role.

This error indicates that an element has a mouse or keyboard event handler (**click**, **mousedown**, **mouseup**, **mousemove**, **mouseout**, **mouseover**, **keyup**, **keydown**, or **keypress**), but doesn’t have the [**role**](https://developer.mozilla.org/docs/Web/HTML/Reference) attribute set, and is not one of the HTML tags that has an implicit WAI-ARIA role (for example, **a**, **button**, **img**, **input**, **select** and so on).

Setting the [**role**](https://developer.mozilla.org/docs/Web/HTML/Reference) attribute for interactive elements that have no implicit role (such as a **div** tag) is necessary to expose the element's behavior patterns to screen readers and other assistive technologies.

To fix this error, set the [**role**](https://developer.mozilla.org/docs/Web/HTML/Reference) attribute to a valid WAI-ARIA role that best fits this element's behavior patterns and required attributes. For example, if a **div** tag functions as a button, set the role attribute to "button".

## Example


```HTML
<!-- Setting role attribute allows screen readers to know it can be clicked -->
<div role="button" tabindex="0" aria-label="Back" onclick="mouseAction(event)" onkeyup="keyAction(event)" >
```



 

 




