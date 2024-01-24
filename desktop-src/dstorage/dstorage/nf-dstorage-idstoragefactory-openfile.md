---
UID: NF:dstorage.IDStorageFactory.OpenFile
ms.topic: reference
tech.root: dstorage
title: IDStorageFactory::OpenFile
ms.date: 08/25/2022
targetos: Windows
description: Opens a file for DirectStorage access.
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
 - IDStorageFactory::OpenFile
f1_keywords:
 - IDStorageFactory::OpenFile
 - dstorage/IDStorageFactory::OpenFile
dev_langs:
 - c++
helpviewer_keywords:
 - OpenFile
---

# IDStorageFactory::OpenFile method (dstorage.h)

Opens a file for DirectStorage access.

## Syntax

```cpp
HRESULT OpenFile(
  const WCHAR *path,
  REFIID      riid,
  void        **ppv
);
```

## Parameters

`path`

Path of the file to be opened.

`riid`

Specifies the DirectStorage file interface, such as `__uuidof(IDStorageFile)`.

`ppv`

Receives the new file opened.

## Return value

Standard HRESULT error code.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
