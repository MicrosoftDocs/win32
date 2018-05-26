---
Description: The FreeProps method frees resources allocated by the IPropertySetterGetProps method. Call this method after calling GetProps, passing it the structures returned by GetProps.
ms.assetid: 5920d63d-d8eb-4fd5-b0d6-9d175e8e2c86
title: IPropertySetterFreeProps method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPropertySetter::FreeProps method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `FreeProps` method frees resources allocated by the [**IPropertySetter::GetProps**](ipropertysetter-getprops.md) method. Call this method after calling **GetProps**, passing it the structures returned by **GetProps**.

## Syntax


```C++
void FreeProps(
  [in] LONG         cParams,
  [in] DEXTER_PARAM *paParam,
  [in] DEXTER_VALUE *paValue
);
```



## Parameters

<dl> <dt>

*cParams* \[in\]
</dt> <dd>

The number of elements in the *paParam* array.

</dd> <dt>

*paParam* \[in\]
</dt> <dd>

Pointer to an array of [**DEXTER\_PARAM**](dexter-param.md) structures.

</dd> <dt>

*paValue* \[in\]
</dt> <dd>

Pointer to an array of [**DEXTER\_VALUE**](dexter-value.md) structures.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPropertySetter Interface**](ipropertysetter.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




