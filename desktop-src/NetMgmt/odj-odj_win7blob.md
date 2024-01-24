---
title: ODJ_WIN7BLOB
description: ODJ_WIN7BLOB IDL Definition
ms.assetid: 5802e00c-b943-45d8-8298-5c2b4b996b85
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# ODJ_WIN7BLOB structure

Contains the basic information required to join a client to a domain.

## Syntax

```C++
typedef struct _ODJ_WIN7BLOB
{
    [string] wchar_t *lpDomain;
    [string] wchar_t *lpMachineName;
    [string] wchar_t *lpMachinePassword;
    ODJ_POLICY_DNS_DOMAIN_INFO  DnsDomainInfo;
    DOMAIN_CONTROLLER_INFOW DcInfo;
    DWORD Options;
} ODJ_WIN7BLOB;
```

## Members

### lpDomain

Must be set to the domain name.

### lpMachineName

Must be set to the machine name.

### lpMachinePassword

Must be set to a cleartext password for the machine account identified by lpMachineName

### DnsDomainInfo

Contains information about the domain being joined.

### DcInfo

Contains naming and addressing information about the domain controller that was used to create the machine account Active Directory.

### Options

Must be set to zero.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)

[**ODJ\_POLICY\_DNS\_DOMAIN\_INFO**](odj-odj_policy_dns_domain_info.md)

[**DOMAIN_CONTROLLER_INFOW**](/windows/win32/api/dsgetdc/ns-dsgetdc-domain_controller_infow)



