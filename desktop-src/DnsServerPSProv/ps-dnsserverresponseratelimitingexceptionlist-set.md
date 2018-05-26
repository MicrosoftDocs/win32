---
title: Set method of the PS\_DnsServerResponseRateLimitingExceptionlist class
description: The Syntax Set-DnsServerResponseRateLimitingExceptionlist cmdlet updates the settings of a RRL exceptionlist.
audience: developer
ms.assetid: 760f2e2f-d146-4265-8d6c-efb554298aa6
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServerResponseRateLimitingExceptionlist class
- PS_DnsServerResponseRateLimitingExceptionlist class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServerResponseRateLimitingExceptionlist.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DnsServerResponseRateLimitingExceptionlist class

The Syntax Set-DnsServerResponseRateLimitingExceptionlist cmdlet updates the settings of a RRL exceptionlist.

## Syntax


```mof
uint32 Set(
  [in]  string                                     ClientSubnet,
  [in]  string                                     Fqdn,
  [in]  string                                     ServerInterfaceIP,
  [in]  string                                     Name,
  [in]  string                                     Condition,
  [in]  boolean                                    PassThru,
  [in]  string                                     ComputerName,
  [out] DnsServerResponseRateLimitingExceptionlist cmdletOutput
);
```



## Parameters

<dl> <dt>

*ClientSubnet* \[in\]
</dt> <dd>

The client subnet criteria. See the remarks section for more information.

Example: "EQ,America,Asia,NE,Europe" (where America, Asia and Europe are client subnets)

</dd> <dt>

*Fqdn* \[in\]
</dt> <dd>

FQDN criteria. See the remarks section for more information.

For example, "EQ,\*.contoso.com,NE,\*.fabricam.com"

</dd> <dt>

*ServerInterfaceIP* \[in\]
</dt> <dd>

Server Interface on which the DNS server is listening. See the Remarks section for more information.

For example, "EQ,10.0.0.3,"

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the RRL exception list.

</dd> <dt>

*Condition* \[in\]
</dt> <dd>

Multiple values of the criteria, combined together using the 'Condition' parameter as logical operator.

The same operator is also used for combining EQ and NE expressions within a value.By default, the Condition is set to "AND".

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

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

## Remarks

The clientSubnet, FQDN, and ServerInterfaceIP parameters use the following format for their values:

-   The value must entered in format ?COMPARATOR, value1, value2,?, COMPARATOR, value 3, value 4,..? where the COMPARATOR can be EQ or NE. There can be only one EQ and one NE in a value.
-   The values following the EQ operator will be treated as multiple assertions which are logically combined (OR?d). The values following the NE operator will be treated as multiple assertions which are logically differenced (AND?d).
-   Multiple values are combined together using the 'Condition' parameter as logical operator. The same operator is also used for combining EQ and NE expressions within a value. For example,

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

 

 





