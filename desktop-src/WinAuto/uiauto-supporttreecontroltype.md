---
title: Tree Control Type
description: This topic provides information about Microsoft UI Automation support for the Tree control type.
ms.assetid: 0fa8f308-7815-4561-a1ce-c5f5582861da
keywords:
- UI Automation,support for Tree control type
- UI Automation,Tree control type
- UI Automation,tree structure for Tree control type
- UI Automation,properties for Tree control type
- UI Automation,control patterns for Tree control type
- UI Automation,events for Tree control type
- tree structures,Tree control type
- properties,Tree control type
- control patterns,Tree control type
- events,Tree control type
- support for Tree control type
- Tree control type
- control types,tree structure for Tree control type
- control types,control patterns for Tree control type
- control types,support for Tree
- control types,Tree
ms.topic: article
ms.date: 05/31/2018
---

# Tree Control Type

This topic provides information about Microsoft UI Automation support for the **Tree** control type.

The **Tree** control type is used for containers whose contents have relevance as a hierarchy of nodes, as with the way files and folders are displayed in the left pane of Windows Explorer. Each node has the potential to contain other nodes, called child nodes. Parent nodes, or nodes that contain child nodes, can be displayed as expanded or collapsed. The Windows tree-view control (as identified by [**WC\_TREEVIEW**](/windows/desktop/Controls/common-control-window-classes)) is an example of a control that belongs to the **Tree** control type.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Tree** control type. The UI Automation requirements apply to all tree item controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to tree controls, and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Tree<ul><li>DataItem (0 or more)</li><li>TreeItem (0 or more)<ul><li>TreeItem (0 or more)<ul><li>...</li></ul></li></ul></li><li>ScrollBar (0, 1, 2)</li></ul></li></ul> | <ul><li>Tree<ul><li>DataItem (0 or more)</li><li>TreeItem (0 or more)<ul><li>TreeItem (0 or more)<ul><li>...</li></ul></li></ul></li></ul></li></ul> | 




 

The control view of the UI Automation tree consists of:

-   Zero of many items within the container (items can be based on the [TreeItem](uiauto-supporttreeitemcontroltype.md) or [DataItem](uiauto-supportdataitemcontroltype.md) control types).
-   Zero, one, or two scroll bar controls

The content view of the UI Automation tree consists of zero or many items within the container (items can be based on the [TreeItem](uiauto-supporttreeitemcontroltype.md) or [DataItem](uiauto-supportdataitemcontroltype.md) control types).

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **Tree** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                                               |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                                   |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes. | Tree controls have a clickable point that causes the tree or one of the items in the tree container to receive the focus. A tree control can have a clickable point only if it is possible to click a location in the tree without causing an item to be selected or to receive the focus. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Tree**   | This value is the same for all UI frameworks.                                                                                                                                                                                                                                              |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | The tree control is always included in the content view of the UI Automation tree.                                                                                                                                                                                                         |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | The tree control is always included in the control view of the UI Automation tree.                                                                                                                                                                                                         |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes. | If the control can receive keyboard focus, it must support this property.                                                                                                                                                                                                                  |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | See notes. | If the tree control has a label associated with it, this property returns a [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) pointer for that label. Otherwise, the property returns a null reference.                                                                          |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes. | Localized string corresponding to the **Tree** control type. The default value is "tree" for en-US or English (United States).                                                                                                                                                             |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes. | The value of a tree control's name property usually comes from text that labels the control. If there is no text label, you must provide a value for this property.                                                                                                                        |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all tree controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                                             | Support/Value | Notes                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IScrollProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iscrollprovider)                            | Depends       | Implement the [Scroll](uiauto-implementingscroll.md) control pattern if items in the tree container can be scrolled.                                                                                                                 |
| [**ISelectionProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionprovider)                      | Depends       | Tree controls that contain a set of selectable items must implement the [Selection](uiauto-implementingselection.md) control pattern. It need not be implemented if selecting an item conveys no meaningful information to the user. |
| [**CanSelectMultiple**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionprovider-get_canselectmultiple)     | See notes.    | Implement this property if the tree control supports multiple selection (most tree controls do not support multiple selection).                                                                                                       |
| [**IsSelectionRequired**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionprovider-get_isselectionrequired) | See notes.    | The value of this property is exposed if the control requires that an item be selected.                                                                                                                                               |



 

## Required Events

The following table lists the UI Automation events that all tree controls must support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                        | Notes                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                                           |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event.                      |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                      | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                  | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_ScrollHorizontallyScrollablePropertyId**](uiauto-control-pattern-propids.md) property-changed event.   | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollHorizontalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property-changed event. | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollHorizontalViewSizePropertyId**](uiauto-control-pattern-propids.md) property-changed event.           | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollVerticalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property-changed event.     | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollVerticallyScrollablePropertyId**](uiauto-control-pattern-propids.md) property-changed event.       | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollVerticalViewSizePropertyId**](uiauto-control-pattern-propids.md) property-changed event.               | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_Selection\_InvalidatedEventId**](uiauto-event-ids.md)                                                            | If the control supports the [Selection](uiauto-implementingselection.md) control pattern, it must support this event.     |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                                       |                                                                                                                            |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 
