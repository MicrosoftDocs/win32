---
title: WT\_ISnsServer class
description: Represents an iSNS server that Microsoft iSCSI Target Server uses to register iSCSI targets and query for iSCSI initiator information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 10bf598f-311b-49f9-85cd-a2eb11b332ac
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_ISnsServer class iSCSI Software Target API
- WT_ISnsServer class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_ISnsServer
- WT_ISnsServer.ServerName
api_location:
- WtWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WT\_ISnsServer class

Represents an iSNS server that Microsoft iSCSI Target Server uses to register iSCSI targets and query for iSCSI initiator information.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_ISnsServer
{
  string ServerName;
};
```

## Members

The **WT\_ISnsServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_ISnsServer** class has these properties.

<dl> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The IP address or DNS name of the iSNS server.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





