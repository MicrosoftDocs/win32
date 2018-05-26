---
title: SemanticZoom Control Type
description: This topic provides information about UI Automation support for the SemanticZoom control type.
ms.assetid: 37C14610-431F-46BF-97B6-CB476EA1642D
keywords:
- UI Automation,support for SemanticZoom control type
- UI Automation,SemanticZoom control type
- UI Automation,tree structure for SemanticZoom control type
- UI Automation,properties for SemanticZoom control type
- UI Automation,control patterns for SemanticZoom control type
- UI Automation,events for SemanticZoom control type
- tree structures,SemanticZoom control type
- properties,SemanticZoom control type
- control patterns,SemanticZoom control type
- events,SemanticZoom control type
- support for SemanticZoom control type
- SemanticZoom control type
- control types,tree structure for SemanticZoom control type
- control types,control patterns for SemanticZoom control type
- control types,support for SemanticZoom
- control types,SemanticZoom
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SemanticZoom Control Type

This topic provides information about UI Automation support for the **SemanticZoom** control type.

Semantic Zoom is a technique introduced in Windows 8 for presenting and navigating large sets of related data or content within a single view, such as a photo album, app list, or address book. Semantic Zoom uses two distinct modes of classification, or *zoom levels*, for organizing and presenting the content. The low-level (or *zoomed in*) mode displays items in a flat, "all-up" structure; and the high-level (or *zoomed out*) mode displays items in groups, enabling the user to quickly navigate and browse through the content. For example, zooming a list of cities might change to a list of states containing those cities. Zooming a list of programs might change to a list of logical program groups.

For more information about Semantic Zoom specifically as used for Windows Store apps, see [Guidelines for Semantic Zoom](https://msdn.microsoft.com/library/windows/apps/hh465319).

The usage model for the **SemanticZoom** control type is unusual in that it exists mainly for programmatic access. Microsoft UI Automation clients can monitor and manipulate the Semantic Zoom control to control the zoomed-in state of the list. Users who are not using assistive technology would typically manipulate the Semantic Zoom control directly through touch gestures or keyboard shortcuts.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **SemanticZoom** control type. The UI Automation requirements apply to all Semantic Zoom controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns and Properties](#required-control-patterns-and-properties)
-   [Required Events](#required-events)
-   [Remarks](#remarks)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to the **SemanticZoom** control type and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).



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
<li>List
<ul>
<li>[SemanticZoom]
<ul>
<li>ListItem (0 or more)</li>
</ul></li>
</ul></li>
</ul></td>
<td><ul>
<li>List
<ul>
<li>ListItem (0 or more)</li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>



 

Or:



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
<li>[SemanticZoom]
<ul>
<li>List
<ul>
<li>ListItem (0 or more)</li>
</ul></li>
</ul></li>
</ul></td>
<td><ul>
<li>List
<ul>
<li>ListItem (0 or more)</li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>



 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the controls that implement the **SemanticZoom** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>UI Automation Property</th>
<th>Value</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>UIA_AutomationIdPropertyId</strong>](uiauto-automation-element-propids.md#uia-automationidpropertyid)</td>
<td>See notes.</td>
<td>The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.</td>
</tr>
<tr class="even">
<td>[<strong>UIA_BoundingRectanglePropertyId</strong>](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid)</td>
<td>See notes.</td>
<td>The outermost rectangle that contains the whole control.</td>
</tr>
<tr class="odd">
<td>[<strong>UIA_ClickablePointPropertyId</strong>](uiauto-automation-element-propids.md#uia-clickablepointpropertyid)</td>
<td>See notes.</td>
<td>If the list control has a clickable point (a point that can be clicked to cause the list to take focus), that point must be exposed through this property. If the value of the [<strong>UIA_IsOffscreenPropertyId</strong>](uiauto-automation-element-propids.md#uia-isoffscreenpropertyid) property is <strong>TRUE</strong>, attempting to retrieve this property results in the [<strong>UIA_E_NOCLICKABLEPOINT</strong>](uiauto-error-codes.md#uia-e-noclickablepoint) error.</td>
</tr>
<tr class="even">
<td>[<strong>UIA_ControlTypePropertyId</strong>](uiauto-automation-element-propids.md#uia-controltypepropertyid)</td>
<td><strong>SemanticZoom</strong></td>

</tr>
<tr class="odd">
<td>[<strong>UIA_IsContentElementPropertyId</strong>](uiauto-automation-element-propids.md#uia-iscontentelementpropertyid)</td>
<td>TRUE</td>

</tr>
<tr class="even">
<td>[<strong>UIA_IsControlElementPropertyId</strong>](uiauto-automation-element-propids.md#uia-iscontrolelementpropertyid)</td>
<td>TRUE</td>

</tr>
<tr class="odd">
<td>[<strong>UIA_IsKeyboardFocusablePropertyId</strong>](uiauto-automation-element-propids.md#uia-iskeyboardfocusablepropertyid)</td>
<td>FALSE</td>

</tr>
<tr class="even">
<td>[<strong>UIA_LabeledByPropertyId</strong>](uiauto-automation-element-propids.md#uia-labeledbypropertyid)</td>
<td>See notes.</td>
<td>If there is a static text label, this property must expose a reference to that control.</td>
</tr>
<tr class="odd">
<td>[<strong>UIA_LocalizedControlTypePropertyId</strong>](uiauto-automation-element-propids.md#uia-localizedcontroltypepropertyid)</td>
<td>See notes.</td>
<td>A localized string corresponding to the <strong>SemanticZoom</strong> control type. The default value is &quot;semantic zoom&quot; for en-US or English (United States).
<blockquote>
[!Note]<br />
Some frameworks concatenated this as &quot;semanticzoom&quot;.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>UIA_NamePropertyId</strong>](uiauto-automation-element-propids.md#uia-namepropertyid)</td>
<td>See notes.</td>
<td>An empty string is acceptable, or a more useful name could be provided, as long as it does not contain the term  semantic zoom , which would make the combination of control type and name confusing.</td>
</tr>
</tbody>
</table>



 

## Required Control Patterns and Properties

The following table lists the UI Automation control patterns required to be supported by all Semantic Zoom controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                  | Support/Value | Notes                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IToggleProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-itoggleprovider?branch=master) | Depends       | Semantic Zoom controls support the [Toggle](uiauto-implementingtoggle.md) control pattern to allow the zoom to be enabled or disabled. [**ToggleState\_Off**](uiauto-togglestate.md#togglestate-off) corresponds to the flat, all-up state, and [**ToggleState\_On**](uiauto-togglestate.md#togglestate-on) corresponds to the high level, zoomed-out view. |



 

## Required Events

The following table lists the UI Automation events that Semantic Zoom controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid) property-changed event. |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md#uia-isenabledpropertyid) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md#uia-isoffscreenpropertyid) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md#uia-toggletogglestatepropertyid) property-changed event.    |                                                                                                                            |



 

## Remarks

If a UI has a visible button to toggle Semantic Zoom control behavior, this button should not have a **SemanticZoom** control type. This is counter-intuitive, but the **SemanticZoom** control type characterizes the container of the zooming content, not a button that controls the zoom. (Such a button could be represented simply as a [Button](uiauto-supportbuttoncontroltype.md) control type with the [Toggle](uiauto-implementingtoggle.md) control pattern.)

## Related topics

<dl> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 





