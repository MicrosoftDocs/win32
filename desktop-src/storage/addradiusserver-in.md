---
title: AddRADIUSServer\_IN structure
description: The AddRADIUSServer\_IN structure holds the input data for the AddRADIUSServer method, which is used to add a new RADIUS server entry to existing list.
ms.assetid: 7b7b9f3b-df33-4886-bd22-23429cb05ea7
keywords:
- AddRADIUSServer_IN structure Storage Devices
- PAddRADIUSServer_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- AddRADIUSServer_IN
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

# AddRADIUSServer\_IN structure

The AddRADIUSServer\_IN structure holds the input data for the [AddRADIUSServer](https://msdn.microsoft.com/library/windows/hardware/ff550133) method, which is used to add a new RADIUS server entry to existing list.

## Syntax


```C++
typedef struct _AddRADIUSServer_IN {
  ISCSI_IP_Address RADIUSIPAddress;
} AddRADIUSServer_IN, *PAddRADIUSServer_IN;
```



## Members

<dl> <dt>

**RADIUSIPAddress**
</dt> <dd>

A [**ISCSI\_IP\_Address**](iscsi-ip-address.md) structure that contains an IP version-independent address of the RADIUS server.

</dd> </dl>

## Remarks

It is optional that you implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[AddRADIUSServer](https://msdn.microsoft.com/library/windows/hardware/ff550133)
</dt> <dt>

[**AddRADIUSServer\_OUT**](addradiusserver-out.md)
</dt> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> <dt>

[MSiSCSI\_Operations WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563091)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AddRADIUSServer_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






