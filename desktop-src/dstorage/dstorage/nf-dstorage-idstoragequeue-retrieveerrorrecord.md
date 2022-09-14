---
UID: NF:dstorage.IDStorageQueue.RetrieveErrorRecord
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue::RetrieveErrorRecord
ms.date: 08/25/2022
targetos: Windows
description: When the error event is signaled, this function can be called to retrieve a [DSTORAGE_ERROR_RECORD](ns-dstorage-dstorage_error_record.md).
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
 - IDStorageQueue::RetrieveErrorRecord
f1_keywords:
 - IDStorageQueue::RetrieveErrorRecord
 - dstorage/IDStorageQueue::RetrieveErrorRecord
dev_langs:
 - c++
helpviewer_keywords:
 - RetrieveErrorRecord
---

# IDStorageQueue::RetrieveErrorRecord method (dstorage.h)

When the error event is signaled, this function can be called to retrieve a [DSTORAGE_ERROR_RECORD](ns-dstorage-dstorage_error_record.md). Once the error record is retrieved, this function should not be called until the next time the error event is signaled.

## Syntax

```cpp
void RetrieveErrorRecord(
  DSTORAGE_ERROR_RECORD *record
);
```

## Parameters

`record`

Receives the error record.

## Return value

None

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
