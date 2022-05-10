---
title: IDOManager::EnumDownloads method
description: Retrieves an interface pointer to an enumerator object that is used to enumerate existing downloads.
keywords:
- IDOManager::EnumDownloads method
topic_type:
- apiref
api_name:
- IDOManager.EnumDownloads
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 07/03/2019
---

# IDOManager::EnumDownloads method

Retrieves an interface pointer to an enumerator object that is used to enumerate existing downloads.

## Syntax

```cpp
HRESULT EnumDownloads(
  DO_DOWNLOAD_ENUM_CATEGORY *category, 
  IEnumUnknown **ppEnum
);
```

## Parameters

`category`

Optional. The property name to be used as a category to enumerate. Passing `nullptr` will retrieve all existing downloads. The following properties are supported as a category.

- **DODownloadProperty_Id**
- **DODownloadProperty_Uri**
- **DODownloadProperty_ContentId**
- **DODownloadProperty_DisplayName**
- **DODownloadProperty_LocalPath**

`ppEnum`

The address of an interface pointer to **IEnumUnknown**, which is used to enumerate existing downloads. The contents of the enumerator depend on the value of *category*. The downloads included in the enumeration interface are the ones that were previously created by the same caller to this function. 

## Return Value

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
