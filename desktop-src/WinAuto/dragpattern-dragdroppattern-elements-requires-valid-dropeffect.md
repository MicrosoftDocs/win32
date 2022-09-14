---
title: DragPattern/DragDropPattern elements requires valid DropEffect
description: DragPattern/DragDropPattern elements requires valid DropEffect
ms.assetid: 508DD4F3-4878-4A9E-859D-06BBDA505708
ms.topic: article
ms.date: 05/31/2018
---

# DragPattern/DragDropPattern elements requires valid DropEffect

## Text

Elements that support Drag/Drop should have a valid 'DropEffect' set

## Type

Error

## Description

The element supports either [**IUIAutomationDragPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationdragpattern) or [**IUIAutomationDropTargetPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationdroptargetpattern), but does not have a valid [**DropEffect**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffect) property set.

This issue causes problems for people who rely on a screen-reader. The user will not be able to tell what effect this object has when dragging.

## Possible causes

-   The element, or its parent, has not created the [**DropEffect**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffect) or [**DropEffects**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffects) an incorrectly assigned name or label.
-   A developer is not aware that screen readers read DropEffect(s).

 

 




