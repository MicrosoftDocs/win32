---
title: Vector.Add method
description: Inserts a new element into the Vector collection before the specified Index if Index is not 0. If Index is 0, this method appends a new element to the Vector collection.
ms.assetid: 'b9fe8dc2-e834-4fd0-9bea-cf54a5c5d4d7'
keywords: ["Add method WIA Automation", "Add method WIA Automation , Vector object", "Vector object WIA Automation , Add method"]
topic_type:
- apiref
api_name:
- Vector.Add
api_location:
- Wiaaut.h
api_type:
- COM
---

# Vector.Add method

Inserts a new element into the [**Vector**](-wiaaut-vector.md) collection before the specified *Index* if *Index* is not 0. If *Index* is 0, this method appends a new element to the **Vector** collection.

## Syntax


```VB
Vector.Add( _
  ByVal Value As VARIANT, _
  [ ByVal Index As LONG ] _
) As HRESULT
```



## Parameters

<dl> <dt>

*Value* \[in\]
</dt> <dd>

Type: **VARIANT\***

Required. **Variant** value.

</dd> <dt>

*Index* \[in, optional\]
</dt> <dd>

Type: **LONG**

**Long** value.



| Value                                                                                                                              | Meaning              |
|------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| <dl> <dt></dt> <dt>0</dt> </dl> | Default. <br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For example code, see [Create an ImageFile Object that Contains a Blank Page](-wiaaut-shared-samples.md#create-an-imagefile-object-that-contains-a-blank-page) in Shared Samples.

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

 

 





