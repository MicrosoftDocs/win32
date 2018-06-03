---
title: Deprecated Node Functions
description: Deprecated Node Functions
ms.assetid: 72833757-a356-4727-8fc8-77a60e26aa99
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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
<td>[<strong>UiaAddEvent</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaaddevent)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the Microsoft UI Automation COM interfaces instead.
</blockquote>
<br/> Adds a listener for events on a node in the UI Automation tree.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaEventAddWindow</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaeventaddwindow)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Adds a window to the event listener.<br/></td>
</tr>
<tr class="odd">
<td>[<em>UiaEventCallback</em>](/windows/desktop/api/UIAutomationCoreApi/nc-uiautomationcoreapi-uiaeventcallback)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> A client-implemented function that is called by UI Automation when an event is raised that the client has subscribed to.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaEventRemoveWindow</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaeventremovewindow)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Removes a window from the event listener.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaFind</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiafind)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves one or more UI Automation nodes that match the search criteria.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaGetErrorDescription</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiageterrordescription)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets an error string so that it can be passed to the client. This method is not used directly by clients.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaGetPatternProvider</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetpatternprovider)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves a <em>control pattern</em>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaGetPropertyValue</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetpropertyvalue)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the value of a UI Automation property.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaGetRootNode</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetrootnode)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the root UI Automation node.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaGetRuntimeId</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetruntimeid)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the runtime identifier of a UI Automation node.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaGetUpdatedCache</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetupdatedcache)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Updates the cache of property values and control patterns.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaHPatternObjectFromVariant</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahpatternobjectfromvariant)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets a control pattern object from a [<strong>VARIANT</strong>](https://msdn.microsoft.com/library/windows/desktop/ms221627) type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaHTextRangeFromVariant</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahtextrangefromvariant)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets a text range from a [<strong>VARIANT</strong>](https://msdn.microsoft.com/library/windows/desktop/ms221627) type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaHUiaNodeFromVariant</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahuianodefromvariant)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets an HUIANODE from a [<strong>VARIANT</strong>](https://msdn.microsoft.com/library/windows/desktop/ms221627) type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaLookupId</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uialookupid)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets the integer identifier that can be used in methods that require a PROPERTYID, PATTERNID, CONTROLTYPEID, TEXTATTRIBUTEID, or EVENTID.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaNavigate</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianavigate)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Navigates in the UI Automation tree, optionally retrieving cached information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaNodeFromFocus</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromfocus)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the UI Automation node for the UI element that currently has input focus.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaNodeFromHandle</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromhandle)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the UI Automation node associated with a window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaNodeFromPoint</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefrompoint)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the UI Automation node for the element at the specified point.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaNodeFromProvider</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianodefromprovider)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Retrieves the UI Automation node for a raw element provider.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaNodeRelease</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uianoderelease)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Deletes a node from memory.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaPatternRelease</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiapatternrelease)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Deletes an allocated pattern object from memory.<br/></td>
</tr>
<tr class="odd">
<td>[<em>UiaProviderCallback</em>](/windows/desktop/api/UIAutomationCoreApi/nc-uiautomationcoreapi-uiaprovidercallback)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> An application-defined function that is called by UI Automation to obtain a client-side provider for an element.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaRectIsEmpty</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiarectisempty)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Gets a Boolean value that specifies whether a rectangle has all its coordinates set to 0.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaRectSetEmpty</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiarectsetempty)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Sets the elements of a [<strong>UiaRect</strong>](/windows/desktop/api/UIAutomationCore/ns-uiautomationcore-uiarect) structure to 0.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaRegisterProviderCallback</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaregisterprovidercallback)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Registers the application-defined method that is called by UI Automation to obtain a provider for an element.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaRemoveEvent</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaremoveevent)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Removes a listener for events on a node in the UI Automation tree.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UiaSetFocus</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiasetfocus)<br/></td>
<td><blockquote>
[!Note]<br />
This function is deprecated. Client applications should use the UI Automation COM interfaces instead.
</blockquote>
<br/> Sets the input focus to the specified element in the UI.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UiaTextRangeRelease</strong>](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiatextrangerelease)<br/></td>
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

 

 





