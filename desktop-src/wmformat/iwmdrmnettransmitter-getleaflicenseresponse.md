---
title: IWMDRMNetTransmitter GetLeafLicenseResponse method (Wmdrmsdk.h)
description: The GetLeafLicenseResponse method generates a leaf license response message.
ms.assetid: b2893d22-b6f3-44d2-b6db-e2b07fbe098d
keywords:
- GetLeafLicenseResponse method windows Media Format
- GetLeafLicenseResponse method windows Media Format , IWMDRMNetTransmitter interface
- IWMDRMNetTransmitter interface windows Media Format , GetLeafLicenseResponse method
topic_type:
- apiref
api_name:
- IWMDRMNetTransmitter.GetLeafLicenseResponse
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMNetTransmitter::GetLeafLicenseResponse method

The **GetLeafLicenseResponse** method generates a leaf license response message.

## Syntax


```C++
HRESULT GetLeafLicenseResponse(
  [in]  BSTR            bstrKID,
  [in]  WMDRMNET_POLICY *pPolicy,
  [out] IWMDRMEncrypt   **ppIWMDRMEncrypt,
  [out] BYTE            **ppbLicenseResponse,
  [out] DWORD           *pcbLicenseResponse
);
```



## Parameters

<dl> <dt>

*bstrKID* \[in\]
</dt> <dd>

Base64-encoded key identifier to be used for the new leaf license. The key identifier should be a randomly generated GUID value.

</dd> <dt>

*pPolicy* \[in\]
</dt> <dd>

Pointer to the [**WMDRMNET\_POLICY**](wmdrmnet-policy.md) structure that defines the policy to use for the leaf license.

</dd> <dt>

*ppIWMDRMEncrypt* \[out\]
</dt> <dd>

Address of a variable that receives a pointer to the [**IWMDRMEncrypt**](iwmdrmencrypt.md) interface that can be used to encrypt data for the new leaf license.

</dd> <dt>

*ppbLicenseResponse* \[out\]
</dt> <dd>

Address of a variable that receives the address of the generated license response. When finished with this data, you must release the memory by calling **CoTaskMemFree**.

</dd> <dt>

*pcbLicenseResponse* \[out\]
</dt> <dd>

Address of a variable that receives the size of the license response, in bytes.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                | Description                                              |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**NS\_E\_DRM\_RIV\_TOO\_SMALL**</dt> </dl> | An updated content revocation list is needed.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>                       | The method succeeded.<br/>                         |



 

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMNetTransmitter Interface**](iwmdrmnettransmitter.md)
</dt> </dl>

 

 





