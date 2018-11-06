---
title: DragPattern/DragDropPattern elements requires Name
description: DragPattern/DragDropPattern elements requires Name
ms.assetid: DEF58FB2-5830-4162-87D0-40DEC1237529
ms.topic: article
ms.date: 05/31/2018
---

# DragPattern/DragDropPattern elements requires Name

## Text

Elements that support Drag/Drop should have a valid 'Name' set

## Type

Error

## Description

The element supports either [**IUIAutomationDragPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationdragpattern) or [**IUIAutomationDropTargetPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationdroptargetpattern), but does not have a valid Name set.

This issue causes problems for people who rely on a screen-reader. The user will not be able to tell what this object is since the screen read will not read out a valid name to distinguish what this element is when dragging.

## Possible causes

-   The element, or its parent, has an incorrectly assigned name or label.
-   A developer is not aware that screen readers read names and control types.

## Related topics

<dl> <dt>

[**IAccessible::get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)
</dt> <dt>

[Name Property](name-property.md)
</dt> <dt>

[**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)
</dt> <dt>

[**IUIAutomationElement::CurrentName**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentname)
</dt> </dl>

 

 




