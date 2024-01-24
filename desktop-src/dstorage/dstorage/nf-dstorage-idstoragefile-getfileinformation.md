---
UID: NF:dstorage.IDStorageFile.GetFileInformation
ms.topic: reference
tech.root: dstorage
title: IDStorageFile::GetFileInformation
ms.date: 08/25/2022
targetos: Windows
description: Retrieves file information for an opened file.
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
 - IDStorageFile::GetFileInformation
f1_keywords:
 - IDStorageFile::GetFileInformation
 - dstorage/IDStorageFile::GetFileInformation
dev_langs:
 - c++
helpviewer_keywords:
 - GetFileInformation
---

# IDStorageFile::GetFileInformation method (dstorage.h)

Retrieves file information for an opened file.

## Syntax

```cpp
HRESULT GetFileInformation(
  BY_HANDLE_FILE_INFORMATION *info
);
```

## Parameters

`info`

Receives the file information.

## Return value

Standard HRESULT error code.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
