---
title: SelectionItem Control Pattern
description: Describes guidelines and conventions for implementing ISelectionItemProvider, including information about properties, methods, and events.
ms.assetid: '9314547f-7062-42db-b6a7-8a8eaef21d4e'
keywords: ["UI Automation,implementing SelectionItem control pattern", "UI Automation,SelectionItem control pattern", "UI Automation,ISelectionItemProvider", "ISelectionItemProvider", "implementing UI Automation SelectionItem control patterns", "SelectionItem control patterns", "control patterns,ISelectionItemProvider", "control patterns,implementing UI Automation SelectionItem", "control patterns,SelectionItem", "interfaces,ISelectionItemProvider"]
---

# SelectionItem Control Pattern

Describes guidelines and conventions for implementing [**ISelectionItemProvider**](uiauto-iselectionitemprovider.md), including information about properties, methods, and events. The **SelectionItem** control pattern is used to support controls that act as individual, selectable child items of container controls that implement [**ISelectionProvider**](uiauto-iselectionprovider.md).

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **ISelectionItemProvider**](#required-members-for-iselectionitemprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **SelectionItem** control pattern, note the following guidelines and conventions:

-   Single-selection controls that manage child controls that implement [**IRawElementProviderFragmentRoot**](uiauto-irawelementproviderfragmentroot.md), such as the **Screen Resolution** slider in the **Display Properties** dialog for Windows, should implement [**ISelectionProvider**](uiauto-iselectionprovider.md); their children should implement both [**IRawElementProviderFragment**](uiauto-irawelementproviderfragment.md) and [**ISelectionItemProvider**](uiauto-iselectionitemprovider.md).

## Required Members for **ISelectionItemProvider**

The following properties, methods, and events are required for implementing the [**ISelectionItemProvider**](uiauto-iselectionitemprovider.md) interface.



| Required members                                                                                                                        | Member type | Notes |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------|-------|
| [**AddToSelection**](uiauto-iselectionitemprovider-addtoselection.md)                                                                  | Method      | None  |
| [**IsSelected**](uiauto-iselectionitemprovider-isselected.md)                                                                          | Property    | None  |
| [**RemoveFromSelection**](uiauto-iselectionitemprovider-removefromselection.md)                                                        | Method      | None  |
| [**Select**](uiauto-iselectionitemprovider-select.md)                                                                                  | Method      | None  |
| [**SelectionContainer**](uiauto-iselectionitemprovider-selectioncontainer.md)                                                          | Property    | None  |
| [**UIA\_SelectionItem\_ElementAddedToSelectionEventId**](uiauto-event-ids.md#uia-selectionitem-elementaddedtoselectioneventid)         | Event       | None  |
| [**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md#uia-selectionitem-elementremovedfromselectioneventid) | Event       | None  |
| [**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md#uia-selectionitem-elementselectedeventid)                         | Event       | None  |



 

If the result of a [**Select**](uiauto-iuiautomationselectionitempattern-select.md), an [**AddToSelection**](uiauto-iuiautomationselectionitempattern-addtoselection.md), or a [**RemoveFromSelection**](uiauto-iuiautomationselectionitempattern-removefromselection.md) is a single selected item, an **ElementSelected** event ([**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md#uia-selectionitem-elementselectedeventid)) should be raised; otherwise raise **ElementAddedToSelection** ([**UIA\_SelectionItem\_ElementAddedToSelectionEventId**](uiauto-event-ids.md#uia-selectionitem-elementaddedtoselectioneventid)) or **ElementRemovedFromSelection** ([**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md#uia-selectionitem-elementremovedfromselectioneventid)) events as appropriate.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




