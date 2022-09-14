---
title: UI Automation Support for Drag-and-Drop
description: This topic describes the control patterns that expose information about an element's drag-and-drop functionality.
ms.assetid: FFF5A296-C9FF-4B47-AAF8-A9DD581D9DBE
keywords:
- UI Automation,drag-and-drop support
- UI Automation,Drag pattern overview
- UI Automation,DropTarget pattern overview
- UI Automation,drag-and-drop overview
- drag-and-drop patterns,about
- Drag control pattern
- DropTarget control pattern
- control patterns,Drag
- control patterns,DropTarget
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation Support for Drag-and-Drop

Microsoft UI Automation defines two control patterns for supporting drag-and-drop scenarios, the [Drag](/windows/desktop/WinAuto/uiauto-implementingdrag) control pattern, and the [DropTarget](/windows/desktop/WinAuto/uiauto-implementingdroptarget) control pattern. You implement the Drag control pattern for an element that can be dragged, and the DropTarget control pattern for an element that can receive a dragged element; that is, a drop target. The two control patterns expose information that an assistive technology can use to help an accessibility user complete a drag-and-drop operation.

-   [Dragging Styles](#dragging-styles)
    -   [Source/target Style](#sourcetarget-style)
    -   [Source-only Style](#source-only-style)
-   [Dragging Multiple Items](#dragging-multiple-items)
-   [Client Interfaces for Drag-and-Drop](#client-interfaces-for-drag-and-drop)

## Dragging Styles

When you implement the [Drag](/windows/desktop/WinAuto/uiauto-implementingdrag) control pattern for a draggable element, you need to decide whether to implement the *source/target* dragging style, or the *source-only* dragging style.

### Source/target Style

In the source/target style of drag-and-drop, the dragged element (the "source") and the drop-target element (the "target") are distinct, and each raises a distinct set of events. Here's the life cycle for a drag operation that uses the source/target style: <dl> When the user starts a drag operation:

-   The source raises the DragStart ([**UIA\_Drag\_DragStartEventId**](uiauto-event-ids.md)) event.
-   The source sets the [**IDragProvider::IsGrabbed**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_isgrabbed) property to **TRUE**.
-   Targets update their [**DropTargetEffect**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idroptargetprovider-get_droptargeteffect) properties.

  
When the drag operation enters a target region:

-   The target raises the DragEnter ([**UIA\_DropTarget\_DragEnterEventId**](uiauto-event-ids.md)) event.

  
When the drag operation leaves a target region:

-   The target raises the DragLeave ([**UIA\_DropTarget\_DragLeaveEventId**](uiauto-event-ids.md)) event.

  
When the user releases the dragged item over a non-target:

-   The source raises the DragCancel ([**UIA\_Drag\_DragCancelEventId**](uiauto-event-ids.md)) event.
-   The source sets the [**IDragProvider::IsGrabbed**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_isgrabbed) property to **FALSE**.

  
When the user releases the dragged item over a target:

-   The source raises the DragComplete ([**UIA\_Drag\_DragCompleteEventId**](uiauto-event-ids.md)) event.
-   The source sets the [**IDragProvider::IsGrabbed**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_isgrabbed) property to **FALSE**.
-   The target sets the [**IDropTargetProvider::DropTargetEffect**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idroptargetprovider-get_droptargeteffect) property to indicate the effect that occurred.
-   The target raises the Dropped ([**UIA\_DropTarget\_DroppedEventId**](uiauto-event-ids.md)) event.

  
</dl>

The events from the source and target objects are closely related, but distinct. The data about what is being dragged comes from the source, while the data about "what could happen" and "what did happen" comes from the target.

When a drag operation is in progress, the dragged item can be dragged in and out of target regions any number of times before the operation completes.

Any drop target that needs to update its [**IDropTargetProvider::DropTargetEffect**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idroptargetprovider-get_droptargeteffect) property on the fly should raise an additional property changed event on that property.

### Source-only Style

The source-only dragging style lets a provider avoid implementing drop targets. Not implementing drop targets helps lower the implementation cost, but does not give accessibility client applications any information about the object that received the drop. Here's the life cycle for a drag operation that uses the source-only style: <dl> When the user starts a drag operation:

-   The source raises the DragStart ([**UIA\_Drag\_DragStartEventId**](uiauto-event-ids.md)) event.
-   The source sets the [**IDragProvider::IsGrabbed**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_isgrabbed) property to **TRUE**.

  
When the drag operation enters a target region:

-   The source sets the [**IDragProvider::DropEffect**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffect) property to the appropriate value.

  
When the drag operation leaves a target region:

-   The source sets the [**IDragProvider::DropEffect**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffect) property to the appropriate value.

  
When the user releases the dragged item over a non-target:

-   The source raises the DragCancel ([**UIA\_Drag\_DragCancelEventId**](uiauto-event-ids.md)) event.
-   The source sets the [**IDragProvider::IsGrabbed**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_isgrabbed) property to **FALSE**.

  
When the user releases the dragged item over a target:

-   The source raises the DragComplete ([**UIA\_Drag\_DragCompleteEventId**](uiauto-event-ids.md)) event.
-   The source sets the [**IDragProvider::DropEffect**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_dropeffect) property to indicate the effect that took place when the item was dropped.

  
</dl>

## Dragging Multiple Items

If a provider implements drag-and-drop operations where the user can drag multiple objects at the same time, the provider uses the source/target or source-only styles as described in the previous section, but with a small difference. When the user begins the drag operation, the provider creates a master source element that represents the full set of items that are being dragged. The master source element raises all events on behalf of the set of dragged items; the items don't raise any events of their own.<dl> When the user starts a drag operation:

-   The provider creates the master source element.
-   The master source element raises the DragStart ([**UIA\_Drag\_DragStartEventId**](uiauto-event-ids.md)) event.
-   The master source element sets the [**IDragProvider::IsGrabbed**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-get_isgrabbed) property to **TRUE**.
-   The master source element updates the list of grabbed items to include all items being dragged so that the [**GetGrabbedItems**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-idragprovider-getgrabbeditems) method can retrieve the list.

  
</dl>

For that point on, the master source element performs the same role as that of the source element as described in the previous section.

## Client Interfaces for Drag-and-Drop

UI Automation client applications use the [**IUIAutomationDragPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationdragpattern) and [**IUIAutomationDropTargetPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationdroptargetpattern) interfaces to access drag-and-drop information from UI elements.

 

 