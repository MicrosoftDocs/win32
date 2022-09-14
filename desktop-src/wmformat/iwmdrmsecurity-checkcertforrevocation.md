---
title: IWMDRMSecurity CheckCertForRevocation method (Wmdrmsdk.h)
description: The CheckCertForRevocation method determines whether a certificate has been revoked.
ms.assetid: 3efde398-f2ba-486e-b017-6787ca402e4c
keywords:
- CheckCertForRevocation method windows Media Format
- CheckCertForRevocation method windows Media Format , IWMDRMSecurity interface
- IWMDRMSecurity interface windows Media Format , CheckCertForRevocation method
topic_type:
- apiref
api_name:
- IWMDRMSecurity.CheckCertForRevocation
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMSecurity::CheckCertForRevocation method

The **CheckCertForRevocation** method determines whether a certificate has been revoked.

## Syntax


```C++
HRESULT CheckCertForRevocation(
  [in]  REFGUID rguidRevocationList,
  [in]  BYTE    *pbCert,
  [in]  DWORD   cbCert,
  [out] BOOL    *fRevoked
);
```



## Parameters

<dl> <dt>

*rguidRevocationList* \[in\]
</dt> <dd>

GUID identifying the revocation list to use. Set to one of the values in the following table.



| GUID constant                 | Description                                                                                |
|-------------------------------|--------------------------------------------------------------------------------------------|
| WMDRM\_REVOCATIONTYPE\_APP    | Specifies the application certificate revocation list.                                     |
| WMDRM\_REVOCATIONTYPE\_DEVICE | Specifies the device certificate revocation list.                                          |
| WMDRM\_REVOCATIONTYPE\_CARDEA | Specifies the Microsoft Windows Media DRM for Network Devices certificate revocation list. |



 

</dd> <dt>

*pbCert* \[in\]
</dt> <dd>

Buffer containing the certificate to look up.

</dd> <dt>

*cbCert* \[in\]
</dt> <dd>

Size of the buffer *pbCert*, in bytes.

</dd> <dt>

*fRevoked* \[out\]
</dt> <dd>

On output, indicates whether the certificate is present in the revocation list.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMSecurity Interface**](iwmdrmsecurity.md)
</dt> </dl>

 

 





