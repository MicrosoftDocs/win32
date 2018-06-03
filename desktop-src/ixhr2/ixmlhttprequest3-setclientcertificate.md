---
title: IXMLHTTPRequest3 SetClientCertificate method
description: Sets a client certificate to be used to authenticate against the URL specified in the Open method.
ms.assetid: fc3e2645-666c-42af-babd-1f476b6356b8
keywords:
- SetClientCertificate method XMLHttpRequest2
- SetClientCertificate method XMLHttpRequest2 , IXMLHTTPRequest3 interface
- IXMLHTTPRequest3 interface XMLHttpRequest2 , SetClientCertificate method
topic_type:
- apiref
api_name:
- IXMLHTTPRequest3.SetClientCertificate
api_location:
- Msxml6.idl
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IXMLHTTPRequest3::SetClientCertificate method

Sets a client certificate to be used to authenticate against the URL specified in the [**Open**](/previous-versions/windows/desktop/api/msxml6/nf-msxml6-ixmlhttprequest2-open) method.

## Syntax


```C++
HRESULT SetClientCertificate(
  [in]                                                 DWORD cbClientCertificateHash,
  [in, size_is(cbClientCertificateHash), unique] const BYTE  *pbClientCertificateHash,
  [in, unique]                                   const WCHAR *pwszPin
);
```



## Parameters

<dl> <dt>

*cbClientCertificateHash* \[in\]
</dt> <dd>

The number of bytes of *pbClientCertHash* parameter.

</dd> <dt>

*pbClientCertificateHash* \[in\]
</dt> <dd>

The thumbprint or hash completed over the complete client certificate being set on the HTTPS request.

</dd> <dt>

*pwszPin* \[in\]
</dt> <dd>

This parameter is reserved.

</dd> </dl>

## Return value

Returns S\_OK on success.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| IDL<br/>                      | <dl> <dt>Msxml6.idl</dt> </dl>   |



## See also

<dl> <dt>

[**IXMLHTTPRequest3**](/previous-versions/windows/desktop/api/msxml6/nn-msxml6-ixmlhttprequest3)
</dt> <dt>

[**Open**](/previous-versions/windows/desktop/api/msxml6/nf-msxml6-ixmlhttprequest2-open)
</dt> </dl>

 

 





