---
title: SetByName method of the PS\_DnsServerZoneDelegation class
description: Updates the zone delegation.
audience: developer
ms.assetid: '0914e9c3-0279-42d9-92d8-646915b651eb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByName method", "SetByName method, PS_DnsServerZoneDelegation class", "PS_DnsServerZoneDelegation class, SetByName method"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneDelegation.SetByName
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# SetByName method of the PS\_DnsServerZoneDelegation class

Updates the zone delegation.

## Syntax


```mof
uint32 SetByName(
  [in]  string                  ChildZoneName,
  [in]  string                  IPAddress[],
  [in]  string                  NameServer,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerZoneDelegation cmdletOutput
);
```



## Parameters

<dl> <dt>

*ChildZoneName* \[in\]
</dt> <dd>

Name of the child zone

</dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

Overwrite with the specified NameServers

</dd> <dt>

*NameServer* \[in\]
</dt> <dd>

Specifies a name server for the domain.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the Parent

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

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

[**PS\_DnsServerZoneDelegation**](ps-dnsserverzonedelegation.md)
</dt> </dl>

 

 





