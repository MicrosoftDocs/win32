---
title: READ\_ELEMENT\_ADDRESS\_INFO structure
description: This structure is to retrieve changer elements based on a search criterion specified in a call to the ChangerQueryVolumeTags routine.
ms.assetid: '5fc5b38e-8eef-4ba0-9f29-025df55e4525'
keywords: ["READ_ELEMENT_ADDRESS_INFO structure Storage Devices", "PREAD_ELEMENT_ADDRESS_INFO structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- READ_ELEMENT_ADDRESS_INFO
api_location:
- ntddchgr.h
api_type:
- HeaderDef
---

# READ\_ELEMENT\_ADDRESS\_INFO structure

This structure is to retrieve changer elements based on a search criterion specified in a call to the [**ChangerQueryVolumeTags**](changerqueryvolumetags.md) routine.

## Syntax


```C++
typedef struct _READ_ELEMENT_ADDRESS_INFO {
  ULONG                  NumberOfElements;
  CHANGER_ELEMENT_STATUS ElementStatus[1];
} READ_ELEMENT_ADDRESS_INFO, *PREAD_ELEMENT_ADDRESS_INFO;
```



## Members

<dl> <dt>

**NumberOfElements**
</dt> <dd>

Indicates the number of elements that matched the criteria specified by **ActionCode** and **VolumeTemplateID** in the [**CHANGER\_SEND\_VOLUME\_TAG\_INFORMATION**](changer-send-volume-tag-information.md) structure passed to the driver. If no element matches the criteria, this member is zero.

</dd> <dt>

**ElementStatus**
</dt> <dd>

Contains an array holding the first [**CHANGER\_ELEMENT\_STATUS**](changer-element-status.md) structure that matched the criteria in the CHANGER\_SEND\_VOLUME\_TAG\_INFORMATION structure passed to the driver.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**CHANGER\_SEND\_VOLUME\_TAG\_INFORMATION**](changer-send-volume-tag-information.md)
</dt> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> <dt>

[**CHANGER\_ELEMENT\_STATUS**](changer-element-status.md)
</dt> <dt>

[**ChangerQueryVolumeTags**](changerqueryvolumetags.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20READ_ELEMENT_ADDRESS_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






