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
ms.topic: article
ms.date: 05/31/2018
---

# SemanticZoom Control Type

This topic provides information about UI Automation support for the **SemanticZoom** control type.

Semantic Zoom is a technique introduced in Windows 8 for presenting and navigating large sets of related data or content within a single view, such as a photo album, app list, or address book. Semantic Zoom uses two distinct modes of classification, or *zoom levels*, for organizing and presenting the content. The low-level (or *zoomed in*) mode displays items in a flat, "all-up" structure; and the high-level (or *zoomed out*) mode displays items in groups, enabling the user to quickly navigate and browse through the content. For example, zooming a list of cities might change to a list of states containing those cities. Zooming a list of programs might change to a list of logical program groups.

For more information about Semantic Zoom specifically as used for Windows Store apps, see [Guidelines for Semantic Zoom](/windows/uwp/controls-and-patterns/semantic-zoom).

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




| Control View | Content View | 
|--------------|--------------|
| <ul><li>List<ul><li>[SemanticZoom]<ul><li>ListItem (0 or more)</li></ul></li></ul></li></ul> | <ul><li>List<ul><li>ListItem (0 or more)</li></ul></li></ul> | 




 

Or:




| Control View | Content View | 
|--------------|--------------|
| <ul><li>[SemanticZoom]<ul><li>List<ul><li>ListItem (0 or more)</li></ul></li></ul></li></ul> | <ul><li>List<ul><li>ListItem (0 or more)</li></ul></li></ul> | 




 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the controls that implement the **SemanticZoom** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).




| UI Automation Property | Value | Notes | 
|------------------------|-------|-------|
| <a href="uiauto-automation-element-propids.md"><strong>UIA_AutomationIdPropertyId</strong></a> | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree. | 
| <a href="uiauto-automation-element-propids.md"><strong>UIA_BoundingRectanglePropertyId</strong></a> | See notes. | The outermost rectangle that contains the whole control. | 
| <a href="uiauto-automation-element-propids.md"><strong>UIA_ClickablePointPropertyId</strong></a> | See notes. | If the list control has a clickable point (a point that can be clicked to cause the list to take focus), that point must be exposed through this property. If the value of the <a href="uiauto-automation-element-propids.md"><strong>UIA_IsOffscreenPropertyId</strong></a> property is <strong>TRUE</strong>, attempting to retrieve this property results in the <a href="uiauto-error-codes.md"><strong>UIA_E_NOCLICKABLEPOINT</strong></a> error. | 
| <a href="uiauto-automation-element-propids.md"><strong>UIA_ControlTypePropertyId</strong></a> | <strong>SemanticZoom</strong> | 
| <a href="uiauto-automation-element-propids.md"><strong>UIA_IsContentElementPropertyId</strong></a> | TRUE | 
| <a href="uiauto-automation-element-propids.md"><strong>UIA_IsControlElementPropertyId</strong></a> | TRUE | 
| <a href="uiauto-automation-element-propids.md"><strong>UIA_IsKeyboardFocusablePropertyId</strong></a> | FALSE | 
| <a href="uiauto-automation-element-propids.md"><strong>UIA_LabeledByPropertyId</strong></a> | See notes. | If there is a static text label, this property must expose a reference to that control. | 
| <a href="uiauto-automation-element-propids.md"><strong>UIA_LocalizedControlTypePropertyId</strong></a> | See notes. | A localized string corresponding to the <strong>SemanticZoom</strong> control type. The default value is "semantic zoom" for en-US or English (United States).<blockquote>[!Note]<br />Some frameworks concatenated this as "semanticzoom".</blockquote><br /> | 
| <a href="uiauto-automation-element-propids.md"><strong>UIA_NamePropertyId</strong></a> | See notes. | An empty string is acceptable, or a more useful name could be provided, as long as it does not contain the term  semantic zoom , which would make the combination of control type and name confusing. | 




 

## Required Control Patterns and Properties

The following table lists the UI Automation control patterns required to be supported by all Semantic Zoom controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                  | Support/Value | Notes                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider) | Depends       | Semantic Zoom controls support the [Toggle](uiauto-implementingtoggle.md) control pattern to allow the zoom to be enabled or disabled. [**ToggleState\_Off**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-togglestate) corresponds to the flat, all-up state, and [**ToggleState\_On**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-togglestate) corresponds to the high level, zoomed-out view. |



 

## Required Events

The following table lists the UI Automation events that Semantic Zoom controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md) property-changed event.    |                                                                                                                            |



 

## Remarks

If a UI has a visible button to toggle Semantic Zoom control behavior, this button should not have a **SemanticZoom** control type. This is counter-intuitive, but the **SemanticZoom** control type characterizes the container of the zooming content, not a button that controls the zoom. (Such a button could be represented simply as a [Button](uiauto-supportbuttoncontroltype.md) control type with the [Toggle](uiauto-implementingtoggle.md) control pattern.)

## Related topics

<dl> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

