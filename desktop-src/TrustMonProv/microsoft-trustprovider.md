---
Description: 'Includes properties that control how domains are enumerated.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '5db6c38a-0cbf-46c9-8a90-dbd401d3b015'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Microsoft\_TrustProvider class'
---

# Microsoft\_TrustProvider class

The Microsoft\_TrustProvider [WMI class](https://msdn.microsoft.com/library/aa393244) includes properties that control how domains are enumerated.

## Syntax

``` syntax
[singleton]
class Microsoft_TrustProvider
{
  uint32  TrustListLifetime;
  uint32  TrustStatusLifetime;
  uint32  TrustCheckLevel;
  boolean ReturnAll;
};
```

## Members

The **Microsoft\_TrustProvider** class has these types of members:

-   [Properties](#properties)

### Properties

The **Microsoft\_TrustProvider** class has these properties.

<dl> <dt>

**ReturnAll**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, enumerations return trusting as well as trusted domains.

</dd> <dt>

**TrustCheckLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of enumeration to use when enumerating domains.

<dt>

0
</dt> <dd>

Enumerate only

</dd> <dt>

1
</dt> <dd>

Enumerate with SC\_QUERY (verifies the secure channel between the domains).

</dd> <dt>

2
</dt> <dd>

Enumerate with password check

</dd> <dt>

3
</dt> <dd>

Enumerate with SC\_RESET (resets the secure channel between the domains.)

</dd> </dl>

</dd> <dt>

**TrustListLifetime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time in minutes to cache the last trust enumeration.

</dd> <dt>

**TrustStatusLifetime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time in minutes to cache the last request for status.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\microsoftactivedirectory<br/>                                               |
| MOF<br/>                      | <dl> <dt>Trustmon.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Trustmon.dll</dt> </dl> |



## See also

<dl> <dt>

[Microsoft\_DomainTrustStatus](microsoft-domaintruststatus.md)
</dt> <dt>

[Microsoft\_LocalDomainInfo](microsoft-localdomaininfo.md)
</dt> <dt>

[Trustmon Provider](trustmon-provider.md)
</dt> </dl>

 

 




