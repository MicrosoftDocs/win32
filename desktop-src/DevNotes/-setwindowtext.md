---
Description: Changes the text of the specified window's title bar (if it has one).
ms.assetid: 0da53972-8f2e-4ca5-92f8-97eb88514e35
title: '\_SetWindowText function'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
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

Changes the text of the specified window's title bar (if it has one). See [**SetWindowText**](_win32_setwindowtext_cpp).

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



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Sqlunirl.dll</dt> </dl> |



## See also

<dl> <dt>

[**SetWindowText**](_win32_setwindowtext_cpp)
</dt> </dl>

 

 




