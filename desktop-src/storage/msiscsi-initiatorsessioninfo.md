---
title: MSiSCSI\_InitiatorSessionInfo structure
description: The MSiSCSI\_InitiatorSessionInfo structure contains information about a collection of sessions that belong to the indicated HBA initiator.
ms.assetid: 0406efa5-26ad-4a3d-829b-d9b03b7c3b26
keywords:
- MSiSCSI_InitiatorSessionInfo structure Storage Devices
- PMSiSCSI_InitiatorSessionInfo structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_InitiatorSessionInfo
api_location:
- iscsimgt.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MSiSCSI\_InitiatorSessionInfo structure

The MSiSCSI\_InitiatorSessionInfo structure contains information about a collection of sessions that belong to the indicated HBA initiator.

## Syntax


```C++
typedef struct _MSiSCSI_InitiatorSessionInfo {
  ULONGLONG               UniqueAdapterId;
  ULONG                   SessionCount;
  ISCSI_SessionStaticInfo SessionsList[1];
} MSiSCSI_InitiatorSessionInfo, *PMSiSCSI_InitiatorSessionInfo;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID). The initiator reports this value in the **UniqueAdapterId** member of the [**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md) structure.

</dd> <dt>

**SessionCount**
</dt> <dd>

The number of sessions that have been established with the provided adapter ID.

</dd> <dt>

**SessionsList**
</dt> <dd>

A variable length array of [**ISCSI\_SessionStaticInfo**](iscsi-sessionstaticinfo.md) structures, which describe the static information that is associated with a session.

</dd> </dl>

## Remarks

You must implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_SessionStaticInfo**](iscsi-sessionstaticinfo.md)
</dt> <dt>

[**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md)
</dt> <dt>

[MSiSCSI\_InitiatorSessionInfo WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563057)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_InitiatorSessionInfo%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






