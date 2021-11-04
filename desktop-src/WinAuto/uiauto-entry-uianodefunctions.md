---
title: Deprecated Node Functions
description: Deprecated Node Functions
ms.assetid: 72833757-a356-4727-8fc8-77a60e26aa99
ms.topic: article
ms.date: 05/31/2018
---

# Deprecated Node Functions

> [!Note]  
> The control pattern functions described in this section are deprecated. Client applications should use the Component Object Model (COM) interfaces described in the following sections:
>
> -   [UI Automation Element Interfaces for Clients](uiauto-entry-uiautoclientinterfaces.md)
> -   [Property Condition Interface for Clients](uiauto-client-propconditioninterfaces.md)
> -   [Control Pattern Interfaces for Clients](uiauto-client-controlpatterninterfaces.md)
> -   [Event Handling Interfaces for Clients](uiauto-client-eventhandlinginterfaces.md)
> -   [Proxy Factory Interfaces for Clients](uiauto-client-proxyfactoryinterfaces.md)

 

## In this section




| Function | Description | 
|----------|-------------|
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaaddevent"><strong>UiaAddEvent</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the Microsoft UI Automation COM interfaces instead.</blockquote><br /> Adds a listener for events on a node in the UI Automation tree.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaeventaddwindow"><strong>UiaEventAddWindow</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Adds a window to the event listener.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nc-uiautomationcoreapi-uiaeventcallback"><em>UiaEventCallback</em></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> A client-implemented function that is called by UI Automation when an event is raised that the client has subscribed to.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaeventremovewindow"><strong>UiaEventRemoveWindow</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Removes a window from the event listener.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiafind"><strong>UiaFind</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Retrieves one or more UI Automation nodes that match the search criteria.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiageterrordescription"><strong>UiaGetErrorDescription</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Gets an error string so that it can be passed to the client. This method is not used directly by clients.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetpatternprovider"><strong>UiaGetPatternProvider</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Retrieves a <em>control pattern</em>.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetpropertyvalue"><strong>UiaGetPropertyValue</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Retrieves the value of a UI Automation property.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetrootnode"><strong>UiaGetRootNode</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Retrieves the root UI Automation node.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetruntimeid"><strong>UiaGetRuntimeId</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Retrieves the runtime identifier of a UI Automation node.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetupdatedcache"><strong>UiaGetUpdatedCache</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Updates the cache of property values and control patterns.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahpatternobjectfromvariant"><strong>UiaHPatternObjectFromVariant</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Gets a control pattern object from a <a href="/windows/win32/api/oaidl/ns-oaidl-variant"><strong>VARIANT</strong></a> type.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahtextrangefromvariant"><strong>UiaHTextRangeFromVariant</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Gets a text range from a <a href="/windows/win32/api/oaidl/ns-oaidl-variant"><strong>VARIANT</strong></a> type.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahuianodefromvariant"><strong>UiaHUiaNodeFromVariant</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Gets an HUIANODE from a <a href="/windows/win32/api/oaidl/ns-oaidl-variant"><strong>VARIANT</strong></a> type.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uialookupid"><strong>UiaLookupId</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Gets the integer identifier that can be used in methods that require a PROPERTYID, PATTERNID, CONTROLTYPEID, TEXTATTRIBUTEID, or EVENTID.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianavigate"><strong>UiaNavigate</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Navigates in the UI Automation tree, optionally retrieving cached information.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromfocus"><strong>UiaNodeFromFocus</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Retrieves the UI Automation node for the UI element that currently has input focus.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromhandle"><strong>UiaNodeFromHandle</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Retrieves the UI Automation node associated with a window.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefrompoint"><strong>UiaNodeFromPoint</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Retrieves the UI Automation node for the element at the specified point.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromprovider"><strong>UiaNodeFromProvider</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Retrieves the UI Automation node for a raw element provider.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianoderelease"><strong>UiaNodeRelease</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Deletes a node from memory.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiapatternrelease"><strong>UiaPatternRelease</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Deletes an allocated pattern object from memory.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nc-uiautomationcoreapi-uiaprovidercallback"><em>UiaProviderCallback</em></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> An application-defined function that is called by UI Automation to obtain a client-side provider for an element.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiarectisempty"><strong>UiaRectIsEmpty</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Gets a Boolean value that specifies whether a rectangle has all its coordinates set to 0.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiarectsetempty"><strong>UiaRectSetEmpty</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Sets the elements of a <a href="/windows/desktop/api/UIAutomationCore/ns-uiautomationcore-uiarect"><strong>UiaRect</strong></a> structure to 0.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaregisterprovidercallback"><strong>UiaRegisterProviderCallback</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Registers the application-defined method that is called by UI Automation to obtain a provider for an element.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaremoveevent"><strong>UiaRemoveEvent</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Removes a listener for events on a node in the UI Automation tree.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiasetfocus"><strong>UiaSetFocus</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Sets the input focus to the specified element in the UI.<br /> | 
| <a href="/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiatextrangerelease"><strong>UiaTextRangeRelease</strong></a><br /> | <blockquote>[!Note]<br />This function is deprecated. Client applications should use the UI Automation COM interfaces instead.</blockquote><br /> Deletes an allocated text range object from memory.<br /> | 




 

## Related topics

<dl> <dt>

[UI Automation Clients](uiauto-entry-uiautoclientsforwin32apps.md)
</dt> </dl>

 

