---
title: ConvertToByFileZone method of the PS\_DnsServerPrimaryZone class
description: Converts a zone to DNS server primary zone.
audience: developer
ms.assetid: 3501f194-06ed-4217-b59b-25f6d8eca2e6
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ConvertToByFileZone method
- ConvertToByFileZone method, PS_DnsServerPrimaryZone class
- PS_DnsServerPrimaryZone class, ConvertToByFileZone method
topic_type:
- apiref
api_name:
- PS_DnsServerPrimaryZone.ConvertToByFileZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConvertToByFileZone method of the PS\_DnsServerPrimaryZone class

Converts a zone to DNS server primary zone.

## Syntax


```mof
uint32 ConvertToByFileZone(
  [in]  string               ComputerName,
  [in]  string               Name,
  [in]  boolean              LoadExisting,
  [in]  boolean              PassThru,
  [in]  string               ZoneFile,
  [in]  boolean              Force,
  [out] DnsServerPrimaryZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies name of the zone

</dd> <dt>

*LoadExisting* \[in\]
</dt> <dd>

Specifies existing file to be used while loading the zone

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*ZoneFile* \[in\]
</dt> <dd>

Specifies File based zone path or custom directory partition path.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Converts a zone without prompting you for confirmation. By default, the method prompts you for confirmation before it proceeds.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerPrimaryZone**](dnsserverprimaryzone.md) class.

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

[**PS\_DnsServerPrimaryZone**](ps-dnsserverprimaryzone.md)
</dt> </dl>

 

 





