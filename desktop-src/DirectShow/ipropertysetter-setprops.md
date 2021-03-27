---
description: The SetProps method sets the properties of the target object to the appropriate state for the specified time.
ms.assetid: 65e701c9-d3a1-4396-9cba-a7830757701f
title: IPropertySetter::SetProps method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPropertySetter.SetProps
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IPropertySetter::SetProps method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetProps` method sets the properties of the target object to the appropriate state for the specified time.

## Syntax


```C++
HRESULT SetProps(
  [in] IUnknown       *pTarget,
  [in] REFERENCE_TIME rtNow
);
```



## Parameters

<dl> <dt>

*pTarget* \[in\]
</dt> <dd>

Pointer to the target object for which to set the properties.

</dd> <dt>

*rtNow* \[in\]
</dt> <dd>

Time at which to set the properties, in 100-nanosecond units, or –1 to set static properties (those that do not vary over time).

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is called by DES to set the properties on a transition or effect. An application will not normally call this method.

The object specified by *pTarget* must implement the **IDispatch** interface.

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

[**IPropertySetter Interface**](ipropertysetter.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




