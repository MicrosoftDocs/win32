---
title: AddByInputObject method of the PS\_DnsServerZoneTransferPolicy class
description: Adds a new zone transfer policy by input object.
audience: developer
ms.assetid: bf6ce530-699a-489c-84c9-a479c88672f9
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByInputObject method
- AddByInputObject method, PS_DnsServerZoneTransferPolicy class
- PS_DnsServerZoneTransferPolicy class, AddByInputObject method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneTransferPolicy.AddByInputObject
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByInputObject method of the PS\_DnsServerZoneTransferPolicy class

Adds a new zone transfer policy by input object.

## Syntax


```mof
uint32 AddByInputObject(
  [in]  string          ComputerName,
  [in]  boolean         PassThru,
  [in]  DnsServerPolicy InputObject,
  [in]  string          ZoneName,
  [out] DnsServerPolicy cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Name of the computer.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

Input object to add.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains a [**DnsServerPolicy**](dnsserverpolicy.md). This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerZoneTransferPolicy**](ps-dnsserverzonetransferpolicy.md)
</dt> </dl>

 

 





