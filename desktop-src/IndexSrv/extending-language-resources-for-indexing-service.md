---
title: Extending Language Resources for Indexing Service
description: Extending Language Resources for Indexing Service
ms.assetid: 47e18e5e-b877-4471-b44d-1c66d1291358
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extending Language Resources for Indexing Service

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service uses language resources such as word breakers and stemmers to break text in its native locale during index creation and query processing. Microsoft provides word breakers and stemmers for a number of languages.

This section describes how to implement and use custom word breakers and stemmers for languages and locales not provided for by Microsoft. This section contains the following topics:

-   [About Language Resources](about-language-resources.md) describes how the Indexing Service language resources process text and properties in their native locale.
-   [Applying Language Resources](applying-language-resources.md) describes how the index building and querying process for Indexing Service determines which language resources to use for a particular file.
-   [Constructing Language Resource Components](constructing-language-resource-components.md) describes how to create custom word breakers and stemmers.
-   [Linguistic and Unicode Considerations](linguistic-and-unicode-considerations.md) describes a variety of linguistic and Unicode character set considerations that may apply to some languages.
-   [Troubleshooting Language Resources](troubleshooting-language-resources.md) describes some tips on troubleshooting word breaker and stemmer implementations.
-   [Language Resource Samples](language-resource-samples.md) presents details about the sample word breaker and stemmer in the Platform Software Development Kit (SDK).

 

 




