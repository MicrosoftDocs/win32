---
title: Remove method of the PS\_DnsServerResponseRateLimitingExceptionlist class
description: The Remove-DnsServerResponseRateLimitingExceptionlist cmdlet removes a RRL exceptionlist from the DNS server.
audience: developer
ms.assetid: edecfa4e-bd9b-4be7-abb3-e76fd286482f
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DnsServerResponseRateLimitingExceptionlist class
- PS_DnsServerResponseRateLimitingExceptionlist class, Remove method
topic_type:
- apiref
api_name:
- PS_DnsServerResponseRateLimitingExceptionlist.Remove
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_DnsServerResponseRateLimitingExceptionlist class

The Remove-DnsServerResponseRateLimitingExceptionlist cmdlet removes a RRL exceptionlist from the DNS server.

## Syntax


```mof
uint32 Remove(
  [in]  string                                     ComputerName,
  [in]  boolean                                    Force,
  [in]  string                                     Name,
  [in]  boolean                                    PassThru,
  [out] DnsServerResponseRateLimitingExceptionlist cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to not require user confirmation before continuing with the operation; **false** to require user confirmation. The default value is **false**.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the RRL exception list.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains a [**DnsServerResponseRateLimitingExceptionlist**](dnsserverresponseratelimitingexceptionlist.md) with the following fields:

-   Name
-   Condition
-   ClientSubNet
-   Fqdn
-   ServerInterfaceIP

This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerResponseRateLimitingExceptionlist**](ps-dnsserverresponseratelimitingexceptionlist.md)
</dt> </dl>

 

 





