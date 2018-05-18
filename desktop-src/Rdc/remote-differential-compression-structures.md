---
title: Remote Differential Compression Structures
description: The following structures are defined in RDC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5144a94b-4af8-4ac2-b5b3-f0674a51c03b'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-differential-compression'
ms.tgt_platform: multiple
---

# Remote Differential Compression Structures

The following structures are defined in RDC.



| Structure                                                          | Description                                                                                                                                                                           |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FindSimilarFileIndexResults**](findsimilarfileindexresults.md) | Contains the file index information that the [**ISimilarityTraitsTable::FindSimilarFileIndex**](isimilaritytraitstable-findsimilarfileindex.md) method returned for a matching file. |
| [**RdcBufferPointer**](rdcbufferpointer.md)                       | Describes an input or output buffer.                                                                                                                                                  |
| [**RdcNeed**](rdcneed.md)                                         | Describes a chunk that is required to synchronize two sets of data.                                                                                                                   |
| [**RdcNeedPointer**](rdcneedpointer.md)                           | Describes what chunks from the source or seed data are required to create the target data.                                                                                            |
| [**RdcSignature**](rdcsignature.md)                               | Describe a signature and the length of the chunk used to generate the signature.                                                                                                      |
| [**RdcSignaturePointer**](rdcsignaturepointer.md)                 | Describes an array of [**RdcSignature**](rdcsignature.md) structures.                                                                                                                |
| [**SimilarityData**](similaritydata.md)                           | Contains the similarity data for a file.                                                                                                                                              |
| [**SimilarityDumpData**](similaritydumpdata.md)                   | Contains the similarity information that was returned for a file by the [**ISimilarityTableDumpState::GetNextData**](isimilaritytabledumpstate-getnextdata.md) method.               |
| [**SimilarityFileId**](similarityfileid.md)                       | Contains the similarity file ID for a file.                                                                                                                                           |
| [**SimilarityMappedViewInfo**](similaritymappedviewinfo.md)       | Contains information about a similarity mapped view.                                                                                                                                  |



 

 

 




