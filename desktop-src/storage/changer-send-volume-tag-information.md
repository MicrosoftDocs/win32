---
title: CHANGER\_SEND\_VOLUME\_TAG\_INFORMATION structure
description: This structure is passed to the ChangerQueryVolumeTags routine and is used to specify a search criterion for retrieving changer elements.
ms.assetid: 'cfe0673c-1dcb-4c4e-9ec4-8d9f27919c85'
keywords: ["CHANGER_SEND_VOLUME_TAG_INFORMATION structure Storage Devices", "PCHANGER_SEND_VOLUME_TAG_INFORMATION structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- CHANGER_SEND_VOLUME_TAG_INFORMATION
api_location:
- ntddchgr.h
api_type:
- HeaderDef
---

# CHANGER\_SEND\_VOLUME\_TAG\_INFORMATION structure

This structure is passed to the [**ChangerQueryVolumeTags**](changerqueryvolumetags.md) routine and is used to specify a search criterion for retrieving changer elements.

## Syntax


```C++
typedef struct _CHANGER_SEND_VOLUME_TAG_INFORMATION {
  CHANGER_ELEMENT StartingElement;
  ULONG           ActionCode;
  UCHAR           VolumeIDTemplate[MAX_VOLUME_TEMPLATE_SIZE];
} CHANGER_SEND_VOLUME_TAG_INFORMATION, *PCHANGER_SEND_VOLUME_TAG_INFORMATION;
```



## Members

<dl> <dt>

**StartingElement**
</dt> <dd>

Describes the first element of the range to search for or to set in a structure of type [**CHANGER\_ELEMENT**](changer-element.md).

</dd> <dt>

**ActionCode**
</dt> <dd>

Indicates the operation to perform. The **Features0** member of [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) indicates whether the changer supports a particular category of operation:

-   Translate operations, also known as "searching operations", request that the target device search its volume tag information for elements that match the template passed to the device. Valid only if **Features0** is set to CHANGER\_VOLUME\_SEARCH.

-   Assert operations define volume tag information for a single element. Valid only if **Features0** is set to CHANGER\_VOLUME\_ASSERT.

-   Replace operations define volume tag information for a single element, overwriting any information previously defined. Valid only if **Features0** is set to CHANGER\_VOLUME\_REPLACE.

-   Undefined operations clear previously defined volume tag information for a single element. Valid only if **Features0** is set to CHANGER\_VOLUME\_UNDEFINE.

</dd> <dt>

**VolumeIDTemplate**
</dt> <dd>

Specifies the template to be used by the device to search for volume IDs. For a translate operation, the template can include the wildcard characters, asterisk (\*) and question mark (?), to search for volumes that match the template. For other operations, the template specifies a single volume.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**READ\_ELEMENT\_ADDRESS\_INFO**](read-element-address-info.md)
</dt> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> <dt>

[**ChangerQueryVolumeTags**](changerqueryvolumetags.md)
</dt> <dt>

[**CHANGER\_ELEMENT**](changer-element.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_SEND_VOLUME_TAG_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






