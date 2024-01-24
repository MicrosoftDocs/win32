---
title: CheckBox Control Type
description: This topic provides information about Microsoft UI Automation support for the CheckBox control type.
ms.assetid: 5a9061bc-2eac-4839-8f2c-32b9d58fe712
keywords:
- UI Automation,support for CheckBox control type
- UI Automation,CheckBox control type
- UI Automation,tree structure for CheckBox control type
- UI Automation,properties for CheckBox control type
- UI Automation,control patterns for CheckBox control type
- UI Automation,events for CheckBox control type
- tree structures,CheckBox control type
- properties,CheckBox control type
- control patterns,CheckBox control type
- events,CheckBox control type
- support for CheckBox control type
- CheckBox control type
- control types,tree structure for CheckBox control type
- control types,control patterns for CheckBox control type
- control types,support for CheckBox
- control types,CheckBox
ms.topic: article
ms.date: 05/31/2018
---

# CheckBox Control Type

This topic provides information about Microsoft UI Automation support for the **CheckBox** control type.

A check box is an object used to indicate a state that users can interact with to cycle through that state. Check boxes either present a binary (Yes/No), (On/Off), or tertiary (On, Off, Indeterminate) option to the user.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **CheckBox** control type. The UI Automation requirements apply to all check box controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [DefaultAction](#defaultaction)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to check box controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>CheckBox</li></ul> | <ul><li>CheckBox</li></ul> | 




 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **CheckBox** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value        | Notes                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.   | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                                       |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.   | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                           |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.   | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point.                                                                               |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **CheckBox** |                                                                                                                                                                                                                                                                                    |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE         | The value of this property must always be **TRUE**. This means that the check box control must always be included in the content view of the UI Automation tree.                                                                                                                   |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE         | The value of this property must always be **TRUE**. This means that the check box control must always be included in the control view of the UI Automation tree.                                                                                                                   |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.   | If the control can receive keyboard focus, it must support this property.                                                                                                                                                                                                          |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | Null         | Check box controls are self-labeling.                                                                                                                                                                                                                                              |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.   | Localized string corresponding to the **CheckBox** control type. The default value is "check box" for en-US or English (United States).                                                                                                                                            |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.   | The value of the check box control's [**IUIAutomationElement::CurrentName**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentname) (or [**CachedName**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_cachedname)) property is the text that is displayed beside the box that maintains the toggle state. |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all check box controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                  | Support/Value | Notes                                                                                                                                                             |
|---------------------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider) | Required      | Check boxes support the [Toggle](uiauto-implementingtoggle.md) control pattern to allow the check box to be programmatically cycled through its internal states. |



 

## Required Events

The following table lists the UI Automation events that check box controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                  |                                                                                                                            |
| [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md) property-changed event.    |                                                                                                                            |



 

## DefaultAction

The default action of the check box is to cause a radio button to become focused and toggle its current state. As mentioned previously, check boxes either present a binary (Yes/No or On/Off) decision to the user or a tertiary (On, Off, Indeterminate). If the check box is binary the default action causes the "on" state to become "off" or the "off" state to become "on". In a tertiary check box the default action cycles through the states of the check box in the same order as if the user had sent successive mouse clicks to the control.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




