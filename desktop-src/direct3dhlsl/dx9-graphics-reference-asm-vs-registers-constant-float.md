---
title: Constant Float Register
description: Vertex shader input register for a four component floating-point constant. Set a constant register with either def - vs or SetVertexShaderConstantF.
ms.assetid: 45a14258-52d5-4c22-885f-5af20ae36251
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Constant Float Register

Vertex shader input register for a four component floating-point constant. Set a constant register with either [def - vs](def---vs.md) or [**SetVertexShaderConstantF**](https://msdn.microsoft.com/library/windows/desktop/bb174467).

The constant register file is read-only from the perspective of the vertex shader. Any single instruction may access only one constant register. However, each source in that instruction may independently swizzle and negate that vector as it is read.

The behavior of shader constants has changed between Direct3D 8 and Direct3D 9.

-   For Direct3D 9, constants set with defx assign values to the shader constant space. The lifetime of a constant declared with defx is confined to the execution of that shader only. Conversely, constants set using the APIs SetXXXShaderConstantX initialize constants in global space. Constants in global space are not copied to local space (visible to the shader) until SetxxxShaderConstants is called.
-   For Direct3D 8, constants set with defx or the APIs both assign values to the shader constant space. Each time the shader is executed, the constants are used by the current shader regardless of the technique used to set them.

A constant register is designated as either absolute or relative:


```
c[n]           ; absolute
c[a0.x + n]    ; relative - supported only in version 1_1
```



The constant register can be read, therefore, either by using an absolute index or with a relative index from an address register. Reads from out-of-range registers return (0.0, 0.0, 0.0, 0.0).

## Examples

Here is an example declaring two floating-point constants within a shader.


```
def c40, 0.0f,0.0f,0.0f,0.0f;
```



These constants are loaded every time [**SetVertexShader**](https://msdn.microsoft.com/library/windows/desktop/bb174465) is called.

Here is an example using the API.


```
    // Set up the vertex shader constants.
    {
        D3DXMATRIXA16 mat;
        D3DXMatrixMultiply( &amp;mat, &amp;m_matView, &amp;m_matProj );
        D3DXMatrixTranspose( &amp;mat, &amp;mat );

        D3DXVECTOR4 vA( sinf(m_fTime)*15.0f, 0.0f, 0.5f, 1.0f );
        D3DXVECTOR4 vD( D3DX_PI, 1.0f/(2.0f*D3DX_PI), 2.0f*D3DX_PI, 0.05f );

        // Taylor series coefficients for sin and cos.
        D3DXVECTOR4 vSin( 1.0f, -1.0f/6.0f, 1.0f/120.0f, -1.0f/5040.0f );
        D3DXVECTOR4 vCos( 1.0f, -1.0f/2.0f, 1.0f/ 24.0f, -1.0f/ 720.0f );

        m_pd3dDevice->SetVertexShaderConstantF(  0, (float*)&amp;mat,  4 );
        m_pd3dDevice->SetVertexShaderConstantF(  4, (float*)&amp;vA,   1 );
        m_pd3dDevice->SetVertexShaderConstantF(  7, (float*)&amp;vD,   1 );
        m_pd3dDevice->SetVertexShaderConstantF( 10, (float*)&amp;vSin, 1 );
        m_pd3dDevice->SetVertexShaderConstantF( 11, (float*)&amp;vCos, 1 );
    }
```



If you are setting constant values with the API, there is no shader declaration required.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| Constant Register      | x    | x    | x     | x    | x    | x     |



 

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




