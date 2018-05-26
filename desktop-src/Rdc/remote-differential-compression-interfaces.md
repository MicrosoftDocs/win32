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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remote Differential Compression Interfaces

RDC provides the following COM interfaces that enable synchronization between two locations with an efficient use of bandwidth between the locations.



| Interface                                                                    | Description                                                                                                                                                                                 |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IFindSimilarResults**](/windows/previous-versions/MsRdc/nn-msrdc-ifindsimilarresults?branch=master)                           | Provides methods for retrieving information from the file list returned by the [**ISimilarity::FindSimilarFileId**](/windows/previous-versions/MsRdc/nf-msrdc-isimilarity-findsimilarfileid?branch=master) method.                              |
| [**IRdcComparator**](/windows/previous-versions/MsRdc/nn-msrdc-irdccomparator?branch=master)                                     | Compares two signature streams (seed and source) and produces the list of seed and source file data chunks needed to create the target file.                                                |
| [**IRdcFileReader**](/windows/previous-versions/MsRdc/nn-msrdc-irdcfilereader?branch=master)                                     | Provides the equivalent of a file handle, because the data being synchronized may not exist as a file on disk.                                                                              |
| [**IRdcGenerator**](/windows/previous-versions/MsRdc/nn-msrdc-irdcgenerator?branch=master)                                       | Processes the input data and reads the parameters used by the generator.                                                                                                                    |
| [**IRdcGeneratorFilterMaxParameters**](/windows/previous-versions/MsRdc/nn-msrdc-irdcgeneratorfiltermaxparameters?branch=master) | Sets and retrieves parameters used by the FilterMax generator.                                                                                                                              |
| [**IRdcGeneratorParameters**](/windows/previous-versions/MsRdc/nn-msrdc-irdcgeneratorparameters?branch=master)                   | The generic interface for all types of generator parameters. All generator parameter objects must support this interface.                                                                   |
| [**IRdcLibrary**](/windows/previous-versions/MsRdc/nn-msrdc-irdclibrary?branch=master)                                           | The primary interface for using RDC.                                                                                                                                                        |
| [**IRdcSignatureReader**](/windows/previous-versions/MsRdc/nn-msrdc-irdcsignaturereader?branch=master)                           | Reads the signatures and the parameters used to generate the signatures.                                                                                                                    |
| [**IRdcSimilarityGenerator**](/windows/previous-versions/MsRdc/nn-msrdc-irdcsimilaritygenerator?branch=master)                   | Defines methods for enabling the signature generator to generate similarity data and for retrieving the similarity data after it is generated.                                              |
| [**ISimilarity**](/windows/previous-versions/MsRdc/nn-msrdc-isimilarity?branch=master)                                           | Defines methods for storing and retrieving per-file similarity data and file IDs in a similarity file.                                                                                      |
| [**ISimilarityFileIdTable**](/windows/previous-versions/MsRdc/nn-msrdc-isimilarityfileidtable?branch=master)                     | Defines methods for storing and retrieving similarity file ID information.                                                                                                                  |
| [**ISimilarityReportProgress**](/windows/previous-versions/MsRdc/nn-msrdc-isimilarityreportprogress?branch=master)               | Defines a method for RDC to report the current completion percentage of a similarity operation.                                                                                             |
| [**ISimilarityTableDumpState**](/windows/previous-versions/MsRdc/nn-msrdc-isimilaritytabledumpstate?branch=master)               | Provides a method for retrieving information from the similarity traits list that was returned by the [**ISimilarityTraitsTable::BeginDump**](/windows/previous-versions/MsRdc/nf-msrdc-isimilaritytraitstable-begindump?branch=master) method. |
| [**ISimilarityTraitsTable**](/windows/previous-versions/MsRdc/nn-msrdc-isimilaritytraitstable?branch=master)                     | Defines methods for storing per-file similarity data and performing similarity lookups.                                                                                                     |



 

 

 




