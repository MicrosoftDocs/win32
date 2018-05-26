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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LegacyIAccessible Control Pattern

Describes guidelines and conventions for using [**ILegacyIAccessibleProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-ilegacyiaccessibleprovider?branch=master), including information about properties, methods, and events. The **LegacyIAccessible** control pattern is supported by the Microsoft Active Accessibility to Microsoft UI Automation Proxy.

Application and control providers never implement the [**ILegacyIAccessibleProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-ilegacyiaccessibleprovider?branch=master) interface.

The **LegacyIAccessible** control pattern exposes the [**IUIAutomationLegacyIAccessiblePattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationlegacyiaccessiblepattern?branch=master) interface to UI Automation clients, enabling them to access the underlying [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) implementation for certain UI elements. However, **IUIAutomationLegacyIAccessiblePattern** does not support methods that are obsolete or that are redundant with the UI Automation features.

This topic contains the following sections:

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Members of the **LegacyIAccessible** Control Pattern](#members-of-the-legacyiaccessible-control-pattern)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

No application or control implements [**ILegacyIAccessibleProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-ilegacyiaccessibleprovider?branch=master). The UI Automation framework automatically supplies the provider implementation for a native Microsoft Active Accessibility server.

The **LegacyIAccessible** control pattern is not available for controls based on UI Automation.

## Members of the **LegacyIAccessible** Control Pattern

The following properties, methods, and events are members of the **LegacyIAccessible** control pattern. The notes are for UI Automation clients.



| Members                                                                        | Member type | Notes                                                                                                                                |
|--------------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**ChildId**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_childid?branch=master)                   | Property    | Returns **CHILDID\_SELF** (0) for a non-child object.                                                                                |
| [**DefaultAction**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_defaultaction?branch=master)       | Property    | None                                                                                                                                 |
| [**Description**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_description?branch=master)           | Property    | None                                                                                                                                 |
| [**Help**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_help?branch=master)                         | Property    | None                                                                                                                                 |
| [**KeyboardShortcut**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_keyboardshortcut?branch=master) | Property    | None                                                                                                                                 |
| [**Name**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_name?branch=master)                         | Property    | None                                                                                                                                 |
| [**Role**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_role?branch=master)                         | Property    | Use the [**GetRoleText**](/windows/win32/Oleacc/nf-oleacc-getroletexta?branch=master) function to retrieve localized string.                                                    |
| [**GetSelection**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-getselection?branch=master)         | Method      | Retrieves an [**IUIAutomationElementArray**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelementarray?branch=master) interface pointer.                                |
| [**State**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_state?branch=master)                       | Property    | Use the [**GetStateText**](/windows/win32/Oleacc/nf-oleacc-getstatetexta?branch=master) function to retrieve localized string.                                                  |
| [**Value**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-get_value?branch=master)                       | Property    | None                                                                                                                                 |
| [**DoDefaultAction**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-dodefaultaction?branch=master)   | Method      | None                                                                                                                                 |
| [**GetIAccessible**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-getiaccessible?branch=master)     | Method      | None                                                                                                                                 |
| [**Select**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-select?branch=master)                     | Method      | The selection flag is a Microsoft Active Accessibility**SELFLAG** value. For more information, see [SELFLAG Constants](selflag.md). |
| [**SetValue**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ilegacyiaccessibleprovider-setvalue?branch=master)                 | Method      | None                                                                                                                                 |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




