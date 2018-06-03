---
title: DnsServerVirtualizationInstance class
description: Describes a DNS virtualization instance.
audience: developer
ms.assetid: 6cb62909-8736-4542-bb0c-632cbccac965
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerVirtualizationInstance class
- DnsServerVirtualizationInstance class, described
topic_type:
- apiref
api_name:
- DnsServerVirtualizationInstance
- DnsServerVirtualizationInstance.VirtualizationInstance
- DnsServerVirtualizationInstance.FriendlyName
- DnsServerVirtualizationInstance.Description
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerVirtualizationInstance class

Describes a DNS virtualization instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerVirtualizationInstance
{
  string VirtualizationInstance;
  string FriendlyName;
  string Description;
};
```

## Members

The **DnsServerVirtualizationInstance** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerVirtualizationInstance** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description of the virtualization instance.

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

user friendly name of the virtualization instance.

</dd> <dt>

**VirtualizationInstance**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Unique identifier of the virtualization instance.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



 

 





