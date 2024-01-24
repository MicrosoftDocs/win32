---
title: MenuBar Control Type
description: This topic provides information about Microsoft UI Automation support for the MenuBar control type.
ms.assetid: e93a92ce-7c98-4e8f-8a6a-a365ccb705d6
keywords:
- UI Automation,support for MenuBar control type
- UI Automation,MenuBar control type
- UI Automation,tree structure for MenuBar control type
- UI Automation,properties for MenuBar control type
- UI Automation,control patterns for MenuBar control type
- UI Automation,events for MenuBar control type
- tree structures,MenuBar control type
- properties,MenuBar control type
- control patterns,MenuBar control type
- events,MenuBar control type
- support for MenuBar control type
- MenuBar control type
- control types,tree structure for MenuBar control type
- control types,control patterns for MenuBar control type
- control types,support for MenuBar
- control types,MenuBar
ms.topic: article
ms.date: 05/31/2018
---

# MenuBar Control Type

This topic provides information about Microsoft UI Automation support for the **MenuBar** control type.

Menu bar controls are an example of controls that implement the **MenuBar** control type. Menu bars provide a means for users to activate commands and options contained in an application.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **MenuBar** control type. The UI Automation requirements apply to all menu bar controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to menu bar controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>MenuBar<ul><li>MenuItem (1 or more)</li><li>Other controls (0 or many)</li></ul></li></ul> | <ul><li>Not applicable<ul><li>MenuItem (1 or more)</li><li>Other controls (0 or many)</li></ul></li></ul> | 




 

A menu bar control always appears in the control view, but not in content view because it usually does not convey meaningful information to the end user (unless the application contains more than one menu bar).

UI Automation clients can listen for the [**UIA\_MenuModeStartEventId**](uiauto-event-ids.md) event to ensure that they are consistently notified when the UI enters menu mode. When the application is in menu mode, all of the keyboard input may be captured for menu navigation (for example, typing 's' might invoke the **Save** menu instead of typing the character on the application client area). The **UIA\_MenuModeStartEventId** event must precede the first [**UIA\_MenuOpenedEventId**](uiauto-event-ids.md) event to ensure logical consistency. The [**UIA\_MenuModeEndEventId**](uiauto-event-ids.md) event follows the last [**UIA\_MenuClosedEventId**](uiauto-event-ids.md) event. Clicking a menu item may also immediately trigger the **UIA\_MenuModeStartEventId** event, followed by a **UIA\_MenuOpenedEventId** event.

A menu bar control can contain other controls, such as edit controls and combo boxes, within its structure. These additional controls correspond to the "other controls" listed above in the control and content views.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **MenuBar** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value       | Notes                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AcceleratorKeyPropertyId**](uiauto-automation-element-propids.md)             | NULL        | Menu bars usually do not have accelerator keys.                                                                                                                                                                                          |
| [**UIA\_AccessKeyPropertyId**](uiauto-automation-element-propids.md)                       | "ALT"       | Pressing the ALT key should usually bring focus to the menu bar within the application.                                                                                                                                                  |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.  | The value exposed by this property must include all of the controls contained within it.                                                                                                                                                 |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **MenuBar** |                                                                                                                                                                                                                                          |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | FALSE       | The menu bar control is not included in the content view of the UI Automation tree.                                                                                                                                                      |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE        | The menu bar control is always included in the control view of the UI Automation tree.                                                                                                                                                   |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | TRUE        | Menu bar controls are keyboard-focusable because the controls they contain can take keyboard focus.                                                                                                                                      |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md)                   | See notes.  | The value of this property depends on whether the control is viewable on the screen.                                                                                                                                                     |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | NULL        | Menu bar controls usually do not have a label.                                                                                                                                                                                           |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.  | Localized string corresponding to the **MenuBar** control type. The default value is "menu bar" for en-US or English (United States).                                                                                                    |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.  | The menu bar control does not need a name unless an application has more than one menu bar. If there is more than one menu bar in an application, use this property to expose distinguishing names, such as "Formatting" or "Outlining". |
| [**UIA\_OrientationPropertyId**](uiauto-automation-element-propids.md)                   | Depends     | This property exposes whether the menu bar control is horizontal or vertical.                                                                                                                                                            |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by menu bar controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                                   | Support | Notes                                                                                                                                       |
|-------------------------------------------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**IExpandCollapseProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider) | Depends | If the control can be expanded or collapsed, it must implement the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern. |
| [**IDockProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-idockprovider)                     | Depends | If the control can be docked to different parts of the screen, it must implement the [Dock](uiauto-implementingdock.md) control pattern.   |
| [**ITransformProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itransformprovider)           | Depends | If the control can be resized, rotated, or moved, it must implement the [Transform](uiauto-implementingtransform.md) control pattern.      |



 

## Required Events

The following table lists the UI Automation events that menu bar controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                                | Notes                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                                                   |                                                                                                                                  |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event.                              |                                                                                                                                  |
| [**UIA\_ExpandCollapseExpandCollapseStatePropertyId**](uiauto-control-pattern-propids.md) property-changed event. | If the control supports the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern, it must support this event. |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                              | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.         |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                          | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event.       |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                                               |                                                                                                                                  |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




