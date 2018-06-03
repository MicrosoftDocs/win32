---
title: HeaderItem Control Type
description: This topic provides information about Microsoft UI Automation support for the HeaderItem control type.
ms.assetid: c70420d6-d9f3-47c8-a09f-35ed170f815f
keywords:
- UI Automation,support for HeaderItem control type
- UI Automation,HeaderItem control type
- UI Automation,tree structure for HeaderItem control type
- UI Automation,properties for HeaderItem control type
- UI Automation,control patterns for HeaderItem control type
- UI Automation,events for HeaderItem control type
- tree structures,HeaderItem control type
- properties,HeaderItem control type
- control patterns,HeaderItem control type
- events,HeaderItem control type
- support for HeaderItem control type
- HeaderItem control type
- control types,tree structure for HeaderItem control type
- control types,control patterns for HeaderItem control type
- control types,support for HeaderItem
- control types,HeaderItem
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HeaderItem Control Type

This topic provides information about Microsoft UI Automation support for the **HeaderItem** control type.

The **HeaderItem** control type provides a visual label for a row or column of information.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **HeaderItem** control type. The UI Automation requirements apply to all header item controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to header item controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Control View</th>
<th>Content View</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li>HeaderItem</li>
</ul></td>
<td>(Not applicable)</td>
</tr>
</tbody>
</table>



 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **HeaderItem** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value          | Notes                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](https://www.bing.com/search?q=**UIA\_AutomationIdPropertyId**)                 | See notes.     | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                         |
| [**UIA\_BoundingRectanglePropertyId**](https://www.bing.com/search?q=**UIA\_BoundingRectanglePropertyId**)       | See notes.     | The outermost rectangle that contains the whole control.                                                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](https://www.bing.com/search?q=**UIA\_ClickablePointPropertyId**)             | See notes.     | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point. |
| [**UIA\_ControlTypePropertyId**](https://www.bing.com/search?q=**UIA\_ControlTypePropertyId**)                   | **HeaderItem** | This value is the same for all UI frameworks.                                                                                                                                                        |
| [**UIA\_IsContentElementPropertyId**](https://www.bing.com/search?q=**UIA\_IsContentElementPropertyId**)         | FALSE          | The header item control is not included in the content view of the UI Automation tree.                                                                                                               |
| [**UIA\_IsControlElementPropertyId**](https://www.bing.com/search?q=**UIA\_IsControlElementPropertyId**)         | TRUE           | The header item control is always included in the control view of the UI Automation tree.                                                                                                            |
| [**UIA\_IsKeyboardFocusablePropertyId**](https://www.bing.com/search?q=**UIA\_IsKeyboardFocusablePropertyId**)   | See notes.     | If the control can receive keyboard focus, it must support this property.                                                                                                                            |
| [**UIA\_ItemStatusPropertyId**](https://www.bing.com/search?q=**UIA\_ItemStatusPropertyId**)                     | See notes      | This property provides information for sort orders by the header item.                                                                                                                               |
| [**UIA\_LabeledByPropertyId**](https://www.bing.com/search?q=**UIA\_LabeledByPropertyId**)                       | NULL           | Header item controls do not have a static text label.                                                                                                                                                |
| [**UIA\_LocalizedControlTypePropertyId**](https://www.bing.com/search?q=**UIA\_LocalizedControlTypePropertyId**) | See notes.     | Localized string corresponding to the **HeaderItem** control type. The default value is "header item" for en-US or English (United States).                                                          |
| [**UIA\_NamePropertyId**](https://www.bing.com/search?q=**UIA\_NamePropertyId**)                                 | See notes.     | The header item control is always self-labeling.                                                                                                                                                     |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all header item controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                         | Support | Notes                                                                                                                             |
|---------------------------------------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider)       | Depends | Implement the [Invoke](uiauto-implementinginvoke.md) control pattern if the header item control can be clicked to sort the data. |
| [**ITransformProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itransformprovider) | Depends | Implement the [Transform](uiauto-implementingtransform.md) control pattern if the header item control can be resized.            |



 

## Required Events

The following table lists the UI Automation events that header item controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](https://www.bing.com/search?q=**UIA\_AutomationFocusChangedEventId**)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](https://www.bing.com/search?q=**UIA\_BoundingRectanglePropertyId**) property-changed event. |                                                                                                                            |
| [**UIA\_Invoke\_InvokedEventId**](https://www.bing.com/search?q=**UIA\_Invoke\_InvokedEventId**)                                                     | If the control supports the [Invoke](uiauto-implementinginvoke.md) control pattern, it must support this event.           |
| [**UIA\_IsEnabledPropertyId**](https://www.bing.com/search?q=**UIA\_IsEnabledPropertyId**) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](https://www.bing.com/search?q=**UIA\_IsOffscreenPropertyId**) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_StructureChangedEventId**](https://www.bing.com/search?q=**UIA\_StructureChangedEventId**)                                                  |                                                                                                                            |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




