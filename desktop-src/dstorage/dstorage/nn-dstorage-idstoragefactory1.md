---
UID: NN:dstorage.IDStorageFactory1
ms.topic: reference
tech.root: dstorage
title: IDStorageFactory1
ms.date: 10/30/2026
targetos: Windows
description: Represents the static DirectStorage object used to create DirectStorage queues, open files for DirectStorage access, and other global operations. Also allows you to create a queue that services a declared compression format.
prerelease: true
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
 - IDStorageFactory1
f1_keywords:
 - IDStorageFactory1
 - dstorage/IDStorageFactory1
dev_langs:
 - c++
helpviewer_keywords:
 - IDStorageFactory1
---

# IDStorageFactory1 interface (dstorage.h)

Represents the static DirectStorage object used to create DirectStorage queues, open files for DirectStorage access, and other global operations. Also allows you to create a queue that services a declared compression format.

## Inheritance

The **IDStorageFactory1** interface inherits from the [**IDStorageFactory**](nn-dstorage-idstoragefactory.md) interface.

## Methods

The **IDStorageFactory1** interface has these methods.

| &nbsp; |
| ---- |
| [IDStorageFactory1::CreateQueue1](../dstorage/nf-dstorage-idstoragefactory1-createqueue1.md) <br><br> Creates a DirectStorage queue object that services a declared compression format.|

## Remarks

Obtain it with [DStorageGetFactory](nf-dstorage-dstoragegetfactory.md)`(IID_PPV_ARGS(...))`.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
