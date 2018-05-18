---
title: Reset method of the PS\_DnsServerZoneKeyMasterRole class
description: Performs a key master role transfer for an AD integrated zone.
audience: developer
ms.assetid: 'fbe23735-77a5-471a-be36-08139f4c2bee'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Reset method", "Reset method, PS_DnsServerZoneKeyMasterRole class", "PS_DnsServerZoneKeyMasterRole class, Reset method"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneKeyMasterRole.Reset
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Reset method of the PS\_DnsServerZoneKeyMasterRole class

Performs a key master role transfer for an AD integrated zone.

## Syntax


```mof
uint32 Reset(
  [in]  string  ZoneName,
  [in]  boolean Force,
  [in]  string  KeyMasterServer,
  [in]  boolean SeizeRole,
  [in]  boolean PassThru,
  [out] string  cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone on which DnsSec operations are performed.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*KeyMasterServer* \[in\]
</dt> <dd>

Server which will become the key master for the current zone.

</dd> <dt>

*SeizeRole* \[in\]
</dt> <dd>

If specified, seizes the keymaster role.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true**.

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

[**PS\_DnsServerZoneKeyMasterRole**](ps-dnsserverzonekeymasterrole.md)
</dt> </dl>

 

 





