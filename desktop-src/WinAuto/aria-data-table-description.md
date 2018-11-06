---
title: ARIA Data Table Warning
description: ARIA Data Table Warning
ms.assetid: 3CFCF248-6A66-4140-B3E7-133E3809B287
keywords:
- AriaDataTableWarningId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Data Table Warning

## Text

Table contains data but has neither summary nor a valid **aria-describedby** attribute.

## Type

Warning

## Description

This warning applies to HTML tables with more than one cell. It does not apply to tables with `role="presentation"` since these are considered to be layout tables.

This warning indicates that the table is identified as a data table but it doesn’t have an accessible description defined.

> [!Note]  
> Not all data tables are required to have an accessible description. You should define an accessible description if users need more information to understand the data table structure and content.

 

To address this warning, define a table accessible description by using the summary attribute or the **aria-describedby** attribute.

## Example


```HTML
<!-- Define a table description by using the summary attribute. -->
<table summary="The first column contains the list of examples. In the second column ...">
...
</table>

<!-- Define a table description using the aria-describedby attribute. -->
<p id="tableHeader" >The first column contains the list of examples. In the second column ...</p>
<table aria-describedby="tableHeader" >
...
</table>
```



 

 




