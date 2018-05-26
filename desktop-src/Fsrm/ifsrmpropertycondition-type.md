---
title: IFsrmPropertyCondition Type property
description: The comparison operator used to determine whether the property condition is met.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2cec0753-20ec-4df4-9a74-c65bfed28070
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Type property File Server Resource Manager
- Type property File Server Resource Manager , IFsrmPropertyCondition interface
- IFsrmPropertyCondition interface File Server Resource Manager , Type property
topic_type:
- apiref
api_name:
- IFsrmPropertyCondition.Type
- IFsrmPropertyCondition.get_Type
- IFsrmPropertyCondition.put_Type
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IFsrmPropertyCondition::Type property

The comparison operator used to determine whether the property condition is met.

This property is read/write.

## Syntax


```C++
HRESULT put_Type(
  [in]  FsrmPropertyConditionType type
);

HRESULT get_Type(
  [out] FsrmPropertyConditionType *pType
);
```



## Property value

The comparison operator used to compare the value of the specified classification property in the file to the property condition's value. For possible values, see the [**FsrmPropertyConditionType**](/windows/previous-versions/Fsrm/ne-fsrmenums-_fsrmpropertyconditiontype?branch=master) enumeration.

## Error codes

The method returns the following return values.

<dl> <dt>

S\_OK
</dt> <dd>

Success

</dd> <dt>

E\_INVALIDARG
</dt> <dd>

The type is not a valid value.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                         |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |
| IID<br/>                      | IID\_IFsrmPropertyCondition is defined as 326af66f-2ac0-4f68-bf8c-4759f054fa29<br/> |



## See also

<dl> <dt>

[**IFsrmPropertyCondition**](/windows/previous-versions/Fsrm/nn-fsrmreports-ifsrmpropertycondition?branch=master)
</dt> </dl>

 

 





