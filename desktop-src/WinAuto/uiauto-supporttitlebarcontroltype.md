---
title: TitleBar Control Type
description: This topic provides information about Microsoft UI Automation support for the TitleBar control type. A title bar control represents a title or caption bar in a window.
ms.assetid: dc707198-ceb6-4fbf-ace4-8fec88c92b98
keywords:
- UI Automation,support for TitleBar control type
- UI Automation,TitleBar control type
- UI Automation,tree structure for TitleBar control type
- UI Automation,properties for TitleBar control type
- UI Automation,control patterns for TitleBar control type
- UI Automation,events for TitleBar control type
- tree structures,TitleBar control type
- properties,TitleBar control type
- control patterns,TitleBar control type
- events,TitleBar control type
- support for TitleBar control type
- TitleBar control type
- control types,tree structure for TitleBar control type
- control types,control patterns for TitleBar control type
- control types,support for TitleBar
- control types,TitleBar
ms.topic: article
ms.date: 05/31/2018
---

# TitleBar Control Type

This topic provides information about Microsoft UI Automation support for the **TitleBar** control type. A title bar control represents a title or caption bar in a window.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **TitleBar** control type. The UI Automation requirements apply to all title bar controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to title bar controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>TitleBar<ul><li>Menu (0 or 1)</li><li>Button (0 or more)</li></ul></li></ul> | (Not applicable; the title bar control has no content) | 




 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **TitleBar** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value        | Notes                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.   | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                         |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.   | The value exposed by this property must include all of the controls contained within it.                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.   | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **TitleBar** | This value is the same for all UI frameworks.                                                                                                                                                        |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | FALSE        | The title bar control is never included in the content view of the UI Automation tree.                                                                                                               |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE         | The title bar control is always included in the control view of the UI Automation tree.                                                                                                              |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | FALSE        | A title bar control never has keyboard focus.                                                                                                                                                        |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md)                   | Depends      | A title bar control returns a value depending on whether it is visible on the screen.                                                                                                                |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | See notes.   | A title bar control typically does not have a label.                                                                                                                                                 |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.   | Localized string corresponding to the TitleBar control type. The default value is "title bar" for en-US or English (United States).                                                                  |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | ""           | A title bar is not content; its textual information is exposed by the name of the parent window.                                                                                                     |



 

## Required Control Patterns

The **TitleBar** control type is not required to support any control patterns. Its functionality is exposed through the [Window](uiauto-implementingwindow.md) control pattern on the [Window](uiauto-supportwindowcontroltype.md) control type.

## Required Events

The following table lists the UI Automation events that title bar controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



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

 

 




