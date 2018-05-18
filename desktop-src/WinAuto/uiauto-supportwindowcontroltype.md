---
title: Window Control Type
description: This topic provides information about Microsoft UI Automation support for the Window control type.
ms.assetid: '521fb514-e083-48b3-b4a0-52c530154740'
keywords: ["UI Automation,support for Window control type", "UI Automation,Window control type", "UI Automation,tree structure for Window control type", "UI Automation,properties for Window control type", "UI Automation,control patterns for Window control type", "UI Automation,events for Window control type", "tree structures,Window control type", "properties,Window control type", "control patterns,Window control type", "events,Window control type", "support for Window control type", "Window control type", "control types,tree structure for Window control type", "control types,control patterns for Window control type", "control types,support for Window", "control types,Window"]
---

# Window Control Type

This topic provides information about Microsoft UI Automation support for the **Window** control type.

The window control consists of the window frame, which contains child objects such as title bar, client, and other objects.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Window** control type. The UI Automation requirements apply to all window controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to window controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).



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
<li>Window</li>
</ul></td>
<td><ul>
<li>Window</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to window controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md#uia-automationidpropertyid)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md#uia-clickablepointpropertyid)             | See notes. | The window control must have a clickable point that causes the window to become selected or unselected.                                                 |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md#uia-controltypepropertyid)                   | **Window** | This value is the same for all UI frameworks.                                                                                                           |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontentelementpropertyid)         | TRUE       | The window control is always included in the content view of the UI Automation tree.                                                                    |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontrolelementpropertyid)         | TRUE       | The window control is always included in the control view of the UI Automation tree.                                                                    |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md#uia-iskeyboardfocusablepropertyid)   | See notes. | If the control can receive keyboard focus, it must support this property.                                                                               |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md#uia-labeledbypropertyid)                       | NULL       | Window controls do not have a static window label.                                                                                                      |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md#uia-localizedcontroltypepropertyid) | See notes. | Localized string corresponding to the **Window** control type. The default value is "window" for en-US or English (United States).                      |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md#uia-namepropertyid)                                 | See notes. | The window control always contains a primary window element that relates to what the user would associate as the most semantic identifier for the item. |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by window controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                        | Support/Value | Notes                                                                                                                                                                        |
|---------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDockProvider**](uiauto-idockprovider.md)           | Conditional   | The [Dock](uiauto-implementingdock.md) control pattern must be supported if the window can be docked.                                                                       |
| [**ITransformProvider**](uiauto-itransformprovider.md) | Required      | The [Transform](uiauto-implementingtransform.md) control pattern enables the window to be moved, resized, or rotated on the screen. (Does not apply to Windows Store apps.) |
| [**IWindowProvider**](uiauto-iwindowprovider.md)       | Required      | The [Window](uiauto-implementingwindow.md) control pattern enables specific operations for the window.                                                                      |



 

## Required Events

The following table lists the UI Automation events that **Window** controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                        | Notes                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AsyncContentLoadedEventId**](uiauto-event-ids.md#uia-asynccontentloadedeventid)                                                                   |                                                                                                                                                                                                                           |
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md#uia-automationfocuschangedeventid)                                                           |                                                                                                                                                                                                                           |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid) property-changed event.                      |                                                                                                                                                                                                                           |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md#uia-isenabledpropertyid) property-changed event.                                      | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.                                                                                                  |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md#uia-isoffscreenpropertyid) property-changed event.                                  | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event.                                                                                                |
| [**UIA\_LayoutInvalidatedEventId**](uiauto-event-ids.md#uia-layoutinvalidatedeventid)                                                                     |                                                                                                                                                                                                                           |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md#uia-namepropertyid) property-changed event.                                                |                                                                                                                                                                                                                           |
| [**UIA\_ScrollHorizontallyScrollablePropertyId**](uiauto-control-pattern-propids.md#uia-scrollhorizontallyscrollablepropertyid) property-changed event.   | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                                          |
| [**UIA\_ScrollHorizontalScrollPercentPropertyId**](uiauto-control-pattern-propids.md#uia-scrollhorizontalscrollpercentpropertyid) property-changed event. | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                                          |
| [**UIA\_ScrollHorizontalViewSizePropertyId**](uiauto-control-pattern-propids.md#uia-scrollhorizontalviewsizepropertyid) property-changed event.           | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                                          |
| [**UIA\_ScrollVerticallyScrollablePropertyId**](uiauto-control-pattern-propids.md#uia-scrollverticallyscrollablepropertyid) property-changed event.       | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                                          |
| [**UIA\_ScrollVerticalScrollPercentPropertyId**](uiauto-control-pattern-propids.md#uia-scrollverticalscrollpercentpropertyid) property-changed event.     | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                                          |
| [**UIA\_ScrollVerticalViewSizePropertyId**](uiauto-control-pattern-propids.md#uia-scrollverticalviewsizepropertyid) property-changed event.               | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                                          |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md#uia-structurechangedeventid)                                                                       |                                                                                                                                                                                                                           |
| [**UIA\_Window\_WindowClosedEventId**](uiauto-event-ids.md#uia-window-windowclosedeventid)                                                                |                                                                                                                                                                                                                           |
| [**UIA\_Window\_WindowOpenedEventId**](uiauto-event-ids.md#uia-window-windowopenedeventid)                                                                |                                                                                                                                                                                                                           |
| [**UIA\_WindowWindowVisualStatePropertyId**](uiauto-control-pattern-propids.md#uia-windowwindowvisualstatepropertyid) property-changed event.             | If the control supports the [**WindowVisualState**](uiauto-iuiautomationwindowpattern-cachedwindowvisualstate.md) property of the [Window](uiauto-implementingwindow.md) control pattern, this event must be supported. |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




