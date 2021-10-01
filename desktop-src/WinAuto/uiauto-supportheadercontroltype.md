---
title: Header Control Type
description: This topic provides information about Microsoft UI Automation support for the Header control type.
ms.assetid: 032fc3a1-f939-40db-abbb-532afe309ba3
keywords:
- UI Automation,support for Header control type
- UI Automation,Header control type
- UI Automation,tree structure for Header control type
- UI Automation,properties for Header control type
- UI Automation,control patterns for Header control type
- UI Automation,events for Header control type
- tree structures,Header control type
- properties,Header control type
- control patterns,Header control type
- events,Header control type
- support for Header control type
- Header control type
- control types,tree structure for Header control type
- control types,control patterns for Header control type
- control types,support for Header
- control types,Header
ms.topic: article
ms.date: 05/31/2018
---

# Header Control Type

This topic provides information about Microsoft UI Automation support for the **Header** control type.

The header control provides a visual container for the labels for rows or columns of information.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Header** control type. The UI Automation requirements apply to all header controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to header controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Header<ul><li>HeaderItem (1 or more)</li></ul></li></ul> | (Not applicable) | 




 

Header controls always have one or more children in the control view of the UI Automation tree.

Header controls have zero children in the content view of the UI Automation tree.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to header controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value                                                            | Notes                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.                                                       | The value of this property must be unique across all controls in an application.                                                                                                                     |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.                                                       | The outermost rectangle that contains the whole control.                                                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.                                                       | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Header**                                                       |                                                                                                                                                                                                      |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | FALSE                                                            | The header control is not included in the content view of the UI Automation tree.                                                                                                                    |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE                                                             | The header control is always included in the control view of the UI Automation tree.                                                                                                                 |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.                                                       | If the control can receive keyboard focus, it must support this property.                                                                                                                            |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | NULL                                                             | Header controls do not have a static label.                                                                                                                                                          |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.                                                       | The default value is "header" for en-US or English (United States).                                                                                                                                  |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.                                                       | The header control needs a name if there is more than one row header or more than one column header. This identifies the information within the header.                                              |
| [**UIA\_OrientationPropertyId**](uiauto-automation-element-propids.md)                   | **OrientationType\_Horizontal** or **OrientationType\_Vertical** | The value of this property exposes the position of the header control—whether it is a row header (**OrientationType\_Horizontal**) or column header (**OrientationType\_Vertical**).                 |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported for header controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                         | Support | Notes                                                                                                             |
|---------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------|
| [**ITransformProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itransformprovider) | Depends | Implement the [Transform](uiauto-implementingtransform.md) control pattern if the header control can be resized. |



 

## Required Events

The following table lists the UI Automation events that header controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



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

 

 




