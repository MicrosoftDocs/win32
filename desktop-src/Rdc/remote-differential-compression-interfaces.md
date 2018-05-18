---
title: Remote Differential Compression Interfaces
description: Enable synchronization between two locations with an efficient use of bandwidth between the locations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a3131654-e849-4a88-acec-c49a61653bad'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-differential-compression'
ms.tgt_platform: multiple
---

# Remote Differential Compression Interfaces

RDC provides the following COM interfaces that enable synchronization between two locations with an efficient use of bandwidth between the locations.



| Interface                                                                    | Description                                                                                                                                                                                 |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IFindSimilarResults**](ifindsimilarresults.md)                           | Provides methods for retrieving information from the file list returned by the [**ISimilarity::FindSimilarFileId**](isimilarity-findsimilarfileid.md) method.                              |
| [**IRdcComparator**](irdccomparator.md)                                     | Compares two signature streams (seed and source) and produces the list of seed and source file data chunks needed to create the target file.                                                |
| [**IRdcFileReader**](irdcfilereader.md)                                     | Provides the equivalent of a file handle, because the data being synchronized may not exist as a file on disk.                                                                              |
| [**IRdcGenerator**](irdcgenerator.md)                                       | Processes the input data and reads the parameters used by the generator.                                                                                                                    |
| [**IRdcGeneratorFilterMaxParameters**](irdcgeneratorfiltermaxparameters.md) | Sets and retrieves parameters used by the FilterMax generator.                                                                                                                              |
| [**IRdcGeneratorParameters**](irdcgeneratorparameters.md)                   | The generic interface for all types of generator parameters. All generator parameter objects must support this interface.                                                                   |
| [**IRdcLibrary**](irdclibrary.md)                                           | The primary interface for using RDC.                                                                                                                                                        |
| [**IRdcSignatureReader**](irdcsignaturereader.md)                           | Reads the signatures and the parameters used to generate the signatures.                                                                                                                    |
| [**IRdcSimilarityGenerator**](irdcsimilaritygenerator.md)                   | Defines methods for enabling the signature generator to generate similarity data and for retrieving the similarity data after it is generated.                                              |
| [**ISimilarity**](isimilarity.md)                                           | Defines methods for storing and retrieving per-file similarity data and file IDs in a similarity file.                                                                                      |
| [**ISimilarityFileIdTable**](isimilarityfileidtable.md)                     | Defines methods for storing and retrieving similarity file ID information.                                                                                                                  |
| [**ISimilarityReportProgress**](isimilarityreportprogress.md)               | Defines a method for RDC to report the current completion percentage of a similarity operation.                                                                                             |
| [**ISimilarityTableDumpState**](isimilaritytabledumpstate.md)               | Provides a method for retrieving information from the similarity traits list that was returned by the [**ISimilarityTraitsTable::BeginDump**](isimilaritytraitstable-begindump.md) method. |
| [**ISimilarityTraitsTable**](isimilaritytraitstable.md)                     | Defines methods for storing per-file similarity data and performing similarity lookups.                                                                                                     |



 

 

 




