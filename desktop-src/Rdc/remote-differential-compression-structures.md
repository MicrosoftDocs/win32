---
title: Remote Differential Compression Structures
description: The following structures are defined in RDC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5144a94b-4af8-4ac2-b5b3-f0674a51c03b
ms.prod: windows-server-dev
ms.technology: remote-differential-compression
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remote Differential Compression Structures

The following structures are defined in RDC.



| Structure                                                          | Description                                                                                                                                                                           |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FindSimilarFileIndexResults**](/windows/previous-versions/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0013?branch=master) | Contains the file index information that the [**ISimilarityTraitsTable::FindSimilarFileIndex**](/windows/previous-versions/MsRdc/nf-msrdc-isimilaritytraitstable-findsimilarfileindex?branch=master) method returned for a matching file. |
| [**RdcBufferPointer**](/windows/previous-versions/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0005?branch=master)                       | Describes an input or output buffer.                                                                                                                                                  |
| [**RdcNeed**](/windows/previous-versions/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0004?branch=master)                                         | Describes a chunk that is required to synchronize two sets of data.                                                                                                                   |
| [**RdcNeedPointer**](/windows/previous-versions/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0006?branch=master)                           | Describes what chunks from the source or seed data are required to create the target data.                                                                                            |
| [**RdcSignature**](/windows/previous-versions/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0007?branch=master)                               | Describe a signature and the length of the chunk used to generate the signature.                                                                                                      |
| [**RdcSignaturePointer**](/windows/previous-versions/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0008?branch=master)                 | Describes an array of [**RdcSignature**](/windows/previous-versions/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0007?branch=master) structures.                                                                                                                |
| [**SimilarityData**](/windows/previous-versions/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0012?branch=master)                           | Contains the similarity data for a file.                                                                                                                                              |
| [**SimilarityDumpData**](/windows/previous-versions/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0014?branch=master)                   | Contains the similarity information that was returned for a file by the [**ISimilarityTableDumpState::GetNextData**](/windows/previous-versions/MsRdc/nf-msrdc-isimilaritytabledumpstate-getnextdata?branch=master) method.               |
| [**SimilarityFileId**](/windows/previous-versions/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0015?branch=master)                       | Contains the similarity file ID for a file.                                                                                                                                           |
| [**SimilarityMappedViewInfo**](/windows/previous-versions/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0011?branch=master)       | Contains information about a similarity mapped view.                                                                                                                                  |



 

 

 




