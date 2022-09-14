---
description: Changes the text of the specified window's title bar (if it has one).
ms.assetid: 0da53972-8f2e-4ca5-92f8-97eb88514e35
title: '_SetWindowText function'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _SetWindowText
api_type: 
- DllExport
api_location: 
- Sqlunirl.dll
---

# \_SetWindowText function

\[This function is a wrapper over the **SetWindowText** function. This function may be altered or unavailable in the future. Applications should call **SetWindowText** directly.\]

Changes the text of the specified window's title bar (if it has one). See [**SetWindowText**](/windows/win32/api/winuser/nf-winuser-setwindowtexta).

## Syntax


```C++
BOOL _SetWindowText(
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

[**SetWindowText**](/windows/win32/api/winuser/nf-winuser-setwindowtexta)
</dt> </dl>

 

 
