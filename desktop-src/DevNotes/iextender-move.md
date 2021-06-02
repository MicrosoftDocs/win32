---
description: Moves an MDIForm, form, or control.
ms.assetid: 963e6533-f571-4043-bdd8-2596df6b5b35
title: IExtender::Move method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IExtender.Move
api_type: 
- COM
api_location: 
- Ole2disp.dll
- Oleaut32.dll
---

# IExtender::Move method

Moves an MDIForm, form, or control.

## Syntax


```C++
void Move(
  [in] object left,
  [in] object top,
  [in] object width,
  [in] object height
);
```



## Parameters

<dl> <dt>

*left* \[in\]
</dt> <dd>

The left edge of the form or control.

</dd> <dt>

*top* \[in\]
</dt> <dd>

The top edge of the form or control.

</dd> <dt>

*width* \[in\]
</dt> <dd>

The width of the form or control.

</dd> <dt>

*height* \[in\]
</dt> <dd>

The height of the form or control.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ole2disp.dll; </dt> <dt>Oleaut32.dll</dt> </dl> |



## See also

<dl> <dt>

[**IExtender**](iextender.md)
</dt> </dl>

 

 




