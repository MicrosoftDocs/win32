---
title: IWMDRMDevice GetSecureClockChallenge method
description: The GetSecureClockChallenge method retrieves the secure clock challenge result.
ms.assetid: cbef160c-91a3-47d1-9d7a-e649ce2c77ff
keywords:
- GetSecureClockChallenge method windows Media Device Manager
- GetSecureClockChallenge method windows Media Device Manager , IWMDRMDevice interface
- IWMDRMDevice interface windows Media Device Manager , GetSecureClockChallenge method
topic_type:
- apiref
api_name:
- IWMDRMDevice.GetSecureClockChallenge
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDevice::GetSecureClockChallenge method

The **GetSecureClockChallenge** method retrieves the secure clock challenge result.

## Syntax


```C++
HRESULT GetSecureClockChallenge(
  [out] BYTE  **ppbChallenge,
  [out] DWORD *pcbChallenge
);
```



## Parameters

<dl> <dt>

*ppbChallenge* \[out\]
</dt> <dd>

Retrieved challenge result.

</dd> <dt>

*pcbChallenge* \[out\]
</dt> <dd>

Size of the challenge result, in bytes.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMDDRMSP.idl</dt> </dl> |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**GetSecureClock**](iwmdrmdevice-getsecureclock.md)
</dt> <dt>

[**IWMDRMDevice Interface**](iwmdrmdevice.md)
</dt> </dl>

 

 





