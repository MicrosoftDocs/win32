---
title: ToolTip Control Type
description: This topic provides information about Microsoft UI Automation support for the ToolTip control type. Tooltip controls are pop-up windows that contain text.
ms.assetid: 810f85a9-4d3b-4ceb-bd2c-bf70e8712ae2
keywords:
- UI Automation,support for ToolTip control type
- UI Automation,ToolTip control type
- UI Automation,tree structure for ToolTip control type
- UI Automation,properties for ToolTip control type
- UI Automation,control patterns for ToolTip control type
- UI Automation,events for ToolTip control type
- tree structures,ToolTip control type
- properties,ToolTip control type
- control patterns,ToolTip control type
- events,ToolTip control type
- support for ToolTip control type
- ToolTip control type
- control types,tree structure for ToolTip control type
- control types,control patterns for ToolTip control type
- control types,support for ToolTip
- control types,ToolTip
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ToolTip Control Type

This topic provides information about Microsoft UI Automation support for the **ToolTip** control type. Tooltip controls are pop-up windows that contain text.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **ToolTip** control type. The UI Automation requirements apply to all tooltip controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to tooltip controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).



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
<li>ToolTip
<ul>
<li>Text (0 or more)</li>
<li>Image (0 or more)</li>
</ul></li>
</ul></td>
<td><ul>
<li>ToolTip</li>
</ul></td>
</tr>
</tbody>
</table>



 

Tooltip controls appear only in the content view of the UI Automation tree if they can receive keyboard focus. Otherwise, all of the tooltip's information is available from the [**IUIAutomationElement::CurrentHelpText**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currenthelptext) (or [**CachedHelpText**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_cachedhelptext)) property on the element that the tooltip is referring to.

Tooltips should appear beneath the control to which their information is referring. Clients must listen for the [**UIA\_ToolTipOpenedEventId**](uiauto-event-ids.md#uia-tooltipopenedeventid) to ensure that they consistently obtain information contained in tooltips.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **ToolTip** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value       | Notes                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md#uia-automationidpropertyid)                 | See notes.  | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                                                                                                                   |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid)       | See notes.  | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                                                                                                       |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md#uia-clickablepointpropertyid)             | See notes.  | The clickable point should be the part of the tooltip that dismisses the control. Some tooltips do not have this ability and will not have a clickable point.                                                                                                                                                                                                  |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md#uia-controltypepropertyid)                   | **ToolTip** |                                                                                                                                                                                                                                                                                                                                                                |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontentelementpropertyid)         | Depends     | If the tooltip control can receive keyboard focus, it must appear in the content view of the tree. If it is text only, it is available as the [**IUIAutomationElement::CurrentHelpText**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currenthelptext) (or [**CachedHelpText**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_cachedhelptext)) property from the control that raised it. |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontrolelementpropertyid)         | True        | The tooltip control is always included in the control view of the UI Automation tree.                                                                                                                                                                                                                                                                          |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md#uia-iskeyboardfocusablepropertyid)   | See notes.  | If the control can receive keyboard focus, it must support this property.                                                                                                                                                                                                                                                                                      |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md#uia-labeledbypropertyid)                       | NULL        | Tooltip controls are always self-labeled by their contents.                                                                                                                                                                                                                                                                                                    |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md#uia-localizedcontroltypepropertyid) | See notes.  | Localized string corresponding to the ToolTip control type. The default value is "tooltip" for en-US or English (United States).                                                                                                                                                                                                                               |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md#uia-namepropertyid)                                 | See notes.  | The name of the tooltip control is the text that is displayed within the tooltip.                                                                                                                                                                                                                                                                              |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by tooltip controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                   | Support | Notes                                                                                                                                                                                                                                                                             |
|---------------------------------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ITextProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itextprovider)     | Depends | For better accessibility, a tooltip control can support the [Text](uiauto-implementingtextandtextrange.md) control pattern, although it is not required. The Text control pattern is useful when the text has rich style and attributes (for example, color, bold, and italics). |
| [**IWindowProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iwindowprovider) | Depends | Tooltips that can be closed by clicking a UI item must support the [Window](uiauto-implementingwindow.md) control pattern so that they can closed automatically.                                                                                                                 |



 

## Required Events

Tooltip controls must raise the [**UIA\_ToolTipOpenedEventId**](uiauto-event-ids.md#uia-tooltipopenedeventid) event when they appear on the screen. The event will include a reference to the UI Automation element of the tooltip itself.

The following table lists the UI Automation events that tooltip controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                            | Notes                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md#uia-automationfocuschangedeventid)                                               |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid) property-changed event.          |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md#uia-isenabledpropertyid) property-changed event.                          | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md#uia-isoffscreenpropertyid) property-changed event.                      | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md#uia-namepropertyid) property-changed event.                                    |                                                                                                                            |
| [**UIA\_Text\_TextChangedEventId**](uiauto-event-ids.md#uia-text-textchangedeventid)                                                          | If the control supports the [Text](uiauto-implementingtextandtextrange.md) control pattern, it must support this event.   |
| [**UIA\_ToolTipClosedEventId**](uiauto-event-ids.md#uia-tooltipclosedeventid)                                                                 |                                                                                                                            |
| [**UIA\_ToolTipOpenedEventId**](uiauto-event-ids.md#uia-tooltipopenedeventid)                                                                 |                                                                                                                            |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md#uia-structurechangedeventid)                                                           |                                                                                                                            |
| [**UIA\_Window\_WindowClosedEventId**](uiauto-event-ids.md#uia-window-windowclosedeventid)                                                    | If the control supports the [Window](uiauto-implementingwindow.md) control pattern, it must support this event.           |
| [**UIA\_Window\_WindowOpenedEventId**](uiauto-event-ids.md#uia-window-windowopenedeventid)                                                    | If the control supports the [Window](uiauto-implementingwindow.md) control pattern, it must support this event.           |
| [**UIA\_WindowWindowVisualStatePropertyId**](uiauto-control-pattern-propids.md#uia-windowwindowvisualstatepropertyid) property-changed event. | If the control supports the [Window](uiauto-implementingwindow.md) control pattern, it must support this event.           |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




