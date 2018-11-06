---
title: LegacyIAccessible Control Pattern
description: Describes guidelines and conventions for using ILegacyIAccessibleProvider, including information about properties, methods, and events.
ms.assetid: 4d66b9b8-ddbe-4bbc-b475-72dad1fe9393
keywords:
- UI Automation,implementing LegacyIAccessible control pattern
- UI Automation,LegacyIAccessible control pattern
- UI Automation,ILegacyIAccessibleProvider
- ILegacyIAccessibleProvider
- implementing UI Automation LegacyIAccessible control patterns
- LegacyIAccessible control patterns
- control patterns,ILegacyIAccessibleProvider
- control patterns,implementing UI Automation LegacyIAccessible
- control patterns,LegacyIAccessible
- interfaces,ILegacyIAccessibleProvider
ms.topic: article
ms.date: 05/31/2018
---

# LegacyIAccessible Control Pattern

Describes guidelines and conventions for using [**ILegacyIAccessibleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ilegacyiaccessibleprovider), including information about properties, methods, and events. The **LegacyIAccessible** control pattern is supported by the Microsoft Active Accessibility to Microsoft UI Automation Proxy.

Application and control providers never implement the [**ILegacyIAccessibleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ilegacyiaccessibleprovider) interface.

The **LegacyIAccessible** control pattern exposes the [**IUIAutomationLegacyIAccessiblePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationlegacyiaccessiblepattern) interface to UI Automation clients, enabling them to access the underlying [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) implementation for certain UI elements. However, **IUIAutomationLegacyIAccessiblePattern** does not support methods that are obsolete or that are redundant with the UI Automation features.

This topic contains the following sections:

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Members of the **LegacyIAccessible** Control Pattern](#members-of-the-legacyiaccessible-control-pattern)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

No application or control implements [**ILegacyIAccessibleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ilegacyiaccessibleprovider). The UI Automation framework automatically supplies the provider implementation for a native Microsoft Active Accessibility server.

The **LegacyIAccessible** control pattern is not available for controls based on UI Automation.

## Members of the **LegacyIAccessible** Control Pattern

The following properties, methods, and events are members of the **LegacyIAccessible** control pattern. The notes are for UI Automation clients.



| Members                                                                        | Member type | Notes                                                                                                                                |
|--------------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**ChildId**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_childid)                   | Property    | Returns **CHILDID\_SELF** (0) for a non-child object.                                                                                |
| [**DefaultAction**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_defaultaction)       | Property    | None                                                                                                                                 |
| [**Description**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_description)           | Property    | None                                                                                                                                 |
| [**Help**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_help)                         | Property    | None                                                                                                                                 |
| [**KeyboardShortcut**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_keyboardshortcut) | Property    | None                                                                                                                                 |
| [**Name**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_name)                         | Property    | None                                                                                                                                 |
| [**Role**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_role)                         | Property    | Use the [**GetRoleText**](/windows/desktop/api/Oleacc/nf-oleacc-getroletexta) function to retrieve localized string.                                                    |
| [**GetSelection**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-getselection)         | Method      | Retrieves an [**IUIAutomationElementArray**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelementarray) interface pointer.                                |
| [**State**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_state)                       | Property    | Use the [**GetStateText**](/windows/desktop/api/Oleacc/nf-oleacc-getstatetexta) function to retrieve localized string.                                                  |
| [**Value**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_value)                       | Property    | None                                                                                                                                 |
| [**DoDefaultAction**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-dodefaultaction)   | Method      | None                                                                                                                                 |
| [**GetIAccessible**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-getiaccessible)     | Method      | None                                                                                                                                 |
| [**Select**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-select)                     | Method      | The selection flag is a Microsoft Active Accessibility**SELFLAG** value. For more information, see [SELFLAG Constants](selflag.md). |
| [**SetValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-setvalue)                 | Method      | None                                                                                                                                 |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




