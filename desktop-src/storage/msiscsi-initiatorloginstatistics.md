---
title: MSiSCSI\_InitiatorLoginStatistics structure
description: The MSiSCSI\_InitiatorLoginStatistics structure is used by iSCSI initiators to report logon statistics.
ms.assetid: 8d670887-e8bb-4b99-99ae-16c0dd9c4431
keywords:
- MSiSCSI_InitiatorLoginStatistics structure Storage Devices
- PMSiSCSI_InitiatorLoginStatistics structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_InitiatorLoginStatistics
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

# MSiSCSI\_InitiatorLoginStatistics structure

The MSiSCSI\_InitiatorLoginStatistics structure is used by iSCSI initiators to report logon statistics.

## Syntax


```C++
typedef struct _MSiSCSI_InitiatorLoginStatistics {
  ULONGLONG UniqueAdapterId;
  ULONG     LoginAcceptRsps;
  ULONG     LoginOtherFailRsps;
  ULONG     LoginRedirectRsps;
  ULONG     LoginAuthFailRsps;
  ULONG     LoginAuthenticateFails;
  ULONG     LoginNegotiateFails;
  ULONG     LogoutNormals;
  ULONG     LogoutOtherCodes;
  ULONG     LoginFailures;
} MSiSCSI_InitiatorLoginStatistics, *PMSiSCSI_InitiatorLoginStatistics;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID). The initiator reports this value in the **UniqueAdapterId** member of the [**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md) structure.

</dd> <dt>

**LoginAcceptRsps**
</dt> <dd>

The number of login accept responses.

</dd> <dt>

**LoginOtherFailRsps**
</dt> <dd>

The number of failed responses.

</dd> <dt>

**LoginRedirectRsps**
</dt> <dd>

The number of redirect responses.

</dd> <dt>

**LoginAuthFailRsps**
</dt> <dd>

The number of logon responses that failed because the initiator and target did not have compatible authentication algorithms.

</dd> <dt>

**LoginAuthenticateFails**
</dt> <dd>

The number of logons that failed because of a target authentication failure (the initiator and target did not have matching credentials).

</dd> <dt>

**LoginNegotiateFails**
</dt> <dd>

The number of logons that failed because of negotiation failures.

</dd> <dt>

**LogoutNormals**
</dt> <dd>

The number of logoff PDUs with a reason code of 0.

</dd> <dt>

**LogoutOtherCodes**
</dt> <dd>

The number of logoff PDUs with a status code other than 0.

</dd> <dt>

**LoginFailures**
</dt> <dd>

The number of times that a logon attempt by the initiator has failed.

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

[MSiSCSI\_InitiatorLoginStatistics WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563042)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_InitiatorLoginStatistics%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






