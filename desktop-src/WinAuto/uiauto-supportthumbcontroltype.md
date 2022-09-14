---
title: Thumb Control Type
description: This topic provides information about Microsoft UI Automation support for the Thumb control type.
ms.assetid: 3b1d6802-cfd4-4b07-80a0-2950ca7f4e96
keywords:
- UI Automation,support for Thumb control type
- UI Automation,Thumb control type
- UI Automation,tree structure for Thumb control type
- UI Automation,properties for Thumb control type
- UI Automation,control patterns for Thumb control type
- UI Automation,events for Thumb control type
- tree structures,Thumb control type
- properties,Thumb control type
- control patterns,Thumb control type
- events,Thumb control type
- support for Thumb control type
- Thumb control type
- control types,tree structure for Thumb control type
- control types,control patterns for Thumb control type
- control types,support for Thumb
- control types,Thumb
ms.topic: article
ms.date: 05/31/2018
---

# Thumb Control Type

This topic provides information about Microsoft UI Automation support for the **Thumb** control type.

Thumb controls provide the functionality that enables a control to be moved (or dragged), such as a scroll bar button, or resized, such as a window resizing widget. Note that a thumb control does not provide drag-and-drop functionality. Thumb controls can receive mouse focus but not keyboard focus. The control developer must implement the control so that it acts appropriately (can be dragged or resized).

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Thumb** control type. The UI Automation requirements apply all thumb controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to thumb controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Thumb</li></ul> | (Not applicable) | 




 

Thumb controls never appear in the content view because they exist only to be manipulated with a mouse. They are exposed though another control pattern, such as the [Scroll](uiauto-implementingscroll.md) control pattern, [Transform](uiauto-implementingtransform.md) control pattern, or [RangeValue](uiauto-implementingrangevalue.md) control pattern, being supported on the thumb control's container.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to thumb controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                 |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                                                                                     |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes. | A point within the visible client area of the thumb control.                                                                                                                                                                                                 |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Thumb**  |                                                                                                                                                                                                                                                              |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | FALSE      | The thumb control is never included in the content view of the UI Automation tree.                                                                                                                                                                           |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | The thumb control is always included in the control view of the UI Automation tree.                                                                                                                                                                          |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes. | If the control can receive keyboard focus, it must support this property. A thumb control can receive the focus if it is used as a "gripper" object for sizing a window or a pane. A thumb control in a slider or scroll bar should never receive the focus. |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | NULL       | Thumb controls never have a label.                                                                                                                                                                                                                           |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes. | Localized string corresponding to the **Thumb** control type. The default value is "thumb" for en-US or English (United States).                                                                                                                             |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | NULL       | Because the thumb control is not available in the content view of the UI Automation tree, it does not require a name.                                                                                                                                        |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by thumb controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                         | Support  | Notes                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ITransformProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itransformprovider) | Required | Enables the thumb control to be moved on the screen. Because the thumb control typically cannot be resized or rotated, the [Transform](uiauto-implementingtransform.md) control pattern primarily supports the [**Move**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itransformprovider-move) function. |



 

## Required Events

The following table lists the UI Automation events that thumb controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                  |                                                                                                                            |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




