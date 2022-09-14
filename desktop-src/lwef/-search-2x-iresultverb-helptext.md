---
title: IResultVerb HelpText property (WdsSharedIDL.h)
description: This property returns a pointer to the localized help string for the verb.
ms.assetid: 14e91101-5ee2-459a-97d7-35c76d3ba990
keywords:
- HelpText property Legacy Windows Environment Features
- HelpText property Legacy Windows Environment Features , IResultVerb interface
- IResultVerb interface Legacy Windows Environment Features , HelpText property
topic_type:
- apiref
api_name:
- IResultVerb.HelpText
- IResultVerb.get_HelpText
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultVerb::HelpText property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

This property returns a pointer to the localized help string for the verb.

This property is read-only.

## Syntax


```C++
HRESULT get_HelpText(
  [out, retval] BSTR *text
);
```



## Property value

The value of this property is a pointer to the localized help string for this verb.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





