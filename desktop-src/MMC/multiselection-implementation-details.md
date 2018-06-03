---
title: Multiselection Implementation Details
description: Multiselection Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cc469374-3969-4104-91a3-6c28ce617af5
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- multiselection MMC , implementation details
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Multiselection: Implementation Details

## To implement multiselection for items in a result pane list view

1.  In the snap-in's [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) implementation, set the pViewOptions parameter passed in the method call to MMC\_VIEW\_OPTIONS\_MULTISELECT. This enables multiselection. Be aware that multiselection can be enabled on a per-list view basis.
2.  In the snap-in's [**IComponent::QueryDataObject**](/windows/desktop/api/Mmc/nf-mmc-icomponent-querydataobject) implementation, handle the case when the MMC\_MULTI\_SELECT\_COOKIE special cookie is passed in the method call. MMC uses this special cookie to indicate to the snap-in that MMC is requesting a special, snap-in-defined multiselection data object.

    Snap-ins can use the [**IS\_SPECIAL\_COOKIE**](/windows/desktop/api/Mmc/nf-mmc-is_special_cookie) macro to determine whether or not the value contained in the method call's cookie parameter refers to a special cookie.

3.  Create the multiselection data object when the [**IComponent::QueryDataObject**](/windows/desktop/api/Mmc/nf-mmc-icomponent-querydataobject) implementation is called with the MMC\_MULTI\_SELECT\_COOKIE special cookie. Follow these guidelines when creating the data object:

    -   The multiselection data object should define some data structure that identifies the items currently selected in the result pane. A simple solution is to define an array of cookies whose elements are the cookie values of the currently selected items. The data object can then provide access to the array's data by either defining a custom clipboard format or through a public member function.

        To query MMC for the currently selected items that it owns, the snap-in should call [**IResultData::GetNextItem**](/windows/desktop/api/Mmc/nf-mmc-iresultdata-getnextitem). Set the mask, nIndex, and nState members of the [**RESULTDATAITEM**](/windows/desktop/api/Mmc/ns-mmc-_resultdataitem) structure passed in the method call. To retrieve only selected items, the value of the nState member should be LVIS\_SELECTED.

    -   The multiselection data object must also provide the list of node type GUIDs of all its currently selected items. This is done by supporting the [**CCF\_OBJECT\_TYPES\_IN\_MULTI\_SELECT**](ccf-object-types-in-multi-select.md) clipboard format in the multiselection data object's [**IDataObject::GetData**](https://www.bing.com/search?q=**IDataObject::GetData**) implementation. The data format used with the clipboard format is an [**SMMCObjectTypes**](/windows/desktop/api/Mmc/ns-mmc-_smmcobjecttypes) structure. MMC uses this structure to determine the extension snap-ins that extend any of the selected items.
    -   The multiselection data object should have some way of that identifies itself as a "nonstandard" data object. This is so that the snap-in can properly handle subsequent notification messages that pass the multiselection data object. One simple method is to create a member variable of type MMC\_COOKIE, say m\_lCookie, and set its value to MMC\_MULTI\_SELECT\_COOKIE. Be aware that, in general, all data objects created by the snap-in in response to calls to [**QueryDataObject**](/windows/desktop/api/Mmc/nf-mmc-icomponent-querydataobject) should store the cookie parameter passed in the call. For more information about cookies, see [Cookies](cookies.md).

4.  MMC forwards the multiselection data object to the snap-in's [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) implementation along with the [**MMCN\_SELECT**](mmcn-select.md) notification message. This gives the snap-in the opportunity to enable verbs for its selected items. Be aware that the snap-in only must explicitly enable verbs for any one of the selected items. MMC then sets the verbs for the other items.
5.  Implement the [**IDataObject::GetData**](https://www.bing.com/search?q=**IDataObject::GetData**) method and handle the case in which the MMC calls the method on the multiselection data object with the [**CCF\_OBJECT\_TYPES\_IN\_MULTI\_SELECT**](ccf-object-types-in-multi-select.md) clipboard format to request a list of the node type GUIDs of all the currently selected items. The snap-in should provide the requested information using the [**SMMCObjectTypes**](/windows/desktop/api/Mmc/ns-mmc-_smmcobjecttypes) structure.
6.  If necessary, handle the case where the snap-in can receive an MMC-provided composite data object in calls to its [**IExtendContextMenu**](/windows/desktop/api/Mmc/nn-mmc-iextendcontextmenu) or [**IExtendPropertySheet2**](/windows/desktop/api/Mmc/nn-mmc-iextendpropertysheet2) methods. The composite data object contains an array of multiselection data objects. The multiselection data objects are provided by the source snap-ins (primary or extension) that own items in the multiselection. Be aware that each source snap-in is responsible for defining the format of the multiselection data object that it provides.

    The snap-in can use the [**CCF\_MMC\_MULTISELECT\_DATAOBJECT**](ccf-mmc-multiselect-dataobject.md) clipboard format to determine whether or not a data object passed to it is a composite data object.

    If the data object is a composite data object, the snap-in must use the [**CCF\_MULTI\_SELECT\_SNAPINS**](ccf-multi-select-snapins.md) clipboard format for extracting the array of multiselection data objects from it. The data format used with the clipboard format is the [**SMMCDataObjects**](/windows/desktop/api/Mmc/ns-mmc-_smmcdataobjects) structure.

## Related topics

<dl> <dt>

[Drag and Drop](drag-and-drop.md)
</dt> <dt>

[Enabling MMC Standard Verbs](enabling-mmc-standard-verbs.md)
</dt> <dt>

[Using IPropertySheetProvider Directly](using-ipropertysheetprovider-directly.md)
</dt> </dl>

 

 




