---
title: DropTarget Control Pattern
description: Provides guidelines and conventions for implementing the DropTarget control pattern by using IDropTargetProvider, including information about properties and methods.
ms.assetid: DD5EE4A0-E6C0-4657-A60F-7F59FC569E04
keywords:
- UI Automation,implementing DropTarget control pattern
- UI Automation,DropTarget control pattern
- UI Automation,IDropTargetProvider
- IDropTargetProvider
- implementing UI Automation DropTarget control patterns
- DropTarget control patterns
- control patterns,IDropTargetProvider
- control patterns,implementing UI Automation DropTarget
- control patterns,DropTarget
- interfaces,IDropTargetProvider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DropTarget Control Pattern

Provides guidelines and conventions for implementing the **DropTarget** control pattern by using [**IDropTargetProvider**](https://msdn.microsoft.com/library/windows/desktop/hh707345), including information about properties and methods. The **DropTarget** control pattern is used to support controls that can be the target of a drag-and-drop operation.

## Implementation Guidelines and Conventions

When implementing the **DropTarget** control pattern, use the following guidelines and conventions:

-   The **DropTarget** pattern must be supported while a drag operation is in progress. It can be supported even when a drag operation is not in progress.
-   The [**IDropTargetProvider::DropTargetEffect**](/windows/win32/UIAutomationCore/nf-uiautomationcore-idroptargetprovider-get_droptargeteffect?branch=master) property is required.
-   The [**IDropTargetProvider::DropTargetEffects**](/windows/win32/UIAutomationCore/nf-uiautomationcore-idroptargetprovider-get_droptargeteffects?branch=master) property is required when there is more than one possible drop effect for the target.
-   The element must raise property changed events for the **DropTargetEffect** ([**UIA\_DropTargetDropTargetEffectPropertyId**](uiauto-control-pattern-propids.md#uia-droptargetdroptargeteffectpropertyid)) and **DropTargetEffects** ([**UIA\_DropTargetDropTargetEffectsPropertyId**](uiauto-control-pattern-propids.md#uia-droptargetdroptargeteffectspropertyid)) properties when they change.

## Required Members for **IDropTargetProvider**

The following properties and methods are required for implementing the [**IDropTargetProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-idroptargetprovider?branch=master) interface.



| Required members                                                                              | Member type | Notes                                                                    |
|-----------------------------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------|
| [**DropTargetEffect**](/windows/win32/UIAutomationCore/nf-uiautomationcore-idroptargetprovider-get_droptargeteffect?branch=master)                       | Property    | None                                                                     |
| [**DropTargetEffects**](/windows/win32/UIAutomationCore/nf-uiautomationcore-idroptargetprovider-get_droptargeteffects?branch=master)                     | Property    | Required if the drop target supports more than one possible drop effect. |
| [**UIA\_DropTarget\_DragEnterEventId**](uiauto-event-ids.md#uia-droptarget-dragentereventid) | Event       | None                                                                     |
| [**UIA\_DropTarget\_DragLeaveEventId**](uiauto-event-ids.md#uia-droptarget-dragleaveeventid) | Event       | None                                                                     |
| [**UIA\_DropTarget\_DroppedEventId**](uiauto-event-ids.md#uia-droptarget-droppedeventid)     | Event       | None                                                                     |



 

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[Drag Control Pattern](https://msdn.microsoft.com/library/windows/desktop/hh707348)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> <dt>

[UI Automation Support for Drag-and-Drop](ui-automation-support-for-drag-and-drop.md)
</dt> </dl>

 

 




