---
title: Drag Control Pattern
description: Provides guidelines and conventions for implementing the Drag control pattern by using IDragProvider, including information about properties and methods. The Drag control pattern is used to support draggable controls, or controls with draggable items.
ms.assetid: 9853E9CB-D04B-4F67-8E9E-7F1F99BACEA7
keywords:
- UI Automation,implementing Drag control pattern
- UI Automation,Drag control pattern
- UI Automation,IDragProvider
- IDragProvider
- implementing UI Automation Drag control patterns
- Drag control patterns
- control patterns,IDragProvider
- control patterns,implementing UI Automation Drag
- control patterns,Drag
- interfaces,IDragProvider
ms.topic: article
ms.date: 05/31/2018
---

# Drag Control Pattern

Provides guidelines and conventions for implementing the **Drag** control pattern by using [**IDragProvider**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-idragprovider), including information about properties and methods. The **Drag** control pattern is used to support draggable controls, or controls with draggable items.

## Implementation Guidelines and Conventions

When implementing the **Drag** control pattern, use these guidelines and conventions:

-   The [**IDragProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-idragprovider) interface supports two different dragging styles: the source/target style, and the source-only style. You need to choose the style that works best for your drag-and-drop scenarios:
    -   **Source/target style:** Each possible drop target is represented by an element that implements the [**IDropTargetProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-idroptargetprovider) interface. During a drag operation, Microsoft UI Automation events originate from the element that is being dragged, and from the drop-target elements.
    -   **Source-only style:** Drop targets are not represented by UI Automation elements. During a drag operation, events originate only from the element that is being dragged.
-   [**IDragProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-idragprovider) is a read-only interface intended for monitoring drag operations. You cannot use it to control a drag operation. You can automate drag operations by sending mouse input to a control.
-   The [**IDragProvider::IsGrabbed**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_isgrabbed) property is required.
-   The [**IDragProvider::DropEffect**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffect) and [**IDragProvider::DropEffects**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffects) properties are required for a source-only style implementation, and prohibited for a source/target style implementation. In a source/target style implementation, drop-target elements can be queried for their drop effects.
-   The [**IDragProvider::GrabbedItems**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-getgrabbeditems) property represents the dragging of multiple items. When the user begins the drag operation, you need to create a new UI Automation element to serve as the event source element. This new element fires all events that the source element would have fired in either the source/target or source-only mode, while none of the elements that are actually being dragged fire any events. When the drag operation is complete, destroy the event source element.
-   The element must fire property-changed events for the **DropEffect** ([**UIA\_DragDropEffectPropertyId**](uiauto-control-pattern-propids.md)) and **DropEffects** ([**UIA\_DragDropEffectsPropertyId**](uiauto-control-pattern-propids.md)) properties when they change. Property-changed events for the other properties are allowed, but can be inferred from the required **DragStart** ([**UIA\_Drag\_DragStartEventId**](uiauto-event-ids.md)), **DragCancel** ([**UIA\_Drag\_DragCancelEventId**](uiauto-event-ids.md)), and **DragComplete** ([**UIA\_Drag\_DragCompleteEventId**](uiauto-event-ids.md)) events.
-   

## Required Members for **IDragProvider**

The following properties and methods are required for implementing the [**IDragProvider**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-idragprovider) interface.



| Required members                                                                        | Member type | Notes                                                                         |
|-----------------------------------------------------------------------------------------|-------------|-------------------------------------------------------------------------------|
| [**IsGrabbed**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_isgrabbed)                                     | Property    | None                                                                          |
| [**DropEffect**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffect)                                   | Property    | Required for an implementation of the source-only style.                      |
| [**DropEffects**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffects)                                 | Property    | Required if there is more than one possible drop effect for the grabbed item. |
| [**GetGrabbedItems**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-getgrabbeditems)                         | Method      | Required for a multiple-item drag operation.                                  |
| [**UIA\_Drag\_DragStartEventId**](uiauto-event-ids.md)       | Event       | None                                                                          |
| [**UIA\_Drag\_DragCancelEventId**](uiauto-event-ids.md)     | Event       | None                                                                          |
| [**UIA\_Drag\_DragCompleteEventId**](uiauto-event-ids.md) | Event       | None                                                                          |



 

## Related topics

<dl> <dt>

[Control Types and their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[DropTarget Control Pattern](/windows/desktop/WinAuto/uiauto-implementingdroptarget)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> <dt>

[UI Automation Support for Drag-and-Drop](ui-automation-support-for-drag-and-drop.md)
</dt> </dl>

 

 