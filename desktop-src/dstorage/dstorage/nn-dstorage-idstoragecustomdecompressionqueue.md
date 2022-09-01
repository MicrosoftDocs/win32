---
UID: NN:dstorage.IDStorageCustomDecompressionQueue
ms.topic: reference
tech.root: dstorage
title: IDStorageCustomDecompressionQueue
ms.date: 08/25/2022
targetos: Windows
description: A queue of decompression requests.
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
 - IDStorageCustomDecompressionQueue
f1_keywords:
 - IDStorageCustomDecompressionQueue
 - dstorage/IDStorageCustomDecompressionQueue
dev_langs:
 - c++
helpviewer_keywords:
 - IDStorageCustomDecompressionQueue
---

# IDStorageCustomDecompressionQueue interface (dstorage.h)

A queue of decompression requests. This can be obtained using **QueryInterface** against the factory. Your application must take requests from this queue, decompress them, and report that decompression is complete. That allows an application to provide its own custom decompression.

## Inheritance

The **IDStorageCustomDecompressionQueue** interface inherits from the **IUnknown** interface.

## Methods

The **IDStorageCustomDecompressionQueue** interface has these methods.

| &nbsp; |
| ---- |
| [IDStorageCustomDecompressionQueue::GetEvent](../dstorage/nf-dstorage-idstoragecustomdecompressionqueue-getevent.md) <br><br> Obtains an event to wait on. This event is set when there are pending decompression requests.|
| [IDStorageCustomDecompressionQueue::GetRequests](../dstorage/nf-dstorage-idstoragecustomdecompressionqueue-getrequests.md) <br><br> Populates the given array of request structs with new pending requests.|
| [IDStorageCustomDecompressionQueue::SetRequestResults](../dstorage/nf-dstorage-idstoragecustomdecompressionqueue-setrequestresults.md) <br><br> Your application calls this to indicate that requests have been completed.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
