---
title: IDXCoreAdapterFactory::CreateAdapterList
description: Generates a list of adapter objects representing the current adapter state of the system, and meeting the criteria specified.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapterFactory::CreateAdapterList method

Generates a list of adapter objects representing the current adapter state of the system, and meeting the criteria specified. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md).

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE CreateAdapterList(
  uint32_t numAttributes,
  _In_reads_(numAttributes) const GUID *filterAttributes,
  REFIID riid,
  _COM_Outptr_ void **ppvAdapterList) = 0;

template<class T>
HRESULT STDMETHODCALLTYPE CreateAdapterList(
  uint32_t numAttributes,
  _In_reads_(numAttributes) const GUID *filterAttributes,
  _COM_Outptr_ T **ppvAdapterList);
```

## Parameters

### numAttributes

Type: **uint32_t**

The number of elements in the array pointed to by the *filterAttributes* argument.

### filterAttributes [in]

Type: **const GUID\***

A pointer to an array of adapter attribute GUIDs. For a list of attribute GUIDs, see [DXCore adapter attribute GUIDs](../dxcore-adapter-attribute-guids.md). At least one GUID must be provided. In the case that more than one GUID is provided in the array, only adapters that meet *all* of the requested attributes will be included in the returned list.

### riid

Type: **REFIID**

A reference to the globally unique identifier (GUID) of the interface that you wish to be returned in *ppvAdapterList*. This is expected to be the interface identifier (IID) of [IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md).

### ppvAdapterList [out]

Type: **void\*\***

The address of a pointer to an interface with the IID specified in the *riid* parameter. Upon successful return, *\*ppvAdapterList* (the dereferenced address) contains a pointer to the adapter list created.

## Returns

Type: **[HRESULT](../../com/structure-of-com-error-codes.md)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](../../com/structure-of-com-error-codes.md) [error code](../../com/com-error-codes-10.md).

|Return value|Description|
|-|-|
|E_INVALIDARG|`nullptr` was provided for *filterAttributes*, or 0 was provided for *numAttributes*.|
|E_NOINTERFACE|An invalid value was provided for *riid*.|
|E_POINTER|`nullptr` was provided for *ppvAdapterList*.|

## Remarks

Even if no adapters are found, as long as the arguments are valid, **CreateAdapterList** creates a valid [IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md) object, and returns **S_OK**. Once generated, the adapters in this specific list won't change. But the list will be considered stale if one of the adapters later becomes invalid, or if a new adapter arrives that meets the provided filter criteria. The list returned by **CreateAdapterList** is not ordered in any particular way, but the ordering of a list is consistent across multiple calls, and even across operating system restarts. The ordering may change upon system configuration changes, including the addition or removal of an adapter, or a driver update on an existing adapter. You can register for these changes with [IDXCoreAdapterFactory::RegisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-registereventnotification.md) using the notification type **DXCoreNotificationType.AdapterListStale**.

## See also

[IDXCoreAdapterFactory](./nn-dxcore_interface-idxcoreadapterfactory.md), [DXCore Reference](../dxcore-reference.md), [DXCore adapter attribute GUIDs](../dxcore-adapter-attribute-guids.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
