---
title: SmpFilt Sample
description: SmpFilt Sample
ms.assetid: 5ceab72d-008a-4e20-b461-2cf2d0cd89e6
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SmpFilt Sample

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The SmpFilt sample is an example [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) implementation that reads an unformatted text file (with the extension .smp), using the ANSI code page of the current thread, and outputs UNICODE text for the current locale. It accepts as input only single-byte-character text files and not multibyte-character or UNICODE text files. It is the simplest sample of an **IFilter** implementation included in the Indexing Service sample code.

Source: mssdk\\samples\\winbase\\indexing\\smpfilt\\

**To build the sample**

1.  Set the Lib environment variable to "D:\\mssdk\\Lib;%Lib%" and the Include environment variable to "D:\\mssdk\\Include;%Include%", where D: is the drive on which you installed the Platform SDK.

2.  Correctly set the CPU environment variable to, for example, "i386".

3.  Open a command window and change the directory to the source path of the sample.

4.  Build the filter DLL by entering, at the command-line prompt, "nmake".

**To register the sample**

1.  Copy the filter DLL file SmpFilt.dll to your %windir%\\System32 directory.

2.  Self-register the filter by entering, at the command-line prompt, "regsvr32.exe %windir%\\System32\\SmpFilt.dll".

3.  Enable automatic registration of the filter by adding it to the MULTI\_SZ value of the [**DLLsToRegister**](dllstoregister.md) entry in the registry under the following key.

    **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\ContentIndex**

**To filter files and submit queries using the sample**

1.  Create one or more files to filter. For example, copy the source file SmpFilt.cxx to a file named SmpFilt.smp.

2.  Restart the cisvc service. Touch the .smp files and wait for Indexing Service to filter them.

3.  Formulate queries that you know will succeed on the .smp files and submit them using the Indexing Service MMC snap-in or one of the sample query programs in the Platform SDK.

### Programming Notes

The SmpFilt sample illustrates the basic structure of a filter. It minimally implements the methods of the [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) and [**IPersistFile**](https://www.bing.com/search?q=**IPersistFile**) interfaces. Because the SmpFilt sample does not filter any value-type properties, the implementation of [**IFilter::GetChunk**](/windows/desktop/api/Filter/nf-filter-ifilter-getchunk) does not process properties other than "contents," and [**IFilter::GetValue**](/windows/desktop/api/Filter/nf-filter-ifilter-getvalue) always indicates no values. For examples of how to filter value-type properties as well as text, refer to the [IFilter Sample](ifilter-sample.md) (HtmlFilt) or the [HtmlProp Sample](htmlprop-sample.md) in the Platform SDK.

Error-handling in the SmpFilt sample is rudimentary. The sample handles only the most obvious error conditions. Comments in the source code list all the standard result codes and indicate whether they are implemented. If you use SmpFilt as a basis for your own filter, carefully determine the additional error conditions that you need to detect and handle.

 

 




