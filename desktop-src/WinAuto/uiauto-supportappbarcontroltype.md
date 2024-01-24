---
title: AppBar Control Type
description: This topic provides information about Microsoft UI Automation support for the AppBar control type.
ms.assetid: B56F4E7A-934F-8516-9B1B-B23B80D54273
keywords:
- UI Automation,support for AppBar control type
- UI Automation,AppBar control type
- UI Automation,control patterns for AppBar control type
- control patterns,AppBar control type
- support for AppBar control type
- AppBar control type
- control types,AppBar
ms.topic: article
ms.date: 05/31/2018
---

# AppBar Control Type

This topic provides information about Microsoft UI Automation support for the **AppBar** control type.

An app bar is a UI element that presents navigation, commands, and tools to the user. For Windows Store apps, app bars for apps can be displayed by pressing Windows Key + Z.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **AppBar** control type.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Events](#required-events)
-   [Relevant Events](#relevant-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to **AppBar** controls and describes what can be contained in each view. **Button** is the most common element within an **AppBar** but other controls that invoke actions for an app are also possible. An **AppBar** can also have 0 or more separators (**Separator** control type), which appear in the control view as placed between the other controls. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>AppBar<ul><li>Button (0 or many)</li><li>Other controls (0 or many)</li></ul></li></ul> | <ul><li>Not applicable<ul><li>Button (0 or many)</li><li>Other controls (0 or many)</li></ul></li></ul> | 




 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the controls that implement the **AppBar** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes. | The value exposed by this property must include all of the controls contained within it.                                                                                                                                    |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **AppBar** |                                                                                                                                                                                                                             |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | FALSE      | An app bar control is not included in the content view of the UI Automation tree.                                                                                                                                           |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | An app bar control is always included in the control view of the UI Automation tree.                                                                                                                                        |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes  | If the control can receive keyboard focus, it must support this property. Controls within the app bar typically can take keyboard focus.                                                                                    |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md)                   | See notes. | The value of this property depends on whether the control is viewable on the screen.                                                                                                                                        |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | Null       | App bar controls usually do not have a label.                                                                                                                                                                               |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes. | Localized string corresponding to the **AppBar** control type. The default value is "app bar" for en-US or English (United States).                                                                                         |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes. | The app bar control does not need a name unless an application has more than one app bar. If there is more than one app bar in an application, use this property to expose distinguishing names, such as "Top" or "Bottom." |



 

## Required Events

The following table lists the UI Automation events that app bar controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                  |                                                                                                                            |



 

## Relevant Events

The following table lists the UI Automation events that are especially relevant to the controls that implement the **AppBar** control type but not strictly required.



| UI Automation Event                                                                                 | Notes                                                                              |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**UIA\_MenuClosedEventId**](uiauto-event-ids.md)                            | Platform implementations might fire this event when the app bar control is closed. |
| [**UIA\_MenuOpenedEventId**](uiauto-event-ids.md)                            | Platform implementations might fire this event when the app bar control is opened. |
| [**IUIAutomationPropertyChangedEventHandler**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationpropertychangedeventhandler) | Property-changed event handler.                                                    |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**AppBar XAML control**](/uwp/api/Windows.UI.Xaml.Controls.AppBar)
</dt> <dt>

[**WinJS.UI.AppBar object**](/previous-versions/windows/apps/br229670(v=win.10))
</dt> </dl>

 

 
