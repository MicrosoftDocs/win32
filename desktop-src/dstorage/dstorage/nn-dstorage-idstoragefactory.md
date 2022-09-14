---
UID: NN:dstorage.IDStorageFactory
ms.topic: reference
tech.root: dstorage
title: IDStorageFactory
ms.date: 08/25/2022
targetos: Windows
description: Represents the static DirectStorage object used to create DirectStorage queues, open files for DirectStorage access, and other global operations.
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
 - IDStorageFactory
f1_keywords:
 - IDStorageFactory
 - dstorage/IDStorageFactory
dev_langs:
 - c++
helpviewer_keywords:
 - IDStorageFactory
---

# IDStorageFactory interface (dstorage.h)

Represents the static DirectStorage object used to create DirectStorage queues, open files for DirectStorage access, and other global operations.

## Inheritance

The **IDStorageFactory** interface inherits from the **IUnknown** interface.

## Methods

The **IDStorageFactory** interface has these methods.

| &nbsp; |
| ---- |
| [IDStorageFactory::CreateQueue](../dstorage/nf-dstorage-idstoragefactory-createqueue.md) <br><br> Creates a DirectStorage queue object.|
| [IDStorageFactory::CreateStatusArray](../dstorage/nf-dstorage-idstoragefactory-createstatusarray.md) <br><br> Creates a DirectStorage status array object.|
| [IDStorageFactory::OpenFile](../dstorage/nf-dstorage-idstoragefactory-openfile.md) <br><br> Opens a file for DirectStorage access.|
| [IDStorageFactory::SetDebugFlags](../dstorage/nf-dstorage-idstoragefactory-setdebugflags.md) <br><br> Sets flags used to control the debug layer.|
| [IDStorageFactory::SetStagingBufferSize](../dstorage/nf-dstorage-idstoragefactory-setstagingbuffersize.md) <br><br> Sets the size of staging buffer(s) used to temporarily store content loaded from the storage device before they are decompressed.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
