---
title: EM_SEARCHWEB message (Commctrl.h)
description: Opens the browser and performs a web search with the selected text as the search term.
ms.assetid: 1b1ff5e7-e0b8-40c1-8b7e-7003e9ef959b
keywords:
- EM_SEARCHWEB message Windows Controls
topic_type:
- apiref
api_name:
- EM_SEARCHWEB
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SEARCHWEB message

Opens the browser and performs a web search with the selected text as the search term.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

If the "Search the web" feature is disabled using the [**EM\_ENABLESEARCHWEB**](em-enablesearchweb.md) message, this message has no effect.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, 1809 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2019 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_ENABLESEARCHWEB**](em-enablesearchweb.md)
</dt> </dl>

 

 





