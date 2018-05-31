---
title: Testing Filters
description: Testing Filters
ms.assetid: 66f596d0-3416-4792-9e84-dba46dbf85ce
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Testing Filters

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

You can test your filter implementations using the programs of the IFilter Test Suite. The IFilter Test Suite can validate [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface implementations by calling **IFilter** methods and checking the returned values for compliance with the **IFilter** interface specification. Programs of the Test Suite will, for example, check that chunk identifiers are unique and increasing, that the **IFilter** interface behaves consistently after reinitialization, and that **IFilter**method calls with invalid parameters return expected error codes. The programs will also dump the output of a file filtered by an **IFilter** interface implementation and check the filter registration information in the registry.

The IFilter Test Suite consists of three programs, ifilttst.exe, filtdump.exe, and filtreg.exe, plus an initialization file, ifilttst.ini. The programs are all command-line applications. The IFilter Test Suite requires Indexing Service and Internet Information Services (IIS).

The topics in this section describe how to test your filter implementations using the IFilter Test Suite.

-   [Command-Line Invocation](command-line-invocation.md)
-   [The ifilttst.ini File](the-ifilttst-ini-file.md)
-   [Sample IfiltTst.ini File](sample-ifilttst-ini-file.md)
-   [IFilter Test Procedure](ifilter-test-procedure.md)
-   [Sample Log File](sample-log-file.md)
-   [Sample Dump File](sample-dump-file.md)

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 




