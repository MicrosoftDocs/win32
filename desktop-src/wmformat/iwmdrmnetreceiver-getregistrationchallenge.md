---
title: IWMDRMNetReceiver GetRegistrationChallenge method (Wmdrmsdk.h)
description: The GetRegistrationChallenge method generates a Windows Media DRM for Network Devices registration challenge message.
ms.assetid: 7b3641a1-ccc5-4e29-b0e9-808b111f8841
keywords:
- GetRegistrationChallenge method windows Media Format
- GetRegistrationChallenge method windows Media Format , IWMDRMNetReceiver interface
- IWMDRMNetReceiver interface windows Media Format , GetRegistrationChallenge method
topic_type:
- apiref
api_name:
- IWMDRMNetReceiver.GetRegistrationChallenge
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMNetReceiver::GetRegistrationChallenge method

The **GetRegistrationChallenge** method generates a Windows Media DRM for Network Devices registration challenge message.

## Syntax


```C++
HRESULT GetRegistrationChallenge(
  [out] BYTE  **ppbRegistrationChallenge,
  [out] DWORD *pcbRegistrationChallenge
);
```



## Parameters

<dl> <dt>

*ppbRegistrationChallenge* \[out\]
</dt> <dd>

Address of a pointer that receives the address of the generated challenge. When finished with this data, you must release the memory by calling **CoTaskMemFree**.

</dd> <dt>

*pcbRegistrationChallenge* \[out\]
</dt> <dd>

Address of a variable that receives the size of the registration challenge in bytes.

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

[**IWMDRMNetReceiver::ProcessRegistrationResponse**](iwmdrmnetreceiver-processregistrationresponse.md)
</dt> </dl>

 

 





