---
description: To select a NIC from an NPP BLOB table returned by Network Monitor, call the GetNPPBlobTable function. This function returns an NPP BLOB table, which can then be enumerated by your application to select the NIC you are interested in.
ms.assetid: 51428cc9-0b48-4da6-bbf6-b22798e01263
title: Selecting a NIC from a Returned NPP BLOB table
ms.topic: article
ms.date: 05/31/2018
---

# Selecting a NIC from a Returned NPP BLOB table

To select a NIC from an NPP BLOB table returned by Network Monitor, call the [**GetNPPBlobTable**](getnppblobtable.md) function. This function returns an NPP BLOB table, which can then be enumerated by your application to select the NIC you are interested in.

When you call this function you can return either a BLOB table of all the NICs registered on the local computer or a smaller set of filtered NICs. To filter the NICs that are returned, you can provide a [*filter BLOB*](f.md) when the call is made.



| For information about                                                       | See                                                                                                  |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| How to specify a filter that limits the NICs returned in an NPP BLOB table. | [Specifying a Filter BLOB](specifying-a-filter-blob.md)                                             |
| How to select a NIC registered on a local computer.                         | [Selecting a Registered NIC](selecting-a-registered-nic.md)                                         |
| How to select a NIC from a supplied NPP BLOB table                          | [Selecting a NIC from a Supplied NPP BLOB Table](selecting-a-nic-from-a-supplied-npp-blob-table.md) |



 

 

 



