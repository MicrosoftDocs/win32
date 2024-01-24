---
title: IWMDRMDevice2 GetPartialSyncList method
description: The GetPartialSyncList method gets a partial synchronization list.
ms.assetid: 4ee8e9d7-d5d1-4614-b7a1-1dcb7f07b161
keywords:
- GetPartialSyncList method windows Media Device Manager
- GetPartialSyncList method windows Media Device Manager , IWMDRMDevice2 interface
- IWMDRMDevice2 interface windows Media Device Manager , GetPartialSyncList method
topic_type:
- apiref
api_name:
- IWMDRMDevice2.GetPartialSyncList
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDevice2::GetPartialSyncList method

The **GetPartialSyncList** method gets a partial synchronization list.

## Syntax


```C++
HRESULT GetPartialSyncList(
  [in]  DWORD cMinCountThreshold,
  [in]  DWORD cMinHoursThreshold,
  [in]  DWORD dwStartingIndex,
  [in]  DWORD cItems,
  [out] BYTE  **ppbSyncList,
  [out] DWORD *pcbSyncList,
  [out] DWORD *pdwNextStartingIndex,
  [out] DWORD *pcItemsProcessed
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

*dwStartingIndex* \[in\]
</dt> <dd>

Start position for indexing.

</dd> <dt>

*cItems* \[in\]
</dt> <dd>

Count of items to be indexed.

</dd> <dt>

*ppbSyncList* \[out\]
</dt> <dd>

Retrieved license synchronization list.

</dd> <dt>

*pcbSyncList* \[out\]
</dt> <dd>

Size of the license synchronization list, in bytes.

</dd> <dt>

*pdwNextStartingIndex* \[out\]
</dt> <dd>

Next start position for indexing.

</dd> <dt>

*pcItemsProcessed* \[out\]
</dt> <dd>

Count of items being processed.

</dd> </dl>

## Return value

The method returns an **HRESULT**. All the interface methods in Windows Media Device Manager can return any of the following classes of error codes:

-   Standard COM error codes
-   Windows error codes converted to HRESULT values
-   Windows Media Device Manager error codes

For an extensive list of possible error codes, see [Error Codes](error-codes.md).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMDDRMSP.idl</dt> </dl> |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMDevice::GetSyncList**](iwmdrmdevice-getsynclist.md)
</dt> <dt>

[**IWMDRMDevice2 Interface**](iwmdrmdevice2.md)
</dt> </dl>

 

 





