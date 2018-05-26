---
title: MSFT\_StorageObject class
description: MSFT\_StorageObject is the base class for all storage object classes.
ms.assetid: 0B9FF9B2-98AE-49C7-AD19-501FE30DE723
keywords:
- MSFT_StorageObject class Windows Storage Management API
- MSFT_StorageObject class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageObject
- MSFT_StorageObject.ObjectId
- MSFT_StorageObject.UniqueId
- MSFT_StorageObject.PassThroughIds
- MSFT_StorageObject.PassThroughServer
- MSFT_StorageObject.PassThroughNamespace
- MSFT_StorageObject.PassThroughClass
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_StorageObject class

**MSFT\_StorageObject** is the base class for all storage object classes.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_StorageObject
{
  String ObjectId;
  String UniqueId;
  String PassThroughIds;
  String PassThroughServer;
  String PassThroughNamespace;
  String PassThroughClass;
};
```

## Members

The **MSFT\_StorageObject** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageObject** class has these properties.

<dl> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**ObjectId** is a mandatory property that is used to opaquely and uniquely identify an instance of a class. **ObjectId** values are required to be globally unique. That is, no two objects should ever have the same **ObjectId**, even if they are managed by separate storage management providers, or are on different storage subsystems.

The **ObjectId** is created and maintained for use of the Storage Management Providers and their clients to track instances of objects. If an object is visible through two different paths for example, if there are two separate storage management providers that point to the same storage subsystem then the same object may appear with two different **ObjectId** values. For determining if two object instances are the same object, refer to the **UniqueId** property.

</dd> <dt>

**PassThroughClass**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The WMI class name of the proprietary storage provider object.

</dd> <dt>

**PassThroughIds**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A comma-separated list of all implementation specific keys. This list is used by storage management applications to access the vendor proprietary object model. The list should be in the form: `key1='value1', key2='value2'`.

</dd> <dt>

**PassThroughNamespace**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The WMI namespace that contains the proprietary storage provider classes.

</dd> <dt>

**PassThroughServer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The computer that is hosting the proprietary storage provider classes.

</dd> <dt>

**UniqueId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**UniqueId** is a mandatory property that is used to uniquely identify a logical instance of a storage subsystem's object. This value must be the same for an object viewed by two or more provider instances, even if they are running on separate management servers. **UniqueId** can be any globally unique, opaque value, unless otherwise specified by a derived class.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





