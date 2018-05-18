---
title: IMimeSecurity GetCertData method
description: Gets the specified certificate.
ms.assetid: '6d9945a0-1f83-42da-9e28-19cedf6db371'
keywords: ["GetCertData method Windows Mail (formerly Outlook Express)", "GetCertData method Windows Mail (formerly Outlook Express) , IMimeSecurity interface", "IMimeSecurity interface Windows Mail (formerly Outlook Express) , GetCertData method"]
topic_type:
- apiref
api_name:
- IMimeSecurity.GetCertData
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeSecurity::GetCertData method

Gets the specified certificate.

## Syntax


```C++
HRESULT GetCertData(
  [in]       const PCX509CERT    pX509Cert,
  [in]       const CERTDATAID    dataid,
  [out, ref]       LPPROPVARIANT &amp;pValue
);
```



## Parameters

<dl> <dt>

*pX509Cert* \[in\]
</dt> <dd>

Type: **const PCX509CERT**

Specifies a pointer to the [CERT\_CONTEXT](http://msdn.microsoft.com/library/seccrypto/security/cert_context.asp) structure from which to read data.

</dd> <dt>

*dataid* \[in\]
</dt> <dd>

Type: **const [**CERTDATAID**](oe-certdataid.md)**

Specifies a [**CERTDATAID**](oe-certdataid.md) value.

</dd> <dt>

*pValue* \[out, ref\]
</dt> <dd>

Type: **LPPROPVARIANT**

Receives a pointer to a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072) structure that contains the certificate data.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                         | Description                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | Indicates success. <br/>                                                                                                                                                                                                                                               |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>  | Indicates that the certificate contains no data. <br/>                                                                                                                                                                                                                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>        | Indicates that *pX509Cert* or [CERT\_CONTEXT](http://msdn.microsoft.com/library/seccrypto/security/cert_context.asp)-&gt;[pCertInfo](http://msdn.microsoft.com/library/seccrypto/security/cert_context.asp) is **NULL** or that *dataid* is invalid. <br/> |
| <dl> <dt>**CRYPT\_E\_NOT\_FOUND**</dt> </dl> | Indicates that there are no more certificates. <br/>                                                                                                                                                                                                                   |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





