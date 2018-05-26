---
title: Functions for Providers
description: This section describes the functions for UI Automation provider for Microsoft Win32 applications.
ms.assetid: 76012ec7-0114-4b6b-a35e-5cfde5b90230
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Functions for Providers

This section describes the functions for UI Automation provider for Microsoft Win32 applications.

## In this section



| Function                                                                                                 | Description                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UiaClientsAreListening**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaclientsarelistening?branch=master)<br/>                       | Gets a value that indicates whether any client application is subscribed to Microsoft UI Automation events.<br/>                                             |
| [**UiaDisconnectAllProviders**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiadisconnectallproviders?branch=master)<br/>                         | Releases all UI Automation resources that are held by all providers associated with the calling process. <br/>                                               |
| [**UiaDisconnectProvider**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiadisconnectprovider?branch=master)<br/>                                 | Releases all references that a particular provider holds to UI Automation objects.<br/>                                                                      |
| [**UiaGetReservedMixedAttributeValue**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetreservedmixedattributevalue?branch=master)<br/> | Retrieves a reserved value indicating that the value of a UI Automation text attribute varies within a text range.<br/>                                      |
| [**UiaGetReservedNotSupportedValue**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetreservednotsupportedvalue?branch=master)<br/>     | Retrieves a reserved value indicating that a UI Automation property or a text attribute is not supported.<br/>                                               |
| [**UiaHostProviderFromHwnd**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahostproviderfromhwnd?branch=master)<br/>                     | Gets the host provider for a window.<br/>                                                                                                                    |
| [**UiaIAccessibleFromProvider**](https://msdn.microsoft.com/library/windows/desktop/hh437313)<br/>                   | Retrieves an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) implementation that provides Microsoft Active Accessibility data on behalf of a UI Automation provider.<br/> |
| [**UiaProviderForNonClient**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaproviderfornonclient?branch=master)<br/>                     | Gets the provider for the entire non-client area of a window, or for a control in the non-client area of a window.<br/>                                      |
| [**UiaProviderFromIAccessible**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaproviderfromiaccessible?branch=master)<br/>               | Creates a UI Automation provider based on the specified Microsoft Active Accessibility object.<br/>                                                          |
| [**UiaRaiseAsyncContentLoadedEvent**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraiseasynccontentloadedevent?branch=master)<br/>     | Called by a provider to notify the UI Automation core that content is being loaded asynchronously.<br/>                                                      |
| [**UiaRaiseAutomationEvent**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraiseautomationevent?branch=master)<br/>                     | Notifies listeners of an event.<br/>                                                                                                                         |
| [**UiaRaiseAutomationPropertyChangedEvent**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraiseautomationpropertychangedevent?branch=master)<br/>    | Called by providers to notify the UI Automation core that an element property has changed.<br/>                                                              |
| [**UiaRaiseChangesEvent**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraisechangesevent?branch=master)<br/>                           | Called by providers to notify the UI Automation core that a change has occurred.<br/>                                                                        |
| [**UiaRaiseNotificationEvent**](winauto-uiauto_UiaRaiseNotificationEventFunction)<br/>             | Called by providers to initiate a notification event.<br/>                                                                                                   |
| [**UiaRaiseStructureChangedEvent**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraisestructurechangedevent?branch=master)<br/>         | Called by a provider to notify the UI Automation core that the tree structure has changed.<br/>                                                              |
| [**UiaRaiseTextEditTextChangedEvent**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraisetextedittextchangedevent?branch=master)<br/>   | Called by a provider to notify the UI Automation core that a text control has programmatically changed text.<br/>                                            |
| [**UiaReturnRawElementProvider**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiareturnrawelementprovider?branch=master)<br/>             | Gets an interface to the UI Automation provider for a window.<br/>                                                                                           |



 

## Related topics

<dl> <dt>

[UI Automation Providers](uiauto-entry-uiautoprovidersforwin32apps.md)
</dt> </dl>

 

 





