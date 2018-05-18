---
title: Numeric Weights
description: Numeric Weights
ms.assetid: '0d6ec4a8-1356-42f9-8c15-78e9420acdea'
---

# Numeric Weights

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Query terms can be weighted when submitting a query by using the {weight} tag. This tag is a unary operator, and it appears before the query term and has no closing tag. The syntax is the following.

{weight value = *n*} *query term*

The value attribute specifies the weight to assign to the query term. The value of *n* can range from 0.0 to 1.0. Search engines are free to interpret weighting values within these guidelines.

A linear scale is assumed between 0.0 and 1.0. In Dialect 2, no short-form expression is available for weighting. For information about term weighting in Dialect 1, see [Incompatibilities of Dialect 2 with Dialect 1](incompatibilities-of-dialect-2-with-dialect-1.md).

The following table gives an example of term weighting.



| To Search For                                      | Example                                                                               | Results                                                                                                   |
|----------------------------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Documents that match terms with specified weights. | {weight value=0.25} dog **OR** {weight value=0.50} cat **OR** {weight value=1.00} pig | Documents containing *pig* followed by documents containing *cat* followed by documents containing *dog*. |



 

 

 




