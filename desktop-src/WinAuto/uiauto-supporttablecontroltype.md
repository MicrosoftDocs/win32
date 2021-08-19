---
title: Table Control Type
description: This topic provides information about Microsoft UI Automation support for the Table control type.
ms.assetid: 508db2af-1ca3-4003-8e1f-6e225cf79b7a
keywords:
- UI Automation,support for Table control type
- UI Automation,Table control type
- UI Automation,tree structure for Table control type
- UI Automation,properties for Table control type
- UI Automation,control patterns for Table control type
- UI Automation,events for Table control type
- tree structures,Table control type
- properties,Table control type
- control patterns,Table control type
- events,Table control type
- support for Table control type
- Table control type
- control types,tree structure for Table control type
- control types,control patterns for Table control type
- control types,support for Table
- control types,Table
ms.topic: article
ms.date: 05/31/2018
---

# Table Control Type

This topic provides information about Microsoft UI Automation support for the **Table** control type.

Table controls contain rows and columns of text and, optionally, row headers and column headers.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Table** control type. The UI Automation requirements apply to all table controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to table controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Table<ul><li>Text (0 or 1)</li><li>Header (0 or more)</li><li>Various controls (0 or more)</li></ul></li></ul> | <ul><li>Table<ul><li>Text (1 or more)</li><li>Various controls (0 or more)</li></ul></li></ul> | 




 

If a table control has row or column headers, they must be exposed in the control view of the UI Automation tree. The content view does not need to expose this information because it can be accessed using [**IUIAutomationTablePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtablepattern).

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to table controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                      |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                                                          |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes. | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point.                              |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Table**  |                                                                                                                                                                                                                                   |
| [**UIA\_DescribedByPropertyId**](uiauto-automation-element-propids.md)                   | See notes. | If the table is annotated by other UI element (for example, a text element that holds the description for the table), the DescribedBy property should expose a reference to the automation element of the text control.           |
| [**UIA\_HelpTextPropertyId**](uiauto-automation-element-propids.md)                         | See notes. | More details about the purpose of the table should be exposed through this property if it is not sufficiently explained by the [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md) property.      |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | The table control must always appear in the content view of the UI Automation tree.                                                                                                                                               |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | The table control must always appear in the control view of the UI Automation tree.                                                                                                                                               |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes. | If the control can receive keyboard focus, it must support this property.                                                                                                                                                         |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | See notes. | If there is a static text label, this property should expose a reference to the automation element of the control.                                                                                                                |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes. | Localized string corresponding to the **Table** control type. The default value is "table" for en-US or English (United States).                                                                                                  |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes. | The table control typically gets the value for its name from a static text label. If there is not a static text label, the element must assign a Name property that must always be available to explain the purpose of the table. |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all table controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                         | Support                     | Notes                                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IGridProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igridprovider)           | Required                    | Because the table control contains items presented in a grid, it always supports the [Grid](uiauto-implementinggrid.md) control pattern.                                                                                                                                                    |
| [**IGridItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igriditemprovider)   | Required with child objects | The inner objects of a table should support both the [GridItem](uiauto-implementinggriditem.md) and [TableItem](uiauto-implementingtableitem.md) control patterns. The table itself need not support the GridItem or TableItem control pattern unless the table is part of another table.  |
| [**ITableProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itableprovider)         | Required                    | The table control can always have headers associated with the content.                                                                                                                                                                                                                       |
| [**ITableItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itableitemprovider) | Required with child objects | The inner objects of a table should support both the [GridItem](uiauto-implementinggriditem.md) and [TableItem](uiauto-implementingtableitem.md) control patterns. The table itself need not support the GridItem or TableItem control patterns unless the table is part of another table. |



 

## Required Events

The following table lists the UI Automation events that table controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



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

 

 




