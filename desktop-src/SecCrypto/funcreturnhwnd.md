---
description: Used by a cryptographic service provider (CSP) to obtain the window handle that the CSP should use as the parent or owner of any user interface that is displayed.
ms.assetid: 56f189e7-073b-4b42-b6ab-0147853fe6d5
title: CRYPT_RETURN_HWND function pointer (Cspdk.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRYPT_RETURN_HWND
api_type: 
- UserDefined
api_location: 
- Cspdk.h
---

# CRYPT\_RETURN\_HWND function pointer

The **FuncReturnhWnd** callback function is used by a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) to obtain the window handle that the CSP should use as the parent or owner of any user interface that is displayed.

## Syntax


```C++
typedef void ( WINAPI *CRYPT_RETURN_HWND)(
  _Inout_ HWND *phWnd
);
```



## Parameters

<dl> <dt>

*phWnd* \[in, out\]
</dt> <dd>

The address of an **HWND** variable that receives the parent window handle.

</dd> </dl>

## Return value

This function pointer does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Cspdk.h</dt> </dl> |



## See also

<dl> <dt>

[**CPAcquireContext**](https://www.bing.com/search?q=**CPAcquireContext**)
</dt> <dt>

[**VTableProvStruc**](vtableprovstruc.md)
</dt> </dl>

 

 
