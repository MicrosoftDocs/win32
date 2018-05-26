---
title: MSiSCSI\_HBAInformation structure
description: The MSiSCSI\_HBAInformation structure is used by storage miniport drivers to report information about the host bus adapters (HBAs) that they manage to the iSCSI initiator service.
ms.assetid: ee2951e0-2632-44b0-870d-33d4d48ac8e8
keywords:
- MSiSCSI_HBAInformation structure Storage Devices
- PMSiSCSI_HBAInformation structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_HBAInformation
api_location:
- iscsimgt.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSiSCSI\_HBAInformation structure

The MSiSCSI\_HBAInformation structure is used by storage miniport drivers to report information about the host bus adapters (HBAs) that they manage to the iSCSI initiator service.

## Syntax


```C++
typedef struct _MSiSCSI_HBAInformation {
  ULONGLONG UniqueAdapterId;
  BOOLEAN   IntegratedTCPIP;
  BOOLEAN   RequiresBinaryIpAddresses;
  UCHAR     VersionMin;
  UCHAR     VersionMax;
  BOOLEAN   MultifunctionDevice;
  BOOLEAN   CacheValid;
  ULONG     NumberOfPorts;
  ULONG     Status;
  ULONG     FunctionalitySupported;
  UCHAR     GenerationalGuid[16];
  ULONG     MaxCDBLength;
  BOOLEAN   BiDiScsiCommands;
  WCHAR     VendorID[255 + 1];
  WCHAR     VendorModel[255 + 1];
  WCHAR     VendorVersion[255 + 1];
  WCHAR     FirmwareVersion[255 + 1];
  WCHAR     AsicVersion[255 + 1];
  WCHAR     OptionRomVersion[255 + 1];
  WCHAR     SerialNumber[255 + 1];
  WCHAR     DriverName[255 + 1];
} MSiSCSI_HBAInformation, *PMSiSCSI_HBAInformation;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID).

</dd> <dt>

**IntegratedTCPIP**
</dt> <dd>

A Boolean value that indicates if the Windows TCP/IP stack manages TCP/IP traffic for the HBA. If this member is **TRUE**, the Windows TCP/IP stack manages TCP/IP traffic for the HBA. If this member is **FALSE**, the Windows TCP/IP stack does not manage TCP/IP traffic for the HBA. A miniport driver for an adapter with its own TCP/IP stack should set this member to **FALSE**.

</dd> <dt>

**RequiresBinaryIpAddresses**
</dt> <dd>

A Boolean value that indicates whether the miniport driver for the HBA instructs the iSCSI initiator service to perform DNS lookup and provide the HBA with binary IP addresses. If this member is **TRUE**, the miniport driver for the HBA instructs the iSCSI initiator service to perform DNS lookup and provide the HBA with binary IP addresses. For the iSCSI initiator service to honor this request, the HBA must be on the same network as the Windows TCP/IP stack. If **RequiresBinaryIpAddresses** is **FALSE**, the HBA and its miniport driver have direct access to DNS.

</dd> <dt>

**VersionMin**
</dt> <dd>

The earliest version of the iSCSI specification that the HBA and its miniport driver support.

</dd> <dt>

**VersionMax**
</dt> <dd>

The most recent version of the iSCSI specification that the HBA and its miniport driver support.

</dd> <dt>

**MultifunctionDevice**
</dt> <dd>

A Boolean value that indicates whether the HBA is a multifunction device. If this member is **TRUE**, the HBA is a multifunction device, and it exposes a netcard interface. If this member **FALSE**, the HBA is not a multifunction device.

</dd> <dt>

**CacheValid**
</dt> <dd>

A Boolean value that indicates if the adapter caches are value. If this member is **TRUE**, the adapter caches are valid. If this member is **FALSE**, the caches are invalid or the adapter does not cache data.

</dd> <dt>

**NumberOfPorts**
</dt> <dd>

The number of ports (or TCP/IP addresses on the adapter).

</dd> <dt>

**Status**
</dt> <dd>

The current status of HBA. This member can hold any of the following values:



| Status                                  | Meaning                                                                 |
|-----------------------------------------|-------------------------------------------------------------------------|
| ISCSI\_HBA\_STATUS\_WORKING<br/>  | The HBA is functioning normally. <br/>                            |
| ISCSI\_HBA\_STATUS\_DEGRADED<br/> | The HBA is functioning in a degraded state of operation.<br/>     |
| ISCSI\_HBA\_STATUS\_CRITICAL<br/> | The HBA is in a critical state and might fail at any moment.<br/> |
| ISCSI\_HBA\_STATUS\_FAILED<br/>   | The HBA is not functioning at all.<br/>                           |



 

</dd> <dt>

**FunctionalitySupported**
</dt> <dd>

A bitwise OR of the flags that define the functionality that the HBA supports. The following table describes the possible flags.



| Flags                                               | Meaning                                                                                                                                                   |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ISCSI\_HBA\_PRESHARED\_KEY\_CACHE<br/>        | The host bus adapter (HBA) supports an onboard cache for a preshared key.<br/>                                                                      |
| ISCSI\_HBA\_ISCSI\_AUTHENTICATION\_CACHE<br/> | The HBA supports an onboard cache for CHAP secrets. <br/>                                                                                           |
| ISCSI\_HBA\_IPSEC\_TUNNEL\_MODE<br/>          | The HBA supports IPsec tunnel mode. <br/>                                                                                                           |
| ISCSI\_HBA\_CHAP\_VIA\_RADIUS<br/>            | The HBA supports the Remote Authentication Dial-In User Service (RADIUS) attributes of the challenge handshake authentication protocol (CHAP).<br/> |
| ISCSI\_HBA\_ISNS\_DISCOVERY<br/>              | The HBA supports iSNS discovery.<br/>                                                                                                               |
| ISCSI\_HBA\_SLP\_DISCOVERY<br/>               | The HBA supports SLP discovery. <br/>                                                                                                               |



 

</dd> <dt>

**GenerationalGuid**
</dt> <dd>

The generational GUID. This GUID is the GUID value that the [SetGenerationalGuid](https://msdn.microsoft.com/library/windows/hardware/ff565678) method in the [MSiSCSI\_Operations WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563091) last set.

</dd> <dt>

**MaxCDBLength**
</dt> <dd>

The maximum CDB length, in bytes, that the HBA supports.

</dd> <dt>

**BiDiScsiCommands**
</dt> <dd>

A Boolean value that indicates if the HBA supports bidirectional SCSI commands. If this member is **TRUE**, the HBA supports bidirectional SCSI commands. If this member is **FALSE**, the HBA does not support bidirectional commands.

</dd> <dt>

**VendorID**
</dt> <dd>

The manufacturer of the HBA.

</dd> <dt>

**VendorModel**
</dt> <dd>

A string that specifies the model of the HBA. The manufacturer defines this string.

</dd> <dt>

**VendorVersion**
</dt> <dd>

A string that specifies the version of the HBA. The manufacturer defines this string.

</dd> <dt>

**FirmwareVersion**
</dt> <dd>

A string that specifies the version of the firmware in the HBA. The manufacturer defines this string.

</dd> <dt>

**AsicVersion**
</dt> <dd>

A string that specifies the Asic version. The manufacturer defines this string.

</dd> <dt>

**OptionRomVersion**
</dt> <dd>

A string that specifies the option ROM version of the HBA. The manufacturer defines this string.

</dd> <dt>

**SerialNumber**
</dt> <dd>

A string that specifies the serial number of the HBA. The manufacturer defines this string.

</dd> <dt>

**DriverName**
</dt> <dd>

A string that specifies the name of the driver for the HBA.

</dd> </dl>

## Remarks

You must implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[MSiSCSI\_HBAInformation WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563017)
</dt> <dt>

[MSiSCSI\_Operations WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563091)
</dt> <dt>

[SetGenerationalGuid](https://msdn.microsoft.com/library/windows/hardware/ff565678)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_HBAInformation%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






