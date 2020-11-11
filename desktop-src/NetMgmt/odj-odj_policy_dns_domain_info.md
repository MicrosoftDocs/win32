---
title: ODJ_POLICY_DNS_DOMAIN_INFO
description: ODJ_POLICY_DNS_DOMAIN_INFO IDL Definition
ms.assetid: 44b1145f-3bdd-42cd-a88f-9b41888cc644
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# ODJ_POLICY_DNS_DOMAIN_INFO structure

Contains information about the domain and forest that a client should be joined to.

## Syntax

```C++
typedef struct _ODJ_POLICY_DNS_DOMAIN_INFO
{
    ODJ_UNICODE_STRING Name;
    ODJ_UNICODE_STRING DnsDomainName;
    ODJ_UNICODE_STRING DnsForestName;
    GUID DomainGuid;
    PODJ_SID Sid;
} ODJ_POLICY_DNS_DOMAIN_INFO;
```

## Members

### Name

Must be set to a Netbios domain name.

### DnsDomainName

Must be set to a domain name in DNS format.

### DnsForestName

Must be set to a forest name in DNS format.

### DomainGuid

Must be set to the domain guid.

### Sid

Must be set to the domain sid.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)

[**ODJ\_UNICODE\_STRING**](odj-odj_unicode_string.md)

[**ODJ\_SID**](odj-odj_sid.md)
