---
title: OP_CERT_SST_STORE
description: OP_CERT_SST_STORE IDL Definition
ms.assetid: 6c44756e-29f9-48fc-b678-d2b1f0fb90d4
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_CERT_SST_STORE structure

Contains a serialized certificate store.

## Syntax

```C++
typedef struct _OP_CERT_SST_STORE
{
    ULONG                       StoreLocation;
    [string] wchar_t            *pStoreName;
    ULONG                       cbSst;
    [size_is(cbSst)]    PBYTE   pSst;
} OP_CERT_SST_STORE, *POP_CERT_SST_STORE;
```

## Members

### StoreLocation

Contains an identifier for the certificate store from [**System Store Locations**](../seccrypto/system-store-locations.md).

### pStoreName

Contains the name of the store.

### cbSst

Contains the size of pSst in bytes.

### pSst

Contains a serialized certificate store (see [**RFC 7292**](https://tools.ietf.org/html/rfc7292)).

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)