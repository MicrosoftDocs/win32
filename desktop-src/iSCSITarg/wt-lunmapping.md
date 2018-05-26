---
title: WT\_LUNMapping class
description: Represents a mapping of a virtual disk (WT\_Disk) to an iSCSI target (WT\_Host).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bc5803d3-3c52-4715-922e-92420c0ad063
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_LUNMapping class iSCSI Software Target API
- WT_LUNMapping class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_LUNMapping
- WT_LUNMapping.HostName
- WT_LUNMapping.WTD
- WT_LUNMapping.LUN
api_location:
- WtWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WT\_LUNMapping class

Represents a mapping of a virtual disk ([**WT\_Disk**](wt-disk.md)) to an iSCSI target ([**WT\_Host**](wt-host.md)).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_LUNMapping
{
  string HostName;
  uint32 WTD;
  uint32 LUN;
};
```

## Members

The **WT\_LUNMapping** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_LUNMapping** class has these properties.

<dl> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The iSCSI target name.

</dd> <dt>

**LUN**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The virtual disk LUN number.

</dd> <dt>

**WTD**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The virtual disk's iSCSI disk index.

</dd> </dl>

## Remarks

To establish a new LUN mapping, you can create a new instance of this class and save it.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





