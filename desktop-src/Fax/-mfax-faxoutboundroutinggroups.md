---
Description: The FaxOutboundRoutingGroups configuration collection is used by a fax client application to manage the fax outbound routing groups, represented by FaxOutboundRoutingGroup objects.
ms.assetid: 799a034c-c807-428c-8536-bc68dce5cd8e
title: FaxOutboundRoutingGroups object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRoutingGroups object

The **FaxOutboundRoutingGroups** configuration collection is used by a fax client application to manage the fax outbound routing groups, represented by [**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md) objects. The collection also includes methods to add and remove groups from the collection.

> [!Note]  
> The outbound routing group **All Devices** is always the first object in this collection. You cannot remove the **All Devices** group from the collection. If you attempt to remove it, you will receive an error message.

 

## Members

The **FaxOutboundRoutingGroups** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxOutboundRoutingGroups** object has these methods.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Method</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>Add</strong>](-mfax-faxoutboundroutinggroups-add.md)</td>
<td style="text-align: left;">The [<strong>Add</strong>](-mfax-faxoutboundroutinggroups-add.md) method adds an outbound routing group to the <strong>FaxOutboundRoutingGroups</strong> collection.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>Remove</strong>](-mfax-faxoutboundroutinggroups-remove-vb.md)</td>
<td style="text-align: left;">The [<strong>Remove</strong>](-mfax-faxoutboundroutinggroups-remove-vb.md) method removes an item from the <strong>FaxOutboundRoutingGroups</strong> collection. <br/>
<blockquote>
[!Note]<br />
You cannot remove the special <strong>All Devices</strong> routing group.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **FaxOutboundRoutingGroups** object has these properties.



| Property                                                            | Access type          | Description                                                                                                                                                                                                                                           |
|:--------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Count**](-mfax-faxoutboundroutinggroups-count-vb.md)<br/> | Read-only<br/> | The [**Count**](-mfax-faxoutboundroutinggroups-count-vb.md) property represents the number of objects in the **FaxOutboundRoutingGroups** collection. This is the total number of outbound routing groups associated with the fax server.<br/> |
| [**Item**](-mfax-faxoutboundroutinggroups-item.md)<br/>      | Read-only<br/> | The Item property returns a [**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md) object from the **FaxOutboundRoutingGroups** collection.<br/>                                                                                      |



 

## Remarks

A **FaxOutboundRoutingGroups** object is accessed through a [**FaxOutboundRouting**](-mfax-faxoutboundrouting.md) object.

![faxoutboundrouting and faxoutboundroutinggroups objects](images/faxoutboundroutinggroups.png)

To create a **FaxOutboundRoutingGroups** object in Microsoft Visual Basic, call the [**GetGroups**](-mfax-faxoutboundrouting-getgroups.md) method of the [**FaxOutboundRouting**](-mfax-faxoutboundrouting.md) object.

To create a **FaxOutboundRoutingGroups** object in C++, call the [**GetGroups**](-mfax-faxoutboundrouting-getgroups.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxOutboundRoutingGroups<br/>                                              |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md)
</dt> </dl>

 

 




