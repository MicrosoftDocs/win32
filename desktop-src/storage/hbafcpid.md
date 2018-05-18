---
title: HBAFCPID structure
description: The HBAFCPID structure contains information that uniquely identifies a logical unit on a fibre channel network.
ms.assetid: 'a4fa3093-a328-4d90-bc51-0e7a6db1ed58'
keywords: ["HBAFCPID structure Storage Devices", "PHBAFCPID structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBAFCPID
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# HBAFCPID structure

The HBAFCPID structure contains information that uniquely identifies a logical unit on a fibre channel network.

## Syntax


```C++
typedef struct _HBAFCPID {
  ULONG     Fcid;
  UCHAR     NodeWWN[8];
  UCHAR     PortWWN[8];
  ULONGLONG FcpLun;
} HBAFCPID, *PHBAFCPID;
```



## Members

<dl> <dt>

**Fcid**
</dt> <dd>

Contains the identifier that indicates which port is to be queried for information about the logical unit. For a discussion of the values that this member have, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**NodeWWN**
</dt> <dd>

Contains the 64 bit world-wide name (WWN) of the node (machine) to which the logical unit is connected. If an HBA has multiple ports and is associated with more than one node, this member will contain a name chosen from among the names of the associated nodes. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**PortWWN**
</dt> <dd>

Contains the 64 bit world-wide name of the port to be queried for information about the logical unit. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**FcpLun**
</dt> <dd>

Contains a 64-bit fibre channel protocol (FCP) number for the logical unit.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration for this structure in *hbapiwm.h* after compiling the [HBAFCPID WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff556039).

For more information about the fibre channel protocol (FCP), see the T11 committee's *dpANS Fibre Channel Protocol for SCSI* and *Fibre Channel HBA API* specifications.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[HBA\_FcpId](hba-fcpid.md)
</dt> <dt>

[**HBAFCPBindingEntry**](hbafcpbindingentry.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBAFCPID%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






