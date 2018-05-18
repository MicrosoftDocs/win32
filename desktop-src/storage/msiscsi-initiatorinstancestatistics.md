---
title: MSiSCSI\_InitiatorInstanceStatistics structure
description: The MSiSCSI\_InitiatorInstanceStatistics structure is used by iSCSI initiators to report initiator statistics.
ms.assetid: 'b07b8186-970a-428f-955f-4e7e6ab20bfc'
keywords: ["MSiSCSI_InitiatorInstanceStatistics structure Storage Devices", "PMSiSCSI_InitiatorInstanceStatistics structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MSiSCSI_InitiatorInstanceStatistics
api_location:
- iscsiprf.h
api_type:
- HeaderDef
---

# MSiSCSI\_InitiatorInstanceStatistics structure

The MSiSCSI\_InitiatorInstanceStatistics structure is used by iSCSI initiators to report initiator statistics.

## Syntax


```C++
typedef struct _MSiSCSI_InitiatorInstanceStatistics {
  ULONGLONG UniqueAdapterId;
  ULONG     SessionDigestErrorCount;
  ULONG     SessionConnectionTimeoutErrorCount;
  ULONG     SessionFormatErrorCount;
  ULONG     SessionFailureCount;
} MSiSCSI_InitiatorInstanceStatistics, *PMSiSCSI_InitiatorInstanceStatistics;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID). The initiator reports this value in the **UniqueAdapterId** member of the [**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md) structure. For more information about the class that generates MSiSCSI\_HBAInformation, see [MSiSCSI\_HBAInformation WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563017).

</dd> <dt>

**SessionDigestErrorCount**
</dt> <dd>

The number of session digest errors.

</dd> <dt>

**SessionConnectionTimeoutErrorCount**
</dt> <dd>

The number of session connection time-out errors.

</dd> <dt>

**SessionFormatErrorCount**
</dt> <dd>

The number of session format errors.

</dd> <dt>

**SessionFailureCount**
</dt> <dd>

The number of failed sessions that belong to the initiator instance that **UniqueAdapterId** specifies.

</dd> </dl>

## Remarks

It is optional that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiprf.h (include Iscsiprf.h)</dt> </dl> |



## See also

<dl> <dt>

[**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md)
</dt> <dt>

[MSiSCSI\_HBAInformation WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563017)
</dt> <dt>

[MSiSCSI\_InitiatorInstanceStatistics WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563038)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_InitiatorInstanceStatistics%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






