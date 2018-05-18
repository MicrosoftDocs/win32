---
title: Vector.Remove method
description: Removes the designated element.
ms.assetid: '635371bb-97a8-4b2c-af59-e835dc067881'
keywords: ["Remove method WIA Automation", "Remove method WIA Automation , Vector object", "Vector object WIA Automation , Remove method"]
topic_type:
- apiref
api_name:
- Vector.Remove
api_location:
- Wiaaut.h
api_type:
- COM
---

# Vector.Remove method

Removes the designated element.

## Syntax


```VB
pvResult = .Remove( _
  ByVal Index As LONG _
) As HRESULT
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **LONG**

Required. **Long** value.

</dd> </dl>

## Return value

Type: **VARIANT\***

Returns the designated element on success, otherwise returns **Nothing**.

## Remarks

For example code, see [Use a Vector Object](-wiaaut-shared-samples.md#use-a-vector-object) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Vector**](-wiaaut-vector.md)
</dt> </dl>

 

 





