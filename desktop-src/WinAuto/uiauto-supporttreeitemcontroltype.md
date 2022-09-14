---
title: TreeItem Control Type
description: This topic provides information about Microsoft UI Automation support for the TreeItem control type.
ms.assetid: 03d8a2a7-0b9a-41f8-a9d3-cebba9c25c63
keywords:
- UI Automation,support for TreeItem control type
- UI Automation,TreeItem control type
- UI Automation,tree structure for TreeItem control type
- UI Automation,properties for TreeItem control type
- UI Automation,control patterns for TreeItem control type
- UI Automation,events for TreeItem control type
- tree structures,TreeItem control type
- properties,TreeItem control type
- control patterns,TreeItem control type
- events,TreeItem control type
- support for TreeItem control type
- TreeItem control type
- control types,tree structure for TreeItem control type
- control types,control patterns for TreeItem control type
- control types,support for TreeItem
- control types,TreeItem
ms.topic: article
ms.date: 05/31/2018
---

# TreeItem Control Type

This topic provides information about Microsoft UI Automation support for the **TreeItem** control type.

The **TreeItem** control type represents a node within a tree container. Each node might contain other nodes, called child nodes. Parent nodes, or nodes that contain child nodes, can be displayed as expanded or collapsed.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **TreeItem** control type. The UI Automation requirements apply to all tree item controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Remarks](#remarks)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to tree item controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>TreeItem<ul><li>CheckBox (0 or 1)</li><li>Image (0 or 1)</li><li>Button (0 or 1)</li><li>TreeItem (0 or more)</li></ul></li></ul> | <ul><li>TreeItem<ul><li>TreeItem (0 or more)</li></ul></li></ul> | 




 

Tree item controls can have zero or more tree item children in the content view of the UI Automation tree. If the tree item control has functionality beyond what is exposed in the control patterns listed below, the control should be based on the [DataItem](uiauto-supportdataitemcontroltype.md) control type.

Collapsed tree items do not appear in the control view or content view until they become expanded and visible (or can be scrolled into view).

The control view can contain additional details for a control, including an associated image or a button. For example, an item in an outline view might contain an image as well as a button to expand or collapse the outline. These detail objects do not appear in the content view because the information is already represented by the parent tree item.

Tree items that are scrolled off the screen appear in both the control and content views of the UI Automation tree and should have the [**IUIAutomationElement::CurrentIsOffscreen**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentisoffscreen) (or [**CachedIsOffscreen**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_cachedisoffscreen)) property set to **TRUE**.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **TreeItem** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value        | Notes                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.   | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                  |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.   | The outermost rectangle that contains the whole control.                                                                                                                                      |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.   | This property must return a location that causes the tree item to change selection state or become focused.                                                                                   |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **TreeItem** | This value is the same for all UI frameworks.                                                                                                                                                 |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | **TRUE**     | The tree item control is always included in the content view of the UI Automation tree.                                                                                                       |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | **TRUE**     | The tree item control is always included in the control view of the UI Automation tree.                                                                                                       |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.   | If the control can receive keyboard focus, it must support this property.                                                                                                                     |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md)                   | See notes.   | This property indicates whether a tree item control is scrolled off the screen.                                                                                                               |
| [**UIA\_ItemStatusPropertyId**](uiauto-automation-element-propids.md)                     | See notes.   | If the control contains status that is being updated dynamically, this property must be supported so that an assistive technology can receive updates when the status of the element changes. |
| [**UIA\_ItemTypePropertyId**](uiauto-automation-element-propids.md)                         | See notes.   | If the tree item control uses a visual icon to indicate that is a particular type of item, this property must be supported and must indicate the item type.                                   |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | **NULL**     | Tree item controls are self-labeling.                                                                                                                                                         |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.   | Localized string corresponding to the TreeItem control type. The default value is "tree item" for en-US or English (United States).                                                           |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.   | This property exposes the text displayed for each tree item control.                                                                                                                          |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all tree item controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                                                  | Support/Value                     | Notes                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IExpandCollapseProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider)                 | Required                          | All tree items must support the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern because all items can be expanded or collapsed.                                           |
| [**ExpandCollapseState**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-get_expandcollapsestate) | Expanded, Collapsed, or Leaf Node | Tree items are leaf nodes when they are not expanded or collapsed.                                                                                                                                |
| [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider)                                 | Depends                           | Implement the [Invoke](uiauto-implementinginvoke.md) control pattern if the tree item can perform a command.                                                                                     |
| [**IScrollItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iscrollitemprovider)                         | Depends                           | Implement the [ScrollItem](uiauto-implementingscrollitem.md) control pattern if the tree container supports the [Scroll](uiauto-implementingscroll.md) control pattern.                         |
| [**ISelectionItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider)                   | Depends                           | Implement the [SelectionItem](uiauto-implementingselectionitem.md) control pattern if it is possible to have an active selection that is maintained when the user returns to the tree container. |
| [**SelectionContainer**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-get_selectioncontainer)    | Required                          | This property exposes the same container for all items within the container.                                                                                                                      |



 

## Required Events

The following table lists the UI Automation events that tree item controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                                | Notes                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                                                   |                                                                                                                                |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event.                              |                                                                                                                                |
| [**UIA\_ExpandCollapseExpandCollapseStatePropertyId**](uiauto-control-pattern-propids.md) property-changed event. |                                                                                                                                |
| [**UIA\_Invoke\_InvokedEventId**](uiauto-event-ids.md)                                                                                  | If the control supports the [Invoke](uiauto-implementinginvoke.md) control pattern, it must support this event.               |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                              | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.       |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                          | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event.     |
| [**UIA\_ItemStatusPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                            | If the control supports the [**ItemStatus**](uiauto-automation-element-propids.md) property, it must support this event.      |
| [**UIA\_MultipleViewCurrentViewPropertyId**](uiauto-control-pattern-propids.md) property-changed event.                     | If the control supports the [MultipleView](uiauto-implementingmultipleview.md) control pattern, it must support this event.   |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md) property-changed event.                                                        |                                                                                                                                |
| [**UIA\_SelectionItem\_ElementAddedToSelectionEventId**](uiauto-event-ids.md)                                    | If the control supports the [SelectionItem](uiauto-implementingselectionitem.md) control pattern, it must support this event. |
| [**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md)                            | If the control supports the [SelectionItem](uiauto-implementingselectionitem.md) control pattern, it must support this event. |
| [**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md)                                                    | If the control supports the [SelectionItem](uiauto-implementingselectionitem.md) control pattern, it must support this event. |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                                               |                                                                                                                                |
| [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md) property-changed event.                                 | If the control supports the [Toggle](uiauto-implementingtoggle.md) control pattern, it must support this event.               |
| [**UIA\_ValueValuePropertyId**](uiauto-control-pattern-propids.md) property-changed event.                                               | If the control supports the [Value](uiauto-implementingvalue.md) control pattern, it must support this event.                 |



 

## Remarks

If a tree item has subelements other than child outline nodes, the provider must handle the child object information carefully and clearly. In UI Automation, the tree structure is handled by the tree hierarchy itself. By having one or more non-outline-node children, the differences between them and actual child outline nodes becomes seriously ambiguous.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




