---
title: OP_JOINPROV2_PART
description: OP_JOINPROV2_PART IDL Definition
ms.assetid: c220627e-49bd-49f2-a03c-9cdef4b973ca
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_JOINPROV2_PART structure

Contains additional information used for configuring a client joined to a domain.

## Syntax

```C++
typedef struct _OP_JOINPROV2_PART
{
    DWORD     dwFlags;
    [string] wchar_t *lpNetbiosName;
    [string] wchar_t *lpSiteName;
    [string] wchar_t *lpPrimaryDNSDomain;
    DWORD             dwReserved;
    [string] wchar_t *lpReserved;
} OP_JOINPROV2_PART, *POP_JOINPROV2_PART;
```

## Members

### dwFlags

Must be set to either zero or one of the following values:

|Value|Meaning|
| --- | --- |
|OP_JP2_FLAG_PERSISTENTSITE (0x00000001)|The site specified in lpSiteName MUST be considered the permanent site for the client.|

### lpNetbiosName

Contains the Netbios name of the machine account in Unicode format.

### lpSiteName

Contains the name of the Active Directory site that the client should use.

### lpPrimaryDNSDomain

Contains the primary DNS domain name that the client should use.

### dwReserved

Reserved for future use and must be set to 0.

### lpReserved

Reserved for future use and must be set to NULL.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)
