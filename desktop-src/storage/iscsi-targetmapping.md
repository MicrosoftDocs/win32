---
title: ISCSI\_TargetMapping structure
description: The ISCSI\_TargetMapping structure maps a collection of logical unit numbers (LUNs) that are locally defined to a group of 64-bit iSCSI logical unit numbers.
ms.assetid: '9b8c5024-5d37-4f85-be00-1a60dd9ab323'
keywords: ["ISCSI_TargetMapping structure Storage Devices", "PISCSI_TargetMapping structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ISCSI_TargetMapping
api_location:
- iscsidef.h
api_type:
- HeaderDef
---

# ISCSI\_TargetMapping structure

The ISCSI\_TargetMapping structure maps a collection of logical unit numbers (LUNs) that are locally defined to a group of 64-bit iSCSI logical unit numbers.

## Syntax


```C++
typedef struct _ISCSI_TargetMapping {
  ULONG         OSBus;
  ULONG         OSTarget;
  ULONGLONG     UniqueSessionId;
  ULONG         LUNCount;
  WCHAR         TargetName[223 + 1];
  BOOLEAN       FromPersistentLogin;
  ULONGLONG     Reserved;
  ISCSI_LUNList LUNList[1];
} ISCSI_TargetMapping, *PISCSI_TargetMapping;
```



## Members

<dl> <dt>

**OSBus**
</dt> <dd>

The SCSI bus number (which is valid in the local operating system) that the remote target is mapped to. A value of 0xffffffff indicates that the miniport driver can associate any SCSI bus number with the target.

</dd> <dt>

**OSTarget**
</dt> <dd>

The SCSI target number (which is valid in the local operating system) that the remote target is mapped to. A value of 0xffffffff indicates that the miniport driver can pick any number to identify the remote target device.

</dd> <dt>

**UniqueSessionId**
</dt> <dd>

A 64-bit integer that uniquely identifies the session. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in their UniqueSessionId parameter. Do not confuse this value with the values in the ISID and TSID members.

</dd> <dt>

**LUNCount**
</dt> <dd>

The number of LUNs that are associated with the remote target device.

</dd> <dt>

**TargetName**
</dt> <dd>

A wide character string that indicates the target name.

</dd> <dt>

**FromPersistentLogin**
</dt> <dd>

A Boolean value that indicates whether the logon session is persistent. If this member is **TRUE**, the logon session is persistent and the system creates it automatically when the computer boots up. If this member is **FALSE**, the logon session is not persistent.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for Microsoft use only.

</dd> <dt>

**LUNList**
</dt> <dd>

A [**ISCSI\_LUNList**](iscsi-lunlist.md) structure that holds a list of LUNs that are associated with the target device.

</dd> </dl>

## Remarks

A 64-bit iSCSI LUN by itself does not uniquely identify the logical unit that it represents. However, the combination of an iSCSI LUN and the name of the target that the logical unit belongs to does provide a unique identification for that logical unit that is valid anywhere in the network.

Management applications can use the ISCSI\_TargetMapping structure to specify a local LUN number that can be assigned to the target LUN that the operating system finds during device enumerations.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsidef.h (include Iscsidef.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[**ISCSI\_LUNList**](iscsi-lunlist.md)
</dt> <dt>

[ISCSI\_TargetMapping WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561573)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_TargetMapping%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






