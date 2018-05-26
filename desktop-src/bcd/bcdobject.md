---
title: BcdObject class
description: Represents a BCD object that contains a collection of BCD elements. Each BCD object is identified by a GUID.
ms.assetid: d24c1a74-16e2-48db-aa07-70d2c15a2061
keywords:
- BcdObject class Boot Config
- BcdObject class Boot Config , described
topic_type:
- apiref
api_name:
- BcdObject
- BcdObject.StoreFilePath
- BcdObject.Id
- BcdObject.Type
api_location:
- Root\WMI
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BcdObject class

Represents a BCD object that contains a collection of BCD elements. Each BCD object is identified by a **GUID**.

## Syntax

``` syntax
class BcdObject
{
  string StoreFilePath;
  string Id;
  uint32 Type;
};
```

## Members

The **BcdObject** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **BcdObject** class has these methods.



| Method                                                                                     | Description                                                                   |
|:-------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| [**DeleteElement**](deleteelement-bcdobject.md)                                           | Deletes the specified element.<br/>                                     |
| [**EnumerateElements**](enumerateelements-bcdobject.md)                                   | Enumerates the elements in the object.<br/>                             |
| [**EnumerateElementTypes**](enumerateelementtypes-bcdobject.md)                           | Enumerates the types of elements in the object.<br/>                    |
| [**GetElement**](getelement-bcdobject.md)                                                 | Gets the specified element.<br/>                                        |
| [**GetElementWithFlags**](getelementwithflags-bcdobject.md)                               | Enumerates a qualified boot partition.<br/>                             |
| [**SetBooleanElement**](setbooleanelement-bcdobject.md)                                   | Sets the specified Boolean element.<br/>                                |
| [**SetDeviceElement**](setdeviceelement-bcdobject.md)                                     | Sets the specified device element.<br/>                                 |
| [**SetFileDeviceElement**](setfiledeviceelement-bcdobject.md)                             | Sets the specified file device element.<br/>                            |
| [**SetIntegerElement**](setintegerelement-bcdobject.md)                                   | Sets the specified integer element.<br/>                                |
| [**SetIntegerListElement**](setintegerlistelement-bcdobject.md)                           | Sets the specified integer list element.<br/>                           |
| [**SetObjectElement**](setobjectelement-bcdobject.md)                                     | Sets the specified object element.<br/>                                 |
| [**SetObjectListElement**](setobjectlistelement-bcdobject.md)                             | Sets the specified object list element.<br/>                            |
| [**SetPartitionDeviceElement**](setpartitiondeviceelement-bcdobject.md)                   | Sets the specified partition device element.<br/>                       |
| [**SetPartitionDeviceElementWithFlags**](setpartitiondeviceelementwithflags-bcdobject.md) | Sets the specified partition device element with additional flags.<br/> |
| [**SetQualifiedPartitionDeviceElement**](setqualifiedpartitiondeviceelement-bcdobject.md) | Sets the specified qualified partition device element.<br/>             |
| [**SetStringElement**](setstringelement-bcdobject.md)                                     | Sets the specified string element.<br/>                                 |
| [**SetVhdDeviceElement**](setvhddeviceelement-bcdobject.md)                               | Sets the specified virtual hard disk (VHD) device element.<br/>         |



 

### Properties

The **BcdObject** class has these properties.

<dl> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The **GUID** of this object, unique to this store, in string form.

</dd> <dt>

**StoreFilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The full path to the store. If this parameter is an empty string (""), the method uses the system store.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The object type. The upper 4 bits represent the object type. The meaning of the lower 28 bits varies with object type.

-   **BCD\_OBJECT\_TYPE\_APPLICATION** (0x1*rtaaaaa*) is an object type for a boot environment application, functional usage of the application and the image type. The next four bits (24-27) are reserved, and the following four bits (20-23) specify the type of image (0x1=Firmware, 0x2=Boot, 0x3=Legacy Loader, 0x4=Real Mode code). The lowest 20 bits define the application type (0x1=Firmware boot manager, 0x2=Windows boot manager, 0x3=Windows boot loader, 0x4=Windows resume application, 0x5=Memory tester, 0x6=Legacy NtLdr, 0x7=Legacy SetupLdr, 0x8=Boot sector, 0x9=Startup module, 0xa=Generic application.)
-   **BCD\_OBJECT\_TYPE\_INHERITED** (0x2*nnnnnnn*) describes a set of data elements which can be inherited from a BCD object for a boot application or from another inheritable object.

</dd> </dl>

## Remarks

To retrieve an object instance, use one of the following static methods of the [**BcdStore**](bcdstore.md) class: [**CreateStore**](createstore-bcdstore.md), [**OpenStore**](openstore-bcdstore.md), or [**ImportStore**](importstore-bcdstore.md).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



 

 





