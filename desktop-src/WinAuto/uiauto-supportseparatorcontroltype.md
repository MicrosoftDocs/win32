---
title: Separator Control Type
description: This topic provides information about Microsoft UI Automation support for the Separator control type.
ms.assetid: 4987b05a-101e-48b1-aed2-bd7206146f70
keywords:
- UI Automation,support for Separator control type
- UI Automation,Separator control type
- UI Automation,tree structure for Separator control type
- UI Automation,properties for Separator control type
- UI Automation,control patterns for Separator control type
- UI Automation,events for Separator control type
- tree structures,Separator control type
- properties,Separator control type
- control patterns,Separator control type
- events,Separator control type
- support for Separator control type
- Separator control type
- control types,tree structure for Separator control type
- control types,control patterns for Separator control type
- control types,support for Separator
- control types,Separator
ms.topic: article
ms.date: 05/31/2018
---

# Separator Control Type

This topic provides information about Microsoft UI Automation support for the **Separator** control type.

Separator controls are used to visually divide a space into two regions. For example, a separator control can be a bar that defines two panes in a window. If the separator can be moved, the control should be exposed as Thumb in control type.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Separator** control type. The UI Automation requirements apply to all separator controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to separator controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Separator</li></ul> | <ul><li>The <strong>Separator</strong> control type never has content.</li></ul> | 




 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to separator controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value         | Notes                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.    | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                         |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.    | The outermost rectangle that contains the whole control.                                                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.    | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Separator** |                                                                                                                                                                                                      |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | FALSE         | The separator control is never content.                                                                                                                                                              |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE          | The separator control must always be a control.                                                                                                                                                      |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.    | If the control can receive keyboard focus, it must support this property.                                                                                                                            |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | NULL          | The separator control does not have a static label.                                                                                                                                                  |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.    | Localized string corresponding to the **Separator** control type. The default value is "Separator" for en-US or English (United States).                                                             |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | ""            | The separator control does not require a **Name** property.                                                                                                                                          |



 

## Required Control Patterns

The separator control is not required to support any control patterns. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).

## Required Events

The following table lists the UI Automation events that separator controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



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

 

 




