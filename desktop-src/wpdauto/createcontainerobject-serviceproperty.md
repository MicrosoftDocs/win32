---
title: createContainer.ServiceProperty property
description: The ServiceProperty sets the value of a service-defined property on the Creation Container object.
ms.assetid: '2901cfa2-c6fa-404b-a451-04498678ce99'
keywords: ["ServiceProperty property WPD Automation", "ServiceProperty property WPD Automation , createContainer object", "createContainer object WPD Automation , ServiceProperty property"]
topic_type:
- apiref
api_name:
- createContainer.ServiceProperty
api_type:
- COM
---

# createContainer.ServiceProperty property

The **ServiceProperty** sets the value of a service-defined property on the [**Creation Container**](creation-container-object.md) object.

This property is write-only.

## Syntax


```JScript
createContainer.ServiceProperty = ServiceProperty
```



## Property value

This property has the same name as the service-defined property.

## Examples

The following JScript example uses the **ServiceProperty** to set the value of the service-defined properties, "MusicAlbum" and "MusicArtist", on a createContainer object.


```JScript
var createContainer = serviceObject.CreateNewObject("Mp3");

createContainer.MusicAlbum = "Album Name";
createContainer.MusicArtist = "Artist Name";
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Creation Container Object**](creation-container-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> </dl>

 

 





