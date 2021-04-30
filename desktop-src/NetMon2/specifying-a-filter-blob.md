---
description: When you select a registered network interface card (NIC) listed on a local computer, you can use a filter BLOB to disregard the NICs you are not interested in.
ms.assetid: fa87bb7d-c481-4eb1-b116-b22643a7c9da
title: Specifying a Filter BLOB
ms.topic: article
ms.date: 05/31/2018
---

# Specifying a Filter BLOB

When you select a registered network interface card (NIC) listed on a local computer, you can use a [*filter BLOB*](f.md) to disregard the NICs you are not interested in. For example, you could restrict the search for a specific type of card (such as ETHERNET) or a specific MAC address.

During the search for a NIC, every entry in the filter BLOB must match an equivalent entry in the NPP BLOB that represents the NIC. Filter BLOBs can also be [*special BLOBs*](s.md).

When the [**GetNPPBlobFromUI**](getnppblobfromui.md) function is called, the filter BLOB restricts the NICs displayed in the **Select a network** dialog box. When the [**GetNPPBlobTable**](getnppblobtable.md) function is called, the filter BLOB restricts the NICs returned in the BLOB table.

To use the filter, you must create a filter BLOB, set the values of the properties you want to filter on (including any special BLOB entries), and then specify the BLOB filter and a call to the [**GetNPPBlobTable**](getnppblobtable.md) or [**GetNPPBlobFromUI**](getnppblobfromui.md) function.



| For information on                                 | See                                                                                                  |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------|
| How to select a NIC registered on a local computer | [Selecting a Registered NIC](selecting-a-registered-nic.md)                                         |
| Retrieving an NPP BLOB table                       | [Selecting a NIC from a Returned NPP BLOB table](selecting-a-nic-from-a-returned-npp-blob-table.md) |



 

 

 



