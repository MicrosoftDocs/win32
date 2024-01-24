---
UID: NF:dstorage.IDStorageFile.Close
ms.topic: reference
tech.root: dstorage
title: IDStorageFile::Close
ms.date: 08/25/2022
targetos: Windows
description: Closes the file, regardless of the reference count on this object. 
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
 - IDStorageFile::Close
f1_keywords:
 - IDStorageFile::Close
 - dstorage/IDStorageFile::Close
dev_langs:
 - c++
helpviewer_keywords:
 - Close
---

# IDStorageFile::Close method (dstorage.h)

Closes the file, regardless of the reference count on this object. After an [IDStorageFile](nn-dstorage-idstoragefile.md) object is closed, it can no longer be used in DirectStorage requests.

## Syntax

```cpp
void Close();
```

## Return value

None

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
