---
title: MSiSCSI\_ConnectionStatistics structure
description: The MSiSCSI\_ConnectionStatistics structure is used by iSCSI initiators to report statistics for a connection within a session.
ms.assetid: f1f38292-604f-4618-b6ec-f3822d60a96c
keywords:
- MSiSCSI_ConnectionStatistics structure Storage Devices
- PMSiSCSI_ConnectionStatistics structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_ConnectionStatistics
api_location:
- iscsiprf.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MSiSCSI\_ConnectionStatistics structure

The **MSiSCSI\_ConnectionStatistics** structure is used by iSCSI initiators to report statistics for a connection within a session.

## Syntax


```C++
typedef struct _MSiSCSI_ConnectionStatistics {
  WCHAR     iSCSIName[223 + 1];
  USHORT    CID;
  ULONGLONG USID;
  ULONGLONG UniqueAdapterId;
  ULONGLONG BytesSent;
  ULONGLONG BytesReceived;
  ULONGLONG PDUCommandsSent;
  ULONGLONG PDUResponsesReceived;
} MSiSCSI_ConnectionStatistics, *PMSiSCSI_ConnectionStatistics;
```



## Members

<dl> <dt>

**iSCSIName**
</dt> <dd>

A wide character string that contains the name of the iSCSI target.

</dd> <dt>

**CID**
</dt> <dd>

The iSCSI connection identifier (ID) for this connection instance. This ID is an internal value that the iSCSI protocol uses to identify the connection. Do not use this ID. Application software should use the connection identifier that the [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods return in the *UniqueConnectionId* parameter.

</dd> <dt>

**USID**
</dt> <dd>

The iSCSI session ID for this connection instance. This ID is an internal value that the iSCSI protocol uses to identify the session. Application software should use the session identifier that the [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods return in the *UniqueSessionId* parameter.

</dd> <dt>

**UniqueAdapterId**
</dt> <dd>

A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this ID. The initiator reports this value in the **UniqueAdapterId** member of the [**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md) structure.

</dd> <dt>

**BytesSent**
</dt> <dd>

The number of bytes that are sent over this connection.

</dd> <dt>

**BytesReceived**
</dt> <dd>

The number of bytes that are received over this connection.

</dd> <dt>

**PDUCommandsSent**
</dt> <dd>

The number of PDUs that are sent over this connection.

</dd> <dt>

**PDUResponsesReceived**
</dt> <dd>

The number of PDUs that are received over this connection.

</dd> </dl>

## Remarks

Initiators must register the [MSiSCSI\_ConnectionStatistics WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562989) with the following dynamic instance name for the connection:


```
targetname_#:#
```



The first number sign (\#) is the value in the **USID** member of **MSiSCSI\_ConnectionStatistics**, and the second number sign (\#) is the value in the **CID** member. It is optional that you implement this class.

The totals tracked by this structure are valid for the lifetime of the connection in the session. Totals for all connections in a session are obtained in [**MSiSCSI\_SessionStatistics**](msiscsi-sessionstatistics.md) structure.

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

[MSiSCSI\_ConnectionStatistics WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562989)
</dt> <dt>

[**MSiSCSI\_HBAInformation**](msiscsi-hbainformation.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_ConnectionStatistics%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






