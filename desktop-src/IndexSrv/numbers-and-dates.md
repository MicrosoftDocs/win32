---
title: Numbers and Dates
description: Numbers and Dates
ms.assetid: 5e93c1aa-a521-4d87-bacd-e5c78fde3b61
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Numbers and Dates

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Word breakers must use a common format for representing numbers, times, and dates to facilitate consistent querying.

### Numbers

When you create a word breaker, it is recommended that the word breaker normalize numbers to a canonical representation by using the pattern "NN*dd*D*cc*," where "NN" is the literal sequence "NN," *dd* is the integer portion of the number, "D" is the literal "D," and *cc* is the fractional portion of the number. Word breakers do not restrict the number of digits for either the integer or the fraction portion of the number. It is recommended that word breakers recognize numerical patterns that are delimited by both periods (.) and commas (,). For example, Indexing Service represents both "1,000.2" and "1.000,2" as "NN1000D2."

Choose one format for both word breaker and stemmer. Single-byte Arabic numerals are normalized such that a query containing any of these forms matches documents with the other forms.

### Times

When you create a word breaker, it is recommended that the word breaker present all times as a 24-hour representation that consists of a literal prefix "TT" followed by the time specification "TT*hhmmss*," where *hh* is the hours, *mm* is the minutes, and *ss* is the seconds. Indexing Service does not match additional units of time, such as milliseconds. Parsing A.M. and P.M. patterns is optional.

### Dates

When you create a word breaker, it is recommended that the word breaker generate dates in the canonical format of "DD*yyyymmdd*," where "DD" is the literal "DD," *yyyy* is the years, *mm* is the months, and *dd* is the days. It is also recommended that word breakers store two-digit years in both twentieth-century and twenty-first-century formats. For example, word breakers represent "2.2.99" as "DD19990202" and "DD20990202." At query time, Indexing Service derives the date by using Windows application programming interfaces (APIs) to determine the crossover date for the server to display the correct format, 19*XX* or 20*XX*.

 

 




