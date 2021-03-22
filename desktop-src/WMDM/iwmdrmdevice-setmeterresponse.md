---
title: IWMDRMDevice SetMeterResponse method
description: The SetMeterResponse method sets the metering response.
ms.assetid: 3f2e7d7c-6470-4d53-96b0-d3eebdb08329
keywords:
- SetMeterResponse method windows Media Device Manager
- SetMeterResponse method windows Media Device Manager , IWMDRMDevice interface
- IWMDRMDevice interface windows Media Device Manager , SetMeterResponse method
topic_type:
- apiref
api_name:
- IWMDRMDevice.SetMeterResponse
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDevice::SetMeterResponse method

The **SetMeterResponse** method sets the metering response.

## Syntax


```C++
HRESULT SetMeterResponse(
  [in]  BYTE  *pbMeterResponse,
  [in]  DWORD cbMeterResponse,
  [out] DWORD *pdwFlags
);
```



## Parameters

<dl> <dt>

*pbMeterResponse* \[in\]
</dt> <dd>

The metering response to be set.

</dd> <dt>

*cbMeterResponse* \[in\]
</dt> <dd>

Size of the metering response, in bytes.

</dd> <dt>

*pdwFlags* \[out\]
</dt> <dd>

Response flags. This value must be one of the following flags.



| Flag                            | Description              |
|---------------------------------|--------------------------|
| WMDRM\_METER\_RESPONSE\_ALL     | All meter responses.     |
| WMDRM\_METER\_RESPONSE\_PARTIAL | Partial meter responses. |



 

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

 

 





