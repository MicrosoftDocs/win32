---
title: DuplicateSiblingNames
description: DuplicateSiblingNames
ms.assetid: 4E9FFD16-EAC0-4778-8DEB-D179E2197411
ms.topic: article
ms.date: 05/31/2018
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

[**IAccessible::get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)
</dt> <dt>

[Name Property](name-property.md)
</dt> <dt>

[**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)
</dt> <dt>

[**IUIAutomationElement.CurrentName**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentname)
</dt> </dl>

 

 




