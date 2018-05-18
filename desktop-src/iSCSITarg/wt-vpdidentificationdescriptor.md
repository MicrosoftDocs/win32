---
title: WT\_VPDIdentificationDescriptor class
description: Represents a Vital Product Data Identification Descriptor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '419857dc-31e6-4b94-854d-c63d5085a615'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["WT_VPDIdentificationDescriptor class iSCSI Software Target API", "WT_VPDIdentificationDescriptor class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- WT_VPDIdentificationDescriptor
- WT_VPDIdentificationDescriptor.CodeSet
- WT_VPDIdentificationDescriptor.IdentifierType
- WT_VPDIdentificationDescriptor.Identifier
api_location:
- WtWmiProv.dll
api_type:
- DllExport
---

# WT\_VPDIdentificationDescriptor class

Represents a Vital Product Data Identification Descriptor.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_VPDIdentificationDescriptor
{
  uint8 CodeSet;
  uint8 IdentifierType;
  uint8 Identifier[];
};
```

## Members

The **WT\_VPDIdentificationDescriptor** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_VPDIdentificationDescriptor** class has these properties.

<dl> <dt>

**CodeSet**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (VpdCodeSetReserved, VpdCodeSetBinary, VpdCodeSetAscii, VpdCodeSetUTF8), **ValueMap** (0, 1, 2, 3)
</dt> </dl>

The code set used in the identification descriptor.

</dd> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The actual data for the identifier.

</dd> <dt>

**IdentifierType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (VpdIdentifierTypeVendorSpecific, VpdIdentifierTypeVendorId, VpdIdentifierTypeEUI64, VpdIdentifierTypeFCPHName, VpdIdentifierTypePortRelative, VpdIdentifierTypeTargetPortGroup, VpdIdentifierTypeLogicalUnitGroup, VpdIdentifierTypeMD5LogicalUnitId, VpdIdentifierTypeSCSINameString), **ValueMap** (0, 1, 2, 3, 4, 5, 6, 7, 8)
</dt> </dl>

The naming authority for the identifier.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**VDS\_STORAGE\_IDENTIFIER**](https://msdn.microsoft.com/library/windows/desktop/aa383435)
</dt> </dl>

 

 





