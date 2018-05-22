---
Description: 'Specifies the whole file behind the object. It is also a way of referring to any resource type, including those not covered by other Windows Portable Devices resource types, such as a custom object type.'
ms.assetid: 'e534ea86-4932-45c7-87e7-03926202fa7e'
title: 'WPD\_RESOURCE\_DEFAULT'
---

# WPD\_RESOURCE\_DEFAULT

Specifies the whole file behind the object. It is also a way of referring to any resource type, including those not covered by other Windows Portable Devices resource types, such as a custom object type.

Any resources embedded within the specified resource will be included. For example, the default resource of a root folder of contacts may include all the nested contacts. However, any child resources that are merely *linked* by metadata or references are not included. An example of this would be a playlist, which might only link to audio files through metadata references or textual path references in the file.

The only allowed *pid* value for this **PROPERTYKEY** is zero.

This type of resource must support the following attributes.



| Attribute Name                                                                                                            | Required or Optional                                   |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [WPD\_RESOURCE\_ATTRIBUTE\_TOTAL\_SIZE](resource-attribute-properties.md#wpd-resource-attribute-total-size)              | Required.                                              |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_READ](attributes.md#wpd-resource-attribute-can-read)                                     | Required if clients can read this resource.            |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_WRITE](attributes.md#wpd-resource-attribute-can-write)                                   | Required if clients can write to this resource.        |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_DELETE](attributes.md#wpd-resource-attribute-can-delete)                                 | Required if clients can delete this resource.          |
| [WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_READ\_BUFFER\_SIZE](attributes.md#wpd-resource-attribute-optimal-read-buffer-size)   | Required if clients have read access to the resource.  |
| [WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_WRITE\_BUFFER\_SIZE](attributes.md#wpd-resource-attribute-optimal-write-buffer-size) | Required if clients have write access to the resource. |
| [WPD\_RESOURCE\_ATTRIBUTE\_FORMAT](resource-attribute-properties.md#wpd-resource-attribute-format)                       | Required.                                              |
| [WPD\_RESOURCE\_ATTRIBUTE\_RESOURCE\_KEY](resource-attribute-properties.md)                                              | Recommended.                                           |



 

## See also

<dl> <dt>

[**Requirements for Resources**](requirements-for-resources.md)
</dt> </dl>

 

 



