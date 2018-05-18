---
title: Remove method of the PS\_DnsServerZone class
description: Removes the specified zone.
audience: developer
ms.assetid: 'c9ecda34-7ed8-4a62-89a5-6153aa9266e9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Remove method", "Remove method, PS_DnsServerZone class", "PS_DnsServerZone class, Remove method"]
topic_type:
- apiref
api_name:
- PS_DnsServerZone.Remove
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Remove method of the PS\_DnsServerZone class

Removes the specified zone.

## Syntax


```mof
uint32 Remove(
  [in]  string        Name,
  [in]  string        ComputerName,
  [in]  boolean       PassThru,
  [in]  boolean       Force,
  [in]  string        VirtualizationInstance,
  [out] DnsServerZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone to be deleted.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**true** to not require user confirmation before continuing with the operation; **false** to require user confirmation. The default is **false**.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an embedded [**DnsServerZone**](dnsserverzone.md) object. This parameter returns a value only if *PassThru* is set to **true**.

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

[**PS\_DnsServerZone**](ps-dnsserverzone.md)
</dt> </dl>

 

 





