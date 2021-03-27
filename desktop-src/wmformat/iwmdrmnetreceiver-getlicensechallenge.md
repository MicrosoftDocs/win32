---
title: IWMDRMNetReceiver GetLicenseChallenge method (Wmdrmsdk.h)
description: The GetLicenseChallenge method generates a Windows Media DRM for Network Devices license challenge that can be sent to a transmitter when requesting protected content.
ms.assetid: c13b9e9e-b076-411b-a106-b602544faaba
keywords:
- GetLicenseChallenge method windows Media Format
- GetLicenseChallenge method windows Media Format , IWMDRMNetReceiver interface
- IWMDRMNetReceiver interface windows Media Format , GetLicenseChallenge method
topic_type:
- apiref
api_name:
- IWMDRMNetReceiver.GetLicenseChallenge
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMNetReceiver::GetLicenseChallenge method

The **GetLicenseChallenge** method generates a Windows Media DRM for Network Devices license challenge that can be sent to a transmitter when requesting protected content.

## Syntax


```C++
HRESULT GetLicenseChallenge(
  [in]  BSTR  bstrAction,
  [out] BYTE  **ppbLicenseChallenge,
  [out] DWORD *pcbLicenseChallenge
);
```



## Parameters

<dl> <dt>

*bstrAction* \[in\]
</dt> <dd>

Action for which to generate the challenge.

</dd> <dt>

*ppbLicenseChallenge* \[out\]
</dt> <dd>

Address of a pointer that is set to the address of the generated challenge. When finished with this data, you must release the memory by calling **CoTaskMemFree**.

</dd> <dt>

*pcbLicenseChallenge* \[out\]
</dt> <dd>

Address of a variable that receives the size of the license challenge in bytes.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMNetReceiver Interface**](iwmdrmnetreceiver.md)
</dt> <dt>

[**IWMDRMNetReceiver::ProcessLicenseResponse**](iwmdrmnetreceiver-processlicenseresponse.md)
</dt> </dl>

 

 





