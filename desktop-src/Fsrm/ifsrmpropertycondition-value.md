---
title: IFsrmPropertyCondition Value property
description: The property condition's value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '51316f3b-ca69-4e0c-936c-8cafc0e2b1b7'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["Value property File Server Resource Manager", "Value property File Server Resource Manager , IFsrmPropertyCondition interface", "IFsrmPropertyCondition interface File Server Resource Manager , Value property"]
topic_type:
- apiref
api_name:
- IFsrmPropertyCondition.Value
- IFsrmPropertyCondition.get_Value
- IFsrmPropertyCondition.put_Value
api_location:
- SrmSvc.dll
api_type:
- COM
---

# IFsrmPropertyCondition::Value property

The property condition's value.

This property is read/write.

## Syntax


```C++
HRESULT put_Value(
  [in]  BSTR value
);

HRESULT get_Value(
  [out] BSTR *pValue
);
```



## Property value

The property condition's value.

## Error codes

The method returns the following return values.

<dl> <dt>

S\_OK
</dt> <dd>

Success

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                         |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |
| IID<br/>                      | IID\_IFsrmPropertyCondition is defined as 326af66f-2ac0-4f68-bf8c-4759f054fa29<br/> |



## See also

<dl> <dt>

[**IFsrmPropertyCondition**](ifsrmpropertycondition.md)
</dt> </dl>

 

 





