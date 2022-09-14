---
title: IWMDRMNetTransmitter GetRootLicenseResponse method (Wmdrmsdk.h)
description: The GetRootLicenseResponse method generates a root license response message.
ms.assetid: c735ee52-f0e0-4404-881b-18ee9a7fa9f9
keywords:
- GetRootLicenseResponse method windows Media Format
- GetRootLicenseResponse method windows Media Format , IWMDRMNetTransmitter interface
- IWMDRMNetTransmitter interface windows Media Format , GetRootLicenseResponse method
topic_type:
- apiref
api_name:
- IWMDRMNetTransmitter.GetRootLicenseResponse
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMNetTransmitter::GetRootLicenseResponse method

The **GetRootLicenseResponse** method generates a root license response message.

## Syntax


```C++
HRESULT GetRootLicenseResponse(
  [in]  BSTR  bstrKID,
  [out] BYTE  **ppbLicenseResponse,
  [out] DWORD *pcbLicenseResponse
);
```



## Parameters

<dl> <dt>

*bstrKID* \[in\]
</dt> <dd>

Base64-encoded key identifier to be used for the new root license. The key identifier should be a randomly generated GUID value.

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

The generated root license is created using the information from the license challenge data, which is processed for the interface by calling [**SetLicenseChallenge**](iwmdrmnettransmitter-setlicensechallenge.md).

The root license is used in the generation of leaf licenses, which is accomplished by calling the [**GetLeafLicenseResponse**](iwmdrmnettransmitter-getleaflicenseresponse.md) method. The **IWMDRMNetTransmitter** interface maintains a copy of the root license for that use.

The root license created by calling this method does not have any policies and is configured so that it cannot be persisted on the receiving device.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMNetTransmitter Interface**](iwmdrmnettransmitter.md)
</dt> </dl>

 

 





