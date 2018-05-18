---
Description: 'Describes a two-component vector including operator overloads and type casts.'
ms.assetid: '5b7b4847-b994-48c6-ae3c-e48ee1716ddd'
title: D3DXVECTOR2 structure
---

# D3DXVECTOR2 structure

Describes a two-component vector including operator overloads and type casts.

## Syntax


```C++
typedef struct D3DXVECTOR2 {
  FLOAT x;
  FLOAT y;
} D3DXVECTOR2, *LPD3DXVECTOR2;
```



## Members

<dl> <dt>

**x**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

The x-component.

</dd> <dt>

**y**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

The y-component.

</dd> </dl>

## Remarks

**D3DXVECTOR2** has the following C++ extensions.

### D3DXVECTOR2 Extensions


```
typedef struct D3DXVECTOR2
{
#ifdef __cplusplus
public:
    D3DXVECTOR2() {};
    D3DXVECTOR2( CONST FLOAT * );
    D3DXVECTOR2( CONST D3DXFLOAT16 * );
    D3DXVECTOR2( FLOAT x, FLOAT y );

    // casting
    operator FLOAT* ();
    operator CONST FLOAT* () const;

    // assignment operators
    D3DXVECTOR2&amp; operator += ( CONST D3DXVECTOR2&amp; );
    D3DXVECTOR2&amp; operator -= ( CONST D3DXVECTOR2&amp; );
    D3DXVECTOR2&amp; operator *= ( FLOAT );
    D3DXVECTOR2&amp; operator /= ( FLOAT );

    // unary operators
    D3DXVECTOR2 operator + () const;
    D3DXVECTOR2 operator - () const;

    // binary operators
    D3DXVECTOR2 operator + ( CONST D3DXVECTOR2&amp; ) const;
    D3DXVECTOR2 operator - ( CONST D3DXVECTOR2&amp; ) const;
    D3DXVECTOR2 operator * ( FLOAT ) const;
    D3DXVECTOR2 operator / ( FLOAT ) const;

    friend D3DXVECTOR2 operator * ( FLOAT, CONST D3DXVECTOR2&amp; );

    BOOL operator == ( CONST D3DXVECTOR2&amp; ) const;
    BOOL operator != ( CONST D3DXVECTOR2&amp; ) const;


public:
#endif //__cplusplus
    FLOAT x, y;
} D3DXVECTOR2, *LPD3DXVECTOR2;
        
```



## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](d3d10-graphics-reference-d3dx10-structures.md)
</dt> </dl>

 

 




