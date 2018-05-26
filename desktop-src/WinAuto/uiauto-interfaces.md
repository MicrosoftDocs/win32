---
title: Interfaces for Providers
description: This section describes the basic interfaces implemented by UI Automation providers for Microsoft Win32 applications.
ms.assetid: e76d415d-5f5e-4e17-a5e4-4746e69c5010
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interfaces for Providers

This section describes the basic interfaces implemented by UI Automation providers for Microsoft Win32 applications.

## In this section



| Interface                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAccessibleEx**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iaccessibleex?branch=master)<br/>                                                     | Exposes methods that are called by Microsoft UI Automation to retrieve extra information about a control that supports Microsoft Active Accessibility.<br/>                                                                                                                                                                                                                                                                                                                |
| [**IAccessibleHostingElementProviders**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iaccessiblehostingelementproviders?branch=master)<br/>                  | A Microsoft Active Accessibility object implements this interface when the object is the root of an accessibility tree that includes windowless Microsoft ActiveX controls that implement UI Automation. Because Microsoft Active Accessibility and UI Automation use different interfaces, this interface enables a client to discover the list of hosted windowless ActiveX controls that support UI Automation in case the client needs to treat them differently.<br/> |
| [**IProxyProviderWinEventHandler**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iproxyproviderwineventhandler?branch=master)<br/>                     | Exposes a method that is implemented by proxy providers to handle WinEvents.<br/>                                                                                                                                                                                                                                                                                                                                                                                          |
| [**IProxyProviderWinEventSink**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iproxyproviderwineventsink?branch=master)<br/>                           | Exposes methods used by proxy providers to raise events.<br/>                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**IRawElementProviderAdviseEvents**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovideradviseevents?branch=master)<br/>                 | Exposes methods that are called to notify the root element of a fragment when a UI Automation client application begins or ends listening for events on that fragment.<br/>                                                                                                                                                                                                                                                                                                |
| [**IRawElementProviderFragment**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragment?branch=master)<br/>                         | Exposes methods and properties on UI elements that are part of a structure more than one level deep, such as a list box or list item. Implemented by UI Automation provider.<br/>                                                                                                                                                                                                                                                                                          |
| [**IRawElementProviderFragmentRoot**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragmentroot?branch=master)<br/>                 | Exposes methods and properties on the root element in a fragment.<br/>                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**IRawElementProviderHostingAccessibles**](https://msdn.microsoft.com/library/windows/desktop/hh448785)<br/> | This interface is implemented by a UI Automation provider when the provider is the root of an accessibility tree that includes windowless controls that support Microsoft Active Accessibility. Because UI Automation and Microsoft Active Accessibility use different interfaces, this interface enables a client to discover the list of hosted Microsoft Active Accessibility controls in case it needs to treat them differently.<br/>                                 |
| [**IRawElementProviderHwndOverride**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementproviderhwndoverride?branch=master)<br/>                 | Exposes a method that enables repositioning of window-based elements within the fragment's UI Automation tree.<br/>                                                                                                                                                                                                                                                                                                                                                        |
| [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master)<br/>                             | Defines methods and properties that expose simple UI elements.<br/>                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**IRawElementProviderSimple2**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple2?branch=master)<br/>                           | Extends the [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master) interface to enable programmatically invoking context menus.<br/>                                                                                                                                                                                                                                                                                                                        |
| [**IRawElementProviderSimple3**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple3?branch=master)<br/>                           | Extends the [**IRawElementProviderSimple2**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple2?branch=master) interface to enable retrieving metadata about how accessible technology should say the preferred content type.<br/>                                                                                                                                                                                                                                                                    |
| [**IRawElementProviderWindowlessSite**](https://msdn.microsoft.com/library/windows/desktop/hh448787)<br/>         | A ActiveX control site implements this interface to enable a UI Automation-enabled ActiveX control to express its accessibility. This interface enables the control container to provide an [**IRawElementProviderFragment**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragment?branch=master) pointer for the parent or siblings of the windowless ActiveX control, and to provide a runtime ID that is unique to the control site.<br/>                                                           |



 

## Related topics

<dl> <dt>

[UI Automation Providers](uiauto-entry-uiautoprovidersforwin32apps.md)
</dt> </dl>

 

 





