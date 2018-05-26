---
title: AddConnectionToSession\_IN structure
description: The AddConnectionToSession\_IN structure holds input data for the AddConnectionToSession method, which is used to add a new connection to an already existing session.
ms.assetid: 7fcb0b87-1f9e-4956-a59a-cd83fa04e5db
keywords:
- AddConnectionToSession_IN structure Storage Devices
- PAddConnectionToSession_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- AddConnectionToSession_IN
api_location:
- iscsiop.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AddConnectionToSession\_IN structure

The AddConnectionToSession\_IN structure holds input data for the [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) method, which is used to add a new connection to an already existing session.

## Syntax


```C++
typedef struct _AddConnectionToSession_IN {
  ULONGLONG          UniqueAdapterId;
  ULONGLONG          UniqueSessionId;
  ULONGLONG          SecurityFlags;
  ULONG              PortNumber;
  ISCSI_LoginOptions LoginOptions;
  ISCSI_TargetPortal TargetPortal;
  ULONG              UsernameSize;
  ULONG              PasswordSize;
  ULONG              KeySize;
  UCHAR              Key[1];
} AddConnectionToSession_IN, *PAddConnectionToSession_IN;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

A 64-bit integer that uniquely identifies an adapter and a particular loaded instance of a storage miniport driver that manages the adapter. This identifier is unique, not only on the computer where the adapter is located, but also across the entire network.

</dd> <dt>

**UniqueSessionId**
</dt> <dd>

A 64-bit integer that uniquely identifies the session. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in their *UniqueSessionId* parameter. Do not confuse this value with the values in the ISID and TSID members.

</dd> <dt>

**SecurityFlags**
</dt> <dd>

A bitwise OR of flags that indicate the security requirements of a target. For a list of possible values for this member, see [SECURITY\_FLAG\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff565399).

</dd> <dt>

**PortNumber**
</dt> <dd>

The number of the port from which to initiate the target logon session.

</dd> <dt>

**LoginOptions**
</dt> <dd>

A [**ISCSI\_LoginOptions**](iscsi-loginoptions.md) structure that describes the characteristics of the target logon session that a connection will be added to.

</dd> <dt>

**TargetPortal**
</dt> <dd>

A [**ISCSI\_TargetPortal**](iscsi-targetportal.md) structure that indicates which target portal to use to make the additional connection. The **AddConnectionToSession** method calls the **LoginToTarget** method to establish the new connection. If **LoginToTarget** fails with a status value of either ISCSC\_TARGET\_MOVED\_PERMANENTLY or ISCSC\_TARGET\_MOVED\_TEMPORARILY. **TargetPortal** will indicate, on output from **AddConnectionToSession**, the portal that the logon operation should be redirected to. For more information about the ISCSC\_TARGET\_MOVED\_PERMANENTLY and ISCSC\_TARGET\_MOVED\_TEMPORARILY status values, see [ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568).

</dd> <dt>

**UsernameSize**
</dt> <dd>

The username size, in bytes.

</dd> <dt>

**PasswordSize**
</dt> <dd>

The password size, in bytes.

</dd> <dt>

**KeySize**
</dt> <dd>

The preshared key size, in bytes.

</dd> <dt>

**Key**
</dt> <dd>

A variable-length array of characters that specifies the preshared key that is associated with the target IP address. The number of elements in the array is specified by the KeySize field.

</dd> </dl>

## Remarks

The iSCSI service requires this method. It is optional that you implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[**AddConnectionToSession\_OUT**](addconnectiontosession-out.md)
</dt> <dt>

[**ISCSI\_LoginOptions**](iscsi-loginoptions.md)
</dt> <dt>

[**ISCSI\_TargetPortal**](iscsi-targetportal.md)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> <dt>

[MSiSCSI\_Operations WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563091)
</dt> <dt>

[SECURITY\_FLAG\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff565399)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AddConnectionToSession_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






