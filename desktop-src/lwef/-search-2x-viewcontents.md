---
title: ViewContents enumeration
description: Used by IResultsViewer Contents to indicate or set how the current query return set is displayed.
ms.assetid: aebcbcac-4c45-4097-91a1-5e00611c152c
keywords:
- ViewContents enumeration Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- ViewContents
api_location:
- WdsView.idl
api_type:
- IDLDef
ms.topic: reference
ms.date: 05/31/2018
---

# ViewContents enumeration

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

Used by [**IResultsViewer::Contents**](-search-2x-iresultsviewer-contents.md) to indicate or set how the current query return set is displayed.

## Syntax


```C++
typedef enum ViewContentsEnum { 
  ResultsDisplayed     = 0,
  ShellViewDisplayed   = 1,
  WebBrowserDisplayed  = 2
} ViewContents;
```



## Constants

<dl> <dt>

<span id="ResultsDisplayed"></span><span id="resultsdisplayed"></span><span id="RESULTSDISPLAYED"></span>**ResultsDisplayed**
</dt> <dd>

Indicates the type of contents being displayed in the results view.

</dd> <dt>

<span id="ShellViewDisplayed"></span><span id="shellviewdisplayed"></span><span id="SHELLVIEWDISPLAYED"></span>**ShellViewDisplayed**
</dt> <dd>

Indicates the type of contents being displayed in the results view is currently set to the Shell view.

</dd> <dt>

<span id="WebBrowserDisplayed"></span><span id="webbrowserdisplayed"></span><span id="WEBBROWSERDISPLAYED"></span>**WebBrowserDisplayed**
</dt> <dd>

Indicates the type of contents being displayed in the results view is currently set to the browser view.

</dd> </dl>

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| IDL<br/> | <dl> <dt>WdsView.idl</dt> </dl> |



 

 





