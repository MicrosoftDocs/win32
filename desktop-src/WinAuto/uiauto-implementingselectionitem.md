---
title: SelectionItem Control Pattern
description: Describes guidelines and conventions for implementing ISelectionItemProvider, including information about properties, methods, and events.
ms.assetid: 9314547f-7062-42db-b6a7-8a8eaef21d4e
keywords:
- UI Automation,implementing SelectionItem control pattern
- UI Automation,SelectionItem control pattern
- UI Automation,ISelectionItemProvider
- ISelectionItemProvider
- implementing UI Automation SelectionItem control patterns
- SelectionItem control patterns
- control patterns,ISelectionItemProvider
- control patterns,implementing UI Automation SelectionItem
- control patterns,SelectionItem
- interfaces,ISelectionItemProvider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SelectionItem Control Pattern

Describes guidelines and conventions for implementing [**ISelectionItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider?branch=master), including information about properties, methods, and events. The **SelectionItem** control pattern is used to support controls that act as individual, selectable child items of container controls that implement [**ISelectionProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionprovider?branch=master).

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **ISelectionItemProvider**](#required-members-for-iselectionitemprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **SelectionItem** control pattern, note the following guidelines and conventions:

-   Single-selection controls that manage child controls that implement [**IRawElementProviderFragmentRoot**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragmentroot?branch=master), such as the **Screen Resolution** slider in the **Display Properties** dialog for Windows, should implement [**ISelectionProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionprovider?branch=master); their children should implement both [**IRawElementProviderFragment**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragment?branch=master) and [**ISelectionItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider?branch=master).

## Required Members for **ISelectionItemProvider**

The following properties, methods, and events are required for implementing the [**ISelectionItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider?branch=master) interface.



| Required members                                                                                                                        | Member type | Notes |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------|-------|
| [**AddToSelection**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-addtoselection?branch=master)                                                                  | Method      | None  |
| [**IsSelected**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-get_isselected?branch=master)                                                                          | Property    | None  |
| [**RemoveFromSelection**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-removefromselection?branch=master)                                                        | Method      | None  |
| [**Select**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-select?branch=master)                                                                                  | Method      | None  |
| [**SelectionContainer**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-get_selectioncontainer?branch=master)                                                          | Property    | None  |
| [**UIA\_SelectionItem\_ElementAddedToSelectionEventId**](uiauto-event-ids.md#uia-selectionitem-elementaddedtoselectioneventid)         | Event       | None  |
| [**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md#uia-selectionitem-elementremovedfromselectioneventid) | Event       | None  |
| [**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md#uia-selectionitem-elementselectedeventid)                         | Event       | None  |



 

If the result of a [**Select**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-select?branch=master), an [**AddToSelection**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-addtoselection?branch=master), or a [**RemoveFromSelection**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-removefromselection?branch=master) is a single selected item, an **ElementSelected** event ([**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md#uia-selectionitem-elementselectedeventid)) should be raised; otherwise raise **ElementAddedToSelection** ([**UIA\_SelectionItem\_ElementAddedToSelectionEventId**](uiauto-event-ids.md#uia-selectionitem-elementaddedtoselectioneventid)) or **ElementRemovedFromSelection** ([**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md#uia-selectionitem-elementremovedfromselectioneventid)) events as appropriate.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




