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
ms.topic: article
ms.date: 05/31/2018
---

# SelectionItem Control Pattern

Describes guidelines and conventions for implementing [**ISelectionItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider), including information about properties, methods, and events. The **SelectionItem** control pattern is used to support controls that act as individual, selectable child items of container controls that implement [**ISelectionProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionprovider).

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **ISelectionItemProvider**](#required-members-for-iselectionitemprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **SelectionItem** control pattern, note the following guidelines and conventions:

-   Single-selection controls that manage child controls that implement [**IRawElementProviderFragmentRoot**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragmentroot), such as the **Screen Resolution** slider in the **Display Properties** dialog for Windows, should implement [**ISelectionProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionprovider); their children should implement both [**IRawElementProviderFragment**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragment) and [**ISelectionItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider).

## Required Members for **ISelectionItemProvider**

The following properties, methods, and events are required for implementing the [**ISelectionItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider) interface.



| Required members                                                                                                                        | Member type | Notes |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------|-------|
| [**AddToSelection**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-addtoselection)                                                                  | Method      | None  |
| [**IsSelected**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-get_isselected)                                                                          | Property    | None  |
| [**RemoveFromSelection**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-removefromselection)                                                        | Method      | None  |
| [**Select**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-select)                                                                                  | Method      | None  |
| [**SelectionContainer**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-get_selectioncontainer)                                                          | Property    | None  |
| [**UIA\_SelectionItem\_ElementAddedToSelectionEventId**](uiauto-event-ids.md)         | Event       | None  |
| [**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md) | Event       | None  |
| [**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md)                         | Event       | None  |



 

If the result of a [**Select**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-select), an [**AddToSelection**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-addtoselection), or a [**RemoveFromSelection**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationselectionitempattern-removefromselection) is a single selected item, an **ElementSelected** event ([**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md)) should be raised; otherwise raise **ElementAddedToSelection** ([**UIA\_SelectionItem\_ElementAddedToSelectionEventId**](uiauto-event-ids.md)) or **ElementRemovedFromSelection** ([**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md)) events as appropriate.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




