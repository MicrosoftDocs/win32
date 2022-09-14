---
UID: NN:dstorage.IDStorageStatusArray
ms.topic: reference
tech.root: dstorage
title: IDStorageStatusArray
ms.date: 08/25/2022
targetos: Windows
description: Represents an array of status entries to receive completion results for the read requests before them.
prerelease: false
req.assembly: 
req.construct-type: iface
req.ddi-compliance: 
req.header: dstorage.h
req.idl: 
req.include-header: 
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - COM
api_location:
 - dstorage.h
api_name:
 - IDStorageStatusArray
f1_keywords:
 - IDStorageStatusArray
 - dstorage/IDStorageStatusArray
dev_langs:
 - c++
helpviewer_keywords:
 - IDStorageStatusArray
---

# IDStorageStatusArray interface (dstorage.h)

Represents an array of status entries to receive completion results for the read requests before them.

## Inheritance

The **IDStorageStatusArray** interface inherits from the **IUnknown** interface.

## Methods

The **IDStorageStatusArray** interface has these methods.

| &nbsp; |
| ---- |
| [IDStorageStatusArray::GetHResult](../dstorage/nf-dstorage-idstoragestatusarray-gethresult.md) <br><br> Returns the **HRESULT** code of all requests between the specified status entry and the status entry enqueued before it.|
| [IDStorageStatusArray::IsComplete](../dstorage/nf-dstorage-idstoragestatusarray-iscomplete.md) <br><br> Returns a Boolean value indicating whether all requests enqueued prior to the specified status entry have completed.|

## Remarks

A status entry receives completion status for all the requests in the DStorageQueue between where it is enqueued and the previously enqueued status entry. Only when all requests enqueued before the status entry complete (that is, [IsComplete](nf-dstorage-idstoragestatusarray-iscomplete.md) for the entry returns true), can the status entry be enqueued again.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
