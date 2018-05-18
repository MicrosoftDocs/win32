---
title: PS\_DhcpServerv4FailoverReplication class
description: Dhcp Server v4FailoverReplication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9da21e94-a979-4aa8-9511-00c637b0003c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DhcpServerv4FailoverReplication class", "PS_DhcpServerv4FailoverReplication class, described"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4FailoverReplication
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# PS\_DhcpServerv4FailoverReplication class

Dhcp Server v4FailoverReplication.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4FailoverReplication
{
};
```

## Members

The **PS\_DhcpServerv4FailoverReplication** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4FailoverReplication** class has these methods.



| Method                                                                        | Description                                                                |
|:------------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**InvokeByName**](invokebyname-ps-dhcpserverv4failoverreplication.md)       | Replicate scope configuration between failover partner servers.<br/> |
| [**InvokeByScopeId**](invokebyscopeid-ps-dhcpserverv4failoverreplication.md) | Replicate scope configuration between failover partner servers.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





