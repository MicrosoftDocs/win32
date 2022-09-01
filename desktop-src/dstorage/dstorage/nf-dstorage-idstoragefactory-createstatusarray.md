---
UID: NF:dstorage.IDStorageFactory.CreateStatusArray
ms.topic: reference
tech.root: dstorage
title: IDStorageFactory::CreateStatusArray
ms.date: 08/25/2022
targetos: Windows
description: Creates a DirectStorage status array object.
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
 - COM
api_location:
 - dstorage.h
api_name:
 - IDStorageFactory::CreateStatusArray
f1_keywords:
 - IDStorageFactory::CreateStatusArray
 - dstorage/IDStorageFactory::CreateStatusArray
dev_langs:
 - c++
helpviewer_keywords:
 - CreateStatusArray
---

# IDStorageFactory::CreateStatusArray method (dstorage.h)

Creates a DirectStorage status array object.

## Syntax

```cpp
HRESULT CreateStatusArray(
  UINT32 capacity,
  PCSTR  name,
  REFIID riid,
  void   **ppv
);
```

## Parameters

`capacity`

Specifies the number of statuses that the array can hold.

`name`

Specifies object's name that will appear in the Event Tracing for Windows (ETW) events if enabled through the debug layer. This is an optional parameter.

`riid`

Specifies the DirectStorage status interface, such as `__uuidof(IDStorageStatusArray)`.

`ppv`

Receives the new status array object created.

## Return value

Standard HRESULT error code.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
