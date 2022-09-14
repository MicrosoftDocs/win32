---
description: Tessellation (Direct3D 9)
ms.assetid: ae39b0e1-d2ae-449e-89db-0a2b24171531
title: Tessellation (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Tessellation (Direct3D 9)

## Tessellator Unit

The tessellator unit has been enhanced. You can now use it to:

-   Perform adaptive tessellation of all higher-order primitives.
-   Look up per-vertex displacement values from a displacement map and pass them on to a vertex shader.
-   Support rectangle-patch tessellation. This is specified through a vertex declaration using D3DDECLMETHOD\_PARTIALU or D3DDECLMETHOD\_PARTIALV. If a vertex declaration containing these methods is used to draw a triangle patch, [**IDirect3DDevice9::DrawTriPatch**](/windows/desktop/api) will fail. For more information about vertex declarations, see [**D3DVERTEXELEMENT9**](d3dvertexelement9.md).

In DirectX 8.x, what was called ORDER was really the degree. In Direct3D 9, the degree is now specified by [**D3DDEGREETYPE**](./d3ddegreetype.md).


```
 // This used to be D3DORDERTYPE and D3DORDER* 
 typedef enum _D3DDEGREETYPE 
 { 
 D3DDEGREE_LINEAR = 1, 
 D3DDEGREE_QUADRATIC = 2, 
 D3DDEGREE_CUBIC = 3, 
 D3DDEGREE_QUINTIC = 5, 
 D3DDEGREE_FORCE_DWORD = 0x7fffffff, 
 } D3DDEGREETYPE; 
```



The change in degree type affected two other structures.


```
typedef struct _D3DRECTPATCH_INFO 
 { 
 UINT StartVertexOffsetWidth; 
 UINT StartVertexOffsetHeight; 
 UINT Width; 
 UINT Height; 
 UINT Stride; 
 D3DBASISTYPE Basis; 
 D3DDEGREETYPE Degree; 
 } D3DRECTPATCH_INFO; 
```




```
 typedef struct _D3DTRIPATCH_INFO 
 { 
 UINT StartVertexOffset; 
 UINT NumVertices; 
 D3DBASISTYPE Basis; 
 D3DDEGREETYPE Degree; 
 } D3DTRIPATCH_INFO; 
```



Drivers need to fix compilation errors that will result from this change when they compile with the new headers. No functionality has to be changed.

## Adaptive Tessellation

Adaptive tessellation can be applied to high-order primitives including N-patches, rectangle patches, and triangle patches. This feature is enabled by the D3DRS\_ENABLEADAPTIVETESSELLATION and adaptively tessellates a patch, based on the depth value of the control vertex in eye space.

The z-coordinates (Zi) of control vertices (Vi), which are transformed into eye space (Zieye) by performing a dot product with a 4-vector, are used as the depth values. The 4D vector (Mdm) is specified by the application using four render states (D3DRS\_ADAPTIVETESS\_X, D3DRS\_ADAPTIVETESS\_Y, D3DRS\_ADAPTIVETESS\_Z, and D3DRS\_ADAPTIVETESS\_W). This 4-vector could be the third column of the concatenated world and view matrices. It also could be used to apply a scale to Zieye.

The function to compute a tessellation level Ti from Zieye is assumed to be (MaxTessellationLevel/Zieye), which means that the MaxTessellationLevel is the tessellation level at Z = 1 in eye space. The MaxTessellationLevel is equal to a value set by [**IDirect3DDevice9::SetNPatchMode**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setnpatchmode) for N-patches and, for RT-patches, it is equal to pNumSegs. The tessellation level is then clamped to values, defined by the two additional render states D3DRS\_MINTESSELLATIONLEVEL and D3DRS\_MAXTESSELLATIONLEVEL, which define the minimum and maximum tessellation levels to be clamped to. The Ti's for each vertex along an edge of a patch are averaged to obtain a tessellation level for that edge. The algorithm for computing Ti for rectangle patches, triangle patches, and N-patches differs in what control vertices are used to compute the tessellation level.

For the rectangle patches with a B-spline basis, the four outermost control vertices are used. For example, with D3DORDER\_CUBIC order: vertices (1,1) and (1,width-2) are used with pNumSegs\[0\], vertices (1,width-2) and (height-2,height-2) are used with pNumSegs\[1\], vertices (height-2,width-2) and (1,width-2) are used with pNumSegs\[2\], and vertices (2,1) and (1,1) are used with pNumSegs\[3\].

For the triangle patches, the corner patch vertices are used. With D3DORDER\_CUBIC order: vertices (0) and (9) are used with pNumSegs\[0\], vertices (9) and (6) are used with pNumSegs\[1\] and vertices (6) and (0) are used with pNumSegs\[3\].

For N-patches the triangle vertices are used.

For the rectangle and triangle patches with a Bezier basis, the corner-control vertices are used.

Per-vertex tessellation rate control. An application can optionally supply a single positive floating-point value per vertex, which can be used to control the rate of tessellation. This is supplied using the D3DDECLUSAGE\_TESSFACTOR, for which usage index must be 0 and input type must be D3DDECLTYPE\_FLOAT1. This is multiplied to the per-vertex tessellation level.

### Math

The tessellation level (Te) for an edge e, represented by two control vertices (Ve1, Ve2), is computed as shown below :


```
Vertex Vi: (Xi, Yi, Zi, TFactori (optional)). 
Ze1eye = Ve1 . Mdm 
Ze2eye = Ve2 . Mdm 
Te1 = MaxTessellationLevel * TFactore1 / Ze1eye 
Te2 = MaxTessellationLevel * TFactore2 / Ze2eye 
Te = ( Te1 + Te2 ) / 2; 
if Te > D3DRS_MAXTESSELLATIONLEVEL || Te < 0, then Te = D3DRS_MAXTESSELLATIONLEVEL 
if Te < D3DRS_MINTESSELLATIONLEVEL, then Te = D3DRS_MINTESSELLATIONLEVEL 
```



When D3DRS\_ENABLEADAPTIVETESSELLATION is **TRUE**, triangle primitives (triangle lists, fans, strips) are drawn as N-patches, [**IDirect3DDevice9::SetNPatchMode**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setnpatchmode) has set value less than 1.0.

### API Changes

New render states:


```
 D3DRS_ENABLEADAPTIVETESSELLATION // BOOL 
 D3DRS_MAXTESSELLATIONLEVEL       // Float 
 D3DRS_MINTESSELLATIONLEVEL       // Float 
 D3DRS_ADAPTIVETESS_X             // Float 
 D3DRS_ADAPTIVETESS_Y             // Float 
 D3DRS_ADAPTIVETESS_Z             // Float 
 D3DRS_ADAPTIVETESS_W             // Float 
 
 // D3DRS_MINTESSELLATIONLEVEL and D3DRS_MAXTESSELLATIONLEVEL 
 // cannot be less than 1 
```



And their default values:


```
D3DRS_MAXTESSELLATIONLEVEL = 1.0f 
D3DRS_MINTESSELLATIONLEVEL = 1.0f 
D3DRS_ADAPTIVETESS_X = 0.0f 
D3DRS_ADAPTIVETESS_Y = 0.0f 
D3DRS_ADAPTIVETESS_Z = 1.0f 
D3DRS_ADAPTIVETESS_W = 0.0f 
D3DRS_ENABLEADAPTIVETESSELLATION = FALSE 
```



New hardware caps:


```
D3DDEVCAPS2_ADAPTIVETESSRTPATCH // Can adaptively tessellate RT-patches 
D3DDEVCAPS2_ADAPTIVETESSNPATCH  // Can adaptively tessellate N-patches 
```



## Related topics

<dl> <dt>

[Vertex Pipeline](vertex-pipeline.md)
</dt> </dl>

 

 
