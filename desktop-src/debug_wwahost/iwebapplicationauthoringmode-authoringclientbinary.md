---
Description: Gets the full local path to a DLL to be loaded into the WWAHost process.
ms.assetid: ff75658a-af5a-42d7-be88-b3bc0daed5e2
title: IWebApplicationAuthoringMode::AuthoringClientBinary property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWebApplicationAuthoringMode::AuthoringClientBinary property

Gets the full local path to a DLL to be loaded into the WWAHost process.

This property is read-only.

## Syntax


```C++
HRESULT get_AuthoringClientBinary(
  [out, retval] BSTR *designModeDllPath
);
```



## Property value

The full local path.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                          |
| IDL<br/>                      | <dl> <dt>Webapplication.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWebApplicationAuthoringMode**](/previous-versions/windows/desktop/api/webapplication/nn-webapplication-iwebapplicationauthoringmode)
</dt> </dl>

 

 




