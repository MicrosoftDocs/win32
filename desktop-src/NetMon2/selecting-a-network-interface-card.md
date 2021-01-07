---
description: Network Monitor provides three functions for selecting a network interface card (NIC). These functions provide three ways to enumerate a set of NICs and select the one you want to use. The following table lists these functions.
ms.assetid: fbf319bb-4e24-46e3-81bc-d407b26220fb
title: Selecting a Network Interface Card
ms.topic: article
ms.date: 05/31/2018
---

# Selecting a Network Interface Card

Network Monitor provides three functions for selecting a network interface card (NIC). These functions provide three ways to enumerate a set of NICs and select the one you want to use. The following table lists these functions.



| Function                                                 | Description                                                                                                                                  |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetNPPBlobFromUI**](getnppblobfromui.md)             | Uses the Network Monitor UI to display the registered NICs and returns the NPP BLOB that represents the NIC you are interested in.           |
| [**GetNPPBlobTable**](getnppblobtable.md)               | Returns a BLOB table. The application must enumerate the table and select an NPP BLOB.                                                       |
| [**SelectNPPBlobFromTable**](selectnppblobfromtable.md) | Uses the Network Monitor interface to display the supplied NPP BLOBs and returns the NPP BLOB that represents the NIC you are interested in. |



 

Each NIC is represented by an NPP binary large object (BLOB). These functions can return a single NPP BLOB from those registered on the computer, a single NPP BLOB from a supplied NPP BLOB table, or a table of NPP BLOBs that the caller must then use to select a specific BLOB. In the first two cases, when selecting from the registered NICs or from a supplied NPP BLOB table, the Network Monitor UI displays the NICs you can select.

> [!Note]  
> Network Monitor uses a feature called the NPP Finder to enumerate the NICs registered on the local computer. The NPP Finder is a component of Npptools.dll.

 



| For information about                            | See                                                                                                  |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Selecting a NIC registered on the local computer | [Selecting a Registered NIC](selecting-a-registered-nic.md)                                         |
| Selecting a NIC from a supplied NPP BLOB table   | [Selecting a NIC from a Supplied NPP BLOB Table](selecting-a-nic-from-a-supplied-npp-blob-table.md) |
| Retrieving an NPP BLOB table                     | [Selecting a NIC from a Returned NPP BLOB table](selecting-a-nic-from-a-returned-npp-blob-table.md) |



 

 

 



