---
title: PS\_DnsServerSigningKeyRollover class
description: DNS Server Signing Key Rollover Task Definition.
audience: developer
ms.assetid: 'a1d86b01-2a5e-4a5d-b1a9-2ca45d5d45e6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerSigningKeyRollover class", "PS_DnsServerSigningKeyRollover class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerSigningKeyRollover
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerSigningKeyRollover class

DNS Server Signing Key Rollover Task Definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerSigningKeyRollover
{
};
```

## Members

The **PS\_DnsServerSigningKeyRollover** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerSigningKeyRollover** class has these methods.



| Method                                                    | Description                                                            |
|:----------------------------------------------------------|:-----------------------------------------------------------------------|
| [**Disable**](disable-ps-dnsserversigningkeyrollover.md) | Disables key rollover on input key.<br/>                         |
| [**Enable**](enable-ps-dnsserversigningkeyrollover.md)   | Enables rollover on the input key<br/>                           |
| [**Invoke**](invoke-ps-dnsserversigningkeyrollover.md)   | Initiates rollover of input keys for the zone.<br/>              |
| [**Step**](step-ps-dnsserversigningkeyrollover.md)       | Forces KSK rollover that is waiting for a parent DS update.<br/> |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





