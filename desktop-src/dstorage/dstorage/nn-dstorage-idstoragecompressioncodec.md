---
UID: NN:dstorage.IDStorageCompressionCodec
ms.topic: reference
tech.root: dstorage
title: IDStorageCompressionCodec
ms.date: 11/22/2022
targetos: Windows
description: Represents a DirectStorage object for compressing and decompressing buffers.
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
 - IDStorageCompressionCodec
f1_keywords:
 - IDStorageCompressionCodec
 - dstorage/IDStorageCompressionCodec
dev_langs:
 - c++
helpviewer_keywords:
 - IDStorageCompressionCodec
---

# IDStorageCompressionCodec interface (dstorage.h)

Represents a DirectStorage object for compressing and decompressing buffers. Use [DStorageCreateCompressionCodec](nf-dstorage-dstoragecreatecompressioncodec.md) to get an instance of this.

## Inheritance

The **IDStorageCompressionCodec** interface inherits from the **IUnknown** interface.

## Methods

The **IDStorageCompressionCodec** interface has these methods.

| &nbsp; |
| ---- |
| [IDStorageCompressionCodec::CompressBuffer](../dstorage/nf-dstorage-idstoragecompressioncodec-compressbuffer.md) <br><br> Compresses a buffer of data using a known compression format at the specified compression level.|
| [IDStorageCompressionCodec::CompressBufferBound](../dstorage/nf-dstorage-idstoragecompressioncodec-compressbufferbound.md) <br><br> Retrieves an upper bound estimated size, in bytes, required to compress the specified data size.|
| [IDStorageCompressionCodec::DecompressBuffer](../dstorage/nf-dstorage-idstoragecompressioncodec-decompressbuffer.md) <br><br> Decompresses data previously compressed using [CompressBuffer](nf-dstorage-idstoragecompressioncodec-compressbuffer.md).|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
