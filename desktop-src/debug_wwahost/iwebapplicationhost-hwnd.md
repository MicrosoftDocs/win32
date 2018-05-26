---
Description: Gets the handle of the current WWAHost window.
ms.assetid: 7c013f82-6d1f-494d-9f7a-77c7ff72f0d4
title: IWebApplicationHostHWND property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWebApplicationHost::HWND property

Gets the handle of the current WWAHost window.

This property is read-only.

## Syntax


```C++
HRESULT get_HWND(
  [out, retval] HWND *hwnd
);
```



## Property value

The window handle.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                          |
| IDL<br/>                      | <dl> <dt>Webapplication.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWebApplicationHost**](/windows/previous-versions/webapplication/nn-webapplication-iwebapplicationhost?branch=master)
</dt> </dl>

 

 




