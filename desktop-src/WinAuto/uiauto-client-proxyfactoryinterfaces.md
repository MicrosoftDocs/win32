---
title: Proxy Factory Interfaces for Clients
description: This section describes the proxy factory interfaces for unmanaged UI Automation client applications.
ms.assetid: '46c6720a-19c2-4ddd-893c-1a46af0642fb'
---

# Proxy Factory Interfaces for Clients

This section describes the proxy factory interfaces for unmanaged UI Automation client applications.

## In this section



| Interface                                                                                      | Description                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUIAutomationProxyFactory**](uiauto-iuiautomationproxyfactory.md)<br/>               | Exposes properties and methods of an object that creates a Microsoft UI Automation provider for UI elements that do not have native support for UI Automation. This interface is implemented by proxies.<br/>                                                                          |
| [**IUIAutomationProxyFactoryEntry**](uiauto-iuiautomationproxyfactoryentry.md)<br/>     | Represents a proxy factory in the table maintained by UI Automation, and exposes properties and methods that can be used by client applications to interact with [**IUIAutomationProxyFactory**](uiauto-iuiautomationproxyfactory.md) objects.<br/>                                   |
| [**IUIAutomationProxyFactoryMapping**](uiauto-iuiautomationproxyfactorymapping.md)<br/> | Exposes properties and methods for a table of proxy factories. Each table entry is represented by an [**IUIAutomationProxyFactoryEntry**](uiauto-iuiautomationproxyfactoryentry.md) interface. The entries are in the order in which the system will attempt to use the proxies.<br/> |



 

## Related topics

<dl> <dt>

[UI Automation Clients](uiauto-entry-uiautoclientsforwin32apps.md)
</dt> </dl>

 

 





