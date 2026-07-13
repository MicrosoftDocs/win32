---
UID: NN:dstorage.IDStorageQueue3
title: IDStorageQueue3
description: Represents a DirectStorage queue to perform read operations, allowing enqueuing an operation to set a specific event object to a signaled state. Also allows you to enqueue an array of requests.
ms.date: 06/19/2025
ms.topic: reference
tech.root: dstorage
targetos: Windows
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
 - IDStorageQueue3
f1_keywords:
 - IDStorageQueue3
 - dstorage/IDStorageQueue3
dev_langs:
 - c++
helpviewer_keywords:
 - IDStorageQueue3
---

# IDStorageQueue3 interface (dstorage.h)

Represents a DirectStorage queue to perform read operations, allowing enqueuing an operation to set a specific event object to a signaled state. Also allows you to enqueue an array of requests.

## Inheritance

The **IDStorageQueue3** interface inherits from the [**IDStorageQueue2**](nn-dstorage-idstoragequeue2.md) interface.

## Methods

The **IDStorageQueue3** interface has these methods.

| &nbsp; |
| ---- |
| [IDStorageQueue3::EnqueueRequests](../dstorage/nf-dstorage-idstoragequeue3-enqueurequests.md) <br><br> Enqueues an array of requests to the queue. The requests will be synchronized with the specified ID3D12Fence, and processed after the synchronization point.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
