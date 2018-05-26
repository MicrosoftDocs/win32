---
title: Set method of the PS\_DnsServerSigningKey class
description: Modified input key for the zone.
audience: developer
ms.assetid: d2caf3e0-4295-4a5e-a2cd-0ad6cafad3e4
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServerSigningKey class
- PS_DnsServerSigningKey class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServerSigningKey.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DnsServerSigningKey class

Modified input key for the zone.

## Syntax


```mof
uint32 Set(
  [in]  string              ZoneName,
  [in]  datetime            RolloverPeriod,
  [in]  datetime            DnsKeySignatureValidityPeriod,
  [in]  datetime            DSSignatureValidityPeriod,
  [in]  datetime            ZoneSignatureValidityPeriod,
  [in]  string              KeyId,
  [in]  string              NextRolloverAction,
  [in]  string              ComputerName,
  [in]  boolean             PassThru,
  [out] DnsServerSigningKey cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone on which DnsSec operations are performed.

</dd> <dt>

*RolloverPeriod* \[in\]
</dt> <dd>

Amount of time between scheduled key rollovers.

</dd> <dt>

*DnsKeySignatureValidityPeriod* \[in\]
</dt> <dd>

Amount of time that signatures covering DNSKEY record sets should be valid.

</dd> <dt>

*DSSignatureValidityPeriod* \[in\]
</dt> <dd>

Amount of time that signatures covering DS record sets should be valid.

</dd> <dt>

*ZoneSignatureValidityPeriod* \[in\]
</dt> <dd>

Amount of time that signatures covering all other record sets should be valid.

</dd> <dt>

*KeyId* \[in\]
</dt> <dd>

Uniquely identifies the key.

</dd> <dt>

*NextRolloverAction* \[in\]
</dt> <dd>

Specifies the next rollover action.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

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

[**PS\_DnsServerSigningKey**](ps-dnsserversigningkey.md)
</dt> </dl>

 

 





