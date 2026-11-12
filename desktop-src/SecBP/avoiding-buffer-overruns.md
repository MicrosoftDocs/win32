---
description: Provides a brief introduction to a few types of buffer overrun situations and offers some ideas and resources to help you avoid creating new risks and mitigate existing ones.
ms.assetid: 713fd6de-16af-49d2-8940-763c4a6e414b
title: Avoiding Buffer Overruns
ms.topic: concept-article
ms.date: 07/16/2026
---

# Avoiding Buffer Overruns

A buffer overrun is one of the most common sources of security risk. A buffer overrun is essentially caused by treating unchecked, external input as trustworthy data. The act of copying this data, using operations such as [**CopyMemory**](/previous-versions/windows/desktop/legacy/aa366535(v=vs.85)), **strcat**, **strcpy**, or **wcscpy**, can create unanticipated results, which allows for system corruption. In the best of cases, your application will abort with a core dump, segmentation fault, or access violation. In the worst of cases, an attacker can exploit the buffer overrun by introducing and executing other malicious code in your process. Copying unchecked, input data into a stack-based buffer is the most common cause of exploitable faults.

> [!WARNING]
> Never use unbounded string functions (`strcpy`, `strcat`, `sprintf`, `gets`) in security-sensitive code. Replace them with their bounded equivalents (`StringCbCopy`, `StringCbCat`, `StringCbPrintf`) from the [safe string library](/windows/win32/api/strsafe/) or use the C11 `_s` suffix variants (`strcpy_s`, `strcat_s`).

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

## Compiler and linker mitigations

Modern versions of the Microsoft C/C++ compiler and linker provide multiple layers of defense against buffer overruns. Always enable these protections in production builds:

| Flag | Purpose |
|------|---------|
| `/GS` | Stack buffer overrun detection (enabled by default). Inserts security cookies before return addresses. |
| `/sdl` | Enables additional security checks including stricter `/GS` behavior and variable initialization. |
| `/DYNAMICBASE` | Address Space Layout Randomization (ASLR). Randomizes load addresses to make exploitation harder. |
| `/NXCOMPAT` | Data Execution Prevention (DEP). Marks memory pages as non-executable. |
| `/CETCOMPAT` | Intel Control-flow Enforcement Technology (CET) for hardware-enforced shadow stacks. |
| `/guard:cf` | [Control Flow Guard (CFG)](control-flow-guard.md). Validates indirect call targets at runtime. |

> [!IMPORTANT]
> Compile with `/sdl` and `/GS` at minimum for all new code. For security-critical applications, also enable `/guard:cf` and link with `/CETCOMPAT` when targeting hardware that supports CET.

## Runtime analysis tools

Use these tools during development and testing to detect memory safety issues before they reach production:

- **AddressSanitizer (ASan):** Compile with `/fsanitize=address` to detect buffer overflows, use-after-free, and other memory errors at runtime. Available in Visual Studio 2019 16.9 and later.
- **Application Verifier:** Detects heap corruption, handle misuse, and other common programming errors.
- **Static Analysis (`/analyze`):** The built-in static analyzer detects buffer overruns, uninitialized variables, and other issues at compile time.

## Related topics

- [Control Flow Guard](control-flow-guard.md)
- [Safe string functions](/windows/win32/api/strsafe/)

