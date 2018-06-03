---
title: MSFT\_SMZoneToZoneMembershipData class
description: Represents a relationship between a zone and membership data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dcf94357-8e75-4c6e-a433-584397852eb6
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMZoneToZoneMembershipData class
- MSFT_SMZoneToZoneMembershipData class, described
topic_type:
- apiref
api_name:
- MSFT_SMZoneToZoneMembershipData
- MSFT_SMZoneToZoneMembershipData.Parent
- MSFT_SMZoneToZoneMembershipData.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMZoneToZoneMembershipData class

Represents a relationship between a zone and membership data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMZoneToZoneMembershipData
{
  MSFT_SMZone               REF Parent;
  MSFT_SMZoneMembershipData REF Child;
};
```

## Members

The **MSFT\_SMZoneToZoneMembershipData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMZoneToZoneMembershipData** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMZoneMembershipData**](msft-smzonemembershipdata.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the membership data in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMZone**](msft-smzone.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the zone in the relationship.

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

 

 





