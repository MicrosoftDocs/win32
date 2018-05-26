---
title: Set method of the PS\_DnsServerSetting class
description: Sets Different DNS server settings.
audience: developer
ms.assetid: 409fb302-b378-4f36-bf15-91c34b0dec91
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServerSetting class
- PS_DnsServerSetting class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServerSetting.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DnsServerSetting class

Sets Different DNS server settings. One of the parameters other than RemoteName, Credentials, comments is mandatory. This should also take remote IP address from pipeline from other cmdlets. Hence we may need an additional IP address parameter. This applies to all the cmdlets.

## Syntax


```mof
uint32 Set(
  [in]  DnsServerSetting InputObject,
  [in]  string           ComputerName,
  [in]  boolean          PassThru,
  [out] DnsServerSetting cmdletOutput
);
```



## Parameters

<dl> <dt>

*InputObject* \[in\]
</dt> <dd>

Object containing DNS server settings.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerSetting**](dnsserversetting.md) class.

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

[**PS\_DnsServerSetting**](ps-dnsserversetting.md)
</dt> </dl>

 

 





