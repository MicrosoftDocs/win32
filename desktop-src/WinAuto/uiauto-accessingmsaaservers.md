---
title: Accessing Microsoft Active Accessibility Servers
description: The Microsoft Active Accessibility to UI Automation Proxy is a software component that enables Microsoft UI Automation clients to interact with Microsoft Active Accessibility servers that implement the IAccessible interface natively.
ms.assetid: 44690b16-4a9d-4e8b-865a-b428ad616b1e
keywords:
- UI Automation,accessing Active Accessibility
- UI Automation,Active Accessibility
- UI Automation Proxy
- UI Automation,UI Automation Proxy
- LegacyIAccessible control pattern
- UI Automation,LegacyIAccessible control pattern
- Microsoft Active Accessibility
- Active Accessibility
- clients,accessing Active Accessibility servers
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Microsoft Active Accessibility Servers

The Microsoft Active Accessibility to UI Automation Proxy is a software component that enables Microsoft UI Automation clients to interact with Microsoft Active Accessibility servers that implement the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface natively. The proxy supports the [LegacyIAccessible](uiauto-implementinglegacyiaccessible.md) control pattern, and supplies an instance of the [**IUIAutomationLegacyIAccessiblePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationlegacyiaccessiblepattern) interface for each Microsoft Active Accessibility server detected. UI Automation clients use the methods exposed by **IUIAutomationLegacyIAccessiblePattern** to access the Microsoft Active Accessibility properties and objects supported by the server.

If a UI Automation element has an underlying Microsoft Active Accessibility implementation, a client can obtain an [**IUIAutomationLegacyIAccessiblePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationlegacyiaccessiblepattern) interface pointer for the element by passing the [**UIA\_LegacyIAccessiblePatternId**](uiauto-controlpattern-ids.md) control pattern ID to one of the following [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) methods:

-   [**GetCachedPattern**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcachedpattern)
-   [**GetCachedPatternAs**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcachedpatternas)
-   [**GetCurrentPattern**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpattern)
-   [**GetCurrentPatternAs**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpatternas)

The [**IUIAutomationLegacyIAccessiblePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationlegacyiaccessiblepattern) interface is not available for controls based on UI Automation.

The [**IUIAutomationLegacyIAccessiblePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationlegacyiaccessiblepattern) interface enables UI Automation clients to access the underlying [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) implementation of an Microsoft Active Accessibility element. However, the interface does not support methods that are obsolete or redundant with UI Automation features. For example, **IUIAutomationLegacyIAccessiblePattern** does not have a method that is equivalent to [**IAccessible::accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation) because the current location of a UI element is available from the UI Automation BoundingRectangle property.

The [**IUIAutomationLegacyIAccessiblePattern::GetIAccessible**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationlegacyiaccessiblepattern-getiaccessible) method enables a client to retrieve an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer from an UI Automation element. The reverse is also possible by using the [**IUIAutomation::ElementFromIAccessible**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfromiaccessible) and [**IUIAutomation::ElementFromIAccessibleBuildCache**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfromiaccessiblebuildcache) methods.

[**IUIAutomationLegacyIAccessiblePattern::GetIAccessible**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationlegacyiaccessiblepattern-getiaccessible) returns **NULL** if the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface for the element is provided by a proxy object from OLEACC.dll or from the UI Automation to Microsoft Active Accessibility Bridge.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation and Active Accessibility](uiauto-msaa.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> </dl>

 

 




