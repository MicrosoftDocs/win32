---
title: MSFT\_SMZoneSetToZone class
description: Represents a relationship between a zone set and a zone.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f5cf64a7-45cb-474c-9eb5-71edb19fa115
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMZoneSetToZone class
- MSFT_SMZoneSetToZone class, described
topic_type:
- apiref
api_name:
- MSFT_SMZoneSetToZone
- MSFT_SMZoneSetToZone.Parent
- MSFT_SMZoneSetToZone.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMZoneSetToZone class

Represents a relationship between a zone set and a zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMZoneSetToZone
{
  MSFT_SMZoneSet REF Parent;
  MSFT_SMZone    REF Child;
};
```

## Members

The **MSFT\_SMZoneSetToZone** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMZoneSetToZone** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMZone**](msft-smzone.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the zone in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMZoneSet**](msft-smzoneset.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the zone set in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





