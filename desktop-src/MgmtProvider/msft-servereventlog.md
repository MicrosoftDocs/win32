---
title: MSFT\_ServerEventLog class
description: Represents an event log.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a1dcad90-ea63-4891-9996-9895df7ebc02
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_ServerEventLog class
- MSFT_ServerEventLog class, described
topic_type:
- apiref
api_name:
- MSFT_ServerEventLog
- MSFT_ServerEventLog.Name
- MSFT_ServerEventLog.LocalizedName
api_location:
- MgmtProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_ServerEventLog class

Represents an event log.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mgmtprovider"), AMENDMENT]
class MSFT_ServerEventLog
{
  string Name;
  string LocalizedName;
};
```

## Members

The **MSFT\_ServerEventLog** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerEventLog** class has these properties.

<dl> <dt>

**LocalizedName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The localized name of the event log.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the event log.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetServerInventory method of MSFT\_ServerManagerTasks**](getserverinventory-msft-servermanagertasks.md)
</dt> </dl>

 

 





