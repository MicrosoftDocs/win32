---
title: CopyObjects method of the BcdStore class
description: Copies the objects of the specified type from another store.
ms.assetid: '67b9222f-f9e6-4161-8e98-0d713e8028f1'
keywords: ["CopyObjects method Boot Config", "CopyObjects method Boot Config , BcdStore class", "BcdStore class Boot Config , CopyObjects method"]
topic_type:
- apiref
api_name:
- BcdStore.CopyObjects
api_location:
- Root\WMI
api_type:
- COM
---

# CopyObjects method of the BcdStore class

Copies the objects of the specified type from another store.

## Syntax


```mof
boolean CopyObjects(
  [in] string SourceStoreFile,
  [in] uint32 Type,
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*SourceStoreFile* \[in\]
</dt> <dd>

The full path to the source store. If this parameter is an empty string (""), the method uses the system store.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of object to copy. For more information, see the **Type** property of the [**BCDObject**](bcdobject.md) class.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

This parameter can be set with neither, one, or both of the following values.



| Value                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CreateNewId"></span><span id="createnewid"></span><span id="CREATENEWID"></span><dl> <dt>**CreateNewId**</dt> </dl>                                     | Creates a new object identifier. If CreateNewId is not set, the object identifier from the source store is used.<br/>                                                                                  |
| <span id="DeleteExistingObject"></span><span id="deleteexistingobject"></span><span id="DELETEEXISTINGOBJECT"></span><dl> <dt>**DeleteExistingObject**</dt> </dl> | Deletes the existing object from the target store before copying the object from the source store. If DeleteExistingObject is not set, the existing object is not deleted from the target store. <br/> |



 

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

 

 





