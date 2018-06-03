---
Description: The AddProp method adds a property to the property setter, with an array of time-value pairs defining the value of the property over a range of time.
ms.assetid: bf49e6ed-110d-4851-ace9-04d025f1d21f
title: IPropertySetter::AddProp method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPropertySetter::AddProp method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `AddProp` method adds a property to the property setter, with an array of time-value pairs defining the value of the property over a range of time.

## Syntax


```C++
HRESULT AddProp(
  [in] DEXTER_PARAM Param,
  [in] DEXTER_VALUE *paValue
);
```



## Parameters

<dl> <dt>

*Param* \[in\]
</dt> <dd>

[**DEXTER\_PARAM**](dexter-param.md) structure that specifies the property. The **nValues** member of the structure must equal the size of the array given in the *paValue* parameter.

</dd> <dt>

*paValue* \[in\]
</dt> <dd>

Pointer to an array of [**DEXTER\_VALUE**](dexter-value.md) structures that contain time-value pairs. The array must be in ascending time order. The times are relative to the starting time of the effect or transition.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The first [**DEXTER\_VALUE**](dexter-value.md) structure must specify a reference time of zero and an interpolation flag (**dwInterp**) of **DEXTERF\_JUMP**, or the method returns an error.

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

 

 




