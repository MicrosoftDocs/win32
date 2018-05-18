---
title: HBA\_AdapterAttributes structure
description: The HBA\_AdapterAttributes structure is used in conjunction with the HBA\_GetAdapterAttributes routine to report the attributes of an HBA.
ms.assetid: 'd86a5810-7014-41d5-bd88-3a1bd50032da'
keywords: ["HBA_AdapterAttributes structure Storage Devices", "HBA_ADAPTERATTRIBUTES structure Storage Devices", "PHBA_ADAPTERATTRIBUTES structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_ADAPTERATTRIBUTES
api_location:
- hbaapi.h
api_type:
- HeaderDef
---

# HBA\_AdapterAttributes structure

The HBA\_AdapterAttributes structure is used in conjunction with the [**HBA\_GetAdapterAttributes**](hba-getadapterattributes.md) routine to report the attributes of an HBA.

## Syntax


```C++
typedef struct HBA_AdapterAttributes {
  char       Manufacturer[64];
  char       SerialNumber[64];
  char       Model[256];
  char       ModelDescription[256];
  HBA_WWN    NodeWWN;
  char       NodeSymbolicName[256];
  char       HardwareVersion[256];
  char       DriverVersion[256];
  char       OptionROMVersion[256];
  char       FirmwareVersion[256];
  HBA_UINT32 VendorSpecificID;
  HBA_UINT32 NumberOfPorts;
  char       DriverName[256];
} HBA_ADAPTERATTRIBUTES, *PHBA_ADAPTERATTRIBUTES;
```



## Members

<dl> <dt>

**Manufacturer**
</dt> <dd>

Contains a string not exceeding 64 bytes in length that indicates the name of the manufacturer of the HBA..

</dd> <dt>

**SerialNumber**
</dt> <dd>

Contains a string not exceeding 64 bytes in length that indicates the serial number of the HBA.

</dd> <dt>

**Model**
</dt> <dd>

Contains a string not exceeding 256 bytes in length that indicates a vendor specific name or identifying text for the HBA model.

</dd> <dt>

**ModelDescription**
</dt> <dd>

Contains a string not exceeding 256 bytes in length that provides a description of the HBA model.

</dd> <dt>

**NodeWWN**
</dt> <dd>

Contains the 64 bit world-wide name that indicates the name of the node (machine) that the HBA is located on. If an HBA has multiple ports associated with more than one node, the member will contain a name chosen by vendor-specific means from among the names of the associated nodes. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**NodeSymbolicName**
</dt> <dd>

Contains a string not exceeding 256 bytes in length that indicates the symbolic name of the fibre channel node (machine) that the adapter is located on.

</dd> <dt>

**HardwareVersion**
</dt> <dd>

Contains a string not exceeding 256 bytes in length that indicates the hardware revision level of the HBA.

</dd> <dt>

**DriverVersion**
</dt> <dd>

Contains a string not exceeding 256 bytes in length that indicates version of the driver that manages the HBA.

</dd> <dt>

**OptionROMVersion**
</dt> <dd>

Contains a string not exceeding 256 bytes in length that specifies the option ROM or the version of the BIOS of the HBA.

</dd> <dt>

**FirmwareVersion**
</dt> <dd>

Contains a string not exceeding 256 bytes in length that identifies the version of the HBA's firmware.

</dd> <dt>

**VendorSpecificID**
</dt> <dd>

Contains a vendor-specified ID.

</dd> <dt>

**NumberOfPorts**
</dt> <dd>

Indicates the number of ports on the HBA.

</dd> <dt>

**DriverName**
</dt> <dd>

Contains a string not exceeding 256 bytes in length that indicates name of the file that contains the binary image of the device driver for the HBA.

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_GetAdapterAttributes**](hba-getadapterattributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_AdapterAttributes%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






