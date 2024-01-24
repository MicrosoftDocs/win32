---
title: IWMDRMDevice GetSyncList method
description: The GetSyncList method retrieves the license synchronization list on the device. License synchronization allows the host computer to transfer updated licenses to a device according to the specified criteria.
ms.assetid: 772ac03b-3339-4c5f-a8fc-1c216ec665b7
keywords:
- GetSyncList method windows Media Device Manager
- GetSyncList method windows Media Device Manager , IWMDRMDevice interface
- IWMDRMDevice interface windows Media Device Manager , GetSyncList method
topic_type:
- apiref
api_name:
- IWMDRMDevice.GetSyncList
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDevice::GetSyncList method

The **GetSyncList** method retrieves the license synchronization list on the device. License synchronization allows the host computer to transfer updated licenses to a device according to the specified criteria.

## Syntax


```C++
HRESULT GetSyncList(
  [in]  DWORD cMinCountThreshold,
  [in]  DWORD cMinHoursThreshold,
  [out] BYTE  **ppbSyncList,
  [out] DWORD *pcbSyncList
);
```



## Parameters

<dl> <dt>

*cMinCountThreshold* \[in\]
</dt> <dd>

Minimum count threshold.

</dd> <dt>

*cMinHoursThreshold* \[in\]
</dt> <dd>

Minimum hours threshold.

</dd> <dt>

*ppbSyncList* \[out\]
</dt> <dd>

Retrieved license synchronization list.

</dd> <dt>

*pcbSyncList* \[out\]
</dt> <dd>

Size of the license synchronization list, in bytes.

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

 

 





