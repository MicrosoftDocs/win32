---
Description: 'Describes an animation event.'
ms.assetid: 'ddcdd143-bcbd-450c-a4df-914797a562e6'
title: 'D3DXEVENT\_DESC structure'
---

# D3DXEVENT\_DESC structure

Describes an animation event.

## Syntax


```C++
typedef struct D3DXEVENT_DESC {
  D3DXEVENT_TYPE      Type;
  UINT                Track;
  DOUBLE              StartTime;
  DOUBLE              Duration;
  D3DXTRANSITION_TYPE Transition;
  union {
    FLOAT  Weight;
    FLOAT  Speed;
    DOUBLE Position;
    BOOL   Enable;
  };
} D3DXEVENT_DESC, *LPD3DXEVENT_DESC;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Type: **[**D3DXEVENT\_TYPE**](direct3d9.d3dxevent_type)**

</dd> <dd>

Event type, as defined in [**D3DXEVENT\_TYPE**](direct3d9.d3dxevent_type).

</dd> <dt>

**Track**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Event track identifier.

</dd> <dt>

**StartTime**
</dt> <dd>

Type: **[**DOUBLE**](winprog.windows_data_types)**

</dd> <dd>

Start time of the event in global time.

</dd> <dt>

**Duration**
</dt> <dd>

Type: **[**DOUBLE**](winprog.windows_data_types)**

</dd> <dd>

Duration of the event in global time.

</dd> <dt>

**Transition**
</dt> <dd>

Type: **[**D3DXTRANSITION\_TYPE**](direct3d9.d3dxtransition_type)**

</dd> <dd>

Transition style of the event, as defined in [**D3DXTRANSITION\_TYPE**](direct3d9.d3dxtransition_type).

</dd> <dt>

**Weight**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

Track weight for the event.

</dd> <dt>

**Speed**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

Track speed for the event.

</dd> <dt>

**Position**
</dt> <dd>

Type: **[**DOUBLE**](winprog.windows_data_types)**

</dd> <dd>

Track position for the event.

</dd> <dt>

**Enable**
</dt> <dd>

Type: **[**BOOL**](winprog.windows_data_types)**

</dd> <dd>

Enable flag.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




