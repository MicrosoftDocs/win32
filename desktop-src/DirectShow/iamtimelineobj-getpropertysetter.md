---
description: The GetPropertySetter method retrieves the object's property setter. When the object is rendered, the property information contained in the property setter is applied to the object.
ms.assetid: 7a9c5ee4-2df6-4eaa-a583-5efea0cf7bde
title: IAMTimelineObj::GetPropertySetter method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.GetPropertySetter
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::GetPropertySetter method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetPropertySetter` method retrieves the object's property setter. When the object is rendered, the property information contained in the property setter is applied to the object.

## Syntax


```C++
HRESULT GetPropertySetter(
  [out, retval] IPropertySetter **pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives a pointer to the property setter's [**IPropertySetter**](ipropertysetter.md) interface. If the object does not have a property setter, the value is set to **NULL**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the value returned in *pVal* is not **NULL**, the **IPropertySetter** interface has an outstanding reference count. Be sure to release the interface when you are finished using it.

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

 

 




