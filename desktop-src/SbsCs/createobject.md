---
description: The CreateObject method of the Microsoft.Windows.ActCtx object creates an object in the context of the current manifest.
ms.assetid: 531e6501-bb68-472b-b483-1f52815ba9d7
title: ActCtx.CreateObject method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ActCtx.CreateObject
api_type: 
- COM
api_location: 
- Sxsoa.dll
---

# ActCtx.CreateObject method

The **CreateObject** method of the [**Microsoft.Windows.ActCtx**](microsoft-windows-actctx-object.md) object creates an object in the context of the current manifest.

## Syntax


```JScript
ActCtx.CreateObject(
  objectId
)
```



## Parameters

<dl> <dt>

*objectId* 
</dt> <dd>

A string that specifies the type of object to create. For example, a COM ProgID.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Sxsoa.dll</dt> </dl> |
| IID<br/>                      | IID\_IActCtx is defined as 8FA7728F-B69B-4EE5-99F2-E2AA021BEF28<br/>           |



## See also

<dl> <dt>

[**GetObject Method**](getobject.md)
</dt> </dl>

 

 




