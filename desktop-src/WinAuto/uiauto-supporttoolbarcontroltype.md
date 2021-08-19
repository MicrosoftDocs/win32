---
title: ToolBar Control Type
description: This topic provides information about Microsoft UI Automation support for the ToolBar control type. Toolbar controls enable end users to activate commands and tools contained within a application.
ms.assetid: e2a72ce3-5263-43f8-be4d-715a78224b68
keywords:
- UI Automation,support for ToolBar control type
- UI Automation,ToolBar control type
- UI Automation,tree structure for ToolBar control type
- UI Automation,properties for ToolBar control type
- UI Automation,control patterns for ToolBar control type
- UI Automation,events for ToolBar control type
- tree structures,ToolBar control type
- properties,ToolBar control type
- control patterns,ToolBar control type
- events,ToolBar control type
- support for ToolBar control type
- ToolBar control type
- control types,tree structure for ToolBar control type
- control types,control patterns for ToolBar control type
- control types,support for ToolBar
- control types,ToolBar
ms.topic: article
ms.date: 05/31/2018
---

# ToolBar Control Type

This topic provides information about Microsoft UI Automation support for the **ToolBar** control type. Toolbar controls enable end users to activate commands and tools contained within a application.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **ToolBar** control type. The UI Automation requirements apply to all toolbar controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to toolbar controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>ToolBar<ul><li>Various controls (0 or more)</li></ul></li></ul> | <ul><li>ToolBar<ul><li>Various controls (0 or more)</li></ul></li></ul> | 




 

A toolbar control can contain any type of control within its subtree. They most often contain buttons, combo boxes, and split buttons.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **ToolBar** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value       | Notes                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.  | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                               |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.  | The outermost rectangle that contains the whole control.                                                                                                                                                   |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.  | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point.       |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **ToolBar** | This value is the same for all UI frameworks.                                                                                                                                                              |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE        | The toolbar control is always included in the content view of the UI Automation tree.                                                                                                                      |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE        | The toolbar control is always included in the control view of the UI Automation tree.                                                                                                                      |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.  | If the control can receive keyboard focus, it must support this property.                                                                                                                                  |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | NULL        | A toolbar control never has a label.                                                                                                                                                                       |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.  | Localized string corresponding to the **ToolBar** control type. The default value is "tool bar" for en-US or English (United States).                                                                      |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | Depends     | The toolbar control does not need a name unless more than one is used within an application. If more than one is present, each must have a distinguishing name (for example, "Formatting" or "Outlining"). |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by toolbar controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                                   | Support | Notes                                                                                                                                                         |
|-------------------------------------------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDockProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-idockprovider)                     | Depends | If the toolbar can be docked to different parts of the screen, it must support the [Dock](uiauto-implementingdock.md) control pattern.                       |
| [**IExpandCollapseProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider) | Depends | If the toolbar can be expanded and collapsed to show more items, it must support the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern. |
| [**ITransformProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itransformprovider)           | Depends | If the toolbar can be resized, rotated, or moved, it must support the [Transform](uiauto-implementingtransform.md) control pattern.                          |



 

## Required Events

The following table lists the UI Automation events that toolbar controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



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

 

 




