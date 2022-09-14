---
description: The SetPropertySetter method sets the object's property setter. When the object is rendered, the property information contained in the property setter is applied to the object. Call this method on transition and effect objects.
ms.assetid: 3ce2fe50-a884-4da4-95b5-9c97e188f819
title: IAMTimelineObj::SetPropertySetter method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.SetPropertySetter
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::SetPropertySetter method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetPropertySetter` method sets the object's property setter. When the object is rendered, the property information contained in the property setter is applied to the object. Call this method on transition and effect objects.

## Syntax


```C++
HRESULT SetPropertySetter(
   IPropertySetter *newVal
);
```



## Parameters

<dl> <dt>

*newVal* 
</dt> <dd>

Pointer to the property setter's [**IPropertySetter**](ipropertysetter.md) interface.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineObj Interface**](iamtimelineobj.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




