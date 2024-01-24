---
title: IWMDRMDevice CleanDataStore method
description: The CleanDataStore method starts the process of cleaning the DRM data store on the device.
ms.assetid: aad99137-6d2b-4612-8014-9783035af929
keywords:
- CleanDataStore method windows Media Device Manager
- CleanDataStore method windows Media Device Manager , IWMDRMDevice interface
- IWMDRMDevice interface windows Media Device Manager , CleanDataStore method
topic_type:
- apiref
api_name:
- IWMDRMDevice.CleanDataStore
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDevice::CleanDataStore method

The **CleanDataStore** method starts the process of cleaning the DRM data store on the device.

## Syntax


```C++
HRESULT CleanDataStore(
  [in] DWORD dwFlags
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flags for store cleaning criteria.

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

 

 





