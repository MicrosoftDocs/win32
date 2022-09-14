---
description: Sends the specified message to a window or windows.
ms.assetid: aed898b3-bb48-4da2-aee7-834ae65a2d51
title: '_SendMessage function'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _SendMessage
api_type: 
- DllExport
api_location: 
- Sqlunirl.dll
---

# \_SendMessage function

\[This function is a wrapper over the **SendMessage** function. This function may be altered or unavailable in the future. Applications should call **SendMessage** directly.\]

Sends the specified message to a window or windows. See [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage).

## Syntax


```C++
LRESULT _SendMessage(
    ...
);
```



## Parameters

<dl> <dt>

*...* 
</dt> <dd></dd> </dl>

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Sqlunirl.dll</dt> </dl> |



## See also

<dl> <dt>

[**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage)
</dt> </dl>

 

 
