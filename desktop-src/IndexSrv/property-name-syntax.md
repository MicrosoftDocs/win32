---
title: Property-Name Syntax
description: Property-Name Syntax
ms.assetid: '46c21368-3426-4dd1-9e52-41639c631690'
---

# Property-Name Syntax

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The long form of Dialect 2 expresses property names using the {prop} tag. The general syntax for a property name is the following.

``` syntax
{prop name = <property_name>} [{/prop}]
```

For completeness, the optional closing tag {/prop} is supported. This tag can be used for clarity when specifying relational operators with properties. Property names are case-insensitive, and if *property\_name* consists of more than one word, the words must be quoted. The short form uses the "@" character as a prefix to indicate the property name.

The following table summarizes property names and their long and short forms.



| Long Form                                  | Short Form        |
|--------------------------------------------|-------------------|
| {prop name = *property\_name*} \[{/prop}\] | @*property\_name* |



 

The Contents property, @Contents in short form, is a special case. This property refers to the contents of the text-type property of a document. When a query doesn't specify a property name, @Contents is assumed.

Properties available for all documents include the following.



| Property Name | Description                               |
|---------------|-------------------------------------------|
| All           | Matches words, phrases, and any property. |
| Contents      | Words and phrases in the document.        |
| Filename      | Name of the document.                     |
| Size          | Document size.                            |
| Write         | Last time the document was modified.      |



 

A query can also use Microsoft ActiveX property values. Documents created by most ActiveX-aware applications can be queried for the following properties.



| Property Name | Description                  |
|---------------|------------------------------|
| DocTitle      | Title of the document.       |
| DocSubject    | Subject of the document.     |
| DocAuthor     | Author of the document.      |
| DocKeywords   | Keywords for the document.   |
| DocComments   | Comments about the document. |



 

There is also a list of additional standard Indexing Service properties that are available in queries. For the list, see [Default Property Names for a Web Catalog](default-property-names-for-a-web-catalog.md).

The following table illustrates several property names in both long and short form.



| Long Form                | Short Form   |
|--------------------------|--------------|
| {prop name = filename}   | @filename    |
| {prop name = "shoe size" | @"shoe size" |
| {prop name = contents}   | @contents    |
| {prop name = all}        | @all         |



 

 

 




