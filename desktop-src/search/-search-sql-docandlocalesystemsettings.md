---
description: When the operating system, or even an application, is set to use a particular language and locale, many settings are affected.
ms.assetid: cec164d1-125f-483c-9d74-0e24b8215157
title: Document and System Locale Settings
ms.topic: article
ms.date: 05/31/2018
---

# Document and System Locale Settings

When the operating system, or even an application, is set to use a particular language and locale, many settings are affected. These settings include numeric format, date format, currency format, uppercase and lowercase mapping, dictionary sort ordering, tokenization, and others. Although these settings help Windows Search provide excellent localized support, unexpected results can occur when documents from one locale are searched by using a system that is set to another locale.

When the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) object processes a document's text properties and content, it reports the language of that document to the content indexer. Using this information, Windows Search can apply the appropriate word breaker.

 

 
