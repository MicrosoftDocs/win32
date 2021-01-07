---
description: Provides a brief introduction to a few types of buffer overrun situations and offers some ideas and resources to help you avoid creating new risks and mitigate existing ones.
ms.assetid: 713fd6de-16af-49d2-8940-763c4a6e414b
title: Avoiding Buffer Overruns
ms.topic: article
ms.date: 05/31/2018
---

# Avoiding Buffer Overruns

A buffer overrun is one of the most common sources of security risk. A buffer overrun is essentially caused by treating unchecked, external input as trustworthy data. The act of copying this data, using operations such as [**CopyMemory**](/previous-versions/windows/desktop/legacy/aa366535(v=vs.85)), **strcat**, **strcpy**, or **wcscpy**, can create unanticipated results, which allows for system corruption. In the best of cases, your application will abort with a core dump, segmentation fault, or access violation. In the worst of cases, an attacker can exploit the buffer overrun by introducing and executing other malicious code in your process. Copying unchecked, input data into a stack-based buffer is the most common cause of exploitable faults.

Buffer overruns can occur in a variety of ways. The following list provides a brief introduction to a few types of buffer overrun situations and offers some ideas and resources to help you avoid creating new risks and mitigate existing ones:

<dl> <dt>

<span id="Static_buffer_overruns"></span><span id="static_buffer_overruns"></span><span id="STATIC_BUFFER_OVERRUNS"></span>Static buffer overruns
</dt> <dd>

A static buffer overrun occurs when a buffer, which has been declared on the stack, is written to with more data than it was allocated to hold. The less apparent versions of this error occur when unverified user input data is copied directly to a static variable, causing potential stack corruption.

</dd> <dt>

<span id="Heap_overruns"></span><span id="heap_overruns"></span><span id="HEAP_OVERRUNS"></span>Heap overruns
</dt> <dd>

Heap overruns, like static buffer overruns, can lead to memory and stack corruption. Because heap overruns occur in heap memory rather than on the stack, some people consider them to be less able to cause serious problems; nevertheless, heap overruns require real programming care and are just as able to allow system risks as static buffer overruns.

</dd> <dt>

<span id="Array_indexing_errors"></span><span id="array_indexing_errors"></span><span id="ARRAY_INDEXING_ERRORS"></span>Array indexing errors
</dt> <dd>

Array indexing errors also are a source of memory overruns. Careful bounds checking and index management will help prevent this type of memory overrun.

</dd> </dl>

Preventing buffer overruns is primarily about writing good code. Always validate all your inputs and fail gracefully when necessary. For more information about writing secure code, see the following resources:

-   Maguire, Steve \[1993\], *Writing Solid Code*, ISBN 1-55615-551-4, Microsoft Press, Redmond, Washington.
-   Howard, Michael and LeBlanc, David \[2003\], *Writing Secure Code*, 2d ed., ISBN 0-7356-1722-8, Microsoft Press, Redmond, Washington.

> [!Note]  
> These resources may not be available in some languages and countries.

 

Safe string handling is a long-standing issue that continues to be addressed both by following good programming practices and often by using and retrofitting existing systems with secure, string-handling functions. An example of such a set of functions for the Windows shell starts with [**StringCbCat**](/windows/win32/api/strsafe/nf-strsafe-stringcbcata).

 

 
