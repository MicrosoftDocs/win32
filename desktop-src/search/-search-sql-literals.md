---
description: A literal is a string of characters that represents a value in a query statement. You use literals to compare column values or to specify search terms. Windows Search supports the following types of literals.
ms.assetid: cc526174-3c91-402d-b7d0-69fc9a61c3f9
title: Literals
ms.topic: article
ms.date: 05/31/2018
---

# Literals

A literal is a string of characters that represents a value in a query statement. You use literals to compare column values or to specify search terms. Windows Search supports the following types of literals.


-   **String literals** can be any length and can contain either ANSI or Unicode characters. You must enclose string literals in single quotation marks('). To include a single quotation mark inside a string literal, use two single quotation marks (''). Represent an empty string as two consecutive single quotation marks ('').
-   **Numeric literals** can contain the digits 0-9, a period, and the letter E (or e). Numeric literals represent numbers, including positive and negative integers, decimal numbers, and currency values. Numeric literals can be defined by using scientific notation (for example, 2.3E-05). Do not enclose a numeric literal in single quotation marks, or it will be interpreted as a string literal and compared using string comparison techniques. Currency values cannot contain currency symbols.
-   **Hexadecimal literals** can contain the digits 0-9 and the letters A-F and a-f. A hexadecimal literal represents an unsigned integer specified in hexadecimal notation. Hexadecimal literals must begin with 0x.
    > [!Note]  
    > The SQL-92 standard requires that hexadecimal literals be enclosed in single quotation marks; however, Windows Search does not support that notation.

     

-   **Boolean literals** represent logical values, and can be either **TRUE** or **FALSE**. Do not enclose a Boolean literal in single quotation marks, or it is interpreted as a string literal.
-   **Date literals** represent specific dates, time stamps, or relative times, and are enclosed in single quotation marks. You must put dates in the form year/month/day hours:minutes:seconds or year-month-day hours:minutes:seconds, where the month, day, and year are numbers. Specify the year with a four-digit value, for example, 2004. Time values must be in the form hours:minutes:seconds. Relative time syntax is based on the [DATEADD Function](-search-sql-dateadd.md).

 

 



