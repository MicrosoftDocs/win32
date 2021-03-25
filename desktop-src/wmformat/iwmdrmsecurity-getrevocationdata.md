---
title: IWMDRMSecurity GetRevocationData method (Wmdrmsdk.h)
description: The GetRevocationData method retrieves a certificate revocation list from the local store.
ms.assetid: 218f4f3a-02bc-4b1d-9320-e35ed8cc3b11
keywords:
- GetRevocationData method windows Media Format
- GetRevocationData method windows Media Format , IWMDRMSecurity interface
- IWMDRMSecurity interface windows Media Format , GetRevocationData method
topic_type:
- apiref
api_name:
- IWMDRMSecurity.GetRevocationData
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMSecurity::GetRevocationData method

The **GetRevocationData** method retrieves a certificate revocation list from the local store.

## Syntax


```C++
HRESULT GetRevocationData(
  [in]      REFGUID f_guidRevocationType,
  [out]     BYTE    *f_pbCRL,
  [in, out] DWORD   *f_pcbCRL
);
```



## Parameters

<dl> <dt>

*f\_guidRevocationType* \[in\]
</dt> <dd>

GUID identifying the type of revocation list to retrieve. Use one of the constants in the following table.



| GUID constant                 | Description                                                                      |
|-------------------------------|----------------------------------------------------------------------------------|
| WMDRM\_REVOCATIONTYPE\_APP    | Specifies the application certificate revocation list.                           |
| WMDRM\_REVOCATIONTYPE\_DEVICE | Specifies the device certificate revocation list.                                |
| WMDRM\_REVOCATIONTYPE\_CARDEA | Specifies the Windows Media DRM for Network Devices certificate revocation list. |



 

</dd> <dt>

*f\_pbCRL* \[out\]
</dt> <dd>

Buffer that receives the revocation list. Set to **NULL** to get the required buffer size.

</dd> <dt>

*f\_pcbCRL* \[in, out\]
</dt> <dd>

Size of the buffer in bytes. If *f\_pbCRL* is **NULL**, this value is set to the required buffer size on output.

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

[**Automated Component Revocation and Renewal**](automated-component-revocation-and-renewal.md)
</dt> <dt>

[**GetRevocationDataVersion**](iwmdrmsecurity-getrevocationdataversion.md)
</dt> <dt>

[**IWMDRMSecurity Interface**](iwmdrmsecurity.md)
</dt> <dt>

[**SetRevocationData**](iwmdrmsecurity-setrevocationdata.md)
</dt> </dl>

 

 





