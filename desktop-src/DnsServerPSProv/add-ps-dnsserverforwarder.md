---
title: Add method of the PS\_DnsServerForwarder class
description: Add specified DNS server forwarders to the end of the list.
audience: developer
ms.assetid: d584e8f3-8eb2-4376-a45f-6b8e747acccb
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DnsServerForwarder class
- PS_DnsServerForwarder class, Add method
topic_type:
- apiref
api_name:
- PS_DnsServerForwarder.Add
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DnsServerForwarder class

Add specified DNS server forwarders to the end of the list.

## Syntax


```mof
uint32 Add(
  [in]  string             IPAddress[],
  [in]  string             ComputerName,
  [in]  boolean            PassThru,
  [out] DnsServerForwarder cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

Specifies the forwarders in the order they need to be configured. first time. Subsequent adds will be added at the end of the list.

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

Receives and embedded instance of the [**DnsServerForwarder**](dnsserverforwarder.md) class.

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

[**PS\_DnsServerForwarder**](ps-dnsserverforwarder.md)
</dt> </dl>

 

 





