---
title: KeyValueCompareAndSet method of the Win32_RDSHCollection class
description: Compares the specified key in the collection with a comparand; if they match, the key is set to a new value. If the key does not exist, the method will insert the key into the collection.
ms.assetid: ea6195b3-1a20-4d5b-b9a3-796976818b4f
ms.tgt_platform: multiple
keywords:
- KeyValueCompareAndSet method Remote Desktop Services
- KeyValueCompareAndSet method Remote Desktop Services , Win32_RDSHCollection class
- Win32_RDSHCollection class Remote Desktop Services , KeyValueCompareAndSet method
topic_type:
- apiref
api_name:
- Win32_RDSHCollection.KeyValueCompareAndSet
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# KeyValueCompareAndSet method of the Win32\_RDSHCollection class

Compares the specified key in the collection with a comparand; if they match, the key is set to a new value. If the key does not exist, the method will insert the key into the collection.

## Syntax


```mof
uint32 KeyValueCompareAndSet(
  [in]  string Key,
  [in]  string NewValue,
  [in]  string Comparand,
  [out] string InitialValue
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

The key to compare.

</dd> <dt>

*NewValue* \[in\]
</dt> <dd>

The new value.

</dd> <dt>

*Comparand* \[in\]
</dt> <dd>

The string to compare the key to.

</dd> <dt>

*InitialValue* \[out\]
</dt> <dd>

On success or failure, contains the initial value of the key.

</dd> </dl>

## Remarks

Note that this method can retrieve the value of the key, and as such encapsulates the functionality of [**KeyValueGet**](win32-rdshcollection-keyvalueget.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDSHCollection**](win32-rdshcollection.md)
</dt> </dl>

 

 





