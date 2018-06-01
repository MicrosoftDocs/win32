---
Description: The following are practices for writing secure applications for use with Indexing Service.
ms.assetid: 9095ad80-3f2a-44e1-8ade-f4d318651264
title: Secure Code Practices
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Secure Code Practices

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

The following are practices for writing secure applications for use with Indexing Service.

## Query Applications

When writing query applications, you should choose the API that runs in a security context that allows the user the least privilege. For example, ASP pages can use the IXSSO query object, which runs as a user process.

## IFilters and Language Resources

-   IFilters, word breakers, and stemmers for Indexing Service run in the Local Security context. They should be written to manage buffers and to stack correctly. All string copies must have explicit checks to guard against buffer overruns. You should always verify the allocated size of the buffer and test the size of the data against the size of the buffer. Buffer overruns are a common technique for exploiting code that does not enforce buffer size restrictions.
-   IFilter, word breaker and stemmer components should never call [**ExitProcess**](https://msdn.microsoft.com/windows/desktop/c26dbf15-62e8-4892-b7c5-2e6c085e4cd5) or any similar API that terminates a process and all its threads.
-   Do not allocate or free resources in the [*DllMain*](https://msdn.microsoft.com/windows/desktop/0c3e3083-9297-4626-b2a7-0062d1c2cf9e) entry point. This can lead to failures during low-resource stress tests.
-   Code all objects to be thread-safe. Indexing Service calls any one instance of a word breaker or stemmer in one thread at a time, but it may call multiple instances at the same time across multiple threads.
-   Avoid creating temporary files or writing to the registry.
-   If you use the Microsoft Visual C++ compiler, ensure that you compile your application using the /GS option. The /GS option is used to detect buffer overruns. The /GS option places security checks into the compiled code. For more information, see [/GS (Buffer Security Check)](http://msdn.microsoft.com/en-us/library/8dbf701c.aspx) in the Visual C++ Compiler Options.

## Query Forms for use with Internet Information Services (IIS)

When creating query forms for use with IIS, be sure to do the following.

-   Display only virtual paths for query results. Displaying physical paths reveals details about a server that can be used in an exploit.
-   Always HTML Encode user input when displaying it on result pages. For example, if you display a user's query in the query results page, you must HTML Encode the query. If a query contains script, that script will execute in the user’s browser and can be used for exploits.
-   Create hit highlighting template files (.htw) in the same directory as the content if you have a mix of HTTP and HTTPS content on a site. This is not enforced by Webhits, and is therefore the authors responsibility.

 

 



