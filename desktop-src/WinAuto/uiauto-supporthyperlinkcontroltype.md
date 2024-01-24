---
title: Hyperlink Control Type
description: This topic provides information about Microsoft UI Automation support for the Hyperlink control type.
ms.assetid: 6dd16ae6-eff0-4913-8916-5092aec34f1f
keywords:
- UI Automation,support for Hyperlink control type
- UI Automation,Hyperlink control type
- UI Automation,tree structure for Hyperlink control type
- UI Automation,properties for Hyperlink control type
- UI Automation,control patterns for Hyperlink control type
- UI Automation,events for Hyperlink control type
- tree structures,Hyperlink control type
- properties,Hyperlink control type
- control patterns,Hyperlink control type
- events,Hyperlink control type
- support for Hyperlink control type
- Hyperlink control type
- control types,tree structure for Hyperlink control type
- control types,control patterns for Hyperlink control type
- control types,support for Hyperlink
- control types,Hyperlink
ms.topic: article
ms.date: 05/31/2018
---

# Hyperlink Control Type

This topic provides information about Microsoft UI Automation support for the **Hyperlink** control type.

Hyperlink controls create links that enable users to navigate within the same page, or from one page to another.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Hyperlink** control type. The UI Automation requirements apply to all hyperlink controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Remarks](#remarks)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to hyperlink controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Hyperlink</li></ul> | <ul><li>Hyperlink</li></ul> | 




 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the hyperlink controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value         | Notes                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.    | The value of this property must be unique across all controls in an application.                                                         |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.    | The outermost rectangle that contains the whole control.                                                                                 |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.    | The hyperlink control's clickable point must be a point that launches the hyperlink if clicked with a mouse pointer.                     |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Hyperlink** |                                                                                                                                          |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE          | The hyperlink control is always included in the content view of the UI Automation tree.                                                  |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE          | The hyperlink control is always included in the control view of the UI Automation tree.                                                  |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.    | If the control can receive keyboard focus, it must support this property.                                                                |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | See notes.    | If there is a static text label, this property must expose a reference to that control.                                                  |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.    | Localized string corresponding to the **Hyperlink** control type. The default value is "hyperlink" for en-US or English (United States). |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.    | The hyperlink control's name is the text that is displayed on the screen as underlined.                                                  |



 

## Required Control Patterns

The following table lists the UI Automation control patterns that hyperlink controls are required to support. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                  | Support/Value                | Notes                                                                                                                                                                                                                                                  |
|---------------------------------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider) | Required                     | All hyperlink controls must support the [Invoke](uiauto-implementinginvoke.md) control pattern.                                                                                                                                                       |
| [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider)   | Depends                      | Hyperlink controls should support the [Value](uiauto-implementingvalue.md) control pattern when the link contains information that is usable and meaningful to the user.                                                                              |
| [**Value**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivalueprovider-get_value)      | For example, "https://www..." | A URL for an Internet or intranet address is an example of a hyperlink that contains information that is meaningful to the user. A programmatic link, however, is meaningful only to an application and is not recommended for the **Value** property. |



 

## Required Events

The following table lists the UI Automation events that hyperlink controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_Invoke\_InvokedEventId**](uiauto-event-ids.md)                                                     |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                  |                                                                                                                            |



 

## Remarks

The Hyperlink control type should be applied only to an object that, when clicked, causes navigation to occur; it should not be applied to the container of the hyperlink. For example, only the clickable "hot spots" inside an image map should have the **Hyperlink** control type. The same is true of hyperlinks in a text field or document container. In this case, only the hyperlink text or image should have the **Hyperlink** control type, not the container.

The [Text](uiauto-implementingtextandtextrange.md) control pattern is ideal for supporting embedded hyperlinks in text or document elements.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




