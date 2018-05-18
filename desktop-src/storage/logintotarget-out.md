---
title: LoginToTarget\_OUT structure
description: The LoginToTarget\_OUT structure holds the output data for the LoginToTarget method.
ms.assetid: '569816dc-3b92-45da-a1b8-ce4b504b6592'
keywords: ["LoginToTarget_OUT structure Storage Devices", "PLoginToTarget_OUT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- LoginToTarget_OUT
api_location:
- iscsiop.h
api_type:
- HeaderDef
---

# LoginToTarget\_OUT structure

The LoginToTarget\_OUT structure holds the output data for the [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) method.

## Syntax


```C++
typedef struct _LoginToTarget_OUT {
  ULONG     Status;
  ULONGLONG UniqueSessionId;
  ULONGLONG UniqueConnectionId;
} LoginToTarget_OUT, *PLoginToTarget_OUT;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

On output from **LoginToTarget**, the status of the **LoginToTarget** operation. For a list of status qualifiers, see [ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568).

</dd> <dt>

**UniqueSessionId**
</dt> <dd>

A 64-bit integer that uniquely identifies the session. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in their *UniqueSessionId* parameter. The unique session identifier (ID) does not change until the initiator logs off of the session. The session ID that the iSCSI initiator service exposes to user-mode software is a 128-bit number. The top (most significant) 64 bits consist of a unique adapter ID that the initiator reports in the **UniqueAdapterId** member of the [**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md) class. The lower (least significant) 64 bits correspond to the value in **UniqueSessionId**. When the service communicates with the adapter, the service uses the lower 64 bits (**UniqueSessionId**), while user-mode software uses all of the 128 bits to communicate with the iSCSI initiator service.

</dd> <dt>

**UniqueConnectionId**
</dt> <dd>

On output from **LoginToTarget**, a 64-bit integer that uniquely identifies the connection. The connection ID that the iSCSI initiator service exposes to user-mode software is a 128-bit number. The top (most significant) 64 bits consist of a unique adapter ID that the initiator reports in the **UniqueAdapterId** member of the [**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md) class. The lower (least significant) 64 bits correspond to the value in **UniqueConnectionId**. When the service communicates with the adapter, the service uses the lower 64 bits (**UniqueConnectionId**), while user-mode software uses all the 128 bits to communicate with the iSCSI initiator service.

</dd> </dl>

## Remarks

You must implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> <dt>

[**LoginToTarget\_IN**](logintotarget-in.md)
</dt> <dt>

[**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md)
</dt> <dt>

[MSiSCSI\_Operations WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563091)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20LoginToTarget_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






