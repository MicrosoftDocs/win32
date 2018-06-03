---
title: Import method of the PS\_DnsServerResourceRecordDS class
description: Imports a Delegation Signer (DS) resource record to the DNS server.
audience: developer
ms.assetid: bb9e2aa2-bb77-400e-8ff0-f3c139102625
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Import method
- Import method, PS_DnsServerResourceRecordDS class
- PS_DnsServerResourceRecordDS class, Import method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordDS.Import
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Import method of the PS\_DnsServerResourceRecordDS class

Imports a Delegation Signer (DS) resource record to the DNS server.

## Syntax


```mof
uint32 Import(
  [in]  string                  ZoneName,
  [in]  string                  DSSetFile,
  [in]  boolean                 PassThru,
  [in]  string                  ComputerName,
  [in]  string                  ZoneScope,
  [out] DnsServerResourceRecord cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

The name of a DNS zone on which to add the DS resource record.

</dd> <dt>

*DSSetFile* \[in\]
</dt> <dd>

The absolute path that contains the dsset file that contains the DS resource record to import.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the [**DnsServerResourceRecord**](dnsserverresourcerecord.md) parameter returns an object. **true** to return an object; otherwise **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The computer name of the machine that contains the DS resource record to import.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

The name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**DnsServerResourceRecord**](dnsserverresourcerecord.md) object that receives the imported DS resource record.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerResourceRecordDS**](ps-dnsserverresourcerecordds.md)
</dt> </dl>

 

 





