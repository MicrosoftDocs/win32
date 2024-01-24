---
title: Document Control Type
description: This topic provides information about Microsoft UI Automation support for the Document control type.
ms.assetid: 62565f16-f0d6-42ff-bc36-897a2618c867
keywords:
- UI Automation,support for Document control type
- UI Automation,Document control type
- UI Automation,tree structure for Document control type
- UI Automation,properties for Document control type
- UI Automation,control patterns for Document control type
- UI Automation,events for Document control type
- tree structures,Document control type
- properties,Document control type
- control patterns,Document control type
- events,Document control type
- support for Document control type
- Document control type
- control types,tree structure for Document control type
- control types,control patterns for Document control type
- control types,support for Document
- control types,Document
ms.topic: article
ms.date: 05/31/2018
---

# Document Control Type

This topic provides information about Microsoft UI Automation support for the **Document** control type.

Document controls let a user view and manipulate multiple pages of text. Unlike edit controls which only support a simple line of unformatted text, document controls can host text that is richly styled and formatted

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Document** control type. The UI Automation requirements apply to all document controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to document controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Document<ul><li>Varies</li></ul></li></ul> | <ul><li>Document<ul><li>Varies</li></ul></li></ul> | 




 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to document controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value        | Notes                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.   | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                      |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.   | The outermost rectangle that contains the whole control.                                                                                          |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.   | The document has a clickable point that will cause the document of one of its elements in the document container to have focus.                   |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Document** |                                                                                                                                                   |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE         | The document control is always included in the content view of the UI Automation tree.                                                            |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE         | The document control is always included in the control view of the UI Automation tree.                                                            |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.   | If the control can receive keyboard focus, it must support this property.                                                                         |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | See notes.   | The value of this property should be the label of the document control. Typically, the title of the document is used.                             |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.   | Localized string corresponding to the **Document** control type. The default value is "document" for en-US or English (United States).            |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.   | The document control typically gets its name from the file name it is loaded from. This is often displayed in a containing window or frame title. |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by document controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                  | Support/Value | Notes                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IScrollProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iscrollprovider) | Depends       | The document control can span larger than that span of the viewport. The control should support the [Scroll](uiauto-implementingscroll.md) control pattern if the content is scrollable.                                                                                                                              |
| [**ITextProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itextprovider)     | Required      | All document controls must support the [Text](uiauto-implementingtextandtextrange.md) control pattern.                                                                                                                                                                                                                |
| [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider)   | Depends       | While UI Automation clients can use [**IUIAutomationTextPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtextpattern) to obtain text information about a document, they need the [Value](uiauto-implementingvalue.md) control pattern to set the inner value. Simple text entry is possible only through the Value control pattern. |



 

## Required Events

The following table lists the UI Automation events that document controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                        | Notes                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                                           |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event.                      |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                      | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                  | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                                       |                                                                                                                            |
| [**UIA\_ScrollHorizontallyScrollablePropertyId**](uiauto-control-pattern-propids.md) property-changed event.   | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollHorizontalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property-changed event. | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollHorizontalViewSizePropertyId**](uiauto-control-pattern-propids.md) property-changed event.           | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollVerticallyScrollablePropertyId**](uiauto-control-pattern-propids.md) property-changed event.       | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollVerticalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property-changed event.     | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollVerticalViewSizePropertyId**](uiauto-control-pattern-propids.md) property-changed event.               | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_Selection\_InvalidatedEventId**](uiauto-event-ids.md)                                                            | If the control supports the [Selection](uiauto-implementingselection.md) control pattern, it must support this event.     |
| [**UIA\_Text\_TextSelectionChangedEventId**](uiauto-event-ids.md)                                                    |                                                                                                                            |
| [**UIA\_Text\_TextChangedEventId**](uiauto-event-ids.md)                                                                      |                                                                                                                            |
| [**UIA\_ValueValuePropertyId**](uiauto-control-pattern-propids.md) property-changed event.                                       | If the control supports the [Value](uiauto-implementingvalue.md) control pattern, it must support this event.             |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




