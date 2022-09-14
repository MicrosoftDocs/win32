---
title: EM_SETEDITSTYLEEX message (Richedit.h)
description: Sets the current extended edit style flags.
ms.assetid: C5CECC7C-6418-4A72-9F0B-6F55BE89E302
keywords:
- EM_SETEDITSTYLEEX message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETEDITSTYLEEX
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETEDITSTYLEEX message

Sets the current extended edit style flags.


```C++
#define EM_SETEDITSTYLEEX       (WM_USER + 275)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies one or more extended edit style flags. For a list of possible values, see [**EM\_GETEDITSTYLEEX**](/windows/desktop/Controls/em-geteditstyleex).

</dd> <dt>

*lParam* 
</dt> <dd>

A mask consisting of one or more of the *wParam* values. Only the values specified in this mask will be set or cleared. This allows a single flag to be set or cleared without reading the current flag states.

</dd> </dl>

## Return value

The return value is the state of the extended edit style flags after rich edit has attempted to implement your edit style changes. The edit style flags are a set of flags that indicate the current edit style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETEDITSTYLEEX**](em-geteditstyleex.md)
</dt> </dl>

 

