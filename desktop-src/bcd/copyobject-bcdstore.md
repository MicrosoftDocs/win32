---
title: CopyObject method of the BcdStore class
description: Copies the specified object from another store.
ms.assetid: '398dbf15-aeec-4984-8fde-6231b230c589'
keywords: ["CopyObject method Boot Config", "CopyObject method Boot Config , BcdStore class", "BcdStore class Boot Config , CopyObject method"]
topic_type:
- apiref
api_name:
- BcdStore.CopyObject
api_location:
- Root\WMI
api_type:
- COM
---

# CopyObject method of the BcdStore class

Copies the specified object from another store.

## Syntax


```mof
boolean CopyObject(
  [in]  string    SourceStoreFile,
  [in]  string    SourceId,
  [in]  uint32    Flags,
  [out] BcdObject Object
);
```



## Parameters

<dl> <dt>

*SourceStoreFile* \[in\]
</dt> <dd>

The full path to the store that contains the object to copy. If this parameter is an empty string (""), the method uses the system store.

</dd> <dt>

*SourceId* \[in\]
</dt> <dd>

The object identifier of the object to copy. This is a GUID in string form, surrounded by curly braces.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

This parameter can be neither, one, or both of the following values.



| Value                                                                                                                                                                                                                                                                             | Meaning                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CreateNewId"></span><span id="createnewid"></span><span id="CREATENEWID"></span><dl> <dt>**CreateNewId**</dt> <dt>0x1</dt> </dl>                                     | Creates a new object identifier for the object coped to the target store. If CreateNewId is not set, the object identifier from the source store is used.<br/>                                         |
| <span id="DeleteExistingObject"></span><span id="deleteexistingobject"></span><span id="DELETEEXISTINGOBJECT"></span><dl> <dt>**DeleteExistingObject**</dt> <dt>0x2</dt> </dl> | Deletes the existing object from the target store before copying the object from the source store. If DeleteExistingObject is not set, the existing object is not deleted from the target store. <br/> |



 

</dd> <dt>

*Object* \[out\]
</dt> <dd>

A Bcdobject instance that represents the copied object in the target store.

</dd> </dl>

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdStore**](bcdstore.md)
</dt> </dl>

 

 





