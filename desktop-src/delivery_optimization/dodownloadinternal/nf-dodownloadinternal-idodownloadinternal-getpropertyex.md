---
title: IDODownloadInternal::GetPropertyEx method
description: Retrieves a pointer to a **VARIANT** that contains a specific extended download property value.
keywords:
- IDODownloadInternal::GetPropertyEx method
topic_type:
- apiref
api_name:
- IDODownloadInternal.GetPropertyEx
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 07/29/2019
---

# IDODownloadInternal::GetPropertyEx method

> [!IMPORTANT]
> The **IDODownloadInternal** interface is deprecated. Instead, use the [IDODownload](../do/nn-do-idodownload.md) interface.

Retrieves a pointer to a **VARIANT** that contains a specific extended download property value.

## Syntax

```cpp
HRESULT GetPropertyEx(
  DODownloadPropertyEx propId, 
  VARIANT* propVal
);
```

## Parameters

`propId`

The required property ID to get (of type **DODownloadPropertyEx**).

`propVal`

The resulting property value, stored in a **VARIANT**.

## Return Value

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

|Return value|Description|
|-|-|
|DO_E_UNKNOWN_PROPERTY_ID|*propId* is unknown.|
|DO_E_WRITE_ONLY_PROPERTY|The property is write-only, and cannot be read.|
|E_NOT_SET|No such property was set via **SetPropertyEx**.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | DODownloadInternal.h |
