---
title: Property-Value Queries
description: Property-value queries find documents with value-type properties that match a given criterion.
ms.assetid: c0b0bf19-4ae6-4df4-b457-6e6ea70f6999
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Property-Value Queries

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Property-value queries find documents with value-type properties that match a given criterion. The properties for which you can query include basic document information (such as file name and file size), as well as ActiveX properties (such as the document summary stored in documents created by ActiveX-aware applications). For information about property names, see [Property-Name Syntax](property-name-syntax.md).

Indexing Service provides two types of property-value queries: [relational queries](relational-queries.md) and [pattern-matching queries](pattern-matching-queries.md). It also provides [vector-space queries](vector-space-queries.md) for querying with a (possibly complex) list of properties.

The following general rules apply to the syntax of property-value queries.

-   Date and time values are of the form *yyyy/mm/dd hh:mm:ss* or *yyyy-mm-dd hh:mm:ss*. The first two characters of the year and the entire time can be omitted. If you omit the first two characters of the year, then 29 or less is interpreted as a year between 2000 and 2029, and 30 or greater is interpreted as between the years 1930 and 1999. All dates and times are in Coordinated Universal Time (UTC).
-   Dates and times relative to the current time can be expressed by using a hyphen as a minus sign (-), followed by zero or by more integer-unit and time-unit pairs. Time units are expressed as: (y) for years, (m) for months, (w) for weeks, (d) for days, (h) for hours, (n) for minutes, and (s) for seconds. A three-digit millisecond value can be optionally specified after the seconds value in date expressions, for example, 1997/12/8 10:10:03:452.
-   Currency values are of the form *x.y*, where *x* is the whole value amount and *y* is the fractional amount. There is no assumption about units.
-   Boolean values are (t) or (true) for TRUE and (f) or (false) for FALSE.
-   Vector properties (of type VT\_VECTOR) are expressed as an opening parenthesis "(", followed by a semicolon-separated list of values, then a closing parenthesis ")".
-   Single-value expressions that are compared against vectors are expressed as a relational operator, then an **AllOf** operator (^a) for *all of* or a **SomeOf** operator (^s) for *some of*.
-   Numeric values can be in decimal or hexadecimal (preceded by 0x) form.
-   The contents property does not support relational operators. If a relational operator is specified, no results will be found. For example in short form, *@*contents *Microsoft* will find documents containing *Microsoft*, but @contents=*Microsoft* will find none. However, @title=*vector space* returns results only if the entire title is *vector space*. If you leave out the equal sign, *@*title *vector space* returns results even if *vector space* is only a phrase in a longer title.
-   In the short form, use the number sign (\#) before the property name when using a regular expression in a property value, and an at sign (@) otherwise. The equal to relational operator (=) is assumed for regular-expression queries.
-   The Filename property (\#filename) is the only property that efficiently supports regular expressions with wildcard characters to the *left of* text.

 

 




