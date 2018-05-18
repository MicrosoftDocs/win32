---
title: MS\_SMHBA\_FC\_Port structure
description: The MS\_SMHBA\_FC\_Port structure is used to report the FC port information.
ms.assetid: 'e5d0d58c-f2dd-4c8a-9b15-967d0be89788'
keywords: ["MS_SMHBA_FC_Port structure Storage Devices", "PMS_SMHBA_FC_Port structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MS_SMHBA_FC_Port
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# MS\_SMHBA\_FC\_Port structure

The MS\_SMHBA\_FC\_Port structure is used to report the FC port information.

## Syntax


```C++
typedef struct _MS_SMHBA_FC_Port {
  UCHAR NodeWWN[8];
  UCHAR PortWWN[8];
  ULONG FcId;
  ULONG PortSupportedClassofService;
  UCHAR PortSupportedFc4Types[32];
  UCHAR PortActiveFc4Types[32];
  UCHAR FabricName[8];
  ULONG NumberofDiscoveredPorts;
  UCHAR NumberofPhys;
  WCHAR PortSymbolicName[256 + 1];
} MS_SMHBA_FC_Port, *PMS_SMHBA_FC_Port;
```



## Members

<dl> <dt>

**NodeWWN**
</dt> <dd>

A 64-bit world-wide name (WWN) that uniquely identifies the fibre channel node that is associated with PortWWN. For more information about worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**PortWWN**
</dt> <dd>

A 64-bit world-wide name (WWN) that uniquely identifies the fibre channel port. For more information about worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**FcId**
</dt> <dd>

The current fibre channel address of PortWWN. The high order byte of this member contains the first byte of the address. Successively lower order bytes of this member contain successively lower bytes of the address. The lowest order byte of this member must be zero.

</dd> <dt>

**PortSupportedClassofService**
</dt> <dd>

The class of service that is supported by PortWWN. For a list of the different classes of service and the values that must be assigned to this member for each class, see the ANSI standard for Fibre Channel Generic Services 4th Generation (FC-GS-4).

</dd> <dt>

**PortSupportedFc4Types**
</dt> <dd>

The FC-4 types that are supported by PortWWN. For more information about FC-4 types, see the ANSI standard for Fibre Channel Generic Services 4th Generation (FC-GS-4).

</dd> <dt>

**PortActiveFc4Types**
</dt> <dd>

The FC-4 types that are currently available on PortWWN. For more information about FC-4 types, see the ANSI standard for Fibre Channel Generic Services 4th Generation (FC-GS-4).

</dd> <dt>

**FabricName**
</dt> <dd>

The name identifier for the fabric to which PortWWN is attached.

</dd> <dt>

**NumberofDiscoveredPorts**
</dt> <dd>

The number of ports that are visible to PortWWN. For more information about the types of ports that this number takes into consideration, see the T11 committee's specification for *Fibre Channel HBA API (FC-HBA).*

</dd> <dt>

**NumberofPhys**
</dt> <dd>

The number of physical fibre channel ports.

</dd> <dt>

**PortSymbolicName**
</dt> <dd>

An ASCII string that is less than or equal to 256 bytes in length and that indicates the symbolic name for the fibre channel node.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MS_SMHBA_FC_Port%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





