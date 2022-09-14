---
title: IWMDRMDevice SetLicenseResponse method
description: The SetLicenseResponse method sets the license response.
ms.assetid: 1ef3ba9d-d14c-4a20-92d6-0bcb604fd9e2
keywords:
- SetLicenseResponse method windows Media Device Manager
- SetLicenseResponse method windows Media Device Manager , IWMDRMDevice interface
- IWMDRMDevice interface windows Media Device Manager , SetLicenseResponse method
topic_type:
- apiref
api_name:
- IWMDRMDevice.SetLicenseResponse
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDevice::SetLicenseResponse method

The **SetLicenseResponse** method sets the license response.

## Syntax


```C++
HRESULT SetLicenseResponse(
  [in] BYTE  *pbResponse,
  [in] DWORD cbResponse
);
```



## Parameters

<dl> <dt>

*pbResponse* \[in\]
</dt> <dd>

Specifies the response to be set.

</dd> <dt>

*cbResponse* \[in\]
</dt> <dd>

Size of the response, in bytes.

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

[**IWMDRMDevice Interface**](iwmdrmdevice.md)
</dt> </dl>

 

 





