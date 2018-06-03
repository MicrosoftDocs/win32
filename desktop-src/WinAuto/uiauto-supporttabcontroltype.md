---
title: Tab Control Type
description: This topic provides information about Microsoft UI Automation support for the Tab control type.
ms.assetid: 49e3f025-f49b-44b1-90ca-09f40dce8f2a
keywords:
- UI Automation,support for Tab control type
- UI Automation,Tab control type
- UI Automation,tree structure for Tab control type
- UI Automation,properties for Tab control type
- UI Automation,control patterns for Tab control type
- UI Automation,events for Tab control type
- tree structures,Tab control type
- properties,Tab control type
- control patterns,Tab control type
- events,Tab control type
- support for Tab control type
- Tab control type
- control types,tree structure for Tab control type
- control types,control patterns for Tab control type
- control types,support for Tab
- control types,Tab
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Tab Control Type

This topic provides information about Microsoft UI Automation support for the **Tab** control type.

A tab control is analogous to the dividers in a notebook or the labels in a file cabinet. By using a tab control, an application can define multiple pages for the same area of a window or dialog box.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Tab** control type. The UI Automation requirements apply to all tab controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to tab controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).



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
<li>Tab
<ul>
<li>TabItem (1 or more)</li>
<li>ScrollBar (0 or 1)
<ul>
<li>Button (0 or 2)</li>
</ul></li>
</ul></li>
</ul></td>
<td><ul>
<li>Tab
<ul>
<li>TabItem (1 or more)</li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>



 

Tab controls have child UI Automation elements based on the [TabItem](uiauto-supporttabitemcontroltype.md) control type. When tab items are grouped (for example, as in Microsoft Office applications) the **Tab** control type can also host **Groups** control types for the grouped tab items, as the following tree structure shows.



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
<li>Tab
<ul>
<li>TabItem (1 or more)</li>
<li>Group (0 or more)
<ul>
<li>TabItem (0 or more)</li>
</ul></li>
<li>ScrollBar (0 or 1)
<ul>
<li>Button (0 or 2)</li>
</ul></li>
</ul></li>
</ul></td>
<td><ul>
<li>Tab
<ul>
<li>TabItem (1 or more)</li>
<li>Group (0 or more)
<ul>
<li>TabItem (0 or more)</li>
</ul></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>



 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to tab controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](https://www.bing.com/search?q=**UIA\_AutomationIdPropertyId**)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                                                                                                                                  |
| [**UIA\_BoundingRectanglePropertyId**](https://www.bing.com/search?q=**UIA\_BoundingRectanglePropertyId**)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                                                                                                                      |
| [**UIA\_ClickablePointPropertyId**](https://www.bing.com/search?q=**UIA\_ClickablePointPropertyId**)             | No         | The tab control does not have clickable points.                                                                                                                                                                                                                                                                                                                               |
| [**UIA\_ControlTypePropertyId**](https://www.bing.com/search?q=**UIA\_ControlTypePropertyId**)                   | **Tab**    |                                                                                                                                                                                                                                                                                                                                                                               |
| [**UIA\_IsContentElementPropertyId**](https://www.bing.com/search?q=**UIA\_IsContentElementPropertyId**)         | TRUE       | The tab control is always included in the content view of the UI Automation tree.                                                                                                                                                                                                                                                                                             |
| [**UIA\_IsControlElementPropertyId**](https://www.bing.com/search?q=**UIA\_IsControlElementPropertyId**)         | TRUE       | The tab control is always included in the control view of the UI Automation tree.                                                                                                                                                                                                                                                                                             |
| [**UIA\_IsKeyboardFocusablePropertyId**](https://www.bing.com/search?q=**UIA\_IsKeyboardFocusablePropertyId**)   | TRUE       | The Tab control type must be able to receive keyboard focus. Typically, a UI Automation client calls [**IUIAutomationElement::SetFocus**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-setfocus) on a tab control and one of its items will forward the keyboard focus to the tab control. It is possible for some tab containers to take focus without setting focus to one of its items. |
| [**UIA\_LabeledByPropertyId**](https://www.bing.com/search?q=**UIA\_LabeledByPropertyId**)                       | See notes. | Tab controls typically have a static text label that is exposed through this property.                                                                                                                                                                                                                                                                                        |
| [**UIA\_LocalizedControlTypePropertyId**](https://www.bing.com/search?q=**UIA\_LocalizedControlTypePropertyId**) | See notes. | Localized string corresponding to the **Tab** control type. The default value is "tab" for en-US or English (United States).                                                                                                                                                                                                                                                  |
| [**UIA\_NamePropertyId**](https://www.bing.com/search?q=**UIA\_NamePropertyId**)                                 | See notes. | The tab control rarely requires a **Name** property.                                                                                                                                                                                                                                                                                                                          |
| [**UIA\_OrientationPropertyId**](https://www.bing.com/search?q=**UIA\_OrientationPropertyId**)                   | See notes. | The tab control must always indicate whether it is positioned horizontally or vertically.                                                                                                                                                                                                                                                                                     |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all tab controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                                             | Support/Value | Notes                                                                                                                                                                  |
|------------------------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ISelectionProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionprovider)                      | Required      | All tab controls must support the [Selection](uiauto-implementingselection.md) control pattern.                                                                       |
| [**IsSelectionRequired**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionprovider-get_isselectionrequired) | TRUE          | Tab controls always require that a selection be made.                                                                                                                  |
| [**CanSelectMultiple**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionprovider-get_canselectmultiple)     | FALSE         | Tab controls are always single-selection containers.                                                                                                                   |
| [**IScrollProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iscrollprovider)                            | Depends       | The [Scroll](uiauto-implementingscroll.md) control pattern must be supported if the tab control has widgets that allow for a set of tab items to be scrolled through. |



 

## Required Events

The following table lists the UI Automation events that tab controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                        | Notes                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](https://www.bing.com/search?q=**UIA\_AutomationFocusChangedEventId**)                                                           |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](https://www.bing.com/search?q=**UIA\_BoundingRectanglePropertyId**) property-changed event.                      |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](https://www.bing.com/search?q=**UIA\_IsEnabledPropertyId**) property-changed event.                                      | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](https://www.bing.com/search?q=**UIA\_IsOffscreenPropertyId**) property-changed event.                                  | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_ScrollHorizontallyScrollablePropertyId**](https://www.bing.com/search?q=**UIA\_ScrollHorizontallyScrollablePropertyId**) property-changed event.   | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollHorizontalScrollPercentPropertyId**](https://www.bing.com/search?q=**UIA\_ScrollHorizontalScrollPercentPropertyId**) property-changed event. | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollHorizontalViewSizePropertyId**](https://www.bing.com/search?q=**UIA\_ScrollHorizontalViewSizePropertyId**) property-changed event.           | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollVerticallyScrollablePropertyId**](https://www.bing.com/search?q=**UIA\_ScrollVerticallyScrollablePropertyId**) property-changed event.       | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollVerticalScrollPercentPropertyId**](https://www.bing.com/search?q=**UIA\_ScrollVerticalScrollPercentPropertyId**) property-changed event.     | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_ScrollVerticalViewSizePropertyId**](https://www.bing.com/search?q=**UIA\_ScrollVerticalViewSizePropertyId**) property-changed event.               | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.           |
| [**UIA\_StructureChangedEventId**](https://www.bing.com/search?q=**UIA\_StructureChangedEventId**)                                                                       |                                                                                                                            |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




