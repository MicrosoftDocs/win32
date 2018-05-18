---
title: Functions for Providers
description: This section describes the functions for UI Automation provider for Microsoft Win32 applications.
ms.assetid: '76012ec7-0114-4b6b-a35e-5cfde5b90230'
---

# Functions for Providers

This section describes the functions for UI Automation provider for Microsoft Win32 applications.

## In this section



| Function                                                                                                 | Description                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UiaClientsAreListening**](uiauto-uiaclientsarelisteningfunction.md)<br/>                       | Gets a value that indicates whether any client application is subscribed to Microsoft UI Automation events.<br/>                                             |
| [**UiaDisconnectAllProviders**](uiauto-uiadisconnectallproviders.md)<br/>                         | Releases all UI Automation resources that are held by all providers associated with the calling process. <br/>                                               |
| [**UiaDisconnectProvider**](uiauto-uiadisconnectprovider.md)<br/>                                 | Releases all references that a particular provider holds to UI Automation objects.<br/>                                                                      |
| [**UiaGetReservedMixedAttributeValue**](uiauto-uiagetreservedmixedattributevalueautometh.md)<br/> | Retrieves a reserved value indicating that the value of a UI Automation text attribute varies within a text range.<br/>                                      |
| [**UiaGetReservedNotSupportedValue**](uiauto-uiagetreservednotsupportedvalueautometh.md)<br/>     | Retrieves a reserved value indicating that a UI Automation property or a text attribute is not supported.<br/>                                               |
| [**UiaHostProviderFromHwnd**](uiauto-uiahostproviderfromhwndfunction.md)<br/>                     | Gets the host provider for a window.<br/>                                                                                                                    |
| [**UiaIAccessibleFromProvider**](https://msdn.microsoft.com/library/windows/desktop/hh437313)<br/>                   | Retrieves an [**IAccessible**](iaccessible.md) implementation that provides Microsoft Active Accessibility data on behalf of a UI Automation provider.<br/> |
| [**UiaProviderForNonClient**](uiauto-uiaproviderfornonclientfunction.md)<br/>                     | Gets the provider for the entire non-client area of a window, or for a control in the non-client area of a window.<br/>                                      |
| [**UiaProviderFromIAccessible**](uiauto-uiaproviderfromiaccessiblefunction.md)<br/>               | Creates a UI Automation provider based on the specified Microsoft Active Accessibility object.<br/>                                                          |
| [**UiaRaiseAsyncContentLoadedEvent**](uiauto-uiaraiseasynccontentloadedeventfunction.md)<br/>     | Called by a provider to notify the UI Automation core that content is being loaded asynchronously.<br/>                                                      |
| [**UiaRaiseAutomationEvent**](uiauto-uiaraiseautomationeventfunction.md)<br/>                     | Notifies listeners of an event.<br/>                                                                                                                         |
| [**UiaRaiseAutomationPropertyChangedEvent**](uiauto-raiseautopropchangedeventfunction.md)<br/>    | Called by providers to notify the UI Automation core that an element property has changed.<br/>                                                              |
| [**UiaRaiseChangesEvent**](uiauto-uiaraisechangeseventfunction.md)<br/>                           | Called by providers to notify the UI Automation core that a change has occurred.<br/>                                                                        |
| [**UiaRaiseNotificationEvent**](winauto-uiauto_UiaRaiseNotificationEventFunction)<br/>             | Called by providers to initiate a notification event.<br/>                                                                                                   |
| [**UiaRaiseStructureChangedEvent**](uiauto-uiaraisestructurechangedeventfunction.md)<br/>         | Called by a provider to notify the UI Automation core that the tree structure has changed.<br/>                                                              |
| [**UiaRaiseTextEditTextChangedEvent**](uiauto-uiaraisetextedittextchangedeventfunction.md)<br/>   | Called by a provider to notify the UI Automation core that a text control has programmatically changed text.<br/>                                            |
| [**UiaReturnRawElementProvider**](uiauto-uiareturnrawelementproviderfunction.md)<br/>             | Gets an interface to the UI Automation provider for a window.<br/>                                                                                           |



 

## Related topics

<dl> <dt>

[UI Automation Providers](uiauto-entry-uiautoprovidersforwin32apps.md)
</dt> </dl>

 

 





