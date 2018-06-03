---
Description: Gets the handle of the current WWAHost window.
ms.assetid: 7c013f82-6d1f-494d-9f7a-77c7ff72f0d4
title: IWebApplicationHost::HWND property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

[**IWebApplicationHost**](/previous-versions/windows/desktop/api/webapplication/nn-webapplication-iwebapplicationhost)
</dt> </dl>

 

 




