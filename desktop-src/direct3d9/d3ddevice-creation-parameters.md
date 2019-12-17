---
Description: Describes the creation parameters for a device.
ms.assetid: 7db5ef2b-6894-4113-b726-8b238bb4fb2f
title: D3DDEVICE_CREATION_PARAMETERS structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DDEVICE_CREATION_PARAMETERS
api_type:
- HeaderDef
api_location:
- D3D9Types.h
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

Type: **[**UINT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Ordinal number that denotes the display adapter. D3DADAPTER\_DEFAULT is always the primary display adapter. Use this ordinal as the Adapter parameter for any of the [**IDirect3D9**](/windows/desktop/api) methods. Note that different instances of Direct3D 9.0 objects can use different ordinals. Adapters can enter or leave a system when users, for example, add or remove monitors from a multiple-monitor system or when they hot-swap a laptop. Consequently, use this ordinal only in a Direct3D 9.0 instance known to be valid, that is, either the Direct3D 9.0 that created this [**IDirect3DDevice9**](/windows/desktop/api) interface or the Direct3D 9.0 returned from [**GetDirect3D**](https://msdn.microsoft.com/library/Bb174386(v=VS.85).aspx), as called through this **IDirect3DDevice9** interface.

</dd> <dt>

**DeviceType**
</dt> <dd>

Type: **[**D3DDEVTYPE**](https://msdn.microsoft.com/library/Bb172547(v=VS.85).aspx)**

</dd> <dd>

Member of the [**D3DDEVTYPE**](https://msdn.microsoft.com/library/Bb172547(v=VS.85).aspx) enumerated type. Denotes the amount of emulated functionality for this device. The value of this parameter mirrors the value passed to the [**CreateDevice**](https://msdn.microsoft.com/library/Bb174313(v=VS.85).aspx) call that created this device.

</dd> <dt>

**hFocusWindow**
</dt> <dd>

Type: **[**HWND**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Window handle to which focus belongs for this Direct3D device. The value of this parameter mirrors the value passed to the [**CreateDevice**](https://msdn.microsoft.com/library/Bb174313(v=VS.85).aspx) call that created this device.

</dd> <dt>

**BehaviorFlags**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

A combination of one or more [D3DCREATE](d3dcreate.md) constants that control global behavior of the device. These constants mirror the constants passed to [**CreateDevice**](https://msdn.microsoft.com/library/Bb174313(v=VS.85).aspx) when the device was created.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetCreationParameters**](https://msdn.microsoft.com/library/Bb174382(v=VS.85).aspx)
</dt> <dt>

[**CreateDevice**](https://msdn.microsoft.com/library/Bb174313(v=VS.85).aspx)
</dt> </dl>

 

 




