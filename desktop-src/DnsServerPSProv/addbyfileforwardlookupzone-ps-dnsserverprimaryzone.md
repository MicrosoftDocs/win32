---
title: AddByFileForwardLookupZone method of the PS\_DnsServerPrimaryZone class
description: Adds Primary zone on DNS server.
audience: developer
ms.assetid: 1a016ef1-6b21-43ce-9cf5-69dcb017afc1
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByFileForwardLookupZone method
- AddByFileForwardLookupZone method, PS_DnsServerPrimaryZone class
- PS_DnsServerPrimaryZone class, AddByFileForwardLookupZone method
topic_type:
- apiref
api_name:
- PS_DnsServerPrimaryZone.AddByFileForwardLookupZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByFileForwardLookupZone method of the PS\_DnsServerPrimaryZone class

Adds Primary zone on DNS server.

## Syntax


```mof
uint32 AddByFileForwardLookupZone(
  [in]  string               ResponsiblePerson,
  [in]  string               DynamicUpdate,
  [in]  boolean              LoadExisting,
  [in]  string               ComputerName,
  [in]  string               Name,
  [in]  string               ZoneFile,
  [in]  string               VirtualizationInstance,
  [in]  boolean              PassThru,
  [out] DnsServerPrimaryZone cmdletOutput
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

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

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

 

 





