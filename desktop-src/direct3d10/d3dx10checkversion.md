---
Description: Verify that the version of D3DX you compiled with is the version that you are running.
ms.assetid: 57085b07-f77b-425e-a889-22c3071d7143
title: D3DX10CheckVersion function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10CheckVersion function

Verify that the version of D3DX you compiled with is the version that you are running.

## Syntax


```C++
HRESULT D3DX10CheckVersion(
  _In_ UINT D3DSdkVersion,
  _In_ UINT D3DX10SdkVersion
);
```



## Parameters

<dl> <dt>

*D3DSdkVersion* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Use D3D10\_SDK\_VERSION. See remarks.

</dd> <dt>

*D3DX10SdkVersion* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Use D3DX10\_SDK\_VERSION. See remarks.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the version doesn't match, the function will return FALSE (a number less than or equal to 0, the number itself has no meaning).

## Remarks

Use this function during the initialization of your application.


```
HRESULT hr;
    
if( FAILED( D3DX10CheckVersion(D3D10_SDK_VERSION, D3DX10_SDK_VERSION) ) )
    return E_FAIL;
```



## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




