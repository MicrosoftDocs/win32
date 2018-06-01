---
Description: IFilter Sample
ms.assetid: b6565c41-41f8-4e56-b166-d2d9abd00987
title: IFilter Sample
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IFilter Sample

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IFilter** sample (HtmlFilt) is an example [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) implementation for HTML files. It is more complex than the basic text filter, because it demonstrates techniques for filtering both text-type and value-type properties.

Source: mssdk\\samples\\winbase\\indexing\\ifilter\\

**To build the sample**

1.  Set the Lib environment variable to "D:\\mssdk\\Lib;%Lib%" and the Include environment variable to "D:\\mssdk\\Include;%Include%", where D: is the drive on which you installed the Platform SDK.

2.  Correctly set the CPU environment variable, for example to "i386".

3.  Open a command window and change the directory to the source path of the sample.

4.  Build the filter DLL by entering, at the command-line prompt, "nmake".

**To register the sample**

1.  Copy the filter DLL file HtmlFilt.dll to your %windir%\\System32 directory.

2.  Self-register the filter by entering, at the command-line prompt: "regsvr32.exe %windir%\\System32\\HtmlFilt.dll".

3.  Enable automatic registration of the filter by adding it to the MULTI\_SZ value of the [DLLsToRegister](dllstoregister.md) entry in the registry under the following key.

    **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\ContentIndex**

4.  Remove the default HTML filter, nlhtml.dll, from the registry key given in Step 3. If you don't perform this step, the default HTML filter will re-register when Indexing Service starts.

**To filter files and submit queries using the sample**

1.  Create one or more appropriate HTML files to filter. Or, check that you already have one or more HTML files with the appropriate sample title, headings, and anchors.

2.  Restart the cisvc service. Touch the HTML files and wait for Indexing Service to filter them.

3.  Formulate queries that you know will succeed on the HTML files and submit them using the Indexing Service MMC snap-in or one of the sample query programs in the Platform SDK.

### Programming Notes

HTMLFilt will extract text-type and value-type properties from HTML pages. In addition to the body of the text as a text-type property, headings (levels 1 to 6), title, and anchors are extracted as internal value-type properties available using the [**IFilter::GetValue**](/windows/desktop/api/Filter/nf-filter-ifilter-getvalue) method.

 

 



