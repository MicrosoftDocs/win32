---
title: ARIA Role Error
description: ARIA Role Error
ms.assetid: FEEB4F28-4A71-4417-A2F9-ABCB86B44F0F
keywords:
- AriaRoleErrorId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Role Error

## Text

Element has invalid WAI-ARIA role.

## Type

Error

## Description

This error applies to all elements that have the [**role**](https://developer.mozilla.org/docs/Web/HTML/Reference) attribute. It indicates that the **role** attribute is not a valid Web Accessibility Initiative - Accessible Rich Internet Applications (WAI-ARIA) role value as defined by the WAI-ARIA specification. Setting a valid role helps ensure that the element is correctly interpreted by screen readers and other assistive technology tools.

To fix this error, set the [**role**](https://developer.mozilla.org/docs/Web/HTML/Reference) attribute to a valid WAI-ARIA role value. Note that abstract WAI-ARIA roles are not valid.

## Example


```HTML
<!—The invalid role will not expose this element as a button. -->
<div role="backbutton" tabindex="0" aria-label="Back" onclick="mouseAction(event)" onkeyup="keyAction(event)" >

<!—Setting the correct role will expose this as a button that can be clicked. -->
<div role="button" tabindex="0" aria-label="Back" onclick="mouseAction(event)" onkeyup="keyAction(event)" >
```



## Related topics

<dl> <dt>

[ARIA Container Role Error](aria-container-role.md)
</dt> </dl>

 

 




