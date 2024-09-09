---
UID: NF:dstorage.DStorageGetFactory
ms.topic: reference
tech.root: dstorage
title: DStorageGetFactory
ms.date: 08/25/2022
targetos: Windows
description: Returns the static DirectStorage factory object used to create DirectStorage queues, open files for DirectStorage access, and other global operations.
prerelease: false
req.assembly: 
req.construct-type: function
req.ddi-compliance: 
req.dll: 
req.header: dstorage.h
req.idl: 
req.include-header: 
req.irql: 
req.kmdf-ver: 
req.lib: 
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.type-library: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - DllExport
api_location:
 - dstorage.h
api_name:
 - DStorageGetFactory
f1_keywords:
 - DStorageGetFactory
 - dstorage/DStorageGetFactory
dev_langs:
 - c++
helpviewer_keywords:
 - DStorageGetFactory
---

# DStorageGetFactory function (dstorage.h)

Returns the static DirectStorage factory object used to create DirectStorage queues, open files for DirectStorage access, and other global operations.

## Syntax

```cpp
HRESULT DStorageGetFactory(
  REFIID riid,
  void   **ppv
);
```

## Parameters

`riid`

Specifies the DirectStorage factory interface, such as `__uuidof(IDStorageFactory)`.

`ppv`

Receives the DirectStorage factory object.

## Return value

Standard HRESULT error code.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
