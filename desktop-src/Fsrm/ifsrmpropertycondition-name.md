---
title: IFsrmPropertyCondition Name property
description: The name of the classification property whose value you want to compare to the property conditions value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 45efc964-9632-434a-a4ae-93a65fcb2951
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Name property File Server Resource Manager
- Name property File Server Resource Manager , IFsrmPropertyCondition interface
- IFsrmPropertyCondition interface File Server Resource Manager , Name property
topic_type:
- apiref
api_name:
- IFsrmPropertyCondition.Name
- IFsrmPropertyCondition.get_Name
- IFsrmPropertyCondition.put_Name
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IFsrmPropertyCondition::Name property

The name of the classification property whose value you want to compare to the property condition's value.

This property is read/write.

## Syntax


```C++
HRESULT put_Name(
  [in]  BSTR name
);

HRESULT get_Name(
  [out] BSTR *pName
);
```



## Property value

The name of the classification property.

## Error codes

The method returns the following return values.

<dl> <dt>

S\_OK
</dt> <dd>

Success

</dd> <dt>

E\_INVALIDARG
</dt> <dd>

The name is not a valid name for a property value.

</dd> <dt>

FSRM\_E\_NOT\_FOUND
</dt> <dd>

The name is not an existing property definition.

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

 

 





