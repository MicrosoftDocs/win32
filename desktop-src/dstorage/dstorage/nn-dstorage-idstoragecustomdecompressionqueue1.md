---
UID: NN:dstorage.IDStorageCustomDecompressionQueue1
ms.topic: reference
tech.root: dstorage
title: IDStorageCustomDecompressionQueue1
ms.date: 11/22/2022
targetos: Windows
description: A queue of decompression requests that allows you to retrieve specific types of custom decompression requests from the decompression queue.
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
 - IDStorageCustomDecompressionQueue1
f1_keywords:
 - IDStorageCustomDecompressionQueue1
 - dstorage/IDStorageCustomDecompressionQueue1
dev_langs:
 - c++
helpviewer_keywords:
 - IDStorageCustomDecompressionQueue1
---

# IDStorageCustomDecompressionQueue1 interface (dstorage.h)

A queue of decompression requests that allows you to retrieve specific types of custom decompression requests from the decompression queue. This can be obtained using **QueryInterface** against the factory. Your application must take requests from this queue, decompress them, and report that decompression is complete. That allows an application to provide its own custom decompression.

## Inheritance

The **IDStorageCustomDecompressionQueue1** interface inherits from the [**IDStorageCustomDecompressionQueue**](nn-dstorage-idstoragecustomdecompressionqueue.md) interface.

## Methods

The **IDStorageCustomDecompressionQueue1** interface has these methods.

| &nbsp; |
| ---- |
| [IDStorageCustomDecompressionQueue1::GetRequests1](../dstorage/nf-dstorage-idstoragecustomdecompressionqueue1-getrequests1.md) <br><br> Populates the given array of request structs with new pending requests based on the specified custom decompression request type.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
