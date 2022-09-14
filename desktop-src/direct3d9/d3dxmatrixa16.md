---
description: D3DXMATRIXA16 structure (D3dx9math.h) - A 4x4, 16-byte-aligned matrix that contains methods and operator overloads.
ms.assetid: c7082fe5-f98b-4ab7-b8c2-7cdbab4848ad
title: D3DXMATRIXA16 structure (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXMATRIXA16
api_type:
- HeaderDef
api_location:
- d3dx9math.h
---

# D3DXMATRIXA16 structure (D3dx9math.h)

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

A 4x4, 16-byte-aligned matrix that contains methods and operator overloads.

## Syntax


```C++
typedef struct D3DXMATRIXA16 {
  FLOAT _ij;
} D3DXMATRIXA16, *LPD3DXMATRIXA16;
```



## Members

<dl> <dt>

**\_ij**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

The (i, j) component of the matrix, where i is the row number and j is the column number. For example, \_34 means the same as \[a₃₄\], the component in the third row and fourth column.

</dd> </dl>

## Remarks

A 16-byte aligned matrix, when used by D3DX math functions, has been optimized for improved performance on Intel Pentium 4 processors. Matrices are aligned independent of where they are created: on the program stack, in the heap, or in global scope. Alignment is accomplished using \_\_declspec(align(16)), which works with Visual C++ .NET and with Visual C++ 6.0 only when the processor pack is installed. Unfortunately, there is no way to detect the processor pack, so byte alignment is turned on by default only with Visual C++ .NET.

Vectors and quaternions are not byte aligned in D3DX. When using vectors and quaternions with D3DX math functions, use \_declspec(align(16)) to generate byte aligned vectors and quaternions, because they will perform significantly better. The definition of \_declspec is shown here.


```
#define D3DX_ALIGN16 __declspec(align(16))
```



Other compilers interpret D3DXMATRIXA16 as D3DXMATRIX. Using this structure on a compiler that does not actually align the matrix can be problematic because it will not expose bugs that ignore alignment. For example, if a D3DXMATRIXA16 object is inside a structure or class, a [**memcpy**](https://msdn.microsoft.com/library/dswaw1wk(v=VS.71).aspx) might be done with tight packing (ignoring 16-byte boundaries). This would cause build breaks if the compiler were to sometime add matrix aligning.

### D3DXMATRIXA16

**D3DXMATRIXA16** has the following C++ extensions.


```
typedef struct _D3DXMATRIXA16 : public D3DXMATRIX
{
    _D3DXMATRIXA16();
    _D3DXMATRIXA16( CONST FLOAT * f);
    _D3DXMATRIXA16( CONST D3DMATRIX& m);
    _D3DXMATRIXA16( FLOAT _11, FLOAT _12, FLOAT _13, FLOAT _14,
                    FLOAT _21, FLOAT _22, FLOAT _23, FLOAT _24,
                    FLOAT _31, FLOAT _32, FLOAT _33, FLOAT _34,
                    FLOAT _41, FLOAT _42, FLOAT _43, FLOAT _44 );
    void* operator new(size_t s);
    void* operator new[](size_t s);

    // The two operators below are not virtual operators. If you cast
    //   to D3DXMATRIX, do not delete using them
    void operator delete(void* p);
    void operator delete[](void* p);

    struct _D3DXMATRIXA16& operator=(CONST D3DXMATRIX& rhs);
} _D3DXMATRIXA16;

typedef D3DX_ALIGN16 _D3DXMATRIXA16 D3DXMATRIXA16, *LPD3DXMATRIXA16;

```



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9math.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> <dt>

[**D3DXMATRIX**](d3dxmatrix.md)
</dt> </dl>

 

 
