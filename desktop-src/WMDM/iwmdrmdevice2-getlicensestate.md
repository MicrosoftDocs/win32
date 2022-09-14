---
title: IWMDRMDevice2 GetLicenseState method
description: The GetLicenseState method gets the license state.
ms.assetid: a98847f6-00ec-4211-9716-79714d7ba169
keywords:
- GetLicenseState method windows Media Device Manager
- GetLicenseState method windows Media Device Manager , IWMDRMDevice2 interface
- IWMDRMDevice2 interface windows Media Device Manager , GetLicenseState method
topic_type:
- apiref
api_name:
- IWMDRMDevice2.GetLicenseState
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDevice2::GetLicenseState method

The **GetLicenseState** method gets the license state.

## Syntax


```C++
HRESULT GetLicenseState(
  [in]  BYTE  *pbStateQueryData,
  [in]  DWORD cbStateQueryData,
  [out] DWORD *pdwCategory,
  [out] DWORD *pcRemainingCounts,
  [out] DWORD *pcRemainingHours,
  [out] DWORD *pdwReserved
);
```



## Parameters

<dl> <dt>

*pbStateQueryData* \[in\]
</dt> <dd>

Pointer to the queried data of the license state.

</dd> <dt>

*cbStateQueryData* \[in\]
</dt> <dd>

Count of the queried data.

</dd> <dt>

*pdwCategory* \[out\]
</dt> <dd>

Pointer to the category.

</dd> <dt>

*pcRemainingCounts* \[out\]
</dt> <dd>

Pointer to the remaining counts.

</dd> <dt>

*pcRemainingHours* \[out\]
</dt> <dd>

Pointer to the remaining hours.

</dd> <dt>

*pdwReserved* \[out\]
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                     |
|--------------------------------------------------------------------------------------|---------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeds.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMDDRMSP.idl</dt> </dl> |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMDevice2 Interface**](iwmdrmdevice2.md)
</dt> </dl>

 

 





