---
title: storagesCollection object
description: The storagesCollection object represents a collection of Storage objects.
ms.assetid: bb418975-0473-401c-93fd-d0479e940431
keywords:
- storagesCollection object WPD Automation
- storagesCollection object WPD Automation , described
topic_type:
- apiref
api_name:
- storagesCollection
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# storagesCollection object

The **storagesCollection** object represents a collection of **Storage** objects.

## Members

The **storagesCollection** object has these types of members:

-   [Properties](#properties)

### Properties

The **storagesCollection** object has these properties.



| Property                                             | Access type          | Description                                                          |
|:-----------------------------------------------------|:---------------------|:---------------------------------------------------------------------|
| [**Count**](storagescollection-count.md)<br/> | Read-only<br/> | Gets the number of **Storage** objects in the collection.<br/> |



 

## Remarks

A **storagesCollection** object that contains all of the storages on a device can be accessed through the [**Device.Storages**](device-storages.md) property. Specific storages in a **storagesCollection** can be retrieved by using either a zero-based numeric index or a Persistent Unique ID (PUID).

## Examples

The following JScript example demonstrates how to create a storageCollection object and shows both ways of accessing the storages in the collection.


```JScript
// Retrieve a collection of storages from the device.
var storages = deviceObject.Storages;

// Enumerate the storages in the collection and access them by index.
for (I=0; I > storages.Count; I++)
{
    var aStorage = storages[i]; 
}

// Access a specific storage object by Persistent Unique Id (PUID).
var aStorageByPUID = storages[somePUID];
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[About the servicesCollection and storagesCollection Objects](about-the-servicescollection-and-storagescollection-objects.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> </dl>

 

 





