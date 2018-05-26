---
title: LogoutFromTarget\_OUT structure
description: The LogoutFromTarget\_OUT structure holds the output data for the LogoutFromTarget method.
ms.assetid: 15231188-5c6d-4e36-afe9-74b92f445fa3
keywords:
- LogoutFromTarget_OUT structure Storage Devices
- PLogoutFromTarget_OUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- LogoutFromTarget_OUT
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

# LogoutFromTarget\_OUT structure

The LogoutFromTarget\_OUT structure holds the output data for the [LogoutFromTarget](https://msdn.microsoft.com/library/windows/hardware/ff561602) method.

## Syntax


```C++
typedef struct _LogoutFromTarget_OUT {
  ULONG Status;
} LogoutFromTarget_OUT, *PLogoutFromTarget_OUT;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

On output from **LogoutFromTarget**, the status of the logoff operation. For a list of status qualifiers, see [ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568).

</dd> </dl>

## Remarks

You must implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> <dt>

[LogoutFromTarget](https://msdn.microsoft.com/library/windows/hardware/ff561602)
</dt> <dt>

[**LogoutFromTarget\_IN**](logoutfromtarget-in.md)
</dt> <dt>

[MSiSCSI\_Operations WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563091)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20LogoutFromTarget_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






