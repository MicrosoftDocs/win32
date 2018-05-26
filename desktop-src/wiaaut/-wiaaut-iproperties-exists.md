---
title: Properties.Exists method
description: Indicates whether the specified Property exists in the collection.
ms.assetid: 242bcc6c-a4b3-4b12-857c-78c01ea597ce
keywords:
- Exists method WIA Automation
- Exists method WIA Automation , Properties object
- Properties object WIA Automation , Exists method
topic_type:
- apiref
api_name:
- Properties.Exists
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Properties.Exists method

Indicates whether the specified [**Property**](-wiaaut-property.md) exists in the collection.

## Syntax


```VB
pboolResult = .Exists( _
  ByVal Index As VARIANT _
) As HRESULT
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **VARIANT\***

Required. **Variant** value.

</dd> </dl>

## Return value

Type: **VARIANT\_BOOL\***

Returns **True** if the [**Property**](-wiaaut-property.md) exists in the collection.

## Remarks

For example code, see [Enumerate Root Level Items and Display Their Names](-wiaaut-shared-samples.md#enumerate-root-level-items-and-display-their-names) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Properties**](-wiaaut-properties.md)
</dt> </dl>

 

 





