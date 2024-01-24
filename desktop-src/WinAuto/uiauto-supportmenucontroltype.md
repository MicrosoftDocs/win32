---
title: Menu Control Type
description: This topic provides information about Microsoft UI Automation support for the Menu control type.
ms.assetid: cdbb6db7-63d7-422e-952c-7b59779fefbe
keywords:
- UI Automation,support for Menu control type
- UI Automation,Menu control type
- UI Automation,tree structure for Menu control type
- UI Automation,properties for Menu control type
- UI Automation,control patterns for Menu control type
- UI Automation,events for Menu control type
- tree structures,Menu control type
- properties,Menu control type
- control patterns,Menu control type
- events,Menu control type
- support for Menu control type
- Menu control type
- control types,tree structure for Menu control type
- control types,control patterns for Menu control type
- control types,support for Menu
- control types,Menu
ms.topic: article
ms.date: 05/31/2018
---

# Menu Control Type

This topic provides information about Microsoft UI Automation support for the **Menu** control type.

A menu control allows hierarchal organization of elements associated with commands and event handlers. In a typical Microsoft Windows application, a menu bar contains several menu buttons (such as **File**, **Edit**, and **Window**), and each menu button displays a menu. A menu contains a collection of menu items (such as **New**, **Open**, and **Close**), which can be expanded to display additional menu items or to perform a specific action when clicked.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Menu** control type. The UI Automation requirements apply to all menu controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to menu controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Menu<ul><li>MenuItem (1 or many)</li></ul><ul><li>Other controls (0 or many)</li></ul></li></ul> | <ul><li>Menu<ul><li>MenuItem (1 or many)</li></ul><ul><li>Other controls (0 or many)</li></ul></li></ul> | 




 

Menu controls always appear in the control view and the content view of the UI Automation tree. Menu controls should appear under the control that their information is referring to. UI Automation clients can listen for [**UIA\_MenuOpenedEventId**](uiauto-event-ids.md) to ensure that they consistently obtain information conveyed by menu controls. Context menu controls are a special case. They may appear as children of the desktop or of a top level application window.

A menu control can contain other controls, such as edit controls and combo boxes, within its structure. These additional controls correspond to the "other controls" listed in the previous table in the control and content views.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **Menu** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                      | Value      | Notes                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)           | **Menu**   |                                                                                                                                                                         |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md) | TRUE       | The menu control is always included in the content view of the UI Automation tree.                                                                                      |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md) | TRUE       | The menu control is always included in the control view of the UI Automation tree.                                                                                      |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)               | NULL       | No label is anticipated with a typical menu control.                                                                                                                    |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                         | See notes. | The menu control does not require a **Name** property to be set, or it could have the same name as the associated control, such as a menu item that opened the submenu. |



 

## Required Control Patterns

There are no required control patterns for the Menu control type.

## Required Events

Menu controls must raise the [**UIA\_MenuOpenedEventId**](uiauto-event-ids.md) event when they appear on the screen. The **UIA\_MenuOpenedEventId** event will include the text of the control. The [**UIA\_MenuClosedEventId**](uiauto-event-ids.md) event must be raised when a menu disappears from the screen.

The following table lists the UI Automation events that menu controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_MenuClosedEventId**](uiauto-event-ids.md)                                                              |                                                                                                                            |
| [**UIA\_MenuOpenedEventId**](uiauto-event-ids.md)                                                              |                                                                                                                            |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                  |                                                                                                                            |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




