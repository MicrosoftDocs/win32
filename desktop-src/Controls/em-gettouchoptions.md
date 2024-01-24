---
title: EM_GETTOUCHOPTIONS message (Richedit.h)
description: Retrieves the touch options that are associated with a rich edit control.
ms.assetid: 1D367818-5625-4A5A-A7A1-330FED516990
keywords:
- EM_GETTOUCHOPTIONS message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETTOUCHOPTIONS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETTOUCHOPTIONS message

Retrieves the touch options that are associated with a rich edit control.


```C++
#define EM_GETTOUCHOPTIONS       (WM_USER + 310)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The touch options to retrieve. It can be one of the following values.



| Value                                                                                                                                                                        | Meaning                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <span id="RTO_SHOWHANDLES"></span><span id="rto_showhandles"></span><dl> <dt>**RTO\_SHOWHANDLES**</dt> </dl>          | Retrieves whether the touch grippers are visible.<br/> |
| <span id="RTO_DISABLEHANDLES"></span><span id="rto_disablehandles"></span><dl> <dt>**RTO\_DISABLEHANDLES**</dt> </dl> | Retrieving this flag is not implemented.<br/>          |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

Returns the value of the option specified by the *wParam* parameter. It is nonzero if *wParam* is **RTO\_SHOWHANDLES** and the touch grippers are visible; zero, otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETTOUCHOPTIONS**](em-settouchoptions.md)
</dt> </dl>

 

 





