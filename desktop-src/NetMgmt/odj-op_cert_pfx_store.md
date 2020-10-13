---
title: OP_CERT_PFX_STORE
description: OP_CERT_PFX_STORE IDL Definition
ms.assetid: 10773feb-623c-4256-a973-f006ed66d936
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_CERT_PFX_STORE structure

Contains a serialized PFX structure.

## Syntax

```C++
typedef struct _OP_CERT_PFX_STORE
{
    [string] wchar_t            *pTemplateName;
    ULONG                       ulPrivateKeyExportPolicy;
    [string] wchar_t            *pPolicyServerUrl;
    ULONG                       ulPolicyServerUrlFlags;
    [string] wchar_t            *pPolicyServerId;
    ULONG                       cbPfx;
    [size_is(cbPfx)]    PBYTE   pPfx;
} OP_CERT_PFX_STORE, *POP_CERT_PFX_STORE;
```

## Members

### pTemplateName

Must be set to the name of the certificate template used to create the certificate.

### ulPrivateKeyExportPolicy

Contains one value from the [**X509PrivateKeyExportFlags**](/windows/win32/api/certenroll/ne-certenroll-x509privatekeyexportflags) enumeration.

### pPolicyServerUrl

Must be set the URL of the policy server.

### ulPolicyServerUrlFlags

Contains one value from the [**PolicyServerUrlFlags**](/windows/win32/api/certenroll/ne-certenroll-policyserverurlflags) enumeration.

### pPolicyServerId

Contains a string that uniquely identifies the policy server

### cbPfx

Contains the size of pPfx in bytes.

### pPfx

Contains a serialized PFX structure (see [**RFC 7292**](https://tools.ietf.org/html/rfc7292)).

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)
