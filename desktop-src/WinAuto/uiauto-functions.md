---
title: Functions for Providers
description: This section describes the functions for UI Automation provider for Microsoft Win32 applications.
ms.assetid: 76012ec7-0114-4b6b-a35e-5cfde5b90230
ms.topic: article
ms.date: 05/31/2018
---

# Functions for Providers

This section describes the functions for UI Automation provider for Microsoft Win32 applications.

## In this section



| Function                                                                                                 | Description                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UiaClientsAreListening**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaclientsarelistening)<br/>                       | Gets a value that indicates whether any client application is subscribed to Microsoft UI Automation events.<br/>                                             |
| [**UiaDisconnectAllProviders**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiadisconnectallproviders)<br/>                         | Releases all UI Automation resources that are held by all providers associated with the calling process. <br/>                                               |
| [**UiaDisconnectProvider**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiadisconnectprovider)<br/>                                 | Releases all references that a particular provider holds to UI Automation objects.<br/>                                                                      |
| [**UiaGetReservedMixedAttributeValue**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetreservedmixedattributevalue)<br/> | Retrieves a reserved value indicating that the value of a UI Automation text attribute varies within a text range.<br/>                                      |
| [**UiaGetReservedNotSupportedValue**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetreservednotsupportedvalue)<br/>     | Retrieves a reserved value indicating that a UI Automation property or a text attribute is not supported.<br/>                                               |
| [**UiaHostProviderFromHwnd**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahostproviderfromhwnd)<br/>                     | Gets the host provider for a window.<br/>                                                                                                                    |
| [**UiaIAccessibleFromProvider**](/windows/desktop/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaiaccessiblefromprovider)<br/>                   | Retrieves an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) implementation that provides Microsoft Active Accessibility data on behalf of a UI Automation provider.<br/> |
| [**UiaProviderForNonClient**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaproviderfornonclient)<br/>                     | Gets the provider for the entire non-client area of a window, or for a control in the non-client area of a window.<br/>                                      |
| [**UiaProviderFromIAccessible**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaproviderfromiaccessible)<br/>               | Creates a UI Automation provider based on the specified Microsoft Active Accessibility object.<br/>                                                          |
| [**UiaRaiseAsyncContentLoadedEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraiseasynccontentloadedevent)<br/>     | Called by a provider to notify the UI Automation core that content is being loaded asynchronously.<br/>                                                      |
| [**UiaRaiseAutomationEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraiseautomationevent)<br/>                     | Notifies listeners of an event.<br/>                                                                                                                         |
| [**UiaRaiseAutomationPropertyChangedEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraiseautomationpropertychangedevent)<br/>    | Called by providers to notify the UI Automation core that an element property has changed.<br/>                                                              |
| [**UiaRaiseChangesEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraisechangesevent)<br/>                           | Called by providers to notify the UI Automation core that a change has occurred.<br/>                                                                        |
| [**UiaRaiseNotificationEvent**](https://www.bing.com/search?q=**UiaRaiseNotificationEvent**)<br/>             | Called by providers to initiate a notification event.<br/>                                                                                                   |
| [**UiaRaiseStructureChangedEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraisestructurechangedevent)<br/>         | Called by a provider to notify the UI Automation core that the tree structure has changed.<br/>                                                              |
| [**UiaRaiseTextEditTextChangedEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraisetextedittextchangedevent)<br/>   | Called by a provider to notify the UI Automation core that a text control has programmatically changed text.<br/>                                            |
| [**UiaReturnRawElementProvider**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiareturnrawelementprovider)<br/>             | Gets an interface to the UI Automation provider for a window.<br/>                                                                                           |



 

## Related topics

<dl> <dt>

[UI Automation Providers](uiauto-entry-uiautoprovidersforwin32apps.md)
</dt> </dl>

 

