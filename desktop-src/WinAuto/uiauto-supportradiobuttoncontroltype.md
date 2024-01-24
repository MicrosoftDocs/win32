---
title: RadioButton Control Type
description: This topic provides information about Microsoft UI Automation support for the RadioButton control type.
ms.assetid: 6fc4a6a3-f5c0-402b-b9e7-870dfaa3370d
keywords:
- UI Automation,support for RadioButton control type
- UI Automation,RadioButton control type
- UI Automation,tree structure for RadioButton control type
- UI Automation,properties for RadioButton control type
- UI Automation,control patterns for RadioButton control type
- UI Automation,events for RadioButton control type
- tree structures,RadioButton control type
- properties,RadioButton control type
- control patterns,RadioButton control type
- events,RadioButton control type
- support for RadioButton control type
- RadioButton control type
- control types,tree structure for RadioButton control type
- control types,control patterns for RadioButton control type
- control types,support for RadioButton
- control types,RadioButton
ms.topic: article
ms.date: 05/31/2018
---

# RadioButton Control Type

This topic provides information about Microsoft UI Automation support for the **RadioButton** control type.

A radio button consists of a round button and application-defined text (a label), an icon, or a bitmap that indicates a choice the user can make by selecting the button. An application typically uses radio buttons in a group box to permit the user to choose from a set of related, but mutually exclusive options. For example, the application might present a group of radio buttons from which the user can select a format preference for text selected in the client area. The user could select a left-aligned, right-aligned, or centered format by selecting the corresponding radio button. Typically, the user can select only one option at a time from a set of radio buttons.

> [!Note]  
> Another control generalization for buttons where only one in a group can be selected is the content of a toggle button. Some UI frameworks consider a radio button to be a specialized toggle button.

 

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **RadioButton** control type. The UI Automation requirements apply to all button controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Remarks](#remarks)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to radio button controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>RadioButton</li></ul> | <ul><li>RadioButton</li></ul> | 




 

There are no children in the control view or the content view.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the controls that implement the **RadioButton** control type (such as button controls). For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value           | Notes                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.      | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                  |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.      | The outermost rectangle that contains the whole control.                                                                                      |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.      | The clickable point must be a point that, when clicked, selects the radio button.                                                             |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **RadioButton** |                                                                                                                                               |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE            | The radio button control is always included in the content view of the UI Automation tree.                                                    |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE            | The radio button control is always included in the control view of the UI Automation tree.                                                    |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.      | If the control can receive keyboard focus, it must support this property.                                                                     |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | NULL            | Radio button controls are self-labeled by their contents.                                                                                     |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.      | Localized string corresponding to the **RadioButton** control type. The default value is "radio button" for en-US or English (United States). |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.      | The name of the radio button control is the text that is displayed beside the button that maintains the selection state.                      |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all radio button controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                                               | Support/Value | Notes                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ISelectionItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider)                | Required      | All radio button controls must support the [SelectionItem](uiauto-implementingselectionitem.md) control pattern to enable themselves to be selected.                                                                                                                                                                                                                                                             |
| [**SelectionContainer**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-get_selectioncontainer) | See notes.    | The [**SelectionContainer**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-get_selectioncontainer) property must always be completed so that a UI Automation client can determine what other radio buttons within a specific context relate to one another. For the Microsoft Win32 version of the radio button, this property is not supported because it is not possible to obtain this information from that legacy framework. |
| [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider)                              | Never         | The radio button cannot cycle through its state once it has been set. The [Toggle](uiauto-implementingtoggle.md) control pattern must never be supported on a radio button.                                                                                                                                                                                                                                      |



 

## Required Events

The following table lists the UI Automation events that button controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                     | Notes                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                        |                                                                                                                                |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event.   |                                                                                                                                |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                   | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.       |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.               | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event.     |
| [**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md) | If the control supports the [SelectionItem](uiauto-implementingselectionitem.md) control pattern, it must support this event. |
| [**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md)                         | If the control supports the [SelectionItem](uiauto-implementingselectionitem.md) control pattern, it must support this event. |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                    |                                                                                                                                |



 

## Remarks

A radio button represents a single selectable option among a group of peer radio buttons. Ideally, radio buttons should have a grouping element that clarifies the boundaries of the peer radio buttons. Often, however, the boundary is implied by the UI element structure. For example, a menu might contain a set of consecutive radio buttons instead of menu items, or a set of radio buttons that occur after a group label, but before an actionable element such as button.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




