---
title: DuplicateSiblingNames
description: DuplicateSiblingNames
ms.assetid: '4E9FFD16-EAC0-4778-8DEB-D179E2197411'
---

# DuplicateSiblingNames

## Text

Duplicate sibling Name+Role \\"{0}\\" will cause ambiguity between elements.

## Type

Error

## Description

An element has the same Name and Role/ControlType as another element.

This issue can cause confusion because screen readers will read the same text for all the elements with the same Name and Role/ControlType.

## Possible causes

-   Element’s name contain Role/ControlType text.
-   Element’s name or the name of its parent is not set or is set incorrectly.

## Related topics

<dl> <dt>

[**IAccessible::get\_accName**](iaccessible-iaccessible--get-accname.md)
</dt> <dt>

[Name Property](name-property.md)
</dt> <dt>

[**UIA\_NamePropertyId**](uiauto-automation-element-propids.md#uia-namepropertyid)
</dt> <dt>

[**IUIAutomationElement.CurrentName**](uiauto-iuiautomationelement-currentname.md)
</dt> </dl>

 

 




