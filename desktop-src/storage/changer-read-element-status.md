---
title: CHANGER\_READ\_ELEMENT\_STATUS structure
description: The CHANGER\_READ\_ELEMENT\_STATUS structure is used in conjunction with the IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS request to retrieve the status of all elements or the status of a specified number of elements of a particular type.
ms.assetid: 3e80790c-72b9-4e26-a767-a25e6425118e
keywords:
- CHANGER_READ_ELEMENT_STATUS structure Storage Devices
- PCHANGER_READ_ELEMENT_STATUS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CHANGER_READ_ELEMENT_STATUS
api_location:
- ntddchgr.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CHANGER\_READ\_ELEMENT\_STATUS structure

The CHANGER\_READ\_ELEMENT\_STATUS structure is used in conjunction with the [**IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS**](ioctl-changer-get-element-status.md) request to retrieve the status of all elements or the status of a specified number of elements of a particular type.

## Syntax


```C++
typedef struct _CHANGER_READ_ELEMENT_STATUS {
  CHANGER_ELEMENT_LIST ElementList;
  BOOLEAN              VolumeTagInfo;
} CHANGER_READ_ELEMENT_STATUS, *PCHANGER_READ_ELEMENT_STATUS;
```



## Members

<dl> <dt>

**ElementList**
</dt> <dd>

Specifies the element type and the number of elements of that type for which to report status in a structure of type [**CHANGER\_ELEMENT\_LIST**](changer-element-list.md). This member contains a list of structures of type [**CHANGER\_ELEMENT**](changer-element.md). The **ElementType** member of each CHANGER\_ELEMENT structure in this list can be assigned a value of **ChangerDrive**, **ChangerSlot**, **ChangerTransport**, **ChangerIEPort**, or **AllElements**.

</dd> <dt>

**VolumeTagInfo**
</dt> <dd>

Indicates, when **TRUE**, that volume tag information should be reported in addition to element status. When **FALSE**, it indicates that only element status should be reported. A volume tag can be a bar code or an application-defined value assigned using [**ChangerQueryVolumeTags**](changerqueryvolumetags.md). This member is applicable only if either CHANGER\_BAR\_CODE\_SCANNER\_INSTALLED or CHANGER\_VOLUME\_IDENTIFICATION is set in the **Features0** member of the [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) structure.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS**](ioctl-changer-get-element-status.md)
</dt> <dt>

[**ChangerGetElementStatus**](changergetelementstatus.md)
</dt> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> <dt>

[**CHANGER\_ELEMENT**](changer-element.md)
</dt> <dt>

[**CHANGER\_ELEMENT\_LIST**](changer-element-list.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_READ_ELEMENT_STATUS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






