---
description: The Etype/SAP portion of the capture filter notifies the Network Monitor driver to accept frames that have a specific combination of Etypes and service access points (SAPs).
ms.assetid: 57dcf1cd-f27f-4bd3-a5a8-9e978a2d213e
title: Writing Etype/SAP Filter Portion
ms.topic: article
ms.date: 05/31/2018
---

# Writing Etype/SAP Filter Portion

The Etype/SAP portion of the capture filter notifies the Network Monitor driver to accept frames that have a specific combination of Etypes and [*service access points*](s.md) (SAPs). Etypes and SAPs are both ways that low-level protocols such as Ethernet, LLC, and Snap indicate which protocol follows them. Specifically:

-   Ethernet specifies an Etype
-   LLC specifies a SAP
-   Snap specifies an Etype

## Etype/SAP Capture Filter Flags

Use the following information to set the flags in the **FilterFlags** member of the [**CAPTUREFILTER**](capturefilter.md) structure.



| Flag                                         | Meaning                                                                                                                                                                                                                                                     |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CAPTUREFILTER\_ FLAGS\_INCLUDE\_ ALL\_SAPS   | Passes all SAP values and notifies the driver that all SAP values are valid. If combined with any values in the **lpSapTable** member, this flag notifies the driver that all SAP values except those in the **lpSapTable** are valid.<br/>           |
| CAPTUREFILTER\_ FLAGS\_INCLUDE\_ ALL\_ETYPES | Passes all Etype values and notifies the driver that all Etype values are valid. If combined with any values in the **lpEtypeTable** member, this flag notifies the driver that all Etype values except those in the **lpEtypeTable** are valid.<br/> |
| CAPTUREFILTER\_ FLAGS\_LOCAL\_ONLY           | Setting this flag will not set a NIC to P-Mode. You will only see local traffic (any frames to the local machine).                                                                                                                                          |
| CAPTUREFILTER\_ FLAGS\_KEEP\_RAW             | Keeps SMT and Token Ring MAC frames.                                                                                                                                                                                                                        |



 

## Etype/SAP Capture Filter Settings

Use the following information to set the **lpSapTable** and **lpEtypeTable** members of the [**CAPTUREFILTER**](capturefilter.md) structure.



| Setting          | Meaning                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **lpSapTable**   | Lists the SAP values that you want the driver to pass. This list tells the Network Monitor driver to validate any frame that contains a match. If CAPTUREFILTER\_FLAGS\_INCLUDE\_ALL\_SAPS is set, this becomes an exception list (if found, do not pass).           |
| **lpEtypeTable** | Lists the Etype values that you want the Network Monitor driver to pass. This list alone tells the driver to validate any frame that contains a match. If CAPTUREFILTER\_FLAGS\_INCLUDE\_ALL\_ETYPES is set, this becomes an exception list (if found, do not pass). |



 

 

 




