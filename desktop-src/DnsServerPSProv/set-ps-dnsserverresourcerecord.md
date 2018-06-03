---
title: Set method of the PS\_DnsServerResourceRecord class
description: Updates a resource record.
audience: developer
ms.assetid: d5082762-de9b-49d2-90d2-c5926ced13cc
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DnsServerResourceRecord class

Updates a resource record.

## Syntax


```mof
uint32 Set(
  [in]  DnsServerResourceRecord NewInputObject,
  [in]  DnsServerResourceRecord OldInputObject,
  [in]  string                  ComputerName,
  [in]  string                  ZoneName,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*NewInputObject* \[in\]
</dt> <dd>

A [**DnsServerResourceRecord**](dnsserverresourcerecord.md) that contains the new values. Note that all the values specified in this object will overwrite the existing values.

</dd> <dt>

*OldInputObject* \[in\]
</dt> <dd>

The [**DnsServerResourceRecord**](dnsserverresourcerecord.md) object that needs to be modified.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

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

Receives an embedded instance of the [**DnsServerResourceRecord**](dnsserverresourcerecord.md) class.

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

[**PS\_DnsServerResourceRecord**](ps-dnsserverresourcerecord.md)
</dt> </dl>

 

 





