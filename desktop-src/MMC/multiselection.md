---
title: Enabling Multiselection in the MMC
description: Multiselection is allowed only in the result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9fe5db82-d3b7-4050-b653-6c19cdc21525
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- multiselection MMC
- multiselection MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enabling Multiselection in the MMC

Multiselection is allowed only in the result pane. By default, multiselection is disabled in the list view. To enable multiselection, set the **MMC\_VIEW\_OPTIONS\_MULTISELECT** flag in the *ViewOptions* parameter during calls to the snap-in's [**IComponent::GetResultViewType**](/windows/win32/Mmc/nf-mmc-icomponent-getresultviewtype?branch=master) implementation.

What happens on multiselection depends on the items that are selected in the result pane. Possible scenarios include:

-   Scope or result items owned by a single snap-in are selected.
-   Scope items owned by multiple snap-ins are selected.

## Multiselection and Items Owned by a Single Snap-in

Multiselection for items owned by a single snap-in works in the following way:

1.  In a list view for which multiselection is enabled, the user selects one scope or result item and then selects another one.
2.  Upon selection of the next item, MMC calls the current view's [**IComponent::QueryDataObject**](/windows/win32/Mmc/nf-mmc-icomponent-querydataobject?branch=master) implementation. The cookie parameter passed into the call contains the value of the **MMC\_MULTI\_SELECT\_COOKIE** special cookie, indicating to the snap-in that MMC is requesting a special, snap-in-defined multiselection data object.

    Be aware that, in general, snap-ins can use the [**IS\_SPECIAL\_COOKIE**](/windows/win32/Mmc/nf-mmc-is_special_cookie?branch=master) macro to determine whether or not the value contained in the cookie parameter refers to a special cookie.

3.  The snap-in creates the multiselection data object that identifies the items currently selected in the result pane, and returns it to MMC. The snap-in should call [**IResultData::GetNextItem**](/windows/win32/Mmc/nf-mmc-iresultdata-getnextitem?branch=master) with RESULTDATAITEM.nState = LVIS\_SELECTED to get all its selected items.

    The multiselection data object provided by the snap-in must also provide the list of node type GUIDs of all its currently selected items. This is done by supporting the [**CCF\_OBJECT\_TYPES\_IN\_MULTI\_SELECT**](ccf-object-types-in-multi-select.md) clipboard format in the multiselection data object's [**IDataObject::GetData**](_ole_idataobject_getdata) implementation. The data format used with the clipboard format is an [**SMMCObjectTypes**](/windows/win32/Mmc/ns-mmc-_smmcobjecttypes?branch=master) structure. MMC uses this structure to determine the extension snap-ins that extend any of the selected items.

4.  MMC calls the snap-in's [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) implementation for the current view with the [**MMCN\_SELECT**](mmcn-select.md) notification to indicate that items are selected in the result pane. The *lpDataObject* parameter contains the multiselection data object created by the snap-in.
5.  The snap-in examines the multiselection data object and enables verbs for the selected items. Be aware that the snap-in only must explicitly enable verbs for any one of the selected items. MMC then sets the verbs for the other items. For more information about verb behavior during multiselection, see [Multiselection and Standard Verbs](#multiselection-and-standard-verbs).
6.  MMC then calls the **GetData** method of the multiselection data object with the [**CCF\_OBJECT\_TYPES\_IN\_MULTI\_SELECT**](ccf-object-types-in-multi-select.md) clipboard format to request a list of the node type GUIDs of all the currently selected items. The snap-in uses the [**SMMCObjectTypes**](/windows/win32/Mmc/ns-mmc-_smmcobjecttypes?branch=master) structure for providing the requested information. MMC uses **CCF\_OBJECT\_TYPES\_IN\_MULTI\_SELECT** to determine which extension snap-ins extend any of the selected items.
7.  MMC then finds which extensions can extend all of the selected items and creates them when the appropriate extension feature is required, for example, when the user displays a selected item's context menu.
8.  Control now returns to the user. If the user selects another item as part of the multiselection, MMC releases its interface to the multiselection data object and requests a new one. Steps 2 through 6 in this process are then repeated.

    If the user instead operates on the multiselection by, for example, activating one of the enabled verbs, what happens next depends on the performed operation. See [User Operations During Multiselection](#user-operations-during-multiselection) for details.

9.  After the multiselection operation is completed, MMC releases its interface to the multiselection data object.

## Multiselection and Items Owned by Multiple Snap-ins

Scope items owned (inserted) by multiple snap-ins can be part of a multiselection. In this case, multiselection works in essentially the same way as it does in the case when all items are owned by a single snap-in, with the following differences:

-   MMC calls the [**IComponent::QueryDataObject**](/windows/win32/Mmc/nf-mmc-icomponent-querydataobject?branch=master) implementation (with cookie == MMC\_MULTI\_SELECT\_COOKIE) of the primary snap-in and each namespace extension that owns any of the selected items to request a multiselection data object. Consequently, all namespace extensions whose items are allowed to be part of a multiselection must implement [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master).

    Be aware that, in the call to [**IResultData::GetNextItem**](/windows/win32/Mmc/nf-mmc-iresultdata-getnextitem?branch=master) with RESULTDATAITEM.nState = LVIS\_SELECTED, MMC will only return items that the calling snap-in owns, skipping over the items owned by other snap-ins. Therefore, each snap-in involved in a multiselection provides a multiselection data object that identifies only its items currently selected in the result pane.

-   During some multiselection operations (for example, paste operations) MMC creates a composite data object consisting of an array of multiselection data objects provided by all the snap-ins involved in a multiselection. This composite data object is forwarded to snap-ins, which can then use the [**CCF\_MULTI\_SELECT\_SNAPINS**](ccf-multi-select-snapins.md) clipboard format for extracting the array of multiselection data objects. The data format used with the clipboard format is the [**SMMCDataObjects**](/windows/win32/Mmc/ns-mmc-_smmcdataobjects?branch=master) structure.

## Multiselection and Standard Verbs

For multiselection, verbs behave as follows:

-   Open, rename, and refresh are disabled by default.
-   Copy, cut, and delete are inclusive. That is, if one of the selected items can be copied, then copy is enabled. The same is true for the cut and delete verbs.
-   Property and print are exclusive and are applicable only when items from a single snap-in are selected. Their state depends on the snap-in.

## User Operations During Multiselection

MMC allows the following user operations on multiply selected items:

-   Activation of any of the allowed verbs, either by using context menus or the corresponding toolbar buttons.
-   Selection of any context menu items, placed either by the primary snap-in or any of its extensions. Be aware that MMC only gives extension snap-ins that extend all the selected items an opportunity to add their extensions.
-   Drag-and-drop operations.

## Data Objects Sent During Multiselection Operations

The following table lists the types of data objects that can be sent to snap-ins in response to user operations that involve multiselection items.



| Notification or interface method                                          | Data object sent                                                                                        |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**MMCN\_BTN\_CLICK**](mmcn-btn-click.md)<br/>                     | Provided by MMC. Array of snap-in-provided multiselection data objects.<br/>                      |
| [**MMCN\_CUTORMOVE**](mmcn-cutormove.md)<br/>                      | Provided by the destination snap-in. Data object with the list of successfully pasted items.<br/> |
| [**MMCN\_DELETE**](mmcn-delete.md)<br/>                            | Multiselection data object. Provided by snap-in.<br/>                                             |
| [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md)<br/>                 | Provided by MMC. Array of snap-in-provided multiselection data objects.<br/>                      |
| [**MMCN\_PASTE**](mmcn-paste.md)<br/>                              | Multiselection data object. Provided by snap-in.<br/>                                             |
| [**MMCN\_PRINT**](mmcn-print.md)<br/>                              | Multiselection data object. Provided by snap-in.<br/>                                             |
| [**MMCN\_SELECT**](mmcn-select.md)<br/>                            | Multiselection data object. Provided by snap-in.<br/>                                             |
| [**IExtendContextMenu**](/windows/win32/Mmc/nn-mmc-iextendcontextmenu?branch=master) methods<br/>       | Provided by MMC. Array of snap-in-provided multiselection data objects.<br/>                      |
| [**IExtendControlbar**](/windows/win32/Mmc/nn-mmc-iextendcontrolbar?branch=master) methods<br/>         | Provided by MMC. Array of snap-in-provided multiselection data objects.<br/>                      |
| [**IExtendPropertySheet2**](/windows/win32/Mmc/nn-mmc-iextendpropertysheet2?branch=master) methods<br/> | Provided by MMC. Array of snap-in-provided multiselection data objects.<br/>                      |



 

## Multiselection and Drag and Drop Operations

The [Drag and Drop](drag-and-drop.md) section discusses how to support drag-and-drop functionality in a snap-in. However, the discussion and procedures outlined in that section only discuss drag-and-drop operations that involve a single selected item. Snap-ins that allow drag-and-drop operations on multiple items need to be aware of the following additional issues:

1.  The procedure outlined in [Multiselection: Implementation Details](multiselection-implementation-details.md) must be implemented in all source snap-ins that allow items inserted by them to be part of a multiselection.
2.  During the [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md) notification message, MMC provides a composite data object that contains an array of multiselection data objects. The multiselection data objects are provided by the source snap-ins (primary or extension) that own items in the multiselection. Be aware that each source snap-in is responsible for defining the format of the multiselection data object that it provides.

    The destination snap-in can use the [**CCF\_MMC\_MULTISELECT\_DATAOBJECT**](ccf-mmc-multiselect-dataobject.md) clipboard format to determine whether or not the data object it receives during [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md) is a composite data object.

    If the data object is a composite data object, the destination snap-in must use the [**CCF\_MULTI\_SELECT\_SNAPINS**](ccf-multi-select-snapins.md) clipboard format for extracting the array of multiselection data objects from it. The data format used with the clipboard format is the [**SMMCDataObjects**](/windows/win32/Mmc/ns-mmc-_smmcdataobjects?branch=master) structure.

    The destination snap-in can examine as many of the multiselection data objects as it must in determining whether or not to accept the paste.

3.  If the destination accepts the paste operation, MMC sends it an [**MMCN\_PASTE**](mmcn-paste.md) notification message, once for each multiselection data object. The *lpDataObject* parameter contains the pointer to a multiselection data object.

    If objects that are being pasted need to be deleted at the source as a result of a previous cut or move operation, then the param parameter contains a pointer to an [**IDataObject**](_ole_idataobject) interface. If the paste is successful, the destination snap-in should return a data object with the list of successfully pasted items, which in turn will be passed to each source snap-in for the [**MMCN\_CUTORMOVE**](mmcn-cutormove.md) notification.

    The format to communicate the list of items successfully pasted should be defined by each source snap-in. The most straightforward mechanism is for the destination snap-in to manipulate the multiselection data object in a manner defined by each source snap-in, increment the data object's reference count, and then return it in the param parameter.

    Be aware that the param for [**MMCN\_PASTE**](mmcn-paste.md) will be 0 if it does not involve a previous cut or move operation.

4.  After a successful cut or move operation, each source snap-in will receive the [**MMCN\_CUTORMOVE**](mmcn-cutormove.md) notification message. The *lpDataObject* parameter contains the data object returned by the destination snap-in after a successful paste. The source snap-in must examine the data object for the list of the successfully pasted items and perform whatever actions it deems necessary on the items.

    If the mechanism suggested in Step 3 is followed by the destination snap-in, each source snap-in will receive back its own multiselection data object in the [**MMCN\_CUTORMOVE**](mmcn-cutormove.md) notification message.

## Related topics

<dl> <dt>

[Multiselection: Implementation Details](multiselection-implementation-details.md)
</dt> <dt>

[Enabling MMC Standard Verbs](enabling-mmc-standard-verbs.md)
</dt> <dt>

[Using IPropertySheetProvider Directly](using-ipropertysheetprovider-directly.md)
</dt> </dl>

 

 





