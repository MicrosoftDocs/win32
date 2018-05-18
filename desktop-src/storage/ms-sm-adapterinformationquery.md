---
title: MS\_SM\_AdapterInformationQuery structure
description: The MS\_SM\_AdapterInformationQuery structure is used by a WMI provider to expose attributes that are associated with a SAS adapter.
ms.assetid: '81c05f47-e75a-4d67-8e77-33ebe1750c67'
keywords: ["MS_SM_AdapterInformationQuery structure Storage Devices", "PMS_SM_AdapterInformationQuery structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MS_SM_AdapterInformationQuery
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# MS\_SM\_AdapterInformationQuery structure

The MS\_SM\_AdapterInformationQuery structure is used by a WMI provider to expose attributes that are associated with a SAS adapter.

## Syntax


```C++
typedef struct _MS_SM_AdapterInformationQuery {
  ULONGLONG UniqueAdapterId;
  ULONG     HBAStatus;
  ULONG     NumberOfPorts;
  ULONG     VendorSpecificID;
  WCHAR     Manufacturer[64 + 1];
  WCHAR     SerialNumber[64 + 1];
  WCHAR     Model[256 + 1];
  WCHAR     ModelDescription[256 + 1];
  WCHAR     HardwareVersion[256 + 1];
  WCHAR     DriverVersion[256 + 1];
  WCHAR     OptionROMVersion[256 + 1];
  WCHAR     FirmwareVersion[256 + 1];
  WCHAR     DriverName[256 + 1];
  WCHAR     HBASymbolicName[256 + 1];
  WCHAR     RedundantOptionROMVersion[256 + 1];
  WCHAR     RedundantFirmwareVersion[256 + 1];
  WCHAR     MfgDomain[256 + 1];
} MS_SM_AdapterInformationQuery, *PMS_SM_AdapterInformationQuery;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

The unique adapter ID.

</dd> <dt>

**HBAStatus**
</dt> <dd>

The status of the operation.

</dd> <dt>

**NumberOfPorts**
</dt> <dd>

The number of ports on the HBA.

</dd> <dt>

**VendorSpecificID**
</dt> <dd>

A vendor-specific ID.

</dd> <dt>

**Manufacturer**
</dt> <dd>

An ASCII string that is 64 bytes or fewer in length and that identifies the name of the manufacturer of the HBA.

</dd> <dt>

**SerialNumber**
</dt> <dd>

An ASCII string that is 64 bytes or fewer in length and that identifies the serial number of the HBA.

</dd> <dt>

**Model**
</dt> <dd>

An ASCII string that is 256 bytes or fewer in length and that identifies the vendor-specific name of the HBA model.

</dd> <dt>

**ModelDescription**
</dt> <dd>

An ASCII string that is 256 bytes or fewer in length and that indicates the model description.

</dd> <dt>

**HardwareVersion**
</dt> <dd>

An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific hardware revision level of the HBA.

</dd> <dt>

**DriverVersion**
</dt> <dd>

An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific version of the HBA miniport driver.

</dd> <dt>

**OptionROMVersion**
</dt> <dd>

An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific option ROM or BIOS version of the HBA.

</dd> <dt>

**FirmwareVersion**
</dt> <dd>

An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific firmware version of the HBA.

</dd> <dt>

**DriverName**
</dt> <dd>

An ASCII string that is 256 bytes or fewer in length and that indicates the file name for the driver binary file.

</dd> <dt>

**HBASymbolicName**
</dt> <dd>

An ASCII string that is 256 bytes or fewer in length and that indicates the symbolic name for the fibre channel node.

</dd> <dt>

**RedundantOptionROMVersion**
</dt> <dd>

An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific option ROM or BIOS version of the HBA.

</dd> <dt>

**RedundantFirmwareVersion**
</dt> <dd>

An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific firmware version of the HBA.

</dd> <dt>

**MfgDomain**
</dt> <dd>

The name of the HBA manufacturer.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MS_SM_AdapterInformationQuery%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





