---
title: Production Rule
description: Production Rule
ms.assetid: 3767d047-2f22-4237-baa3-2765cddc5a4e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Production Rule

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

A *production rule* defines a nonterminal symbol in terms of other nonterminal symbols and terminal symbols. A production rule has this form:

*left side* = *right side* ;

The equal sign (=) separates the definition (*right side*) from the defined symbol (*left side*), and a semicolon terminates the rule. As the result of a production rule, *right side* replaces *left side* wherever *left side* appears in a production rule.

To produce a valid instance of a query-language construct, successively (even recursively) apply production rules until only terminal symbols remain.

The definition (*right side*) consists of a combined sequence of nonterminal and terminal symbols that uses several operators. The following table describes the operators.



| Operator   | Name          | Example         | Meaning                         |
|------------|---------------|-----------------|---------------------------------|
| \|         | Alternative   | **a** \| **b**  | Either **a** or **b**           |
| *implicit* | Concatenation | **a** **b**     | **a** followed by **b**; **ab** |
| \-         | Except        | **abc** - **b** | **abc** less **b**; **ac**      |
| \*         | Occurrences   | 5 \* **a**      | Five **a**s; **aaaaa**          |



 

There are four bracketing constructs to represent grouping, repetition, and optional inclusion. The following table describes these constructs.



| Construct | Name                        | Example                  | Meaning                      |
|-----------|-----------------------------|--------------------------|------------------------------|
| ( … )     | Grouped                     | ( **a** \| **b** ) **c** | **ac** or **bc**             |
| \[ … \]   | Optional                    | \[ **a** \] **b**        | **ab** or **b**              |
| { … }     | Repeated zero or more times | **a** { **a** }          | **a**, **aa**, **aaa**, …    |
| { … }-    | Repeated one or more times  | **a** { **a** }-         | **aa**, **aaa**, **aaaa**, … |



 

There also are two miscellaneous constructs. The following table describes these constructs.



| Construct | Name    | Example                    | Meaning                              |
|-----------|---------|----------------------------|--------------------------------------|
| (\* … \*) | Comment | (\* This is a comment. \*) | Not part of the syntax specification |
| ? … ?     | Special | ? Not defined ?            | Not defined by EBNF                  |



 

 

 




