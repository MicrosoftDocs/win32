---
title: ResultsDisplayStyle enumeration
description: Used by IResultsViewer ResultsStyle to set or determine how results are displayed.
ms.assetid: 24b474f2-1aca-4556-ba9a-3b8139e80bf0
keywords:
- ResultsDisplayStyle enumeration Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- ResultsDisplayStyle
api_location:
- WdsView.idl
api_type:
- IDLDef
ms.topic: enumeration
ms.date: 05/31/2018
---

# ResultsDisplayStyle enumeration

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://docs.microsoft.com/windows/desktop/search/-search-reference-entry-page) instead.\]

Used by [**IResultsViewer::ResultsStyle**](-search-2x-iresultsviewer-resultsstyle.md) to set or determine how results are displayed.

## Syntax


```C++
typedef enum ResultsDisplayStyleEnum { 
  SmallIconResults  = 0,
  LargeIconResults  = 1
} ResultsDisplayStyle;
```



## Constants

<dl> <dt>

<span id="SmallIconResults"></span><span id="smalliconresults"></span><span id="SMALLICONRESULTS"></span>**SmallIconResults**
</dt> <dd>

Indicates Results are displayed as small icons.

</dd> <dt>

<span id="LargeIconResults"></span><span id="largeiconresults"></span><span id="LARGEICONRESULTS"></span>**LargeIconResults**
</dt> <dd>

Indicates Results are displayed as large icons.

</dd> </dl>

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| IDL<br/> | <dl> <dt>WdsView.idl</dt> </dl> |



 

 





