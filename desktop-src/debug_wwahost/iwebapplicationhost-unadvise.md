---
Description: Removes a previously established connection.
ms.assetid: daab1a3f-1f84-4559-bdc0-be8f1fb28904
title: IWebApplicationHost::Unadvise method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWebApplicationHost::Unadvise method

Removes a previously established connection.

## Syntax


```C++
HRESULT Unadvise(
  [in] DWORD cookie
);
```



## Parameters

<dl> <dt>

*cookie* \[in\]
</dt> <dd>

Type: **DWORD**

A connection token previously returned from the [**Advise**](iwebapplicationhost-advise.md) method.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                          |
| IDL<br/>                      | <dl> <dt>Webapplication.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWebApplicationHost**](/previous-versions/windows/desktop/api/webapplication/nn-webapplication-iwebapplicationhost)
</dt> <dt>

[**IWebApplicationHost::Advise**](iwebapplicationhost-advise.md)
</dt> </dl>

 

 




