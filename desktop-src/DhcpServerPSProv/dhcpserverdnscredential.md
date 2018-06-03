---
title: DhcpServerDnsCredential class
description: Dhcp Server v4 Multicast Scope Statistics class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f3b25451-d47e-462f-a269-aa019539f0b8
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerDnsCredential class
- DhcpServerDnsCredential class, described
topic_type:
- apiref
api_name:
- DhcpServerDnsCredential
- DhcpServerDnsCredential.UserName
- DhcpServerDnsCredential.DomainName
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerDnsCredential class

Dhcp Server v4 Multicast Scope Statistics class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerDnsCredential
{
  string UserName;
  string DomainName;
};
```

## Members

The **DhcpServerDnsCredential** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerDnsCredential** class has these properties.

<dl> <dt>

**DomainName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The domain name of the account used for DNS registrations.

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The user name of the account used for DNS registrations.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





