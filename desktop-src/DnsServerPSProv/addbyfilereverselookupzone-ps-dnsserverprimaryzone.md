---
title: AddByFileReverseLookupZone method of the PS\_DnsServerPrimaryZone class
description: Adds Primary zone on DNS server.
audience: developer
ms.assetid: 850f01aa-cab8-4762-ab46-27f41e64c30f
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByFileReverseLookupZone method
- AddByFileReverseLookupZone method, PS_DnsServerPrimaryZone class
- PS_DnsServerPrimaryZone class, AddByFileReverseLookupZone method
topic_type:
- apiref
api_name:
- PS_DnsServerPrimaryZone.AddByFileReverseLookupZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByFileReverseLookupZone method of the PS\_DnsServerPrimaryZone class

Adds Primary zone on DNS server.

## Syntax


```mof
uint32 AddByFileReverseLookupZone(
  [in]  string               ResponsiblePerson,
  [in]  string               DynamicUpdate,
  [in]  boolean              LoadExisting,
  [in]  string               NetworkID,
  [in]  string               ZoneFile,
  [in]  string               VirtualizationInstance,
  [in]  string               ComputerName,
  [in]  boolean              PassThru,
  [out] DnsServerPrimaryZone cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ResponsiblePerson* \[in\]
</dt> <dd>

Specifies the responsible person for the zone

</dd> <dt>

*DynamicUpdate* \[in\]
</dt> <dd>

Determines whether the specified zone accepts dynamic updates

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> <dt>

<span id="Secure"></span><span id="secure"></span><span id="SECURE"></span>

**Secure** ("Secure")


</dt> <dd></dd> <dt>

<span id="NonsecureAndSecure"></span><span id="nonsecureandsecure"></span><span id="NONSECUREANDSECURE"></span>

**NonsecureAndSecure** ("NonsecureAndSecure")


</dt> <dd></dd> </dl> </dd> <dt>

*LoadExisting* \[in\]
</dt> <dd>

Specifies Loading of an existing zone

</dd> <dt>

*NetworkID* \[in\]
</dt> <dd>

Specifies the IP address and Mask of reverse lookup zone in X.Y.Z/Mask format

</dd> <dt>

*ZoneFile* \[in\]
</dt> <dd>

Specifies File based zone path or custom directory partition path

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is unavailable prior to Windows Server 2016.

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

 

 





