---
title: Sample Log File
description: Sample Log File
ms.assetid: 77d5c3d8-aa1e-42c7-94de-105333a1c8f3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sample Log File

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

When requested, the Ifilttst.exe program produces a log containing a description of the steps it takes during execution. Here are some excerpts from a log file, with the verbosity set to 3 (highest verbosity).


```CSharp
1. INFO----**** New configuration ****
2. 
3. Section name : Test2
4. grfFlags     : 63
5. cAttributes  : 0
6. aAttributes  : NONE
7. pdwFlags     : 0
8. 
9. INFO----Successfully bound filter.
10. 
11. PASS----Init() returned a valid value for pdwFlags.
12. 
13. INFO----Successfully initialized filter.
14. 
15. INFO----Performing validation test. In this part of the test, the chunks structures
16.         returned by the filter are checked for correctness, and the return values
17.         of the filter calls are checked.
18. 
19. PASS----GetChunk() succeeded.
20. 
21. PASS----The current chunk has a legal value for the flags field.
```



The first line is an informational message, indicating that a new configuration has been loaded from the ifilttst.ini file. Line (3) indicates the section name in the ifilttst.ini file from which the current configuration has been read. Lines (4) through (7) list the parameters to **IFilter::Init**. The lines starting with "INFO" are informational messages about the binding of the filter and start of the validation test. Lines starting with "PASS" are messages regarding specific tests that have passed.

``` syntax
WARNING-First call to GetText() returned FILTER_E_NO_MORE_TEXT.
```

The line above is a warning. Warnings call attention to filter behavior that is problematic, although legal. The above warning indicates that the **IFilter::GetChunk** method has returned a text chunk that contains no text.

``` syntax
ERROR---The filter has emitted a chunk which it was not requested to emit. Check
    the initialization parameters in section Test1 of the initialization file.
 
INFO----Current chunk propid : 0x5
```

Here is an example of an error message. In this case, the filter has emitted a chunk with a property identifier (ID) of 0x5. Inspection of section \[Test1\] in ifilttst.ini would show that the filter was configured to not emit chunks with this propid. For example, if neither IFILTER\_INIT\_APPLY\_INDEX\_ATTRIBUTES nor IFILTER\_INIT\_APPLY\_OTHER\_ATTRIBUTES was specified in the **Flags** entry and if cAttributes was 0, the filter would emit only chunks with a property ID of 0x13, corresponding to PID\_STG\_CONTENTS.

 

 




