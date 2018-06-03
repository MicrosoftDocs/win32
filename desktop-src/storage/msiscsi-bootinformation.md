---
title: MSiSCSI\_BootInformation structure
description: The MSiSCSI\_BootInformation structure is used with the MSiSCSI\_BootInformation WMI Class to expose information about the node that contains the target boot device.
ms.assetid: 971bbd30-5bde-4cf6-9b94-7c21c29590d5
keywords:
- MSiSCSI_BootInformation structure Storage Devices
- PMSiSCSI_BootInformation structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_BootInformation
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

# MSiSCSI\_BootInformation structure

The MSiSCSI\_BootInformation structure is used with the [MSiSCSI\_BootInformation WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562984) to expose information about the node that contains the target boot device.

## Syntax


```C++
typedef struct _MSiSCSI_BootInformation {
  UCHAR NodeName[223];
  ULONG SharedSecretLength;
  UCHAR SharedSecret[255];
} MSiSCSI_BootInformation, *PMSiSCSI_BootInformation;
```



## Members

<dl> <dt>

**NodeName**
</dt> <dd>

The name of the initiator node that contains the boot device.

</dd> <dt>

**SharedSecretLength**
</dt> <dd>

The length, in bytes, of the shared secret for the initiator node.

</dd> <dt>

**SharedSecret**
</dt> <dd>

The shared secret for the initiator node.

</dd> </dl>

## Remarks

You must implement this class if the adapter supports iSCSI boot.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[MSiSCSI\_BootInformationWMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562984)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_BootInformation%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






