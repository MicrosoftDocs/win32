---
Description: IFiltTst
ms.assetid: 53a56ff7-882b-497b-b902-83cb54737d35
title: IFiltTst
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IFiltTst

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The IFiltTst.exe program runs several tests to validate an [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface implementation. You invoke IFiltTst from the command line as follows:

**ifilttst /i test.htm /l /d /v 1**

The preceding command line directs the program to filter the file "test.htm," redirect the log messages to "test.htm.log", redirect the dump messages to "test.htm.dmp", and set the verbosity to 1.

> [!Note]  
> You must include a space between the command line switch and the value.

 

For the preceding command to work, three files must be located in the current working directory: ifilttst.exe, ifilttst.ini, and test.htm. The ifilttst.ini file is described in [The ifilttst.ini File](the-ifilttst-ini-file.md).

The command-line switches can include the following parameters.



| Parameter              | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /i &lt;file name&gt;   | The input file or directory to be filtered. The file name can contain the wildcard characters \* and ?.                                                                                                                                                                                                                                                                                                                                                                                                         |
| /l                     | Log messages are directed to a file, rather than the screen. Log messages describe the individual tests performed and the pass/fail result of the test. The log file name is the same as the input file name with a .log extension.                                                                                                                                                                                                                                                                             |
| /d                     | Dump messages are directed to a file instead of the screen. Dump messages describe the contents of the chunks. The chunk structure is dumped when the verbosity level is 3. The dump file name is the same as the input file name with a .dmp extension.                                                                                                                                                                                                                                                        |
| /-l                    | Disable logging. This flag overrides the */l* parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| /-d                    | Disable dumping. This flag overrides the */d* parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| /v &lt;integer&gt;     | The verbosity level. The default is 3. 0 — The test logs only messages concerning specific [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface failures. The test dumps the chunk contents.<br/> 1 — The test logs warning messages as well as those for level 0.<br/> 2 — The test logs messages concerning tests that passed as well as those for level 1.<br/> 3 — The test logs informational messages as well as those for level 2. In addition, the test dumps the structure of the chunks.<br/> |
| /t &lt;integer&gt;     | The number of threads to launch. One by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| /r \[&lt;integer&gt;\] | Recursively filters subdirectories. The optional integer parameter specifies the depth to which to recurse. If no integer is specified, or if the integer is 0, full recursion is assumed. By default, the recursion depth is 1.                                                                                                                                                                                                                                                                                |
| /c &lt;integer&gt;     | The number of times to loop. If the integer is 0, the test loops infinitely. By default, the test loops only once.                                                                                                                                                                                                                                                                                                                                                                                              |



 

 

 




