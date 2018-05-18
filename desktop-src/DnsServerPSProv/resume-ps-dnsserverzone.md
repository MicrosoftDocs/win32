---
title: Resume method of the PS\_DnsServerZone class
description: Resumes name resolution on suspended zone.
audience: developer
ms.assetid: 'f23f4f05-e923-4873-b023-c847acb43398'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Resume method", "Resume method, PS_DnsServerZone class", "PS_DnsServerZone class, Resume method"]
topic_type:
- apiref
api_name:
- PS_DnsServerZone.Resume
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Resume method of the PS\_DnsServerZone class

Resumes name resolution on suspended zone.

## Syntax


```mof
uint32 Resume(
  [in]  string        Name,
  [in]  string        ComputerName,
  [in]  boolean       PassThru,
  [in]  boolean       Force,
  [out] DnsServerZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

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

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

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

 

 





