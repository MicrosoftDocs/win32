---
title: IDODownload::GetProperty method
description: Retrieves a pointer to a **VARIANT** that contains a specific download property.
keywords:
- IDODownload::GetProperty method
topic_type:
- apiref
api_name:
- IDODownload.GetProperty
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 07/03/2019
---

# IDODownload::GetProperty method

Retrieves a pointer to a **VARIANT** that contains a specific download property.

## Syntax

```cpp
HRESULT GetProperty(
  DODownloadProperty propId, 
  VARIANT* propVal
);
```

## Parameters

`propId`

The required property ID to get (of type **DODownloadProperty**).

`propVal`

The resulting property value, stored in a **VARIANT**.

## Return Value

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

|Return value|Description|
|-|-|
|DO_E_UNKNOWN_PROPERTY_ID|*propId* is unknown.|
|DO_E_WRITE_ONLY_PROPERTY|The property is write-only, and cannot be read.|
|E_NOT_SET|No such property was set via **SetProperty**.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
