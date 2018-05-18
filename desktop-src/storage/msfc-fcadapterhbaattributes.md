---
title: MSFC\_FCAdapterHBAAttributes structure
description: The MSFC\_FCAdapterHBAAttributes structure is used by a WMI provider to expose attribute information associated with a fibre channel adapter.
ms.assetid: '5efe0ede-b55f-499e-9f95-66652cd8a872'
keywords: ["MSFC_FCAdapterHBAAttributes structure Storage Devices", "PMSFC_FCAdapterHBAAttributes structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MSFC_FCAdapterHBAAttributes
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# MSFC\_FCAdapterHBAAttributes structure

The MSFC\_FCAdapterHBAAttributes structure is used by a WMI provider to expose attribute information associated with a fibre channel adapter.

## Syntax


```C++
typedef struct _MSFC_FCAdapterHBAAttributes {
  ULONGLONG UniqueAdapterId;
  ULONG     HBAStatus;
  UCHAR     NodeWWN[8];
  ULONG     VendorSpecificID;
  ULONG     NumberOfPorts;
  WCHAR     Manufacturer[64 + 1];
  WCHAR     SerialNumber[64 + 1];
  WCHAR     Model[256 + 1];
  WCHAR     ModelDescription[256 + 1];
  WCHAR     NodeSymbolicName[256 + 1];
  WCHAR     HardwareVersion[256 + 1];
  WCHAR     DriverVersion[256 + 1];
  WCHAR     OptionROMVersion[256 + 1];
  WCHAR     FirmwareVersion[256 + 1];
  WCHAR     DriverName[256 + 1];
  WCHAR     MfgDomain[256 + 1];
} MSFC_FCAdapterHBAAttributes, *PMSFC_FCAdapterHBAAttributes;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

Indicates the unique adapter ID.

</dd> <dt>

**HBAStatus**
</dt> <dd>

Contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233).

</dd> <dt>

**NodeWWN**
</dt> <dd>

Contains the 64 bit world-wide name that indicates the node name of the HBA. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**VendorSpecificID**
</dt> <dd>

Indicates a vendor-specific ID.

</dd> <dt>

**NumberOfPorts**
</dt> <dd>

Indicates the number of ports on the HBA.

</dd> <dt>

**Manufacturer**
</dt> <dd>

Contains an ASCII string that is 64 bytes or fewer in length and that identifies the name of the manufacturer of the HBA.

</dd> <dt>

**SerialNumber**
</dt> <dd>

Contains an ASCII string that is 64 bytes or fewer in length and that identifies the serial number of the HBA.

</dd> <dt>

**Model**
</dt> <dd>

Contains an ASCII string that is 256 bytes or fewer in length and that identifies the vendor-specific name of the HBA model.

</dd> <dt>

**ModelDescription**
</dt> <dd>

Contains an ASCII string that is 256 bytes or fewer in length and that indicates the model description.

</dd> <dt>

**NodeSymbolicName**
</dt> <dd>

Contains an ASCII string that is 256 bytes or fewer in length and that indicates the symbolic name for the fibre channel node.

</dd> <dt>

**HardwareVersion**
</dt> <dd>

Contains an ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific hardware revision level of the HBA.

</dd> <dt>

**DriverVersion**
</dt> <dd>

Contains an ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific version of the HBA miniport driver.

</dd> <dt>

**OptionROMVersion**
</dt> <dd>

Contains an ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific option ROM or BIOS version of the HBA.

</dd> <dt>

**FirmwareVersion**
</dt> <dd>

Contains an ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific firmware version of the HBA.

</dd> <dt>

**DriverName**
</dt> <dd>

Contains an ASCII string that is 256 bytes or fewer in length and that indicates the file name for the driver binary file.

</dd> <dt>

**MfgDomain**
</dt> <dd>

Contains the name of the HBA manufacturer.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> <dt>

[MSFC\_FCAdapterHBAAttributes WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562497)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSFC_FCAdapterHBAAttributes%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






