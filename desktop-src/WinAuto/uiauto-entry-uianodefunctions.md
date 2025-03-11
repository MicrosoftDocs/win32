---
title: Deprecated Node Functions
description: Deprecated Node Functions
ms.assetid: 72833757-a356-4727-8fc8-77a60e26aa99
ms.topic: reference
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
| [**UiaAddEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaaddevent)<br> |  **Note:** This function is deprecated. Client applications should use the Microsoft UI Automation COM interfaces instead.<br> Adds a listener for events on a node in the UI Automation tree.<br> | 
| [**UiaEventAddWindow**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaeventaddwindow)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Adds a window to the event listener.<br> | 
| [**UiaEventCallback**](/windows/desktop/api/UIAutomationCoreApi/nc-uiautomationcoreapi-uiaeventcallback)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> A client-implemented function that is called by UI Automation when an event is raised that the client has subscribed to.<br> | 
| [**UiaEventRemoveWindow**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaeventremovewindow)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Removes a window from the event listener.<br> | 
| [**UiaFind**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiafind)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves one or more UI Automation nodes that match the search criteria.<br> | 
| [**UiaGetErrorDescription**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiageterrordescription)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Gets an error string so that it can be passed to the client. This method is not used directly by clients.<br> | 
| [**UiaGetPatternProvider**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetpatternprovider)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves a **control pattern**.<br> | 
| [**UiaGetPropertyValue**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetpropertyvalue)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves the value of a UI Automation property.<br> | 
| [**UiaGetRootNode**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetrootnode)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves the root UI Automation node.<br> | 
| [**UiaGetRuntimeId**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetruntimeid)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves the runtime identifier of a UI Automation node.<br> | 
| [**UiaGetUpdatedCache**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetupdatedcache)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Updates the cache of property values and control patterns.<br> | 
| [**UiaHPatternObjectFromVariant**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahpatternobjectfromvariant)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Gets a control pattern object from a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) type.<br> | 
| [**UiaHTextRangeFromVariant**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahtextrangefromvariant)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Gets a text range from a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) type.<br> | 
| [**UiaHUiaNodeFromVariant**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahuianodefromvariant)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Gets an HUIANODE from a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) type.<br> | 
| [**UiaLookupId**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uialookupid)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Gets the integer identifier that can be used in methods that require a PROPERTYID, PATTERNID, CONTROLTYPEID, TEXTATTRIBUTEID, or EVENTID.<br> | 
| [**UiaNavigate**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianavigate)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Navigates in the UI Automation tree, optionally retrieving cached information.<br> | 
| [**UiaNodeFromFocus**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromfocus)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves the UI Automation node for the UI element that currently has input focus.<br> | 
| [**UiaNodeFromHandle**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromhandle)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves the UI Automation node associated with a window.<br> | 
| [**UiaNodeFromPoint**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefrompoint)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves the UI Automation node for the element at the specified point.<br> | 
| [**UiaNodeFromProvider**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromprovider)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves the UI Automation node for a raw element provider.<br> | 
| [**UiaNodeRelease**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianoderelease)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Deletes a node from memory.<br> | 
| [**UiaPatternRelease**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiapatternrelease)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Deletes an allocated pattern object from memory.<br> | 
| [**UiaProviderCallback**](/windows/desktop/api/UIAutomationCoreApi/nc-uiautomationcoreapi-uiaprovidercallback)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> An application-defined function that is called by UI Automation to obtain a client-side provider for an element.<br> | 
| [**UiaRectIsEmpty**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiarectisempty)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Gets a Boolean value that specifies whether a rectangle has all its coordinates set to 0.<br> | 
| [**UiaRectSetEmpty**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiarectsetempty)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Sets the elements of a [**UiaRect**](/windows/desktop/api/UIAutomationCore/ns-uiautomationcore-uiarect) structure to 0.<br> | 
| [**UiaRegisterProviderCallback**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaregisterprovidercallback)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Registers the application-defined method that is called by UI Automation to obtain a provider for an element.<br> | 
| [**UiaRemoveEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaremoveevent)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Removes a listener for events on a node in the UI Automation tree.<br> | 
| [**UiaSetFocus**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiasetfocus)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Sets the input focus to the specified element in the UI.<br> | 
| [**UiaTextRangeRelease**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiatextrangerelease)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Deletes an allocated text range object from memory.<br> | 




 

## Related topics

<dl> <dt>

[UI Automation Clients](uiauto-entry-uiautoclientsforwin32apps.md)
</dt> </dl>

 

