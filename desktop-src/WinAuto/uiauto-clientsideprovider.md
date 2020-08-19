---
title: Implementing a Client-Side (Proxy) UI Automation Provider
description: This topic describes how to write a proxy provider for an unsupported control and add it to the list of proxies used by client applications.
ms.assetid: c66f4a7b-0a12-4c65-a3e9-1c826d54ac6b
keywords:
- UI Automation,client-side provider implementation
- UI Automation,provider implementation
- UI Automation,implementing client-side providers
- UI Automation,implementing providers
- UI Automation,proxies
- proxies
- client-side providers
- providers,implementing
- implementing client-side providers
- implementing providers
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Client-Side (Proxy) UI Automation Provider

Microsoft UI Automation supplies a set of proxies for most standard controls, such as those used in Microsoft Win32, Windows Forms, and Windows Presentation Foundation (WPF) applications. However, many custom controls and third party controls do not implement native UI Automation providers. To be accessible to UI Automation client applications, these controls must be furnished with client-side providers, also known as *proxy providers*, or *proxies*.

This topic describes how to write a proxy provider for an unsupported control and add it to the list of proxies used by client applications. It includes the following topics:

-   [What is a Proxy?](#what-is-a-proxy)
-   [What is a Proxy Factory?](#what-is-a-proxy-factory)
-   [Proxy Factory Mapping](#proxy-factory-mapping)
-   [Managing Default Proxies](#managing-default-proxies)
-   [Related topics](#related-topics)

For code examples that show how to implement proxy providers, see [How-To Topics for UI Automation Providers](uiauto-howto-topics-for-uiautomation-providers.md).

## What is a Proxy?

A client-side provider, or proxy, is an object that implements the [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple) interface on behalf of a control that does not have an **IRawElementProviderSimple** implementation of its own. Without a proxy, such a control is largely opaque to UI Automation, which can supply only basic information available from the window handle (**HWND**), such as the control location.

## What is a Proxy Factory?

Each proxy requires a corresponding *proxy factory*, which is an object that exposes the [**IUIAutomationProxyFactory**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationproxyfactory) interface. UI Automation maintains an internal table of *proxy factory entries*, each of which contains a reference to the proxy factory for each proxy, and a set of conditions. When UI Automation encounters a control that does not have a native [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple) implementation, it searches for a proxy factory entry whose conditions indicate that it supports the control. UI Automation searches the table from the beginning, and when it finds a matching entry, UI Automation calls the factory's [**IUIAutomationProxyFactory::CreateProvider**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationproxyfactory-createprovider) method. If the matching proxy is successfully created, the UI Automation stops searching and uses the newly created proxy object; otherwise, UI Automation continues searching.

A client application creates an instance of a proxy factory entry by using the [**IUIAutomation::CreateProxyFactoryEntry**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-createproxyfactoryentry) method, which returns an [**IUIAutomationProxyFactoryEntry**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationproxyfactoryentry) interface pointer. Clients use methods exposed by **IUIAutomationProxyFactoryEntry** to specify the set of conditions that the proxy factory uses for creating the proxy.

When it calls [**IUIAutomationProxyFactory::CreateProvider**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationproxyfactory-createprovider), UI Automation passes parameters that the proxy factory object can use to determine whether the proxy adequately supports the custom control. If so, the proxy factory creates an instance of the proxy and returns the [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple) interface pointer; otherwise, it returns a **NULL** pointer.

## Proxy Factory Mapping

By default, UI Automation searches through the proxy factory table in the following order.



| Order | Proxy                        | Description                                                                      |
|-------|------------------------------|----------------------------------------------------------------------------------|
| 1     | Microsoft: Non-Control Proxy | For windows with the exact class name or base class name "ComboBoxEx32".         |
| 2     | Microsoft: Non-Control Proxy | For windows with the exact class name or base class name "WorkerW".              |
| 3     | Microsoft: Non-Control Proxy | For windows with the exact class name or base class name "SHELLDLL\_DefView".    |
| 4     | Microsoft: Container Proxy   | For windows with the exact class name or base class name "\#32770".              |
| 5     | Microsoft: Container Proxy   | For windows with a class name or base class name containing "AfxControlBar".     |
| 6     | Microsoft: TreeView Proxy    | For windows with a class name or base class name containing "SysTreeView32".     |
| 7     | Microsoft: ListView Proxy    | For windows with a class name or base class name containing "SysListView32" (1). |
| 8     | Microsoft: ListView Proxy    | For windows with a class name or base class name containing "SysListView32" (2). |
| 9     | Microsoft: MSAA Proxy        | For any window.                                                                  |



 

Proxies 7 and 8 are duplicate entries for the SysListView32 control. Without modification, the proxy 7 is always used for the SysListView32 control, and proxy 8 is never used. Proxy 8 is used only for visible list items, and is typically used by client applications that work only with visible elements, or that have strict performance requirements. These clients can remove proxy 7.

Proxy 9, the Microsoft Active Accessibility to UI Automation proxy, should always be the last entry in the table. This enables Microsoft Active Accessibility fallback functionality for controls that implement Microsoft Active Accessibility, but not UI Automation.

When modifying entries in the proxy factory table, you should carefully evaluate the new position of the entries. We recommend that entries for custom proxies be placed after the non-control and container proxies, but before the Microsoft Active Accessibility to UI Automation proxy. Also, while it is possible to have code in the call to [**CreateProvider**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationproxyfactory-createprovider) determine whether it should support a given window handle (**HWND**), it is more efficient to let UI Automation select the proxy based on the class name, and keep conditional code in the **CreateProvider** method to a minimum.

UI Automation maintains a separate proxy factory table for each client. When a client changes its proxy table, the changes affect only the client itself; other clients are not affected.

## Managing Default Proxies

When a client application creates the [**CUIAutomation**](/previous-versions/windows/desktop/legacy/ff384838(v=vs.85)) object, the proxy factory table initially contains entries only for the default proxy providers for standard controls. By using the [**IUIAutomationProxyFactoryMapping**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationproxyfactorymapping) interface, clients can add new entries, remove unwanted entries, change the order of entries, and so on. A client can retrieve an **IUIAutomationProxyFactoryMapping** interface pointer by calling the [**IUIAutomation::ProxyFactoryMapping**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-get_proxyfactorymapping) method.

The table of available proxies contains an [**IUIAutomationProxyFactoryEntry**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationproxyfactoryentry) interface for each proxy. Each **IUIAutomationProxyFactoryEntry** specifies the [**IUIAutomationProxyFactory**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationproxyfactory) and the control class that the proxy serves, and defines how events are to be handled.

The table of proxies is represented by an [**IUIAutomationProxyFactoryMapping**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationproxyfactorymapping) interface, which can be obtained from the [**IUIAutomation::ProxyFactoryMapping**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-get_proxyfactorymapping) property. An application can use **IUIAutomationProxyFactoryMapping** methods to add and delete proxies. To create a new entry to add to this table, use [**IUIAutomation::CreateProxyFactoryEntry**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-createproxyfactoryentry) to obtain the interface, and then use the [**IUIAutomationProxyFactoryEntry**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationproxyfactoryentry) methods to define the applicable control class and the behavior of the proxy.

## Related topics

<dl> <dt>

[How to Create a Client-Side (Proxy) UI Automation Provider](uiauto-howto-create-clientside-provider.md)
</dt> <dt>

[UI Automation Provider Programmer's Guide](uiauto-providerportal.md)
</dt> </dl>

 

 