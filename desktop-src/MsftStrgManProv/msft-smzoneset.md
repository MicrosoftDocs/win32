---
title: MSFT\_SMZoneSet class
description: Represents a zone set.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dfca017f-653c-4cf5-bb94-35e54bc4c6b1'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMZoneSet class", "MSFT_SMZoneSet class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMZoneSet
- MSFT_SMZoneSet.ObjectId
- MSFT_SMZoneSet.Active
- MSFT_SMZoneSet.ConnectivityStatus
- MSFT_SMZoneSet.Caption
- MSFT_SMZoneSet.Description
- MSFT_SMZoneSet.ElementName
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMZoneSet class

Represents a zone set.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMZoneSet
{
  String  ObjectId;
  boolean Active;
  uint16  ConnectivityStatus;
  string  Caption;
  string  Description;
  string  ElementName;
};
```

## Members

The **MSFT\_SMZoneSet** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMZoneSet** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this ZoneSet is currently active, that is, under enforcement of a fabric.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short textual description of the object.

</dd> <dt>

**ConnectivityStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current or potential connectivity between endpoints in this collection.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Connectivity_Up"></span><span id="connectivity_up"></span><span id="CONNECTIVITY_UP"></span>

**Connectivity/Up** (2)


</dt> <dd></dd> <dt>

<span id="No_Connectivity_Down"></span><span id="no_connectivity_down"></span><span id="NO_CONNECTIVITY_DOWN"></span>

**No Connectivity/Down** (3)


</dt> <dd></dd> <dt>

<span id="Partitioned"></span><span id="partitioned"></span><span id="PARTITIONED"></span>

**Partitioned** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object.

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





