---
description: The GetObject method gets an instance of an existing Microsoft.Windows.ActCtx object.
ms.assetid: 547525f3-afef-463b-823a-df8ccd954f36
title: ActCtx.GetObject method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ActCtx.GetObject
api_type: 
- COM
api_location: 
- Sxsoa.dll
---

# ActCtx.GetObject method

The **GetObject** method gets an instance of an existing [**Microsoft.Windows.ActCtx**](microsoft-windows-actctx-object.md) object.

## Syntax


```JScript
ActCtx.GetObject(
  bstrName
)
```



## Parameters

<dl> <dt>

*bstrName* 
</dt> <dd>

Required string that indicates the object. The name must be in the registry under **HKEY\_LOCAL\_MACHINE**\\**Microsoft**\\**Visual Studio**\\**6.0**\\**<package>**\\**Automation**.

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

[**CreateObject Method**](createobject.md)
</dt> </dl>

 

 




