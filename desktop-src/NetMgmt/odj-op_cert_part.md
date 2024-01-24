---
title: OP_CERT_PART
description: OP_CERT_PART IDL Definition
ms.assetid: 30492801-f26e-447f-bcbf-d1108e7ae524
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_CERT_PART structure

Contains serialized PFX and certificate stores.

## Syntax

```C++
typedef struct _OP_CERT_PART
{
    ULONG                                       cPfxStores;
    [size_is(cPfxStores)]   POP_CERT_PFX_STORE  pPfxStores;
    ULONG                                       cSstStores;
    [size_is(cSstStores)]   POP_CERT_SST_STORE  pSstStores;
    OP_BLOB                                     Extension;
} OP_CERT_PART, *POP_CERT_PART;
```

## Members

### cPfxStores

Contains the number of elements in pPfxStores.

### pPfxStores

Contains an array of OP_CERT_PFX_STORE structures.

### cSstStores

Contains the number of elements in pSstStores.

### pSstStores

Contains an array of OP_CERT_SST_STORE structures.

### Extension

Reserved for future use and must contain all zeros.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)

[**OP\_CERT\_PFX\_STORE**](odj-op_cert_pfx_store.md)

[**OP\_CERT\_SST\_STORE**](odj-op_cert_sst_store.md)

[**OP\_BLOB**](odj-op_blob.md)

