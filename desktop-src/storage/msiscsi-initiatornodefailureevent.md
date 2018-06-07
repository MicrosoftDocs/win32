---
title: MSiSCSI\_InitiatorNodeFailureEvent structure
description: The MSiSCSI\_InitiatorNodeFailureEvent structure is used to report an event when a node failure occurs.
ms.assetid: 0d761b64-d405-4c19-9fd8-e4bf371515a1
keywords:
- MSiSCSI_InitiatorNodeFailureEvent structure Storage Devices
- PMSiSCSI_InitiatorNodeFailureEvent structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_InitiatorNodeFailureEvent
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

# MSiSCSI\_InitiatorNodeFailureEvent structure

The MSiSCSI\_InitiatorNodeFailureEvent structure is used to report an event when a node failure occurs.

## Syntax


```C++
typedef struct _MSiSCSI_InitiatorNodeFailureEvent {
  ULONGLONG        FailureTime;
  UCHAR            FailureType;
  WCHAR            TargetFailureName[223 + 1];
  ISCSI_IP_Address TargetFailureAddr;
} MSiSCSI_InitiatorNodeFailureEvent, *PMSiSCSI_InitiatorNodeFailureEvent;
```



## Members

<dl> <dt>

**FailureTime**
</dt> <dd>

A timestamp that indicates when the node failure occurred.

</dd> <dt>

**FailureType**
</dt> <dd>

The type of node failure. This member can have the following integer values, which are defined in a ValueMap in *Mgmt.mof*.



| Value                            | Failure type                                                                                                                                        |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| LoginOtherFail<br/>        | The logon failed for unspecified reasons. <br/>                                                                                               |
| LoginAuthFail<br/>         | The logon failed, because the initiator and target do not have compatible authentication algorithms. <br/>                                    |
| LoginAuthenticateFail<br/> | The logon failed, because the credentials of the initiator and target do not match and the initiator could not authenticate the target. <br/> |
| LoginNegotiateFail<br/>    | The logon failed, because the initiator could not successfully negotiate a connection with the target. <br/>                                  |
| LogoutOthers<br/>          | The logout failed due to other reasons.<br/>                                                                                                  |



 

</dd> <dt>

**TargetFailureName**
</dt> <dd>

A wide character string that specifies the name of the target that a logon or logoff failed for.

</dd> <dt>

**TargetFailureAddr**
</dt> <dd>

A [**ISCSI\_IP\_Address**](iscsi-ip-address.md) structure that specifies the IP address of the target that a logon or logoff failed for.

</dd> </dl>

## Remarks

It is optional that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> <dt>

[MSiSCSI\_InitiatorNodeFailureEvent WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563049)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_InitiatorNodeFailureEvent%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






