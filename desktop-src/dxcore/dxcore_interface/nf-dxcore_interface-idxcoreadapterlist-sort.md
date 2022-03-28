---
title: IDXCoreAdapterList::Sort
description: Sorts a DXCore adapter list object based on a provided input array of sort criteria.
ms.topic: reference
ms.date: 09/03/2019
---

# IDXCoreAdapterList::Sort method

## Description

Sorts a DXCore adapter list object based on a provided input array of sort criteria, where array items earlier in the array of criteria are given a higher weight. **Sort** helps you to more easily find your ideal adapter in an adapter list.

## Syntax

```cpp
HRESULT Sort(
  uint32_t numPreferences,
  _In_reads_(numPreferences) const DXCoreAdapterPreference* preferences
);
```

## Parameters

### numPreferences

Type: **uint32_t**

The number of elements that are in the array pointed to by the *preferences* parameter.

### preferences [in]

Type: **const [DXCoreAdapterPreference](./ne-dxcore_interface-dxcoreadapterpreference.md)\***

A pointer to a constant array of [DXCoreAdapterPreference](./ne-dxcore_interface-dxcoreadapterpreference.md) values, representing sort criteria.

## Returns

Type: **[HRESULT](../../com/structure-of-com-error-codes.md)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](../../com/structure-of-com-error-codes.md) [error code](../../com/com-error-codes-10.md).

|Return value|Description|
|-|-|
|E_INVALIDARG|The *numPreferences* argument is zero, or the *preferences* argument is `nullptr`.|

## Remarks

In cases where a provided [DXCoreAdapterPreference](./ne-dxcore_interface-dxcoreadapterpreference.md) value isn't recognized by the operating system (OS), it is ignored, and won't cause the API to fail. Known **DXCoreAdapterPreference** values will still be considered in this case. To determine whether a sort type is understood by the API, call [IDXCoreAdapterList::IsAdapterPreferenceSupported](./nf-dxcore_interface-idxcoreadapterlist-isadapterpreferencesupported.md).

**DXCoreAdapterPreference** values that occur earlier in the provided *preferences* array are treated with higher priority. 

Refer to the **DXCoreAdapterPreference** enumeration documentation for details about what logic is applied for each type. The internal logic for a type may develop as the OS develops.

When **Sort** returns, items in the DXCore adapter list will have been sorted from most preferable to least preferable. So, calling [IDXCoreAdapterList::GetAdapter](./nf-dxcore_interface-idxcoreadapterlist-getadapter.md) with index 0 retrieves the adapter that best matches the requested sort preference types; index 1 is the next best match, and so on.

## See also

[IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
