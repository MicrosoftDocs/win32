---
title: WT\_Portal class
description: Represents a TCP/IP address and port pair that are used for iSCSI traffic.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3a61696f-c53a-44b9-b324-39fc838d43be
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_Portal class iSCSI Software Target API
- WT_Portal class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_Portal
- WT_Portal.Address
- WT_Portal.Port
- WT_Portal.Listen
api_location:
- WtWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WT\_Portal class

Represents a TCP/IP address and port pair that are used for iSCSI traffic.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_Portal
{
  string  Address;
  uint32  Port;
  boolean Listen;
};
```

## Members

The **WT\_Portal** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_Portal** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The IP address.

</dd> <dt>

**Listen**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

True if the current address is used for iSCSI traffic; otherwise, false.

</dd> <dt>

**Port**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The TCP port.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





