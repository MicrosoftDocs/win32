---
title: HBAFCPBindingEntry2 structure
description: The HBAFCPBindingEntry2 structure defines a binding between the information that uniquely identifies a logical unit for the operating system and the fibre channel protocol (FCP) identifier for the logical unit.
ms.assetid: 75de51b1-063b-49b2-a390-2bafd44e04b0
keywords:
- HBAFCPBindingEntry2 structure Storage Devices
- PHBAFCPBindingEntry2 structure pointer Storage Devices
topic_type:
- apiref
api_name:
- HBAFCPBindingEntry2
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HBAFCPBindingEntry2 structure

The HBAFCPBindingEntry2 structure defines a binding between the information that uniquely identifies a logical unit for the operating system and the fibre channel protocol (FCP) identifier for the logical unit.

## Syntax


```C++
typedef struct _HBAFCPBindingEntry2 {
  ULONG     Type;
  HBAFCPID  FCPId;
  UCHAR     Luid[256];
  HBAScsiID ScsiId;
} HBAFCPBindingEntry2, *PHBAFCPBindingEntry2;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Indicates the binding type. For a description of the values that this member can have, see the T11 committee's *Fibre Channel HBA API* specification.



| Type Value                      | Meaning                                                                                                                                                                                       |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HBA\_BIND\_TO\_D\_ID<br/> | Indicates that the target is identified by its fibre channel protocol (FCP) ID. The **Fcid** member of the [**HBAFCPID**](hbafcpid.md) structure contains this value.<br/>             |
| HBA\_BIND\_TO\_WWPN<br/>  | Indicates that the target is identified by its worldwide port name. The **PortWWN** member of the [**HBAFCPID**](hbafcpid.md) structure contains this value.<br/>                      |
| HBA\_BIND\_TO\_WWNN<br/>  | Indicates that the fibre channel target device is identified by its worldwide node name. The **NodeWWN** member of the [**HBAFCPID**](hbafcpid.md) structure contains this value.<br/> |
| HBA\_BIND\_TO\_LUID<br/>  | Indicates that the target is identified by its fibre channel logical unit ID. The **FcpLun** member of the [**HBAFCPID**](hbafcpid.md) structure contains this value.<br/>             |
| HBA\_BIND\_TARGETS<br/>   | Indicates that the system should automatically generate target mappings from logical unit numbers to fibre channel protocol identifiers. <br/>                                          |



 

For information about what needs to be included to use the symbols that represent the binding types, see the Headers section.

</dd> <dt>

**FCPId**
</dt> <dd>

Contains a structure of type [**HBAFCPID**](hbafcpid.md) that contains the FCP identifier for the logical unit and information about the port to be queried for information about the device.

</dd> <dt>

**Luid\[256\]**
</dt> <dd>

Contains the logical unit descriptor for the device that the operating system derives from SCSI inquiry data.

</dd> <dt>

**ScsiId**
</dt> <dd>

Contains a structure of type [**HBAScsiID**](hbascsiid.md) that contains the information that uniquely identifies a logical unit for the operating system.

</dd> </dl>

## Remarks

This structure is very similar to the [**HBAFCPBindingEntry**](hbafcpbindingentry.md) structure. The only difference is that HBAFCPBindingEntry2 includes the number that the operating system generates for the logical unit.

The WMI tool suite generates a declaration of HBAFCPBindingEntry2 automatically when it compiles the [HBAFCPBindingEntry WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff556037) that is defined in *hbaapi.mof*.

For an explanation of the fibre channel protocol (FCP), see the T11 committee's *dpANS Fibre Channel Protocol for SCSI* specification.

## Requirements



|                   |                                                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h, Hbaapi.h, or Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBAFCPBindingEntry**](hbafcpbindingentry.md)
</dt> <dt>

[HBAFCPBindingEntry2 WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff556036)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBAFCPBindingEntry2%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






