---
title: Deprecated Node Functions
description: Deprecated Node Functions
ms.assetid: 72833757-a356-4727-8fc8-77a60e26aa99
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>UiaAddEvent</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaaddevent?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the Microsoft UI Automation COM interfaces instead.
</blockquote>
<br/> Adds a listener for events on a node in the UI Automation tree.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaEventAddWindow</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaeventaddwindow?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Adds a window to the event listener.<br/></td>
</tr>
<tr class="odd">
<td>[<em>UiaEventCallback</em>](/windows/win32/UIAutomationCoreApi/nc-uiautomationcoreapi-uiaeventcallback?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> A client-implemented function that is called by UI Automation when an event is raised that the client has subscribed to.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaEventRemoveWindow</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaeventremovewindow?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Removes a window from the event listener.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaFind</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiafind?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves one or more UI Automation nodes that match the search criteria.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaGetErrorDescription</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiageterrordescription?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets an error string so that it can be passed to the client. This method is not used directly by clients.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaGetPatternProvider</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetpatternprovider?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves a <em>control pattern</em>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaGetPropertyValue</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetpropertyvalue?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the value of a UI Automation property.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaGetRootNode</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetrootnode?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the root UI Automation node.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaGetRuntimeId</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetruntimeid?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the runtime identifier of a UI Automation node.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaGetUpdatedCache</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetupdatedcache?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Updates the cache of property values and control patterns.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaHPatternObjectFromVariant</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahpatternobjectfromvariant?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets a control pattern object from a [<strong>VARIANT</strong>](https://msdn.microsoft.com/library/windows/desktop/ms221627) type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaHTextRangeFromVariant</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahtextrangefromvariant?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets a text range from a [<strong>VARIANT</strong>](https://msdn.microsoft.com/library/windows/desktop/ms221627) type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaHUiaNodeFromVariant</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahuianodefromvariant?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets an HUIANODE from a [<strong>VARIANT</strong>](https://msdn.microsoft.com/library/windows/desktop/ms221627) type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaLookupId</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uialookupid?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets the integer identifier that can be used in methods that require a PROPERTYID, PATTERNID, CONTROLTYPEID, TEXTATTRIBUTEID, or EVENTID.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaNavigate</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uianavigate?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Navigates in the UI Automation tree, optionally retrieving cached information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaNodeFromFocus</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromfocus?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the UI Automation node for the UI element that currently has input focus.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaNodeFromHandle</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromhandle?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the UI Automation node associated with a window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaNodeFromPoint</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefrompoint?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the UI Automation node for the element at the specified point.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaNodeFromProvider</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromprovider?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the UI Automation node for a raw element provider.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaNodeRelease</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uianoderelease?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Deletes a node from memory.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaPatternRelease</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiapatternrelease?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Deletes an allocated pattern object from memory.<br/></td>
</tr>
<tr class="odd">
<td>[<em>UiaProviderCallback</em>](/windows/win32/UIAutomationCoreApi/nc-uiautomationcoreapi-uiaprovidercallback?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> An application-defined function that is called by UI Automation to obtain a client-side provider for an element.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaRectIsEmpty</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiarectisempty?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets a Boolean value that specifies whether a rectangle has all its coordinates set to 0.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaRectSetEmpty</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiarectsetempty?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Sets the elements of a [<strong>UiaRect</strong>](/windows/win32/UIAutomationCore/ns-uiautomationcore-uiarect?branch=master) structure to 0.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaRegisterProviderCallback</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaregisterprovidercallback?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Registers the application-defined method that is called by UI Automation to obtain a provider for an element.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaRemoveEvent</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaremoveevent?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Removes a listener for events on a node in the UI Automation tree.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaSetFocus</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiasetfocus?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Sets the input focus to the specified element in the UI.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaTextRangeRelease</strong>](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiatextrangerelease?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Deletes an allocated text range object from memory.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[UI Automation Clients](uiauto-entry-uiautoclientsforwin32apps.md)
</dt> </dl>

 

 





