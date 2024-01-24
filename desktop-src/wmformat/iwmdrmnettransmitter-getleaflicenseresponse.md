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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMNetTransmitter::GetLeafLicenseResponse method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





