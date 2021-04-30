---
description: A union view class is a logical union of source class instances. A union view class includes all the instances of the source classes unless you limit the instances by including a WHERE clause on the source query.
ms.assetid: 54a9804d-644d-4ab6-a3d5-c9c4f7761967
ms.tgt_platform: multiple
title: Creating a Union View Class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Creating a Union View Class

A union view class is a logical union of source class instances. A union view class includes all the instances of the source classes unless you limit the instances by including a WHERE clause on the source query.

Union view classes are useful when you want to see instances of similar or identical classes that are located in different namespaces or on different computers. For example, you can create a union class that contains instances of different disk drives to monitor.

You can also base the properties of a union view class on properties not present in all of the source class instances. If the source class instances do not have the same property, the properties of union class instances have a value of **NULL**. For example, if one hard disk drive has a **temperature** property but another does not, you can still create a union between the two.

The following procedure describes how to create a union view class.

**To create a union view class**

1.  Begin your class definition with the [**Union**](qualifiers-specific-to-the-view-provider.md) string qualifier.

    The [**JoinOn**](qualifiers-specific-to-the-view-provider.md), **Association**, and **Union** qualifiers are mutually exclusive.

2.  Create the queries that define source classes used in the view class with the [**ViewSources**](viewsources-qualifier.md) qualifier.
3.  Define the names and location of the namespaces in which the source classes are located with the [**ViewSpaces**](viewspaces-qualifier.md) qualifier.
4.  Define the properties that map to the properties in the source classes with the [**PropertySources**](propertysources-qualifier.md) qualifier.

    If necessary, you can tag any of the properties as belonging to a source class by using the [**HiddenDefault**](qualifiers-specific-to-the-view-provider.md) qualifier.

5.  Define the key properties of the source classes of your union view class.

    Each source class must have the same number of key properties matched by [**CIMType**](swbemproperty-cimtype.md). Also, the keys of your union view class must uniquely identify all source instances. In some cases, you might need to specify system properties to ensure that instances are unique. For example, if you create a view from the union of two identical classes in two different namespaces, you could include the [**\_\_Namespace**](--namespace.md) property as a key in the view class to differentiate between the two instances. If you use two similar classes from the same namespace to create a view, you could use the **\_\_Class** property to distinguish between the two. Rename any system properties in the view so you can avoid a conflict with the system properties of the view class.

6.  Define any methods you want using the [**MethodSource**](qualifiers-specific-to-the-view-provider.md) qualifier.

    Unlike other view classes, you can create methods to modify a union view.

The following code example describes a union view class.

``` syntax
[Union, ViewSources{"SELECT Description, DeviceID, __Namespace, FileSystem, FreeSpace, VolumeName FROM LocalDisk", 
    "SELECT Description, DeviceID, __Namespace, FileSystem, FreeSpace, VolumeName FROM RemoteDisk"}, 
    ViewSpaces{"\\\\.\\Root\\LocalNamespace","\\\\.\\Root\\RemoteNamespace"}, 
    dynamic: ToInstance, provider("MS_VIEW_INSTANCE_PROVIDER")]

class UnionOfDrives

{
    [PropertySources{"Description", "Description"}] string des;
    [PropertySources{"DeviceID", "DeviceID"}, key] String did;
    [PropertySources{"__Namespace", "__Namespace"}, key] String KEYID;
    [PropertySources{"FileSystem", "FileSystem"}] String fsystem ;
    [PropertySources{"FreeSpace", "FreeSpace"}] uint64 fspace;
    [PropertySources{"VolumeName", "VolumeName"}] String vname;
};
```

 

 



