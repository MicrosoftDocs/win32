---
title: Text Control Type
description: This topic provides information about Microsoft UI Automation support for the Text control type.
ms.assetid: 69a3b243-8ee5-48e4-a01e-c7ad69b9a3aa
keywords:
- UI Automation,support for Text control type
- UI Automation,Text control type
- UI Automation,tree structure for Text control type
- UI Automation,properties for Text control type
- UI Automation,control patterns for Text control type
- UI Automation,events for Text control type
- tree structures,Text control type
- properties,Text control type
- control patterns,Text control type
- events,Text control type
- support for Text control type
- Text control type
- control types,tree structure for Text control type
- control types,control patterns for Text control type
- control types,support for Text
- control types,Text
ms.topic: article
ms.date: 05/31/2018
---

# Text Control Type

This topic provides information about Microsoft UI Automation support for the **Text** control type.

A text control is a basic user interface item that represents a piece of text on the screen.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Text** control type. The UI Automation requirements apply to all tree controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to text controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Text</li></ul> | <ul><li>Text (if content)</li></ul> | 




 

A text control can be used alone as a label or as static text on a form. It can also be contained within the structure of one of the following items:

-   [DataItem](uiauto-supportdataitemcontroltype.md)
-   [ListItem](uiauto-supportlistitemcontroltype.md)
-   [TreeItem](uiauto-supporttreeitemcontroltype.md)

Text controls might not appear in the content view of the UI Automation tree because text is often displayed through the **Name** property of another control. For example, the text used to label a combo box control is exposed through the control's **Name** property. Because the combo box control is in the content view of the UI Automation tree, the text control need not be there. Text controls may have children in the content view if there is an embedded object such as a hyperlink.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the text controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                                                                                                        |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                                                                                            |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes. | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point.                                                                                                                                                |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Text**   |                                                                                                                                                                                                                                                                                                                                                     |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | Depends    | The text control is content if it contains information not exposed in another control's Name property.                                                                                                                                                                                                                                              |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | The text control must always be a control.                                                                                                                                                                                                                                                                                                          |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes. | If the control can receive keyboard focus, it must support this property.                                                                                                                                                                                                                                                                           |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | NULL       | Text controls do not have a static text label.                                                                                                                                                                                                                                                                                                      |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes. | Localized string corresponding to the **Text** control type. The default value is "text" for en-US or English (United States).                                                                                                                                                                                                                      |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes. | The name of a text control can be the text that it displays. However, if the control also supports the [Text](uiauto-implementingtextandtextrange.md) pattern, and the text is extensive, don't use the full text content as the **Name** value. Instead, provide a **Name** value that is shorter, derived from other properties of your control. |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by text controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                         | Support | Notes                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IGridItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igriditemprovider)   | Depends | If the text control is contained within a table control, the [GridItem](uiauto-implementinggriditem.md) control pattern must be supported.                                                                                                                            |
| [**ITableItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itableitemprovider) | Depends | If the text control is contained within a table control, the [TableItem](uiauto-implementingtableitem.md) control pattern must be supported.                                                                                                                          |
| [**ITextProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itextprovider)           | Depends | Text should support the [Text](uiauto-implementingtextandtextrange.md) control pattern for better accessibility; however, it is not required. The Text control pattern is useful when the text has rich style and attributes (for example, color, bold, and italics). |
| [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider)         | Never   | A text control never supports the [Value](uiauto-implementingvalue.md) control pattern. If the text is editable, it is the [Edit](uiauto-supporteditcontroltype.md) control type.                                                                                    |



 

## Required Events

The following table lists the UI Automation events that text controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md) property-changed event.                           |                                                                                                                            |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                  |                                                                                                                            |
| [**UIA\_Text\_TextChangedEventId**](uiauto-event-ids.md)                                                 | If the control supports the [Text](uiauto-implementingtextandtextrange.md) control pattern, it must support this event.   |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




