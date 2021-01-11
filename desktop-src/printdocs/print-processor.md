---
description: The print spooler monitors the current print jobs and the target printer to determine an appropriate time to print a job.
ms.assetid: c3ce7c63-b72d-4e91-9509-5189f2ccac8a
title: Print Processor
ms.topic: article
ms.date: 05/31/2018
---

# Print Processor

The print spooler monitors the current print jobs and the target printer to determine an appropriate time to print a job. Once the spooler determines that a job should be printed, it calls the print processor. The print processor is a plug-in that processes print job data.

Use the following functions to work with print processors.



| Function                                                           | Description                                                          |
|--------------------------------------------------------------------|----------------------------------------------------------------------|
| [**AddPrintProcessor**](addprintprocessor.md)                     | Installs a print processor on a specified server.                    |
| [**DeletePrintProcessor**](deleteprintprocessor.md)               | Removes a printer processor from a specified server.                 |
| [**EnumPrintProcessorDatatypes**](enumprintprocessordatatypes.md) | Enumerates the data types that a specified print processor supports. |
| [**EnumPrintProcessors**](enumprintprocessors.md)                 | Enumerates the print processors installed on a specified server.     |
| [**GetPrintProcessorDirectory**](getprintprocessordirectory.md)   | Retrieves the path for the print processor on the specified server.  |



 

 

 



