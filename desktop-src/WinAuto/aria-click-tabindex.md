---
title: ARIA Tabindex Error
description: ARIA Tabindex Error
ms.assetid: CCBC56E8-8899-4962-8315-762538CA666C
keywords:
- AriaTabIndexErrorId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Tabindex Error

## Text

Element is not disabled and has a **click** event handler but it has **tabIndex** < 0 and is not in the tab order by default.

## Type

Error

## Description

This error applies to elements that have a click event handler and are not disabled. These elements must be in the tab order. This ensures that an element can be reached using the Tab key, which is how screen reader users typically navigate the UI.

To fix this error, set the [**tabindex**](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/tabindex) attribute to a value that is equal to or greater than 0. You do not need to explicitly set the **tabindex** attribute for tags that are in the tab order by default, such as [**a**](https://developer.mozilla.org/docs/Web/HTML/Element/a) (with [**href**](https://developer.mozilla.org/docs/Web/HTML/Attributes) attribute), [**button**](https://developer.mozilla.org/docs/Web/HTML/Element/button), [**input**](https://developer.mozilla.org/docs/Web/HTML/Element/input) (excluding "hidden"), [**select**](https://developer.mozilla.org/docs/Web/HTML/Element/select), [**textarea**](https://developer.mozilla.org/docs/Web/HTML/Element/textarea), and [**area**](https://developer.mozilla.org/docs/Web/HTML/Element/area) (as part of the image map).

## Example


```HTML
<div role="button" tabindex="0" aria-label="Back" onclick="mouseAction(event)" onkeyup="keyAction(event)" >
```



 

 




