---
title: childrenCollection object
description: The childrenCollection object represents a collection of WPDObjects.
ms.assetid: 9339db79-db69-47d8-bcaa-2d40471932de
keywords:
- childrenCollection object WPD Automation
- childrenCollection object WPD Automation , described
topic_type:
- apiref
api_name:
- childrenCollection
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# childrenCollection object

The **childrenCollection** object represents a collection of **WPDObjects**.

## Members

The **childrenCollection** object has these types of members:

-   [Properties](#properties)

### Properties

The **childrenCollection** object has these properties.



| Property                                             | Access type          | Description                                                     |
|:-----------------------------------------------------|:---------------------|:----------------------------------------------------------------|
| [**Count**](childrencollection-count.md)<br/> | Read-only<br/> | Gets the number of **WPDObjects** in the collection.<br/> |



 

## Remarks

An object contained in a **childrenCollection** can be accessed by a zero-based numeric index, by a Persistent Unique Id (PUID), or by an Object Identifier (ObjectID).

## Examples

The following JScript example demonstrates two ways of creating a **childrenCollection** object, and shows all three ways of accessing an object in the collection. This example assumes that the PUID and ObjectID of a specific child is known. For more information on retrieving the PUID or ObjectID for an object, see [Enumerating Services and Storages](enumerating-services-and-storages.md).


```JScript
// Retrieve a collection of all the children in a WPDObject.

var childrenCollection = wpdObject.Children;

// Retrieve a collection of children in a WPDObject for the specified
// data formats.
 
var childrenCollectionByFormat = wpdObject.GetChildrenByFormat(["Wma", "Mp3"]);

// Enumerate the children in the collection.

for (i=0; i < childrenCollection.Count; i++)
{
    // Access a child object by numeric index.
    var aChild = childrenCollection[i]; 
}
     
// Access a specific child object by PUID.

var aChildByPUID = childrenCollection["somePUID"];

// Access a specific child object by ObjectID.

var aChildByObjectID = childrenCollection["someObjectID"];
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[About the childrenCollection Object](about-the-childrencollection-object.md)
</dt> <dt>

[Enumerating Services and Storages](enumerating-services-and-storages.md)
</dt> <dt>

[**servicesCollection Object**](servicescollection-object.md)
</dt> <dt>

[**storagesCollection Object**](storagescollection-object.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





