---
title: SetPresharedKeyForId\_IN structure
description: The SetPresharedKeyForId\_IN structure holds the input data for the SetPresharedKeyForId method.
ms.assetid: f941bc28-f906-4399-be54-09e2bc12e443
keywords:
- SetPresharedKeyForId_IN structure Storage Devices
- PSetPresharedKeyForId_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SetPresharedKeyForId_IN
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

# SetPresharedKeyForId\_IN structure

The SetPresharedKeyForId\_IN structure holds the input data for the [SetPresharedKeyForId](https://msdn.microsoft.com/library/windows/hardware/ff565800) method.

## Syntax


```C++
typedef struct _SetPresharedKeyForId_IN {
  ULONG     PortNumber;
  ULONGLONG SecurityFlags;
  UCHAR     IdType;
  ULONG     IdSize;
  ULONG     KeySize;
  UCHAR     Id[1];
} SetPresharedKeyForId_IN, *PSetPresharedKeyForId_IN;
```



## Members

<dl> <dt>

**PortNumber**
</dt> <dd>

The number of the port that the initiator uses the preshared key with. A value of 0xffffffff indicates all ports.

</dd> <dt>

**SecurityFlags**
</dt> <dd>

A bitwise OR of flags that indicate the security requirements of a target. For a list of possible values for this member, see [SECURITY\_FLAG\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff565399).

</dd> <dt>

**IdType**
</dt> <dd>

The type of identifier to associate with the preshared key. The initiator puts this identifier (ID) in the Internet key exchange (IKE) identification payload to identify itself to the target. The following table describes the possible identification payload types.



| Identification payload type | Meaning                                                                                                                                                        |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID\_IPV4\_ADDR<br/>   | The initiator identifies itself to the target during the key exchange with a single 4-byte version 4 IP address.<br/>                                    |
| ID\_FQDN<br/>         | The initiator identifies itself to the target during the key exchange with a fully qualified domain name string (for example, "website.com"). <br/>      |
| ID\_USER\_FQDN<br/>   | The initiator identifies itself to the target during the key exchange with a fully qualified user name string (for example, "sample@example.com"). <br/> |
| ID\_IPV6\_ADDR<br/>   | The initiator identifies itself to the target during the key exchange with a single 16-byte version 6 IP address.<br/>                                   |



 

</dd> <dt>

**IdSize**
</dt> <dd>

The size, in bytes, of the identifier in **Id***.*

</dd> <dt>

**KeySize**
</dt> <dd>

The size, in bytes, of the key in **Key***.*

</dd> <dt>

**Id**
</dt> <dd>

The ID to associate with the key. The initiator uses this ID to identify itself to the target during key exchange.

</dd> </dl>

## Remarks

You must implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[SECURITY\_FLAG\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff565399)
</dt> <dt>

[SetPresharedKeyForId](https://msdn.microsoft.com/library/windows/hardware/ff565800)
</dt> <dt>

[**SetPresharedKeyForId\_OUT**](setpresharedkeyforid-out.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SetPresharedKeyForId_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






