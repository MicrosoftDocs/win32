---
Description: Gets the HTML document object model of the current top-level document.
ms.assetid: e2ba8ea7-0179-42d6-8d85-1617d14f85e4
title: IWebApplicationHostDocument property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWebApplicationHost::Document property

Gets the HTML document object model of the current top-level document.

This property is read-only.

## Syntax


```C++
HRESULT get_Document(
  [out, retval] IHTMLDocument2 **htmlDocument
);
```



## Property value

The document object.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                          |
| IDL<br/>                      | <dl> <dt>Webapplication.idl</dt> </dl> |



## See also

<dl> <dt>

[**IHTMLDocument2**](_win32_IHTMLDocument2)
</dt> <dt>

[**IWebApplicationHost**](/windows/previous-versions/webapplication/nn-webapplication-iwebapplicationhost?branch=master)
</dt> </dl>

 

 




