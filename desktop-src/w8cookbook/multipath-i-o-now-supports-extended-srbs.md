---
title: Multipath I/O now supports extended storage request blocks
description: Multipath I/O now supports extended storage request blocks
ms.assetid: 5373D9ED-34AF-4D66-8888-49F1EBF768F4
ms.topic: article
ms.date: 05/31/2018
---

# Multipath I/O now supports extended storage request blocks

## Platforms

**Servers** – Windows Server 2012 

## Description

In Windows Server 2012, a new structure, the STORAGE\_REQUEST\_BLOCK (extended SRB) replaces the SCSI\_REQUEST\_BLOCK (legacy SRB) in the core storage stack. Extended SRBs replicate the functionality of the legacy SRBs, but are also extensible and scalable.

Multipath I/O (MPIO) supports extended SRBs and allows Device Specific Modules (DSMs) to specify extended SRB support as well. However, in order for a multipath device’s storage stack to use extended SRBs, **all components in the stack must support extended SRBs, including the DSM**. Note that the Microsoft in-box DSM, MSDSM, does support extended SRBs.

The SCSI\_PASS\_THROUGH\_EX structure is not part of the extended MPIO pass through structure since the extended SCSI pass through can be of a variable size, depending on the command line debugger (CDB). Instead, the extended MPIO pass through has a field that describes the offset from the beginning of the extended MPIO pass through structure to the SCSI\_PASS\_THROUGH\_EX structure. The caller must make sure they allocate a buffer of the appropriate size and set the SCSI pass through offset correctly. As long as the caller follows the rules for extended SCSI pass-throughs, then there should not be any extra work for them to use the extended MPIO pass through.

> [!Note]  
> If the DSM does not support extended SRBs, MPIO will fail extended MPIO pass through requests that have the MPIO\_IOCTL\_FLAG\_INVOLVE\_DSM flag set.

 

## Manifestation

If any part of the device’s storage stack, including DSM, does not support extended SRBs, the storage stack will revert to using legacy SRBs.

## Solution

There are only two MPIO requirements for a DSM to support STORAGE\_REQUEST\_BLOCKS:

-   The DSM must report its type as DsmType6
-   The DSM must provide the DSM\_ADDRESS\_TYPE\_SUPPORTED function

If the DSM does not report DsmType6 or if it reports DsmType6 but does not provide the DSM\_ADDRESS\_TYPE\_SUPPORTED function, MPIO will assume the DSM does not support extended SRBs.

The DSM\_ADDRESS\_TYPE\_SUPPORTED function accepts two parameters, one of which is an address type. This address type must be one of the STORAGE\_ADDRESS\_TYPE\_\* values defined in srb.h. The DSM must return TRUE if it supports the given address type and FALSE if it does not. The definition of “support” is ultimately up to the DSM. MPIO uses this function to ensure that the DSM will not misbehave if it is handed an extended SRB with a STOR\_ADDRESS structure of the given type. As such, MPIO generally calls this function when a multipath device is being enumerated, but the function could be called at any time.

If a DSM never touches an extended SRB’s STOR\_ADDRESS, then it can return TRUE for any valid STORAGE\_ADDRESS\_TYPE\_\* value. Review the sample DSM in the WDK.

**Other important notes**

-   DSMs that support extended SRBs must be able to handle both SCSI\_REQUEST\_BLOCK structures and STORAGE\_REQUEST\_BLOCK structures. Just because a DSM reports that it supports extended SRBs does not mean that it will exclusively receive extended SRBs. It may still receive any number of legacy SRBs in addition to extended SRBs, and therefore must be able to handle both.
-   We have provided a header file in the WDK called srbhelper.h that contains inline functions to help drivers that must handle both extended and legacy SRBs. Our sample DSM uses this header so you can use it as an example of how to use these functions.
-   A DSM that does not support extended SRBs will never have to handle extended SRBs.
-   It’s possible that a MPIO will cause the storage stack to fall back on legacy SRBs in the event that the DSM does not support a given STORAGE\_ADDRESS\_TYPE\_\* (but otherwise supports extended SRBs).
-   “BTL8” is the only STORAGE\_ADDRESS\_TYPE\_\*currently defined for Windows Server 2012.

 

 




