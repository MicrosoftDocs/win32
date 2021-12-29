---
title: IDODownload::SetProperty method
description: Sets a download property.
keywords:
- IDODownload::SetProperty method
topic_type:
- apiref
api_name:
- IDODownload.SetProperty
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 07/03/2019
---

# IDODownload::SetProperty method

Sets a download property. The method accepts a pointer to a **VARIANT** that contains a specific property to apply to the download.

## Syntax

```cpp
HRESULT SetProperty(
  DODownloadProperty propId,
  VARIANT* propVal
);
```

## Parameters

`propId`

The required property ID to set (of type **DODownloadProperty**).

`propVal`

The property value to set, stored in a **VARIANT**.

## Return Value

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

|Return value|Description|
|-|-|
|DO_E_UNKNOWN_PROPERTY_ID|*propId* is unknown.|
|DO_E_INVALID_STATE|The download is not currently in a state that allows setting properties.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
