---
title: Media.getItemInfo method
description: The getItemInfo method retrieves the value of the specified attribute for the current media item.
ms.assetid: 'a1ee0d40-b979-424b-bd4e-d1acf6354d8d'
keywords:
- getItemInfo method Windows Media Player
- getItemInfo method Windows Media Player , Media class
- Media class Windows Media Player , getItemInfo method
topic_type:
- apiref
api_name:
- Media.getItemInfo
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Media.getItemInfo method

The **getItemInfo** method retrieves the value of the specified attribute for the current media item.

## Syntax


```JScript
strRetVal = Media.getItemInfo(
  name
)
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

**String** containing the name of the attribute. For information about the attributes supported by Windows Media Player, see the Windows Media Player [Attribute Reference](attribute-reference.md).

</dd> </dl>

## Return value

This method returns a **String** representing the value of the specified attribute. For attributes whose underlying value is **Boolean**, it returns the string "true" or "false".

## Remarks

This method retrieves the metadata for an individual digital media item or a media item that is part of a playlist.

The **attributeCount** property contains the number of attribute names available for a given **Media** object. Index numbers can then be used with the **getAttributeName** method to determine the name of each available attribute. Individual attribute names can be passed to **getItemInfo**.

To retrieve attributes with multiple values and attributes with complex values, use the **getItemInfoByType** method.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

To share the Windows media libraries over UPnP, Windows Media Player creates a content directory service (CDS) that is exposed over UPnP. Other devices can then navigate and browse the libraries.

In Windows 7, an application can use the Windows Media Player [**TrackingID**](trackingid-attribute.md) and [**MediaType**](mediatype-attribute.md) attributes to construct the object ID of each item in the CDS. Note that this construction might change in future versions of Windows. The application passes each of these attribute strings in the *name* parameter in a call to **getItemInfo**. **getItemInfo** returns the value for each attribute in the return value. The application then uses the following syntax to construct each object ID:

*TrackingID*.0.*MediaTypeID*

This syntax has the following meaning:

-   *TrackingID* is the string that is stored in the Windows Media Player [**TrackingID**](trackingid-attribute.md) attribute of the media item.
-   *MediaTypeID* depends on the value of the [**MediaType**](mediatype-attribute.md) attribute, as shown in the following table:

    | MediaType attribute                      | MediaTypeID |
    |------------------------------------------|-------------|
    | [Audio Items](audio-item-attributes.md) | 4           |
    | [Photo Items](photo-item-attributes.md) | B           |
    | [Video Items](video-item-attributes.md) | 8           |

    

     

**Windows Media Player 10 Mobile:** Attributes for a media item are available only during playback unless they are retrieved from the item through the media collection.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Media.attributeCount**](media-attributecount.md)
</dt> <dt>

[**Media.getAttributeName**](media-getattributename.md)
</dt> <dt>

[**Media.getItemInfoByType**](media-getiteminfobytype.md)
</dt> <dt>

[**Media.setItemInfo**](media-setiteminfo.md)
</dt> <dt>

[**Reading Attribute Values**](reading-attribute-values.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





