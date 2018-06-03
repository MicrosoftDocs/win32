---
title: DnsServerSigningKeyExtendedInformation class
description: Represents extended information for a DNS server signing key.
audience: developer
ms.assetid: ff506731-533d-4dd8-b716-dc81ae57d85b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerSigningKeyExtendedInformation class
- DnsServerSigningKeyExtendedInformation class, described
topic_type:
- apiref
api_name:
- DnsServerSigningKeyExtendedInformation
- DnsServerSigningKeyExtendedInformation.SigningKey
- DnsServerSigningKeyExtendedInformation.SigningKeyOpState
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerSigningKeyExtendedInformation class

Represents extended information for a DNS server signing key.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerSigningKeyExtendedInformation
{
  DnsServerSigningKey        SigningKey;
  DnsServerSigningKeyOpState SigningKeyOpState;
};
```

## Members

The **DnsServerSigningKeyExtendedInformation** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerSigningKeyExtendedInformation** class has these properties.

<dl> <dt>

**SigningKey**
</dt> <dd> <dl> <dt>

Data type: **DnsServerSigningKey**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerSigningKey**](dnsserversigningkey.md)")
</dt> </dl>

An identifier of the signing key.

</dd> <dt>

**SigningKeyOpState**
</dt> <dd> <dl> <dt>

Data type: **DnsServerSigningKeyOpState**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerSigningKeyOpState**](dnsserversigningkeyopstate.md)")
</dt> </dl>

An identifier of the operational state of the signing key.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





