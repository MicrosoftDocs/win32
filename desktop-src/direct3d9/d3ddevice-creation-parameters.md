---
Description: 'Describes the creation parameters for a device.'
ms.assetid: '7db5ef2b-6894-4113-b726-8b238bb4fb2f'
title: 'D3DDEVICE\_CREATION\_PARAMETERS structure'
---

# D3DDEVICE\_CREATION\_PARAMETERS structure

Describes the creation parameters for a device.

## Syntax


```C++
typedef struct D3DDEVICE_CREATION_PARAMETERS {
  UINT       AdapterOrdinal;
  D3DDEVTYPE DeviceType;
  HWND       hFocusWindow;
  DWORD      BehaviorFlags;
} D3DDEVICE_CREATION_PARAMETERS, *LPD3DDEVICE_CREATION_PARAMETERS;
```



## Members

<dl> <dt>

**AdapterOrdinal**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Ordinal number that denotes the display adapter. D3DADAPTER\_DEFAULT is always the primary display adapter. Use this ordinal as the Adapter parameter for any of the [**IDirect3D9**](idirect3d9.md) methods. Note that different instances of Direct3D 9.0 objects can use different ordinals. Adapters can enter or leave a system when users, for example, add or remove monitors from a multiple-monitor system or when they hot-swap a laptop. Consequently, use this ordinal only in a Direct3D 9.0 instance known to be valid, that is, either the Direct3D 9.0 that created this [**IDirect3DDevice9**](idirect3ddevice9.md) interface or the Direct3D 9.0 returned from [**GetDirect3D**](idirect3ddevice9--getdirect3d.md), as called through this **IDirect3DDevice9** interface.

</dd> <dt>

**DeviceType**
</dt> <dd>

Type: **[**D3DDEVTYPE**](direct3d9.d3ddevtype)**

</dd> <dd>

Member of the [**D3DDEVTYPE**](direct3d9.d3ddevtype) enumerated type. Denotes the amount of emulated functionality for this device. The value of this parameter mirrors the value passed to the [**CreateDevice**](idirect3d9--createdevice.md) call that created this device.

</dd> <dt>

**hFocusWindow**
</dt> <dd>

Type: **[**HWND**](winprog.windows_data_types)**

</dd> <dd>

Window handle to which focus belongs for this Direct3D device. The value of this parameter mirrors the value passed to the [**CreateDevice**](idirect3d9--createdevice.md) call that created this device.

</dd> <dt>

**BehaviorFlags**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

A combination of one or more [D3DCREATE](d3dcreate.md) constants that control global behavior of the device. These constants mirror the constants passed to [**CreateDevice**](idirect3d9--createdevice.md) when the device was created.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetCreationParameters**](idirect3ddevice9--getcreationparameters.md)
</dt> <dt>

[**CreateDevice**](idirect3d9--createdevice.md)
</dt> </dl>

 

 




