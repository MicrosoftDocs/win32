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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remote Differential Compression Structures

The following structures are defined in RDC.



| Structure                                                          | Description                                                                                                                                                                           |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FindSimilarFileIndexResults**](/previous-versions/windows/desktop/api/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0013) | Contains the file index information that the [**ISimilarityTraitsTable::FindSimilarFileIndex**](/previous-versions/windows/desktop/api/MsRdc/nf-msrdc-isimilaritytraitstable-findsimilarfileindex) method returned for a matching file. |
| [**RdcBufferPointer**](/previous-versions/windows/desktop/api/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0005)                       | Describes an input or output buffer.                                                                                                                                                  |
| [**RdcNeed**](/previous-versions/windows/desktop/api/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0004)                                         | Describes a chunk that is required to synchronize two sets of data.                                                                                                                   |
| [**RdcNeedPointer**](/previous-versions/windows/desktop/api/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0006)                           | Describes what chunks from the source or seed data are required to create the target data.                                                                                            |
| [**RdcSignature**](/previous-versions/windows/desktop/api/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0007)                               | Describe a signature and the length of the chunk used to generate the signature.                                                                                                      |
| [**RdcSignaturePointer**](/previous-versions/windows/desktop/api/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0008)                 | Describes an array of [**RdcSignature**](/previous-versions/windows/desktop/api/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0007) structures.                                                                                                                |
| [**SimilarityData**](/previous-versions/windows/desktop/api/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0012)                           | Contains the similarity data for a file.                                                                                                                                              |
| [**SimilarityDumpData**](/previous-versions/windows/desktop/api/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0014)                   | Contains the similarity information that was returned for a file by the [**ISimilarityTableDumpState::GetNextData**](/previous-versions/windows/desktop/api/MsRdc/nf-msrdc-isimilaritytabledumpstate-getnextdata) method.               |
| [**SimilarityFileId**](/previous-versions/windows/desktop/api/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0015)                       | Contains the similarity file ID for a file.                                                                                                                                           |
| [**SimilarityMappedViewInfo**](/previous-versions/windows/desktop/api/MsRdc/ns-msrdc-__midl___midl_itf_msrdc_0000_0000_0011)       | Contains information about a similarity mapped view.                                                                                                                                  |



 

 

 




