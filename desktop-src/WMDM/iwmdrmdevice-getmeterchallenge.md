---
title: IWMDRMDevice GetMeterChallenge method
description: The GetMeterChallenge method retrieves the metering challenge.
ms.assetid: 4c122886-46bd-4e63-8e7d-5e6132363662
keywords:
- GetMeterChallenge method windows Media Device Manager
- GetMeterChallenge method windows Media Device Manager , IWMDRMDevice interface
- IWMDRMDevice interface windows Media Device Manager , GetMeterChallenge method
topic_type:
- apiref
api_name:
- IWMDRMDevice.GetMeterChallenge
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDevice::GetMeterChallenge method

The **GetMeterChallenge** method retrieves the metering challenge.

## Syntax


```C++
HRESULT GetMeterChallenge(
  [in]  BSTR  bstrMeterCert,
  [out] BYTE  **ppbMeterChallenge,
  [out] DWORD *pcbMeterChallenge
);
```



## Parameters

<dl> <dt>

*bstrMeterCert* \[in\]
</dt> <dd>

Metering certificate that the content owner sends to the host computer for collecting the associated metering data on the device

</dd> <dt>

*ppbMeterChallenge* \[out\]
</dt> <dd>

Retrieved metering challenge result.

</dd> <dt>

*pcbMeterChallenge* \[out\]
</dt> <dd>

The size of the metering challenge, in bytes.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

Metering data is collected and stored in the DRM data store on the device for content with metering enabled. Actions such as play will be recorded. When this function is called, the device collects the metering data in the DRM data store in the form of an XML document and sends it to the hostcomputer. If there is too much data, it is sent in phases.

When the host computer receives the metering data, it sends the data over the Internet to the URL specified in the metering certificate.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMDDRMSP.idl</dt> </dl> |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMDevice Interface**](iwmdrmdevice.md)
</dt> </dl>

 

 





