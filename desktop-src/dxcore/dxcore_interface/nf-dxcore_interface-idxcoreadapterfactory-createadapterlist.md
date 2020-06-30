---
title: IDXCoreAdapterFactory::CreateAdapterList
description: Generates a list of adapter objects representing the current adapter state of the system, and meeting the criteria specified.
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapterFactory::CreateAdapterList method

Generates a list of adapter objects representing the current adapter state of the system, and meeting the criteria specified. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters).

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

A pointer to an array of adapter attribute GUIDs. For a list of attribute GUIDs, see [DXCore adapter attribute GUIDs](/windows/win32/dxcore/dxcore-adapter-attribute-guids). At least one GUID must be provided. In the case that more than one GUID is provided in the array, only adapters that meet *all* of the requested attributes will be included in the returned list.

### riid

Type: **REFIID**

A reference to the globally unique identifier (GUID) of the interface that you wish to be returned in *ppvAdapterList*. This is expected to be the interface identifier (IID) of [IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist).

### ppvAdapterList [out]

Type: **void\*\***

The address of a pointer to an interface with the IID specified in the *riid* parameter. Upon successful return, *\*ppvAdapterList* (the dereferenced address) contains a pointer to the adapter list created.

## Returns

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/win32/com/com-error-codes-10).

|Return value|Description|
|-|-|
|E_INVALIDARG|`nullptr` was provided for *filterAttributes*, or 0 was provided for *numAttributes*.|
|E_NOINTERFACE|An invalid value was provided for *riid*.|
|E_POINTER|`nullptr` was provided for *ppvAdapterList*.|

## Remarks

Even if no adapters are found, as long as the arguments are valid, **CreateAdapterList** creates a valid [IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist) object, and returns **S_OK**. Once generated, the adapters in this specific list won't change. But the list will be considered stale if one of the adapters later becomes invalid, or if a new adapter arrives that meets the provided filter criteria. The list returned by **CreateAdapterList** is not ordered in any particular way, but the ordering of a list is consistent across multiple calls, and even across operating system restarts. The ordering may change upon system configuration changes, including the addition or removal of an adapter, or a driver update on an existing adapter. You can register for these changes with [IDXCoreAdapterFactory::RegisterEventNotification](https://docs.microsoft.com/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-registereventnotification) using the notification type **DXCoreNotificationType.AdapterListStale **.

## See also

[IDXCoreAdapterFactory](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterfactory), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [DXCore adapter attribute GUIDs](/windows/win32/dxcore/dxcore-adapter-attribute-guids), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)
