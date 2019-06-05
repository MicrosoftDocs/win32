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

To fix this error, set the [**tabindex**](https://msdn.microsoft.com/library/ms534654) attribute to a value that is equal to or greater than 0. You do not need to explicitly set the **tabindex** attribute for tags that are in the tab order by default, such as [**a**](https://msdn.microsoft.com/library/ms535173) (with [**href**](https://msdn.microsoft.com/library/Cc848861) attribute), [**button**](https://msdn.microsoft.com/library/ms535211), [**input**](https://msdn.microsoft.com/library/ms535260) (excluding "hidden"), [**select**](https://msdn.microsoft.com/library/ms535893), [**textarea**](https://msdn.microsoft.com/library/ms535904), and [**area**](https://msdn.microsoft.com/library/ms535185) (as part of the image map).

## Example


```HTML
<div role="button" tabindex="0" aria-label="Back" onclick="mouseAction(event)" onkeyup="keyAction(event)" >
```



 

 




