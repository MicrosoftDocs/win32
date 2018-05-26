---
Description: Verify that the version of D3DX you compiled with is the version that you are running.
ms.assetid: a4e745dd-d573-4e8f-9516-f6a7475f5cc5
title: D3DXCheckVersion function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXCheckVersion function

Verify that the version of D3DX you compiled with is the version that you are running.

## Syntax


```C++
BOOL D3DXCheckVersion(
  _In_ UINT D3DSDKVersion,
  _In_ UINT D3DXSDKVersion
);
```



## Parameters

<dl> <dt>

*D3DSDKVersion* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Use D3D\_SDK\_VERSION. See remarks.

</dd> <dt>

*D3DXSDKVersion* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Use D3DX\_SDK\_VERSION. See remarks.

</dd> </dl>

## Return value

Type: **[**BOOL**](winprog.windows_data_types)**

Returns **TRUE** if the version of D3DX you compiled against is the version you are running with; otherwise, **FALSE** is returned.

## Remarks

Use this function during the initialization of your application like this:


```
HRESULT CD3DXMyApplication::Initialize(HINSTANCE hInstance, 
  LPCSTR szWindowName, LPCSTR szClassName, UINT uWidth, UINT uHeight)
{
    HRESULT hr;
    
    if (!D3DXCheckVersion(D3D_SDK_VERSION, D3DX_SDK_VERSION))
        return E_FAIL;
    
    ...
}
```



Use [**Direct3DCreate9**](/windows/win32/d3d9helper/nf-d3d9-direct3dcreate9?branch=master) to verify that the correct runtime is installed.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[General Purpose Functions](dx9-graphics-reference-d3dx-functions-general-purpose.md)
</dt> </dl>

 

 




