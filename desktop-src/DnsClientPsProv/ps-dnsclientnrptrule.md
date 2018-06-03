---
title: PS\_DnsClientNrptRule class
description: DNS Client NRPT Rule.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c77fe36-9bec-45e6-882d-0fea56f7cca2
ms.prod: windows-server-dev
ms.technology:
- dns-client
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsClientNrptRule class
- PS_DnsClientNrptRule class, described
topic_type:
- apiref
api_name:
- PS_DnsClientNrptRule
api_location:
- DnsClientPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsClientNrptRule class

DNS Client NRPT Rule

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsClientPSProvider"), AMENDMENT]
class PS_DnsClientNrptRule
{
};
```

## Members

The **PS\_DnsClientNrptRule** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsClientNrptRule** class has these methods.



| Method                                        | Description                                                         |
|:----------------------------------------------|:--------------------------------------------------------------------|
| [**Add**](add-ps-dnsclientnrptrule.md)       | Adds a rule to Name Resolution Policy Table.<br/>             |
| [**Get**](get-ps-dnsclientnrptrule.md)       | Retrieves DNS client Name Resolution Policy Table rules.<br/> |
| [**Remove**](remove-ps-dnsclientnrptrule.md) | Removes DNS client NRPT rule.<br/>                            |
| [**Set**](set-ps-dnsclientnrptrule.md)       | Modifies DNS client NRPT rule.<br/>                           |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientPSProvider.dll</dt> </dl> |



 

 





