---
title: MultipleView Control Pattern
description: Describes guidelines and conventions for implementing IMultipleViewProvider, including information about properties and methods.
ms.assetid: c67e7e4f-d2c7-4fca-8e8a-9b6565afa4ed
keywords:
- UI Automation,implementing MultipleView control pattern
- UI Automation,MultipleView control pattern
- UI Automation,IMultipleViewProvider
- IMultipleViewProvider
- implementing UI Automation MultipleView control patterns
- MultipleView control patterns
- control patterns,IMultipleViewProvider
- control patterns,implementing UI Automation MultipleView
- control patterns,MultipleView
- interfaces,IMultipleViewProvider
ms.topic: article
ms.date: 05/31/2018
---

# MultipleView Control Pattern

Describes guidelines and conventions for implementing [**IMultipleViewProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-imultipleviewprovider), including information about properties and methods. Links to additional references are listed at the end of the topic. The **MultipleView** control pattern is used to support controls that provide, and are able to switch between, multiple representations of the same information or the same set of child controls.

Examples of controls that can present multiple views include the list view (which can show its contents as thumbnails, tiles, icons, or details), Microsoft Excel charts (pie, line, bar, cell value with a formula), Microsoft Word documents (normal, web layout, print layout, reading layout, outline), Microsoft Outlook calendar (year, month, week, day), and Microsoft Windows Media Player skins. The supported views are determined by the control developer and are specific to each control.

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IMultipleViewProvider**](#required-members-for-imultipleviewprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **MultipleView** control pattern, note the following guidelines and conventions:

-   [**IMultipleViewProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-imultipleviewprovider) should also be implemented on a container that manages the current view if it is different from a control that provides the current view. For example, Windows Explorer contains a list control for the current folder content while the view for the control is managed from the Windows Explorer application.
-   A control that is able to sort its content is not considered to support multiple views.
-   The collection of views must be identical across instances.
-   View names must be suitable for use in text to speech, Braille, and other human-readable applications.

## Required Members for **IMultipleViewProvider**

The following properties and methods are required for implementing the [**IMultipleViewProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-imultipleviewprovider) interface.



| Required members                                                            | Member type | Notes |
|-----------------------------------------------------------------------------|-------------|-------|
| [**CurrentView**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-imultipleviewprovider-get_currentview)             | Property    | None  |
| [**GetSupportedViews**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-imultipleviewprovider-getsupportedviews) | Method      | None  |
| [**GetViewName**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-imultipleviewprovider-getviewname)             | Method      | None  |
| [**SetCurrentView**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-imultipleviewprovider-setcurrentview)       | Method      | None  |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> <dt>

[ExpandCollapse Control Pattern](uiauto-implementingexpandcollapse.md)
</dt> </dl>

 

 




