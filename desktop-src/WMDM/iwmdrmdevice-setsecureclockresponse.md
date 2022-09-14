---
title: IWMDRMDevice SetSecureClockResponse method
description: The SetSecureClockResponse method sets the secure clock response.
ms.assetid: 3f0a1487-d8c4-478d-bfb0-8d09931fd4b6
keywords:
- SetSecureClockResponse method windows Media Device Manager
- SetSecureClockResponse method windows Media Device Manager , IWMDRMDevice interface
- IWMDRMDevice interface windows Media Device Manager , SetSecureClockResponse method
topic_type:
- apiref
api_name:
- IWMDRMDevice.SetSecureClockResponse
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDevice::SetSecureClockResponse method

The **SetSecureClockResponse** method sets the secure clock response.

## Syntax


```C++
HRESULT SetSecureClockResponse(
  [in] BYTE  *pbResponse,
  [in] DWORD cbResponse
);
```



## Parameters

<dl> <dt>

*pbResponse* \[in\]
</dt> <dd>

The secure clock response to be set.

</dd> <dt>

*cbResponse* \[in\]
</dt> <dd>

The specified size of the secure clock response, in bytes.

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

 

 





