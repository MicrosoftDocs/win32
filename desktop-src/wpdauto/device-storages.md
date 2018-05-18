---
title: Device.Storages property
description: The Storages property provides read-only access to a collection of all the legacy storages on the device.
ms.assetid: '6d2d78be-c823-4e2a-9bab-f485dec65724'
keywords: ["Storages property WPD Automation", "Storages property WPD Automation , Device object", "Device object WPD Automation , Storages property"]
topic_type:
- apiref
api_name:
- Device.Storages
api_type:
- COM
---

# Device.Storages property

The **Storages** property provides read-only access to a collection of all the legacy storages on the device.

This property is read-only.

## Syntax


```JScript
Storages = Device.Storages
```



## Property value

Read-only **storagesCollection** object.

## Remarks

The **storagesCollection** returned by the **Storages** property can be accessed in three ways: by using a zero-based index, by using a Storage Persistent Unique ID (PUID), and by using an Object Identifier (ObjectId).

The following code shows a **storagesCollection** accessed by using a zero-based numeric index.


```JScript
var storage = deviceObject.Storages[0];
```



If the numeric index value is greater than or equal to the value returned by [**storagesCollection.Count**](servicescollection-count.md), a JScript exception will be thrown.

In the following code, a Storage PUID is used to access the **storagesCollection**.


```JScript
var storage = deviceObject.Storages[storagePUID];
```



The Storage PUID for a specific storage can be obtained by using the WPD Automation name **ObjectPersistentUniqueID** that corresponds to the WPD PROPERTYKEY **WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID**; as in the following example:


```JScript
var storagePUID = storage.ObjectPersistentUniqueID;
```



For a complete list of WPD PROPERTYKEYs and their corresponding WPD Automation names, see [**Names for WPD PROPERTYKEYs**](names-for-wpd-propertykeys.md).

The ObjectId of a specific storage can be obtained by using the WPD Automation name **ObjectId** that corresponds to the WPD PROPERTYKEY **WPD\_OBJECT\_ID**; as in the following example:


```JScript
var storageObjectId = storage.ObjectId;
```



For a complete list of WPD PROPERTYKEYs and their corresponding WPD Automation names, see [**Names for WPD PROPERTYKEYs**](names-for-wpd-propertykeys.md).

## Examples

The following JScript example uses the **Storages** property to access the collection of all storages on a **Device** object and then shows retrieving a storage from the collection by using a numeric index, a Storage PUID, and by using an ObjectId.


```JScript
// The storage object storageByIndex is obtained using
// the index value 0.
var storageByIndex = deviceObject.Storages[0];

// The Storage PUID of storageByIndex is read using the 
// ObjectPersistentUniqueID property.  
var storagePUID = storageByIndex.ObjectPersistentUniqueID;

// The storage object storageByPUID, which is identical to the
// storageByIndex object, is obtained by using the Storage PUID
// of storageByIndex. 
var storageByPUID = deviceObject.Storages[storagePUID];

// The ObjectId of storageByIndex is read using the ObjectID
// property.
var storageObjectId = storageByIndex.ObjectId;

// The storage object storageByObjectId, which is identical to
// the storageByIndex object, is obtained by using the ObjectId
// of storageByIndex.
var storageByObjectId = deviceObject.Storages[storageObjectId];
```



The following JScript example uses the **Storages** property to obtain a collection of all the storages on a device, and then enumerates them.


```JScript
var storages = deviceObject.Storages;

for (i=0; i < storages.Count; i++)
{
    var aStorage = storages[i];
}
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**storagesCollection Object**](storagescollection-object.md)
</dt> </dl>

 

 





