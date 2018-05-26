---
title: Constructing Language Resource Components
description: Constructing Language Resource Components
ms.assetid: 9d4d5936-d2ae-407c-a2bd-d838926c9523
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Constructing Language Resource Components

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This section describes how to construct a custom language resource component. Word breakers and stemmers need a DLL wrapper that implements and exports the standard DLL entry points. Implementing a word breaker entails implementing the [**IWordBreaker**](iwordbreaker.md) interface. Implementing a stemmer entails implementing the [**IStemmer**](istemmer.md) interface. The **IWordBreaker** and **IStemmer** interfaces allow flexible implementation of tokenization and morphological analysis. These interfaces can be implemented in the same DLL or in separate DLLs, depending on the approach and whether the implementations share code.

This section includes the following topics:

-   [Implementing the DLL Entry Points](implementing-the-dll-entry-points.md) provides instructions for implementing DLLs for word breakers and stemmers.
-   [Implementing a Word Breaker](implementing-a-word-breaker.md) provides instructions for implementing a custom word breaker by using the [**IWordBreaker**](iwordbreaker.md) interface.
-   [Implementing a Stemmer](implementing-a-stemmer.md) provides instructions for implementing a custom stemmer by using the [**IStemmer**](istemmer.md) interface.

 

 




