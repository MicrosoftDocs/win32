---
Description: Gets the HTML document object model of the current top-level document.
ms.assetid: e2ba8ea7-0179-42d6-8d85-1617d14f85e4
title: IWebApplicationHost::Document property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

[**IHTMLDocument2**](https://www.bing.com/search?q=**IHTMLDocument2**)
</dt> <dt>

[**IWebApplicationHost**](/previous-versions/windows/desktop/api/webapplication/nn-webapplication-iwebapplicationhost)
</dt> </dl>

 

 




