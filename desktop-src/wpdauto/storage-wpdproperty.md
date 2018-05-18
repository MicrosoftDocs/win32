---
title: Storage.WpdProperty property
description: The WpdProperty property gets or sets a predefined WPD property on this Storage object.
ms.assetid: '4a92b41b-0478-47e2-bc22-5167b04d6a0a'
keywords: ["WpdProperty property WPD Automation", "WpdProperty property WPD Automation , Storage object", "Storage object WPD Automation , WpdProperty property"]
topic_type:
- apiref
api_name:
- Storage.WpdProperty
api_type:
- COM
---

# Storage.WpdProperty property

The ***WpdProperty*** property gets or sets a predefined WPD property on this **Storage** object.

This property is read/write.

## Syntax


```JScript
WpdProperty = Storage.WpdProperty
Storage.WpdProperty = WpdProperty
```



## Property value

The same value as the predefined WPD property that is being read from or written to.

## Remarks

The following table contains the minimum required set of predefined WPD properties for a **Storage Object**. The properties are accessed by the WPD Automation name that corresponds to the WPD PROPERTYKEY. For example, the WPD-defined property WPD\_OBJECT\_NAME, would be accessed like this: `storage.ObjectName`.

For a complete list of WPD PROPERTYKEYs and their corresponding WPD Automation names, see [**Names for WPD PROPERTYKEYs**](names-for-wpd-propertykeys.md).



| WPD PROPERTYKEY                     | WPD Automation Name      |
|-------------------------------------|--------------------------|
| WPD\_OBJECT\_ID                     | ObjectId                 |
| WPD\_OBJECT\_NAME                   | ObjectName               |
| WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID | ObjectPersistentUniqueId |
| WPD\_OBJECT\_FORMAT                 | ObjectFormat             |
| WPD\_FUNCTIONAL\_OBJECT\_CATEGORY   | FunctionalObjectCategory |
| WPD\_STORAGE\_TYPE                  | StorageType              |
| WPD\_STORAGE\_CAPACITY              | StorageCapacity          |



 

## Examples

The following JScript example demonstrates how to get and set predefined WPD properties on a storage.


```JScript
var storage = deviceObject.Storages[0];

// Retrieve a value from a predefined WPD property.
// Notice that the property is called by using the 
// WPD Automation Property Name.
var storageType = storage.StorageType;

// Set a predefined WPD property to a new value.
storage.ObjectName = "New Storage Name";
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Storage Object**](storage-object.md)
</dt> </dl>

 

 





