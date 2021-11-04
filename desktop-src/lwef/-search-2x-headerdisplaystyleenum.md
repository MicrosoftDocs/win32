---
title: HeaderDisplayStyle enumeration
description: Used by IResultsViewer HeaderStyle to set or return the current header style.
ms.assetid: 13ae6317-d990-4ccf-83b3-275caf953611
keywords:
- HeaderDisplayStyle enumeration Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- HeaderDisplayStyle
api_location:
- WdsView.idl
api_type:
- IDLDef
ms.topic: reference
ms.date: 05/31/2018
---

# HeaderDisplayStyle enumeration

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

Used by [**IResultsViewer::HeaderStyle**](-search-2x-iresultsviewer-headerstyle.md) to set or return the current header style.

## Syntax


```C++
typedef enum HeaderDisplayStyleEnum { 
  FullHeader     = 0,
  CompactHeader  = 1,
  NoHeader       = 2
} HeaderDisplayStyle;
```



## Constants

<dl> <dt>

<span id="FullHeader"></span><span id="fullheader"></span><span id="FULLHEADER"></span>**FullHeader**
</dt> <dd>

Indicates or sets the use of full headers.

</dd> <dt>

<span id="CompactHeader"></span><span id="compactheader"></span><span id="COMPACTHEADER"></span>**CompactHeader**
</dt> <dd>

Indicates or sets the use of compact headers.

</dd> <dt>

<span id="NoHeader"></span><span id="noheader"></span><span id="NOHEADER"></span>**NoHeader**
</dt> <dd>

Indicates or sets the use of no headers.

</dd> </dl>

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| IDL<br/> | <dl> <dt>WdsView.idl</dt> </dl> |



 

 





