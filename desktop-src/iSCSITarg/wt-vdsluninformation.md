---
title: WT\_VDSLunInformation class
description: Represents the LUN information for an iSCSI target. This information is used by the Virtual Disk Service (VDS). For more information, see VDS\_LUN\_INFORMATION.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 53b92248-ccaa-4617-8641-d51e3ecd0f9a
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_VDSLunInformation class iSCSI Software Target API
- WT_VDSLunInformation class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_VDSLunInformation
- WT_VDSLunInformation.DeviceType
- WT_VDSLunInformation.DeviceTypeModifier
- WT_VDSLunInformation.CommandQueueing
- WT_VDSLunInformation.BusType
- WT_VDSLunInformation.VendorId
- WT_VDSLunInformation.ProductId
- WT_VDSLunInformation.ProductRevision
- WT_VDSLunInformation.SerialNumber
- WT_VDSLunInformation.DiskSignature
- WT_VDSLunInformation.DeviceIdDescriptor
api_location:
- WtWmiProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WT\_VDSLunInformation class

Represents the LUN information for an iSCSI target. This information is used by the [Virtual Disk Service](https://msdn.microsoft.com/library/windows/desktop/bb986750) (VDS). For more information, see [**VDS\_LUN\_INFORMATION**](https://msdn.microsoft.com/library/windows/desktop/aa383387).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_VDSLunInformation
{
  uint8                          DeviceType;
  uint8                          DeviceTypeModifier;
  boolean                        CommandQueueing;
  sint32                         BusType;
  string                         VendorId;
  string                         ProductId;
  string                         ProductRevision;
  string                         SerialNumber;
  string                         DiskSignature;
  WT_VPDIdentificationDescriptor DeviceIdDescriptor[];
};
```

## Members

The **WT\_VDSLunInformation** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_VDSLunInformation** class has these properties.

<dl> <dt>

**BusType**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (VDSBusTypeUnknown, VDSBusTypeScsi, VDSBusTypeAtapi, VDSBusTypeAta, VDSBusType1394, VDSBusTypeSsa, VDSBusTypeFibre, VDSBusTypeUsb, VDSBusTypeRAID, VDSBusTypeiScsi, VDSBusTypeSas, VDSBusTypeSata, VDSBusTypeSd, VDSBusTypeMmc, VDSBusTypeMax, VDSBusTypeFileBackedVirtual), **ValueMap** (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
</dt> </dl>

The bus type of the LUN.

</dd> <dt>

**CommandQueueing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the LUN supports multiple outstanding commands; otherwise, **False**. The synchronization of the queue is the responsibility of the port driver.

</dd> <dt>

**DeviceIdDescriptor**
</dt> <dd> <dl> <dt>

Data type: **[**WT\_VPDIdentificationDescriptor**](wt-vpdidentificationdescriptor.md)** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of VPD identification descriptors.

</dd> <dt>

**DeviceType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SCSI-2 device type of the LUN.

</dd> <dt>

**DeviceTypeModifier**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SCSI-2 device type modifier of the LUN. For LUNs that have no device type modifier, the value is zero.

</dd> <dt>

**DiskSignature**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Signature of the LUN in GUID format.

</dd> <dt>

**ProductId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product identifier, typically a model number.

</dd> <dt>

**ProductRevision**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The product revision.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

LUN serial number.

</dd> <dt>

**VendorId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Vendor identifier.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**VDS\_STORAGE\_DEVICE\_ID\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa383434)
</dt> </dl>

 

 





