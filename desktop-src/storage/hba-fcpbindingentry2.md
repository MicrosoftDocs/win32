---
title: HBA\_FCPBindingEntry2 structure
description: The HBA\_FCPBindingEntry2 structure defines a binding between the information that uniquely identifies a logical unit for the operating system and the fibre channel protocol (FCP) identifier for the logical unit.
ms.assetid: 'e2e7353d-2c83-4704-bec4-9485ab3c7706'
keywords: ["HBA_FCPBindingEntry2 structure Storage Devices", "HBA_FCPBINDINGENTRY2 structure Storage Devices", "PHBA_FCPBINDINGENTRY2 structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_FCPBINDINGENTRY2
api_location:
- hbaapi.h
api_type:
- HeaderDef
---

# HBA\_FCPBindingEntry2 structure

The HBA\_FCPBindingEntry2 structure defines a binding between the information that uniquely identifies a logical unit for the operating system and the fibre channel protocol (FCP) identifier for the logical unit.

## Syntax


```C++
typedef struct HBA_FCPBindingEntry2 {
  HBA_BIND_TYPE type;
  HBA_SCSIID    ScsiId;
  HBA_FCPID     FcpId;
  HBA_LUID      LUID;
  HBA_STATUS    Status;
} HBA_FCPBINDINGENTRY2, *PHBA_FCPBINDINGENTRY2;
```



## Members

<dl> <dt>

**type**
</dt> <dd>

Contains a binding type that indicates how the target is specified in the binding. This member can have any of the following values:



| Type Value                      | Meaning                                                                                                                                                                                      |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HBA\_BIND\_TO\_D\_ID<br/> | Indicates that the target is identified by its fibre channel protocol (FCP) ID. The **Fcid** member of the [HBA\_FcpId](hba-fcpid.md) structure contains this value.<br/>             |
| HBA\_BIND\_TO\_WWPN<br/>  | Indicates that the target is identified by its worldwide port name. The **PortWWN** member of the [HBA\_FcpId](hba-fcpid.md) structure contains this value.<br/>                      |
| HBA\_BIND\_TO\_WWNN<br/>  | Indicates that the fibre channel target device is identified by its worldwide node name. The **NodeWWN** member of the [HBA\_FcpId](hba-fcpid.md) structure contains this value.<br/> |
| HBA\_BIND\_TO\_LUID<br/>  | Indicates that the target is identified by its fibre channel logical unit ID. The **FcpLun** member of the [HBA\_FcpId](hba-fcpid.md) structure contains this value.<br/>             |
| HBA\_BIND\_TARGETS<br/>   | Indicates that the system should automatically generate target mappings from logical unit numbers to fibre channel protocol identifiers. <br/>                                         |



 

For a comparable set of values that define how an HBA specifies targets and logical units in the persistent bindings that it maintains, see the WMI property qualifier [HBA\_BIND\_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff556046).

For a more detailed description of the values that this member can have, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**ScsiId**
</dt> <dd>

Contains a structure of type [**HBA\_ScsiId**](hba-scsiid.md) that contains the information that uniquely identifies a logical unit for the operating system.

</dd> <dt>

**FcpId**
</dt> <dd>

Contains a structure of type [HBA\_FcpId](hba-fcpid.md) that contains the FCP identifier for the logical unit and information about the port to be queried for information about the device.

</dd> <dt>

**LUID**
</dt> <dd>

Contains a structure of type [**HBA\_LUID**](hba-luid.md) that holds a logical unit descriptor for the device that the operating system derives from SCSI inquiry data.

</dd> <dt>

**Status**
</dt> <dd>

Contains, on return, a status value that indicates the condition of the HBA. The status values that can be returned in this member correspond to the values associated with the [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) WMI property qualifier.

</dd> </dl>

## 

### HBA\_fcpbindingtype

typedef enum HBA\_fcpbindingtype { TO\_D\_ID, TO\_WWN, TO\_OTHER } HBA\_FCPBINDINGTYPE;

## Remarks

This structure is very similar to the [**HBAFCPBindingEntry2**](hbafcpbindingentry2.md) structure. The only difference is that HBA\_FCPBindingEntry2 returns HBA status.

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[HBA\_BIND\_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff556046)
</dt> <dt>

[HBA\_FCPBindingEntry](hba-fcpbindingentry.md)
</dt> <dt>

[HBA\_FcpId](hba-fcpid.md)
</dt> <dt>

[**HBA\_LUID**](hba-luid.md)
</dt> <dt>

[**HBA\_ScsiId**](hba-scsiid.md)
</dt> <dt>

[**HBAFCPBindingEntry**](hbafcpbindingentry.md)
</dt> <dt>

[**HBAFCPBindingEntry2**](hbafcpbindingentry2.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_FCPBindingEntry2%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






