---
description: The IsCursorHidden method retrieves the current state of the m\_bCursorHidden data member.
ms.assetid: 4b97b89d-876a-470c-ac41-a88fecb52b2d
title: CBaseControlWindow.IsCursorHidden method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.IsCursorHidden
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.IsCursorHidden method

The `IsCursorHidden` method retrieves the current state of the **m\_bCursorHidden** data member.

## Syntax


```C++
HRESULT IsCursorHidden(
   long *CursorHidden
);
```



## Parameters

<dl> <dt>

*CursorHidden* 
</dt> <dd>

Pointer to the value of **m\_bCursorHidden**.

</dd> </dl>

## Return value

When called without a parameter, returns OATRUE if the cursor is hidden, or OAFALSE if the cursor is visible.

## Remarks

Internal objects should call this member function without the *CursorHidden* parameter to avoid locking the critical section. External objects access this member function with the *CursorHidden* parameter through the [**IVideoWindow::IsCursorHidden**](/windows/desktop/api/Control/nf-control-ivideowindow-iscursorhidden) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




