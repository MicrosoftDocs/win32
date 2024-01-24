---
description: Identifiers specify the names of columns (sometimes referred to as properties), catalogs, and aliases.
ms.assetid: 799afe2c-9217-4006-a4a3-644e5393993c
title: Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Identifiers

Identifiers specify the names of columns (sometimes referred to as properties), catalogs, and aliases. For example, System.ItemName and System.DateCreated are the identifiers of two system-defined property columns. Literals, by contrast, specify string and numeric values.


You can create identifiers that are up to 128 characters long, and in one of two types, distinguished by the characters used in the identifier name:

-   **Regular identifiers** contain only the characters A-Z, a-z, 0-9, underscore (\_), and dot (.), and they begin with a letter. You do not need to enclose regular identifiers in double quotation marks (" ").
-   **Delimited identifiers** can contain any valid Unicode character and must be enclosed in double quotation marks.

> [!Note]  
> In FREETEXT and CONTAINS clauses, you can use the asterisk (\*) as a special column identifier when you want to specify that Windows Search includes all of the indexed properties in the query. Although it is not a regular identifier, it does not require double quotation marks.

 

 

 



