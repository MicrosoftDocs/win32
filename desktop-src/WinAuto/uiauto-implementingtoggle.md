---
title: Toggle Control Pattern
description: Describes guidelines and conventions for implementing IToggleProvider, including information about properties and methods. The Toggle control pattern is used to support controls that can cycle through a set of states and maintain a state once set.
ms.assetid: 9fd1232b-199a-41e6-81b0-667c7e463d09
keywords:
- UI Automation,implementing Toggle control pattern
- UI Automation,Toggle control pattern
- UI Automation,IToggleProvider
- IToggleProvider
- implementing UI Automation Toggle control patterns
- Toggle control patterns
- control patterns,IToggleProvider
- control patterns,implementing UI Automation Toggle
- control patterns,Toggle
- interfaces,IToggleProvider
ms.topic: article
ms.date: 05/31/2018
---

# Toggle Control Pattern

Describes guidelines and conventions for implementing [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider), including information about properties and methods. The **Toggle** control pattern is used to support controls that can cycle through a set of states and maintain a state once set.

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IToggleProvider**](#required-members-for-itoggleprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **Toggle** control pattern, note the following guidelines and conventions:

-   Controls that do not maintain state when activated, such as buttons, toolbar buttons, and hyperlinks, must implement [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider) instead.
-   A control must cycle through its toggle states ([**ToggleState**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-togglestate)) in the following order: **ToggleState\_On**, **ToggleState\_Off** and, if supported, **ToggleState\_Indeterminate**.
-   **Toggle** does not provide a set-state method because of issues surrounding the direct setting of a three-state check box without cycling through its appropriate [**ToggleState**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-togglestate) sequence.
-   The radio button control does not implement [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider), because it is not capable of cycling through its valid states.

## Required Members for **IToggleProvider**

The following properties and methods are required for implementing the [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider) interface.



| Required members                                          | Member type | Notes |
|-----------------------------------------------------------|-------------|-------|
| [**Toggle**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itoggleprovider-toggle)           | Method      | None  |
| [**ToggleState**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itoggleprovider-get_togglestate) | Property    | None  |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




