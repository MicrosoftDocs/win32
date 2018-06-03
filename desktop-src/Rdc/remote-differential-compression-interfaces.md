---
title: Remote Differential Compression Interfaces
description: Enable synchronization between two locations with an efficient use of bandwidth between the locations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a3131654-e849-4a88-acec-c49a61653bad
ms.prod: windows-server-dev
ms.technology: remote-differential-compression
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remote Differential Compression Interfaces

RDC provides the following COM interfaces that enable synchronization between two locations with an efficient use of bandwidth between the locations.



| Interface                                                                    | Description                                                                                                                                                                                 |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IFindSimilarResults**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-ifindsimilarresults)                           | Provides methods for retrieving information from the file list returned by the [**ISimilarity::FindSimilarFileId**](/previous-versions/windows/desktop/api/MsRdc/nf-msrdc-isimilarity-findsimilarfileid) method.                              |
| [**IRdcComparator**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-irdccomparator)                                     | Compares two signature streams (seed and source) and produces the list of seed and source file data chunks needed to create the target file.                                                |
| [**IRdcFileReader**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-irdcfilereader)                                     | Provides the equivalent of a file handle, because the data being synchronized may not exist as a file on disk.                                                                              |
| [**IRdcGenerator**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-irdcgenerator)                                       | Processes the input data and reads the parameters used by the generator.                                                                                                                    |
| [**IRdcGeneratorFilterMaxParameters**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-irdcgeneratorfiltermaxparameters) | Sets and retrieves parameters used by the FilterMax generator.                                                                                                                              |
| [**IRdcGeneratorParameters**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-irdcgeneratorparameters)                   | The generic interface for all types of generator parameters. All generator parameter objects must support this interface.                                                                   |
| [**IRdcLibrary**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-irdclibrary)                                           | The primary interface for using RDC.                                                                                                                                                        |
| [**IRdcSignatureReader**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-irdcsignaturereader)                           | Reads the signatures and the parameters used to generate the signatures.                                                                                                                    |
| [**IRdcSimilarityGenerator**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-irdcsimilaritygenerator)                   | Defines methods for enabling the signature generator to generate similarity data and for retrieving the similarity data after it is generated.                                              |
| [**ISimilarity**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-isimilarity)                                           | Defines methods for storing and retrieving per-file similarity data and file IDs in a similarity file.                                                                                      |
| [**ISimilarityFileIdTable**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-isimilarityfileidtable)                     | Defines methods for storing and retrieving similarity file ID information.                                                                                                                  |
| [**ISimilarityReportProgress**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-isimilarityreportprogress)               | Defines a method for RDC to report the current completion percentage of a similarity operation.                                                                                             |
| [**ISimilarityTableDumpState**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-isimilaritytabledumpstate)               | Provides a method for retrieving information from the similarity traits list that was returned by the [**ISimilarityTraitsTable::BeginDump**](/previous-versions/windows/desktop/api/MsRdc/nf-msrdc-isimilaritytraitstable-begindump) method. |
| [**ISimilarityTraitsTable**](/previous-versions/windows/desktop/api/MsRdc/nn-msrdc-isimilaritytraitstable)                     | Defines methods for storing per-file similarity data and performing similarity lookups.                                                                                                     |



 

 

 




