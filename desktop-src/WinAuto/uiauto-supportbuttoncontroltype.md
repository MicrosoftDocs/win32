---
title: Button Control Type
description: This topic provides information about Microsoft UI Automation support for the Button control type.
ms.assetid: a2942067-461c-4281-80cf-385e3c08c874
keywords:
- UI Automation,support for Button control type
- UI Automation,Button control type
- UI Automation,tree structure for Button control type
- UI Automation,properties for Button control type
- UI Automation,control patterns for Button control type
- UI Automation,events for Button control type
- tree structures,Button control type
- properties,Button control type
- control patterns,Button control type
- events,Button control type
- support for Button control type
- Button control type
- control types,tree structure for Button control type
- control types,control patterns for Button control type
- control types,support for Button
- control types,Button
ms.topic: article
ms.date: 05/31/2018
---

# Button Control Type

This topic provides information about Microsoft UI Automation support for the **Button** control type.

A button is an object that a user interacts with to perform an action such as the OK and Cancel buttons on a dialog box. The button control is a simple control to expose because it maps to a single command that the user wishes to complete.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Button** control type. The UI Automation requirements apply to all button controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to button controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Button<ul><li>Image (0 or more)</li><li>Text (0 or more)</li></ul></li></ul> | <ul><li>Button</li></ul> | 




 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the controls that implement the **Button** control type (such as button controls). For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AcceleratorKeyPropertyId**](uiauto-automation-element-propids.md)             | See notes. | A button control typically supports an accelerator key to enable the end user to quickly perform the action represented by the button from the keyboard.                                             |
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                         |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes. | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Button** |                                                                                                                                                                                                      |
| [**UIA\_HelpTextPropertyId**](uiauto-automation-element-propids.md)                         | See notes. | The help text should indicate what the end result of activating the button will be. This is typically the same type of information presented through a tooltip.                                      |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | The button control must always be content.                                                                                                                                                           |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | The button control must always be a control.                                                                                                                                                         |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes. | If the control can receive keyboard focus, it must support this property.                                                                                                                            |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | Null       | Button controls are self-labeled by their contents.                                                                                                                                                  |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes. | Localized string corresponding to the **Button** control type. The default value is "button" for en-US or English (United States).                                                                   |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes. | The name of the button control is the text used to label it. Whenever an image is used to label a button, alternate text must be supplied for the button's **Name** property.                        |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all button controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                                  | Support/Value | Notes                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IExpandCollapseProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider) | See notes.    | When a button is hosted as a child of a split button, the child button can support the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern instead of the [Invoke](uiauto-implementinginvoke.md) or [Toggle](uiauto-implementingtoggle.md) control pattern. The ExpandCollapse control pattern can be used for opening or closing a menu or other sub-structure associated with the button element. |
| [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider)                 | See notes.    | All buttons should support the [Invoke](uiauto-implementinginvoke.md) control pattern or the [Toggle](uiauto-implementingtoggle.md) control pattern but not both. The Invoke control pattern must be supported when the button performs a command at the request of the user. This command maps to a single operation such as Cut, Copy, Paste, or Delete.                                                              |
| [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider)                 | See notes.    | All buttons should support the [Invoke](uiauto-implementinginvoke.md) control pattern or the [Toggle](uiauto-implementingtoggle.md) control pattern but not both. The Toggle control pattern must be supported if the button can cycle through a series of up to three states. Typically this is seen as an on/off switch for specific features.                                                                        |



 

## Required Events

The following table lists the UI Automation events that button controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_Invoke\_InvokedEventId**](uiauto-event-ids.md)                                                     | If the control supports the [Invoke](uiauto-implementinginvoke.md) control pattern, it must support this event.           |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md) property-changed event.                           |                                                                                                                            |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                  |                                                                                                                            |
| [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md) property-changed event.    | If the control supports the [Toggle](uiauto-implementingtoggle.md) control pattern, it must support this event.           |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




