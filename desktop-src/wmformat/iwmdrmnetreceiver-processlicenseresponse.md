---
title: IWMDRMNetReceiver ProcessLicenseResponse method (Wmdrmsdk.h)
description: The ProcessLicenseResponse method processes the license response that is sent by the transmitter in reply to a license challenge.
ms.assetid: b6d04651-746b-474e-8a02-6b7cbee9db46
keywords:
- ProcessLicenseResponse method windows Media Format
- ProcessLicenseResponse method windows Media Format , IWMDRMNetReceiver interface
- IWMDRMNetReceiver interface windows Media Format , ProcessLicenseResponse method
topic_type:
- apiref
api_name:
- IWMDRMNetReceiver.ProcessLicenseResponse
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMNetReceiver::ProcessLicenseResponse method

The **ProcessLicenseResponse** method processes the license response that is sent by the transmitter in reply to a license challenge.

## Syntax


```C++
HRESULT ProcessLicenseResponse(
  [in]  BYTE  *pbLicenseResponse,
  [in]  DWORD cbLicenseResponse,
  [out] BYTE  **ppbWMDRMNetLicenseRepresentation,
  [out] DWORD *pcbWMDRMNetLicenseRepresentation
);
```



## Parameters

<dl> <dt>

*pbLicenseResponse* \[in\]
</dt> <dd>

License response received from the transmitter.

</dd> <dt>

*cbLicenseResponse* \[in\]
</dt> <dd>

Size of the response in bytes.

</dd> <dt>

*ppbWMDRMNetLicenseRepresentation* \[out\]
</dt> <dd>

Address of a variable that receives the address of the internal license representation for the license contained in the license response message. When finished with this data, you must release the memory by calling **CoTaskMemFree**. This parameter may be set to **NULL** if the license representation is not needed.

</dd> <dt>

*pcbWMDRMNetLicenseRepresentation* \[out\]
</dt> <dd>

Address of a variable that receives the size of the license representation. Must be set to **NULL** if *ppbWMDRMNetLicenseRepresentation* is **NULL**.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                | Description                                              |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**NS\_E\_DRM\_RIV\_TOO\_SMALL**</dt> </dl> | An updated content revocation list is needed.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>                       | The method succeeded.<br/>                         |



 

## Remarks

The license response processed by using this method must correspond to the last license challenge generated on the client computer.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMNetReceiver Interface**](iwmdrmnetreceiver.md)
</dt> <dt>

[**IWMDRMNetReceiver::GetLicenseChallenge**](iwmdrmnetreceiver-getlicensechallenge.md)
</dt> </dl>

 

 





