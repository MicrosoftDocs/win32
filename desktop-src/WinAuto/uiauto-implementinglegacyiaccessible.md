---
title: LegacyIAccessible Control Pattern
description: Describes guidelines and conventions for using ILegacyIAccessibleProvider, including information about properties, methods, and events.
ms.assetid: '4d66b9b8-ddbe-4bbc-b475-72dad1fe9393'
keywords: ["UI Automation,implementing LegacyIAccessible control pattern", "UI Automation,LegacyIAccessible control pattern", "UI Automation,ILegacyIAccessibleProvider", "ILegacyIAccessibleProvider", "implementing UI Automation LegacyIAccessible control patterns", "LegacyIAccessible control patterns", "control patterns,ILegacyIAccessibleProvider", "control patterns,implementing UI Automation LegacyIAccessible", "control patterns,LegacyIAccessible", "interfaces,ILegacyIAccessibleProvider"]
---

# LegacyIAccessible Control Pattern

Describes guidelines and conventions for using [**ILegacyIAccessibleProvider**](uiauto-ilegacyiaccessibleprovider.md), including information about properties, methods, and events. The **LegacyIAccessible** control pattern is supported by the Microsoft Active Accessibility to Microsoft UI Automation Proxy.

Application and control providers never implement the [**ILegacyIAccessibleProvider**](uiauto-ilegacyiaccessibleprovider.md) interface.

The **LegacyIAccessible** control pattern exposes the [**IUIAutomationLegacyIAccessiblePattern**](uiauto-iuiautomationlegacyiaccessiblepattern.md) interface to UI Automation clients, enabling them to access the underlying [**IAccessible**](iaccessible.md) implementation for certain UI elements. However, **IUIAutomationLegacyIAccessiblePattern** does not support methods that are obsolete or that are redundant with the UI Automation features.

This topic contains the following sections:

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Members of the **LegacyIAccessible** Control Pattern](#members-of-the-legacyiaccessible-control-pattern)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

No application or control implements [**ILegacyIAccessibleProvider**](uiauto-ilegacyiaccessibleprovider.md). The UI Automation framework automatically supplies the provider implementation for a native Microsoft Active Accessibility server.

The **LegacyIAccessible** control pattern is not available for controls based on UI Automation.

## Members of the **LegacyIAccessible** Control Pattern

The following properties, methods, and events are members of the **LegacyIAccessible** control pattern. The notes are for UI Automation clients.



| Members                                                                        | Member type | Notes                                                                                                                                |
|--------------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**ChildId**](uiauto-ilegacyiaccessibleprovider-childid.md)                   | Property    | Returns **CHILDID\_SELF** (0) for a non-child object.                                                                                |
| [**DefaultAction**](uiauto-ilegacyiaccessibleprovider-defaultaction.md)       | Property    | None                                                                                                                                 |
| [**Description**](uiauto-ilegacyiaccessibleprovider-description.md)           | Property    | None                                                                                                                                 |
| [**Help**](uiauto-ilegacyiaccessibleprovider-help.md)                         | Property    | None                                                                                                                                 |
| [**KeyboardShortcut**](uiauto-ilegacyiaccessibleprovider-keyboardshortcut.md) | Property    | None                                                                                                                                 |
| [**Name**](uiauto-ilegacyiaccessibleprovider-name.md)                         | Property    | None                                                                                                                                 |
| [**Role**](uiauto-ilegacyiaccessibleprovider-role.md)                         | Property    | Use the [**GetRoleText**](getroletext.md) function to retrieve localized string.                                                    |
| [**GetSelection**](uiauto-ilegacyiaccessibleprovider-getselection.md)         | Method      | Retrieves an [**IUIAutomationElementArray**](uiauto-iuiautomationelementarray.md) interface pointer.                                |
| [**State**](uiauto-ilegacyiaccessibleprovider-state.md)                       | Property    | Use the [**GetStateText**](getstatetext.md) function to retrieve localized string.                                                  |
| [**Value**](uiauto-ilegacyiaccessibleprovider-value.md)                       | Property    | None                                                                                                                                 |
| [**DoDefaultAction**](uiauto-ilegacyiaccessibleprovider-dodefaultaction.md)   | Method      | None                                                                                                                                 |
| [**GetIAccessible**](uiauto-ilegacyiaccessibleprovider-getiaccessible.md)     | Method      | None                                                                                                                                 |
| [**Select**](uiauto-ilegacyiaccessibleprovider-select.md)                     | Method      | The selection flag is a Microsoft Active Accessibility**SELFLAG** value. For more information, see [SELFLAG Constants](selflag.md). |
| [**SetValue**](uiauto-ilegacyiaccessibleprovider-setvalue.md)                 | Method      | None                                                                                                                                 |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




