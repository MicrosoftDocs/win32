---
title: RemoveByParameters method of the PS\_DnsServerZoneDelegation class
description: Removes the zone delegation.
audience: developer
ms.assetid: 0719ba9a-d172-4e75-b870-24b61d09f79d
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByParameters method
- RemoveByParameters method, PS_DnsServerZoneDelegation class
- PS_DnsServerZoneDelegation class, RemoveByParameters method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneDelegation.RemoveByParameters
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveByParameters method of the PS\_DnsServerZoneDelegation class

Removes the zone delegation.

## Syntax


```mof
uint32 RemoveByParameters(
  [in]  string                  NameServer,
  [in]  string                  ChildZoneName,
  [in]  string                  ComputerName,
  [in]  boolean                 PassThru,
  [in]  boolean                 Force,
  [in]  string                  Name,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerZoneDelegation cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*NameServer* \[in\]
</dt> <dd>

Specifies name servers for the child zone.

</dd> <dt>

*ChildZoneName* \[in\]
</dt> <dd>

Specifies the name of child zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the Parent

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true**.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerZoneDelegation**](ps-dnsserverzonedelegation.md)
</dt> </dl>

 

 





