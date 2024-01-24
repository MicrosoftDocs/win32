---
title: ListItem Control Type
description: This topic provides information about Microsoft UI Automation support for the ListItem control type.
ms.assetid: 8cb579ab-92c9-4311-aad7-5363f4cf2eaf
keywords:
- UI Automation,support for ListItem control type
- UI Automation,ListItem control type
- UI Automation,tree structure for ListItem control type
- UI Automation,properties for ListItem control type
- UI Automation,control patterns for ListItem control type
- UI Automation,events for ListItem control type
- tree structures,ListItem control type
- properties,ListItem control type
- control patterns,ListItem control type
- events,ListItem control type
- support for ListItem control type
- ListItem control type
- control types,tree structure for ListItem control type
- control types,control patterns for ListItem control type
- control types,support for ListItem
- control types,ListItem
ms.topic: article
ms.date: 05/31/2018
---

# ListItem Control Type

This topic provides information about Microsoft UI Automation support for the **ListItem** control type.

List item controls are an example of controls that implement the **ListItem** control type.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **ListItem** control type. The UI Automation requirements apply to all list item controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Remarks](#remarks)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to list item controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>ListItem<ul><li>Image (0 or more)</li><li>Text (0 or more)</li><li>Edit (0 or more)</li></ul></li></ul> | <ul><li>ListItem</li></ul> | 




 

The children of a list item control within the content view of the UI Automation tree must always show zero children. If the structure of the control is such that other items are contained underneath the list item then it should follow the requirements for the UI Automation support for the [TreeItem](uiauto-supporttreeitemcontroltype.md) control type.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **ListItem** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value        | Notes                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.   | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree. Allocate the **AutomationId** property for a list item if the element is known to be consistent across different instances of the user interface. If the list item is dynamically populated and not predictable, leave the **AutomationId** property blank.                                                          |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.   | This value of this property should include the area of the image and text contents of the list item.                                                                                                                                                                                                                                                                                                                              |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | Depends      | If the list control has a clickable point (a point that can be clicked to cause the list to take focus), that point must be exposed through this property. If the list control is completely covered by descendant list items, it will return the [**UIA\_E\_NOCLICKABLEPOINT**](uiauto-error-codes.md) error to indicate that the client must ask an item inside the list control for a clickable point. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **ListItem** | This value is the same for all UI frameworks.                                                                                                                                                                                                                                                                                                                                                                                     |
| [**UIA\_HelpTextPropertyId**](uiauto-automation-element-propids.md)                         | See notes.   | The Help text for list controls should explain why the user is being asked to make a choice from a list of options, which is typically the same type of information presented through a tooltip. For example, "Select an item to set the display resolution for your monitor".                                                                                                                                                    |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | **TRUE**     | The list control is always included in the content view of the UI Automation tree.                                                                                                                                                                                                                                                                                                                                                |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | **TRUE**     | The list control is always included in the control view of the UI Automation tree.                                                                                                                                                                                                                                                                                                                                                |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.   | If the container can accept keyboard input then this property value should be **TRUE**.                                                                                                                                                                                                                                                                                                                                           |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md)                   | Depends      | This property must return a value for whether the list item is currently scrolled into view within the parent container that implements [Scroll](uiauto-implementingscroll.md) control pattern.                                                                                                                                                                                                                                  |
| [**UIA\_ItemStatusPropertyId**](uiauto-automation-element-propids.md)                     | Depends      | If the control contains status that is being updated dynamically, this property must be supported so that an assistive technology can receive updates when the status of the element changes.                                                                                                                                                                                                                                     |
| [**UIA\_ItemTypePropertyId**](uiauto-automation-element-propids.md)                         | Depends      | This property should be exposed for list item controls that are representing an underlying object. These list item controls typically have an icon associated with the control that users associate with the underlying object.                                                                                                                                                                                                   |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | See notes.   | If there is a static text label then this property must expose a reference to that control.                                                                                                                                                                                                                                                                                                                                       |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.   | Localized string corresponding to the **ListItem** control type. The default value is "list item" for en-US or English (United States).                                                                                                                                                                                                                                                                                           |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.   | The value of a list item control's name property comes from the text label of the item.                                                                                                                                                                                                                                                                                                                                           |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all list item controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                                   | Support | Notes                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IExpandCollapseProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider) | Depends | If the item can be manipulated to show or hide information, the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern must be implemented.                                                                                                                                                                                                                        |
| [**IGridItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igriditemprovider)             | Depends | If item-to-item spatial navigation is supported within the list container, and the container is arranged in rows and columns, the [GridItem](uiauto-implementinggriditem.md) control pattern must be implemented.                                                                                                                                                                  |
| [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider)                 | Depends | If the item has a command that can be performed on it, separate from selection, the [Invoke](uiauto-implementinginvoke.md) control pattern must be implemented. This is typically an action associated with double-clicking the list item control. Examples would be launching a document from Windows Explorer, or playing a music file in Microsoft Windows Media Player.        |
| [**IScrollItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iscrollitemprovider)         | Depends | If the list item is contained within a container that is scrollable, the [ScrollItem](uiauto-implementingscrollitem.md) control pattern must be implemented.                                                                                                                                                                                                                       |
| [**ISelectionItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider)   | Depends | A list item control that supports selection must implement the [SelectionItem](uiauto-implementingselectionitem.md) control pattern. This allows list items controls to convey when they are selected.                                                                                                                                                                             |
| [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider)                 | Depends | If the list item is checkable and the action does not perform a selection state change, the [Toggle](uiauto-implementingtoggle.md) control pattern must be implemented.                                                                                                                                                                                                            |
| [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider)                   | Depends | If the item can be edited, the [Value](uiauto-implementingvalue.md) control pattern must be implemented. Changes to the list item control will cause changes to the values of the [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md) and [**UIA\_ValueValuePropertyId**](uiauto-control-pattern-propids.md) properties. |



 

## Required Events

The following table lists the UI Automation events that list item controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                                | Notes                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                                                   |                                                                                                                                  |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event.                              |                                                                                                                                  |
| [**UIA\_ExpandCollapseExpandCollapseStatePropertyId**](uiauto-control-pattern-propids.md) property-changed event. | If the control supports the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern, it must support this event. |
| [**UIA\_Invoke\_InvokedEventId**](uiauto-event-ids.md)                                                                                  | If the control supports the [Invoke](uiauto-implementinginvoke.md) control pattern, it must support this event.                 |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                              | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.         |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                          | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event.       |
| [**UIA\_ItemStatusPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                            | If the control supports the [**ItemStatus**](uiauto-automation-element-propids.md) property, is must support this event.        |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md) property-changed event.                                                        |                                                                                                                                  |
| [**UIA\_SelectionItem\_ElementAddedToSelectionEventId**](uiauto-event-ids.md)                                    | If the control supports the [SelectionItem](uiauto-implementingselectionitem.md) control pattern, it must support this event.   |
| [**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md)                            | If the control supports the [SelectionItem](uiauto-implementingselectionitem.md) control pattern, it must support this event.   |
| [**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md)                                                    | If the control supports the [SelectionItem](uiauto-implementingselectionitem.md) control pattern, it must support this event.   |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                                               |                                                                                                                                  |
| [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md) property-changed event.                                 | If the control supports the [Toggle](uiauto-implementingtoggle.md) control pattern, it must support this event.                 |
| [**UIA\_ValueValuePropertyId**](uiauto-control-pattern-propids.md) property-changed event.                                               | If the control supports the [Value](uiauto-implementingvalue.md) control pattern, it must support this event.                   |



 

## Remarks

If a container hosts list items, the primary means of navigation should go to the list items. Placing the focus on subelements through list navigation can be confusing to users and accessibility tools. If the container hosts a vertical list of items, pressing the UP ARROW and DOWN ARROW keys should navigate through the items, but pressing the RIGHT ARROW and LEFT ARROW keys may navigate to subelements of the focused item, such as list columns or UI subelements.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




