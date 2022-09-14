---
UID: NN:dstorage.IDStorageQueue
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue
ms.date: 08/25/2022
targetos: Windows
description: Represents a DirectStorage queue to perform read operations.
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
 - IDStorageQueue
f1_keywords:
 - IDStorageQueue
 - dstorage/IDStorageQueue
dev_langs:
 - c++
helpviewer_keywords:
 - IDStorageQueue
---

# IDStorageQueue interface (dstorage.h)

Represents a DirectStorage queue to perform read operations.

## Inheritance

The **IDStorageQueue** interface inherits from the **IUnknown** interface.

## Methods

The **IDStorageQueue** interface has these methods.

| &nbsp; |
| ---- |
| [IDStorageQueue::CancelRequestsWithTag](../dstorage/nf-dstorage-idstoragequeue-cancelrequestswithtag.md) <br><br> Attempts to cancel a group of previously enqueued read requests.|
| [IDStorageQueue::Close](../dstorage/nf-dstorage-idstoragequeue-close.md) <br><br> Closes the DirectStorage queue, regardless of the reference count on this object.|
| [IDStorageQueue::EnqueueRequest](../dstorage/nf-dstorage-idstoragequeue-enqueuerequest.md) <br><br> Enqueues a read request to the queue.|
| [IDStorageQueue::EnqueueSignal](../dstorage/nf-dstorage-idstoragequeue-enqueuesignal.md) <br><br> Enqueues fence write.|
| [IDStorageQueue::EnqueueStatus](../dstorage/nf-dstorage-idstoragequeue-enqueuestatus.md) <br><br> Enqueues a status write.|
| [IDStorageQueue::GetErrorEvent](../dstorage/nf-dstorage-idstoragequeue-geterrorevent.md) <br><br> Obtains an event to wait on.|
| [IDStorageQueue::Query](../dstorage/nf-dstorage-idstoragequeue-query.md) <br><br> Obtains information about the queue.|
| [IDStorageQueue::RetrieveErrorRecord](../dstorage/nf-dstorage-idstoragequeue-retrieveerrorrecord.md) <br><br> When the error event is signaled, this function can be called to retrieve a [DSTORAGE_ERROR_RECORD](ns-dstorage-dstorage_error_record.md).|
| [IDStorageQueue::Submit](../dstorage/nf-dstorage-idstoragequeue-submit.md) <br><br> Submits all requests enqueued so far to DirectStorage to be executed.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
