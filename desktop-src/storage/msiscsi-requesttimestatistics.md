---
title: MSiSCSI\_RequestTimeStatistics structure
description: The MSiSCSI\_RequestTimeStatistics structure is used by iSCSI initiators to report request time statistics.
ms.assetid: fb884cff-dedb-44cf-b9ea-306bfa66b06f
keywords:
- MSiSCSI_RequestTimeStatistics structure Storage Devices
- PMSiSCSI_RequestTimeStatistics structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_RequestTimeStatistics
api_location:
- iscsiprf.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSiSCSI\_RequestTimeStatistics structure

The MSiSCSI\_RequestTimeStatistics structure is used by iSCSI initiators to report request time statistics.

## Syntax


```C++
typedef struct _MSiSCSI_RequestTimeStatistics {
  WCHAR     iSCSIName[223 + 1];
  USHORT    CID;
  ULONGLONG USID;
  ULONGLONG UniqueAdapterId;
  ULONG     MaximumProcessingTime;
  ULONG     AverageProcessingTime;
} MSiSCSI_RequestTimeStatistics, *PMSiSCSI_RequestTimeStatistics;
```



## Members

<dl> <dt>

**iSCSIName**
</dt> <dd>

The iSCSI target name.

</dd> <dt>

**CID**
</dt> <dd>

The iSCSI connection identifier (ID) for this connection instance. This ID is an internal value that the iSCSI protocol uses to identify the connection. Do not use this ID. Application software should use the connection identifier that the [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods return in the UniqueConnectionId parameter.

</dd> <dt>

**USID**
</dt> <dd>

The iSCSI session ID for this connection instance. This ID is an internal value that the iSCSI protocol uses to identify the session. Do not use this ID. Application software should use the session identifier that the [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods return in the UniqueSessionId parameter.

</dd> <dt>

**UniqueAdapterId**
</dt> <dd>

A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID). The initiator reports this value in the UniqueAdapterId member of the [**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md) structure.

</dd> <dt>

**MaximumProcessingTime**
</dt> <dd>

The maximum time taken to process a request over this connection.

</dd> <dt>

**AverageProcessingTime**
</dt> <dd>

The average time taken to process a request over this connection.

</dd> </dl>

## Remarks

It is optional that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiprf.h (include Iscsiprf.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> <dt>

[**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_RequestTimeStatistics%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






