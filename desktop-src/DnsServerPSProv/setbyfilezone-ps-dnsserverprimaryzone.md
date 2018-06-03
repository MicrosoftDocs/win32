---
title: SetByFileZone method of the PS\_DnsServerPrimaryZone class
description: Overwrites settings of DNS server primary zone.
audience: developer
ms.assetid: 974c4e9c-eaa5-4186-88b7-4ab0ede8ed1e
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByFileZone method
- SetByFileZone method, PS_DnsServerPrimaryZone class
- PS_DnsServerPrimaryZone class, SetByFileZone method
topic_type:
- apiref
api_name:
- PS_DnsServerPrimaryZone.SetByFileZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByFileZone method of the PS\_DnsServerPrimaryZone class

Overwrites settings of DNS server primary zone.

## Syntax


```mof
uint32 SetByFileZone(
  [in]  string               Name,
  [in]  string               ZoneFile,
  [in]  string               VirtualizationInstance,
  [in]  string               ComputerName,
  [in]  boolean              PassThru,
  [out] DnsServerPrimaryZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ZoneFile* \[in\]
</dt> <dd>

Specifies file based zone path or custom directory partition path

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

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

 

 





