---
title: MenuItem Control Type
description: This topic provides information about Microsoft UI Automation support for the MenuItem control type.
ms.assetid: a6a04489-8e28-44ff-a3b0-ecf19c24daab
keywords:
- UI Automation,support for MenuItem control type
- UI Automation,MenuItem control type
- UI Automation,tree structure for MenuItem control type
- UI Automation,properties for MenuItem control type
- UI Automation,control patterns for MenuItem control type
- UI Automation,events for MenuItem control type
- tree structures,MenuItem control type
- properties,MenuItem control type
- control patterns,MenuItem control type
- events,MenuItem control type
- support for MenuItem control type
- MenuItem control type
- control types,tree structure for MenuItem control type
- control types,control patterns for MenuItem control type
- control types,support for MenuItem
- control types,MenuItem
ms.topic: article
ms.date: 05/31/2018
---

# MenuItem Control Type

This topic provides information about Microsoft UI Automation support for the **MenuItem** control type.

A menu control allows hierarchal organization of elements associated with commands and event handlers. In a typical Windows application, a menu bar contains several menu items (such as **File**, **Edit**, and **Window**), and each menu item displays a menu. A menu contains a collection of menu items (such as **New**, **Open**, and **Close**), which can be expanded to display additional menu items or perform a specific action when clicked.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **MenuItem** control type. The UI Automation requirements apply to all menu item controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Legacy Issues](#legacy-issues)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to menu item controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>MenuItem "Help"<ul><li>Menu (submenu of Help menu item)<ul><li>MenuItem "Help Topics"</li><li>MenuItem "About Notepad"</li></ul></li></ul></li></ul> | <ul><li>MenuItem "Help"<ul><li>MenuItem "Help Topics"</li><li>MenuItem "About Notepad"</li></ul></li></ul> | 




 

The control view of the menu item control has the UI Automation tree structure shown above. Note that the menu item for **Help** on the menu bar has been added to better illustrate the structure.

For the content view, **Menu** is absent from the UI Automation tree because it does not convey meaningful information to the end user.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **MenuItem** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value        | Notes                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.   | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree. Allocate the **AutomationId** property for a menu item if the element is known to be consistent across different instances of the user interface. If the menu item is dynamically populated and not predictable, leave the **AutomationId** property blank. |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.   | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                                                                                                                 |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.   | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point.                                                                                                                                                                     |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **MenuItem** |                                                                                                                                                                                                                                                                                                                                                                          |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE         | The menu item control is always included in the content view of the UI Automation tree.                                                                                                                                                                                                                                                                                  |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE         | The menu item control is always included in the control view of the UI Automation tree.                                                                                                                                                                                                                                                                                  |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.   | If the control can receive keyboard focus, it must support this property.                                                                                                                                                                                                                                                                                                |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.   | Localized string corresponding to the **MenuItem** control type. The default value is "menu item" for en-US or English (United States).                                                                                                                                                                                                                                  |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.   | The name of the menu item control is the text used to label it.                                                                                                                                                                                                                                                                                                          |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by menu item controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                                   | Support | Notes                                                                                                                                                |
|-------------------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IExpandCollapseProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider) | Depends | If the control can be expanded or collapsed, implement [**IExpandCollapseProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider).                            |
| [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider)                 | Depends | If the control executes a single action or command, implement [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider).                                     |
| [**ISelectionItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider)   | Depends | If the control is used to select from a list of options among menu items, implement [**ISelectionItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider). |
| [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider)                 | Depends | If the control represents an option that can be turned on or off, implement [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider).                       |



 

## Required Events

The following table lists the UI Automation events that menu item controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                                | Notes                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                                                   |                                                                                                                                  |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event.                              |                                                                                                                                  |
| [**UIA\_ExpandCollapseExpandCollapseStatePropertyId**](uiauto-control-pattern-propids.md) property-changed event. | If the control supports the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern, it must support this event. |
| [**UIA\_Invoke\_InvokedEventId**](uiauto-event-ids.md)                                                                                  | If the control supports the [Invoke](uiauto-implementinginvoke.md) control pattern, it must support this event.                 |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                              | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.         |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                          | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event.       |
| [**UIA\_SelectionItem\_ElementAddedToSelectionEventId**](uiauto-event-ids.md)                                    | If the control supports the [SelectionItem](uiauto-implementingselectionitem.md) control pattern, it must support this event.   |
| [**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md)                            | If the control supports the [SelectionItem](uiauto-implementingselectionitem.md) control pattern, it must support this event.   |
| [**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md)                                                    | If the control supports the [SelectionItem](uiauto-implementingselectionitem.md) control pattern, it must support this event.   |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                                               |                                                                                                                                  |
| [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md) property-changed event.                                 | If the control supports the [Toggle](uiauto-implementingtoggle.md) control pattern, it must support this event.                 |



 

## Legacy Issues

For Microsoft Win32 menu items, the [Toggle](uiauto-implementingtoggle.md) control pattern is supported only when a menu item is checked and it is possible to programmatically determine whether support for the Toggle control pattern is required. Because a Win32 menu item does not expose whether it can be checked, the Invoke control pattern is supported when the menu item is not checked. The Invoke control pattern is always supported, even for menu items that are only required to support the Toggle control pattern. This is so clients do not become confused when a menu item that was supporting the [Invoke](uiauto-implementinginvoke.md) control pattern (when the menu item was unchecked) no longer supports that pattern when it becomes checked.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




