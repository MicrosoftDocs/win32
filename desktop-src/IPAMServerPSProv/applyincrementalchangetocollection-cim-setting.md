---
Description: Applies the subset of the properties in the setting to a collection of managed system elements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7994165a-80cf-4cb0-b1c6-c86c4622cfa7
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: ApplyIncrementalChangeToCollection method of the CIM\_Setting class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ApplyIncrementalChangeToCollection method of the CIM\_Setting class

Applies the subset of the properties in the setting to a collection of managed system elements.

## Syntax


```mof
uint32 ApplyIncrementalChangeToCollection(
  [in]  CIM_CollectionOfMSEs REF Collection,
  [in]  datetime                 TimeToApply,
  [in]  boolean                  ContinueOnError,
  [in]  datetime                 MustBeCompletedBy,
  [in]  string                   PropertiesToApply[],
  [out] string                   CanNotApply[]
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the collection of managed system elements that receives the setting.

</dd> <dt>

*TimeToApply* \[in\]
</dt> <dd>

The time or time interval to verify with the setting.

</dd> <dt>

*ContinueOnError* \[in\]
</dt> <dd>

**True** to continue applying the setting to the collection after the method fails to apply the setting to an element in the collection; Otherwise, **false**.

> [!Note]  
> For each failed application of the setting, the corresponding managed system element is added to the **CanNotApply** array.

 

</dd> <dt>

*MustBeCompletedBy* \[in\]
</dt> <dd>

The required completion time for the method.

</dd> <dt>

*PropertiesToApply* \[in\]
</dt> <dd>

An array that contains the property names of the setting.

</dd> <dt>

*CanNotApply* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array of keys to the managed system elements that can not receive the setting.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>


</dt> <dd>

0

The setting was successfully applied to the collection.

</dd> <dt>


</dt> <dd>

1

The method is not supported.

</dd> <dt>


</dt> <dd>

2

The setting was not applied by the specified time.

</dd> <dt>


</dt> <dd>

3

There was an error using the **ContinueOnError** property value.

</dd> <dt>


</dt> <dd>

4 ...

Any other error.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> </dl>

 

 




