---
title: FiltDump
description: FiltDump
ms.assetid: be2bc16b-11c0-4f10-9261-9f230ce6753b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FiltDump

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The FiltDump.exe program loads an [IFilter](/windows/win32/Filter/nn-filter-ifilter?branch=master) interface implementation for a specified document and prints the output produced by the filter DLL. You invoke the filtdump.exe program from the command line as follows:

**filtdump** *filename.ext*

FiltDump uses the [LoadIFilter](/windows/win32/Ntquery/nf-ntquery-loadifilter?branch=master) function to load the filter DLL appropriate for the specified file name extension and prints the filtered results. For example, the following command instructs filtdump.exe to load the [smpfilt.dll filter](smpfilt-sample.md) for the extension .smp, extract all text and properties from the file myfile.smp, and print the results:

**filtdump myfile.smp**

 

 




