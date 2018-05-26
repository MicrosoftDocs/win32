---
title: DragPattern/DragDropPattern elements requires valid DropEffect
description: DragPattern/DragDropPattern elements requires valid DropEffect
ms.assetid: 508DD4F3-4878-4A9E-859D-06BBDA505708
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DragPattern/DragDropPattern elements requires valid DropEffect

## Text

Elements that support Drag/Drop should have a valid 'DropEffect' set

## Type

Error

## Description

The element supports either [**IUIAutomationDragPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationdragpattern?branch=master) or [**IUIAutomationDropTargetPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationdroptargetpattern?branch=master), but does not have a valid [**DropEffect**](/windows/win32/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffect?branch=master) property set.

This issue causes problems for people who rely on a screen-reader. The user will not be able to tell what effect this object has when dragging.

## Possible causes

-   The element, or its parent, has not created the [**DropEffect**](/windows/win32/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffect?branch=master) or [**DropEffects**](/windows/win32/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffects?branch=master) an incorrectly assigned name or label.
-   A developer is not aware that screen readers read DropEffect(s).

 

 




