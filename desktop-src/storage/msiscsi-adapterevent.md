---
title: MSiSCSI\_AdapterEvent structure
description: The MSiSCSI\_AdapterEvent structure contains information that is reported whenever an adapter event occurs.
ms.assetid: 03820d4d-d013-40fb-a686-1b228f178f50
keywords:
- MSiSCSI_AdapterEvent structure Storage Devices
- PMSiSCSI_AdapterEvent structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_AdapterEvent
api_location:
- iscsiop.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MSiSCSI\_AdapterEvent structure

The MSiSCSI\_AdapterEvent structure contains information that is reported whenever an adapter event occurs.

## Syntax


```C++
typedef struct _MSiSCSI_AdapterEvent {
  ULONGLONG UniqueAdapterId;
  ULONG     EventCode;
} MSiSCSI_AdapterEvent, *PMSiSCSI_AdapterEvent;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID). The initiator reports this value in the **UniqueAdapterId** member of the [**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md) structure.

</dd> <dt>

**EventCode**
</dt> <dd>

An [**ISCSI\_ADAPTER\_EVENT\_CODE**](iscsi-adapter-event-code.md) enumeration value that indicates the type of adapter event that occurred.

</dd> </dl>

## Remarks

The WMI tool suite automatically generates a declaration of the MSiSCSI\_AdapterEvent structure when it compiles the [MSiSCSI\_AdapterEvent WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562971) in *Operations.mof*. You must implement this method if the adapter supports discovery.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_ADAPTER\_EVENT\_CODE**](iscsi-adapter-event-code.md)
</dt> <dt>

[MSiSCSI\_AdapterEvent WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562971)
</dt> <dt>

[**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_AdapterEvent%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






