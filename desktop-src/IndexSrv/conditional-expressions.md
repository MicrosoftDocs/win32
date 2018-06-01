---
Description: Conditional Expressions
ms.assetid: 6ccc0a32-eb2b-4719-91c9-34ad5429b507
title: Conditional Expressions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Conditional Expressions

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

You can add if-then-else conditional logic to control the substitution of variables and parameters. The syntax is similar to conditional expressions in .htx files, but not exactly the same.

The following rules apply to conditional expressions in .idq files:

-   Lines in your .idq file must start with the variable name you're trying to set.
-   Only one line can set a particular variable in an .idq file.
-   Make sure variable references and statements are surrounded by percent signs (%).

The following example shows how to set the [CiRestriction](https://www.bing.com/search?q=CiRestriction) variable:


```
CiRestriction=%if Restriction ISEMPTY%Index Server Help%else%%Restriction%%endif%
```



This example stops users from running empty searches.

The following list shows the possible operators in If statements for .idq files:

<dl> <dt>

<span id="EQ"></span><span id="eq"></span>EQ
</dt> <dd>

if *value1* equals *value2*

</dd> <dt>

<span id="NE"></span><span id="ne"></span>NE
</dt> <dd>

if *value1* does not equal *value2*

</dd> <dt>

<span id="LT"></span><span id="lt"></span>LT
</dt> <dd>

if *value1* is less than *value2*

</dd> <dt>

<span id="LE"></span><span id="le"></span>LE
</dt> <dd>

if *value1* is less than or equal to *value2*

</dd> <dt>

<span id="GT"></span><span id="gt"></span>GT
</dt> <dd>

if *value1* is greater than *value2*

</dd> <dt>

<span id="GE"></span><span id="ge"></span>GE
</dt> <dd>

if *value1* is greater than or equal to *value2*

</dd> <dt>

<span id="CONTAINS"></span><span id="contains"></span>CONTAINS
</dt> <dd>

if any part of *value1* contains the string *value2*

</dd> <dt>

<span id="ISEMPTY"></span><span id="isempty"></span>ISEMPTY
</dt> <dd>

TRUE if *value1* is a Null string. This is a unary postfix operator.

</dd> </dl>

 

 



