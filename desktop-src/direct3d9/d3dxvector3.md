---
Description: Describes a three-component vector including operator overloads and type casts.
ms.assetid: 4d73de4b-82fe-452a-8a1e-17208f172a03
title: D3DXVECTOR3 structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXVECTOR3 structure

Describes a three-component vector including operator overloads and type casts.

## Syntax


```C++
typedef struct D3DXVECTOR3 {
  FLOAT x;
  FLOAT y;
  FLOAT z;
} D3DXVECTOR3, *LPD3DXVECTOR3;
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

</dd> <dt>

**z**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

The z-component.

</dd> </dl>

## Remarks

### D3DXVECTOR3 Extensions

D3DXVECTOR3 has the following C++ extensions.


```
#ifdef __cplusplus
typedef struct D3DXVECTOR3 : public D3DVECTOR
{
public:
    D3DXVECTOR3() {};
    D3DXVECTOR3( CONST FLOAT * );
    D3DXVECTOR3( CONST D3DVECTOR&amp; );
    D3DXVECTOR3( CONST D3DXFLOAT16 * );
    D3DXVECTOR3( FLOAT x, FLOAT y, FLOAT z );

    // casting
    operator FLOAT* ();
    operator CONST FLOAT* () const;

    // assignment operators
    D3DXVECTOR3&amp; operator += ( CONST D3DXVECTOR3&amp; );
    D3DXVECTOR3&amp; operator -= ( CONST D3DXVECTOR3&amp; );
    D3DXVECTOR3&amp; operator *= ( FLOAT );
    D3DXVECTOR3&amp; operator /= ( FLOAT );

    // unary operators
    D3DXVECTOR3 operator + () const;
    D3DXVECTOR3 operator - () const;

    // binary operators
    D3DXVECTOR3 operator + ( CONST D3DXVECTOR3&amp; ) const;
    D3DXVECTOR3 operator - ( CONST D3DXVECTOR3&amp; ) const;
    D3DXVECTOR3 operator * ( FLOAT ) const;
    D3DXVECTOR3 operator / ( FLOAT ) const;

    friend D3DXVECTOR3 operator * ( FLOAT, CONST struct D3DXVECTOR3&amp; );

    BOOL operator == ( CONST D3DXVECTOR3&amp; ) const;
    BOOL operator != ( CONST D3DXVECTOR3&amp; ) const;

} D3DXVECTOR3, *LPD3DXVECTOR3;

#else //!__cplusplus
typedef struct _D3DVECTOR D3DXVECTOR3, *LPD3DXVECTOR3;
#endif //!__cplusplus

typedef struct D3DXVECTOR3_16F
{
#ifdef __cplusplus
public:
    D3DXVECTOR3_16F() {};
    D3DXVECTOR3_16F( CONST FLOAT * );
    D3DXVECTOR3_16F( CONST D3DVECTOR&amp; );
    D3DXVECTOR3_16F( CONST D3DXFLOAT16 * );
    D3DXVECTOR3_16F( CONST D3DXFLOAT16 &amp;x, CONST D3DXFLOAT16 &amp;y, CONST D3DXFLOAT16 &amp;z );

    // casting
    operator D3DXFLOAT16* ();
    operator CONST D3DXFLOAT16* () const;

    // binary operators
    BOOL operator == ( CONST D3DXVECTOR3_16F&amp; ) const;
    BOOL operator != ( CONST D3DXVECTOR3_16F&amp; ) const;

public:
#endif //__cplusplus
    D3DXFLOAT16 x, y, z;

} D3DXVECTOR3_16F, *LPD3DXVECTOR3_16F;
        
```



## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9math.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




