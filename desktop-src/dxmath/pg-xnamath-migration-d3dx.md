---
Description: D3DXMath is a math helper library for Direct3D applications.
ms.assetid: 3067d47f-9b1d-2051-fa24-2094418ea272
title: Working with D3DXMath
ms.topic: article
ms.date: 05/31/2018
---

# Working with D3DXMath

D3DXMath is a math helper library for Direct3D applications. D3DXMath is long-standing, is included in D3DX 9 and D3DX 10, and dates back to older versions of DirectX as well.

> [!Note]  
> The D3DX utility library (D3DX 9, D3DX 10, and D3DX 11) is deprecated for Windows 8, so we highly recommended that you migrate to DirectXMath rather than using D3DXMath.

 

DirectXMath shares much of the same functionality in D3DXMath, and internally D3DXMath includes a number of processor-specific optimizations. The key difference is that D3DXMath is hosted in the D3DX9\*.DLLs and D3DX10\*.DLLs, and very few of the functions are inlined. The DirectXMath Library calling convention is explicitly SIMD friendly, whereas D3DXMath has to perform load and store conversions to implement SIMD optimization.

## Mixing DirectXMath and D3DXMath

D3DX11 does not contain D3DXMath, and in general we recommend using DirectXMath instead. However, you are free to continue to link to D3DX9 and/or D3DX10 in your application, and therefore you could continue to use D3DXMath or use both D3DXMath and DirectXMath in your application at the same time.

It is in general safe to cast an XMVECTOR\* to a function that takes D3DXVECTOR4\* or to cast an XMMATRIX\* to a function that takes D3DXMATRIX\*. The inverse is, however, not generally safe because XMVECTOR and XMMATRIX must be 16-byte aligned, while D3DXVECTOR4 and D3DXMATRIX have no such requirement. Failure to adhere to this requirement can result in invalid alignment exceptions at runtime.

It is safe to cast an XMVECTOR\* to a function that takes D3DXVECTOR2\* or D3DXVECTOR3\*, but not vice-versa. Both alignment concerns and the fact that D3DXVECTOR2 and D3DXVECTOR3 are smaller structures make this an unsafe operation.

> [!Note]  
> D3DX (and therefore D3DXMath) is considered legacy, and is not available to Windows Store apps that run on Windows 8 and is not included in the Windows 8 SDK for desktop apps.

 

## Using DirectXMath with Direct3D

Both DirectXMath and D3DXMath are optional when working with Direct3D. Direct3D 9 defined D3DMATRIX and D3DCOLOR as part of the Direct3D API in support of the (now legacy) fixed-function pipeline. D3DXMath in D3DX9 extends these Direct3D 9 types with common graphics math operations. For Direct3D 10.x and Direct3D 11, the API uses only the programmable pipeline so there is no API-specific structure for either matrices or color values. When the newer APIs require a color value, they take an explicit array of float values or a generic buffer of constant data that is interpreted by the HLSL shader. HLSL itself can support either row-major or column-major matrix formats, so the layout is entirely up to you (for more info, see HLSL, [Matrix Ordering](https://msdn.microsoft.com/library/Bb509634(v=VS.85).aspx); if you use column-major matrix formats in your shaders, you need to transpose the DirectXMath matrix data as you place it into your constant buffer structures). While optional, the DirectXMath and D3DXMath libraries both provide common graphics related functionality, and are therefore extremely convenient when doing Direct3D programming.

It is safe to cast an XMVECTOR\* to a D3DVECTOR\* or XMMATRIX\* to D3DMATRIX\* since Direct3D 9 makes no alignment assumptions about the incoming data structure. It is also safe to cast XMCOLOR to D3DCOLOR. You can convert a 4-float representation of color to XMCOLOR via XMStoreColor() to get the 8:8:8:8 32-bit DWORD that is equivalent to D3DCOLOR.

When working with Direct3D 10.x or Direct3D 11, you will typically use DirectXMath types to build a structure for each of your constant buffers, and in those cases it largely depends on your ability to control the alignment to make these efficient, or to use XMStore\*() operations to convert XMVECTOR and XMMATRIX data to the correct data types. When calling Direct3D 10.x or Direct3D 11 APIs that require a float\[4\] array of color values, you can cast an XMVECTOR\* or XMFLOAT4\* containing the color data.

## Porting from D3DXMath



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>D3DXMath Type</th>
<th>DirectXMath Equivalent</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>D3DXFLOAT16</td>
<td><a href="half-data-type"><strong>HALF</strong></a></td>
</tr>
<tr class="even">
<td>D3DXMATRIX</td>
<td><a href="https://docs.microsoft.com/windows/desktop/api/directxmath/ns-directxmath-xmfloat4x4"><strong>XMFLOAT4X4</strong></a></td>
</tr>
<tr class="odd">
<td>D3DXMATRIXA16</td>
<td><a href="https://docs.microsoft.com/windows/desktop/api/directxmath/ns-directxmath-xmmatrix"><strong>XMMATRIX</strong></a> or <a href="https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ee419623(v=vs.85)"><strong>XMFLOAT4X4A</strong></a></td>
</tr>
<tr class="even">
<td>D3DXQUATERNION<br/> D3DXPLANE<br/> D3DXCOLOR<br/></td>
<td><a href="xmvector-data-type"><strong>XMVECTOR</strong></a> is used rather than having unique types, so you will likely need to use an <a href="https://docs.microsoft.com/windows/desktop/api/directxmath/ns-directxmath-xmfloat4"><strong>XMFLOAT4</strong></a>
<blockquote>
[!Note]<br />
[<strong>D3DXQUATERNION::operator *</strong>](https://msdn.microsoft.com/library/Bb205422(v=VS.85).aspx) calls the <a href="https://docs.microsoft.com/windows/desktop/direct3d9/d3dxquaternionmultiply"><strong>D3DXQuaternionMultiply</strong></a> function, which multiplies two quaternions. But, unless you explicitly use the <a href="https://docs.microsoft.com/windows/desktop/api/directxmath/nf-directxmath-xmquaternionmultiply"><strong>XMQuaternionMultiply</strong></a> function, you get an incorrect answer when you use <a href="xmvector-operator-mul"><strong>XMVECTOR::operator *</strong></a> on a quaternion.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>D3DXVECTOR2</td>
<td><a href="https://docs.microsoft.com/windows/desktop/api/directxmath/ns-directxmath-xmfloat2"><strong>XMFLOAT2</strong></a></td>
</tr>
<tr class="even">
<td>D3DXVECTOR2_16F</td>
<td><a href="/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmhalf2"><strong>XMHALF2</strong></a></td>
</tr>
<tr class="odd">
<td>D3DXVECTOR3</td>
<td><a href="https://docs.microsoft.com/windows/desktop/api/directxmath/ns-directxmath-xmfloat3"><strong>XMFLOAT3</strong></a></td>
</tr>
<tr class="even">
<td>D3DXVECTOR4</td>
<td><a href="https://docs.microsoft.com/windows/desktop/api/directxmath/ns-directxmath-xmfloat4"><strong>XMFLOAT4</strong></a>(or if you can guarantee the data is 16-byte aligned, <a href="xmvector-data-type"><strong>XMVECTOR</strong></a> or <a href="https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ee419609(v=vs.85)"><strong>XMFLOAT4A</strong></a> )<br/></td>
</tr>
<tr class="odd">
<td>D3DXVECTOR4_16F</td>
<td><a href="/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmhalf4"><strong>XMHALF4</strong></a></td>
</tr>
</tbody>
</table>



 

> [!Note]  
> There is no direct equivalent to D3DXVECTOR3\_16F in XNAMath.

 



| D3DXMath Macro | DirectXMath Equivalent                            |
|----------------|---------------------------------------------------|
| D3DX\_PI       | [XM\_PI](ovw-xnamath-reference-constants.md)     |
| D3DX\_1BYPI    | [XM\_1DIVPI](ovw-xnamath-reference-constants.md) |
| D3DXToRadian   | [**XMConvertToRadians**](/windows/desktop/api/DirectXMath/nf-directxmath-xmconverttoradians)  |
| D3DXToDegree   | [**XMConvertToDegrees**](/windows/desktop/api/DirectXMath/nf-directxmath-xmconverttodegrees)  |



 



| D3DXMath Function                  | DirectXMath Equivalent                                                                                                                                                                                                                           |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DXBoxBoundProbe                  | [**BoundingBox::Intersects(XMVECTOR, XMVECTOR, float&)**](https://msdn.microsoft.com/library/Hh437817(v=VS.85).aspx)                                                                                                                                                          |
| D3DXComputeBoundingBox             | [**BoundingBox::CreateFromPoints**](https://msdn.microsoft.com/library/Hh437802(v=VS.85).aspx)                                                                                                                                                                          |
| D3DXComputeBoundingSphere          | [**BoundingSphere::CreateFromPoints**](https://msdn.microsoft.com/library/Hh437795(v=VS.85).aspx)                                                                                                                                                                      |
| D3DXSphereBoundProbe               | [**BoundingSphere::Intersects(XMVECTOR, XMVECTOR, float&)**](https://msdn.microsoft.com/library/Hh437818(v=VS.85).aspx)                                                                                                                                                    |
| D3DXIntersectTriFunction           | [**TriangleTests::Intersects**](ovw-xnamath-triangletests.md)                                                                                                                                                                                   |
| D3DXFloat32To16Array               | [**XMConvertFloatToHalfStream**](https://msdn.microsoft.com/library/Hh437913(v=VS.85).aspx)                                                                                                                                                                                 |
| D3DXFloat16To32Array               | [**XMConvertHalfToFloatStream**](https://msdn.microsoft.com/library/Hh437922(v=VS.85).aspx)                                                                                                                                                                                 |
| D3DXVec2Length                     | [**XMVector2Length**](https://msdn.microsoft.com/library/Ee420775(v=VS.85).aspx) or [**XMVector2LengthEst**](https://msdn.microsoft.com/library/Ee420776(v=VS.85).aspx)                                                                                                                                                   |
| D3DXVec2LengthSq                   | [**XMVector2LengthSq**](https://msdn.microsoft.com/library/Ee420778(v=VS.85).aspx)                                                                                                                                                                                                   |
| D3DXVec2Dot                        | [**XMVector2Dot**](https://msdn.microsoft.com/library/Ee420755(v=VS.85).aspx)                                                                                                                                                                                                             |
| D3DXVec2CCW                        | [**XMVector2Cross**](https://msdn.microsoft.com/library/Ee420754(v=VS.85).aspx)                                                                                                                                                                                                         |
| D3DXVec2Add                        | [**XMVectorAdd**](https://msdn.microsoft.com/library/Ee420991(v=VS.85).aspx)                                                                                                                                                                                                               |
| D3DXVec2Subtract                   | [**XMVectorSubtract**](https://msdn.microsoft.com/library/Ee421358(v=VS.85).aspx)                                                                                                                                                                                                     |
| D3DXVec2Minimize                   | [**XMVectorMin**](https://msdn.microsoft.com/library/Ee421181(v=VS.85).aspx)                                                                                                                                                                                                               |
| D3DXVec2Maximize                   | [**XMVectorMax**](https://msdn.microsoft.com/library/Ee421177(v=VS.85).aspx)                                                                                                                                                                                                               |
| D3DXVec2Scale                      | [**XMVectorScale**](https://msdn.microsoft.com/library/Ee421210(v=VS.85).aspx)                                                                                                                                                                                                           |
| D3DXVec2Lerp                       | [**XMVectorLerp**](https://msdn.microsoft.com/library/Ee421171(v=VS.85).aspx) or [**XMVectorLerpV**](https://msdn.microsoft.com/library/Ee421172(v=VS.85).aspx)                                                                                                                                                                   |
| D3DXVec2Normalize                  | [**XMVector2Normalize**](https://msdn.microsoft.com/library/Ee420783(v=VS.85).aspx) or [**XMVector2NormalizeEst**](https://msdn.microsoft.com/library/Ee420784(v=VS.85).aspx)                                                                                                                                       |
| D3DXVec2Hermite                    | [**XMVectorHermite**](https://msdn.microsoft.com/library/Ee421159(v=VS.85).aspx) or [**XMVectorHermiteV**](https://msdn.microsoft.com/library/Ee421160(v=VS.85).aspx)                                                                                                                                                       |
| D3DXVec2CatmullRom                 | [**XMVectorCatmullRom**](https://msdn.microsoft.com/library/Ee421005(v=VS.85).aspx) or [**XMVectorCatmullRomV**](https://msdn.microsoft.com/library/Ee421006(v=VS.85).aspx)                                                                                                                                           |
| D3DXVec2BaryCentric                | [**XMVectorBaryCentric**](https://msdn.microsoft.com/library/Ee421003(v=VS.85).aspx) or [**XMVectorBaryCentricV**](https://msdn.microsoft.com/library/Ee421004(v=VS.85).aspx)                                                                                                                                       |
| D3DXVec2Transform                  | [**XMVector2Transform**](https://msdn.microsoft.com/library/Ee420793(v=VS.85).aspx)                                                                                                                                                                                                 |
| D3DXVec2TransformCoord             | [**XMVector2TransformCoord**](https://msdn.microsoft.com/library/Ee420794(v=VS.85).aspx)                                                                                                                                                                                       |
| D3DXVec2TransformNormal            | [**XMVector2TransformNormal**](https://msdn.microsoft.com/library/Ee420796(v=VS.85).aspx)                                                                                                                                                                                     |
| D3DXVec2TransformArray             | [**XMVector2TransformStream**](https://msdn.microsoft.com/library/Hh404775(v=VS.85).aspx)                                                                                                                                                                                     |
| D3DXVec2TransformCoordArray        | [**XMVector2TransformCoordStream**](https://msdn.microsoft.com/library/Hh404773(v=VS.85).aspx)                                                                                                                                                                           |
| D3DXVec2TransformNormalArray       | [**XMVector2TransformNormalStream**](https://msdn.microsoft.com/library/Hh404774(v=VS.85).aspx)                                                                                                                                                                         |
| D3DXVec3Length                     | [**XMVector3Length**](https://msdn.microsoft.com/library/Ee420821(v=VS.85).aspx) or [**XMVector3LengthEst**](https://msdn.microsoft.com/library/Ee420822(v=VS.85).aspx)                                                                                                                                                   |
| D3DXVec3LengthSq                   | [**XMVector3LengthSq**](https://msdn.microsoft.com/library/Ee420823(v=VS.85).aspx)                                                                                                                                                                                                   |
| D3DXVec3Dot                        | [**XMVector3Dot**](https://msdn.microsoft.com/library/Ee420807(v=VS.85).aspx)                                                                                                                                                                                                             |
| D3DXVec3Cross                      | [**XMVector3Cross**](https://msdn.microsoft.com/library/Ee420806(v=VS.85).aspx)                                                                                                                                                                                                         |
| D3DXVec3Add                        | [**XMVectorAdd**](https://msdn.microsoft.com/library/Ee420991(v=VS.85).aspx)                                                                                                                                                                                                               |
| D3DXVec3Subtract                   | [**XMVectorSubtract**](https://msdn.microsoft.com/library/Ee421358(v=VS.85).aspx)                                                                                                                                                                                                     |
| D3DXVec3Minimize                   | [**XMVectorMin**](https://msdn.microsoft.com/library/Ee421181(v=VS.85).aspx)                                                                                                                                                                                                               |
| D3DXVec3Maximize                   | [**XMVectorMax**](https://msdn.microsoft.com/library/Ee421177(v=VS.85).aspx)                                                                                                                                                                                                               |
| D3DXVec3Scale                      | [**XMVectorScale**](https://msdn.microsoft.com/library/Ee421210(v=VS.85).aspx)                                                                                                                                                                                                           |
| D3DXVec3Lerp                       | [**XMVectorLerp**](https://msdn.microsoft.com/library/Ee421171(v=VS.85).aspx) or [**XMVectorLerpV**](https://msdn.microsoft.com/library/Ee421172(v=VS.85).aspx)                                                                                                                                                                   |
| D3DXVec3Normalize                  | [**XMVector3Normalize**](https://msdn.microsoft.com/library/Ee420828(v=VS.85).aspx) or [**XMVector3NormalizeEst**](https://msdn.microsoft.com/library/Ee420829(v=VS.85).aspx)                                                                                                                                       |
| D3DXVec3Hermite                    | [**XMVectorHermite**](https://msdn.microsoft.com/library/Ee421159(v=VS.85).aspx) or [**XMVectorHermiteV**](https://msdn.microsoft.com/library/Ee421160(v=VS.85).aspx)                                                                                                                                                       |
| D3DXVec3CatmullRom                 | [**XMVectorCatmullRom**](https://msdn.microsoft.com/library/Ee421005(v=VS.85).aspx) or [**XMVectorCatmullRomV**](https://msdn.microsoft.com/library/Ee421006(v=VS.85).aspx)                                                                                                                                           |
| D3DXVec3BaryCentric                | [**XMVectorBaryCentric**](https://msdn.microsoft.com/library/Ee421003(v=VS.85).aspx) or [**XMVectorBaryCentricV**](https://msdn.microsoft.com/library/Ee421004(v=VS.85).aspx)                                                                                                                                       |
| D3DXVec3Transform                  | [**XMVector3Transform**](https://msdn.microsoft.com/library/Ee420942(v=VS.85).aspx)                                                                                                                                                                                                 |
| D3DXVec3TransformCoord             | [**XMVector3TransformCoord**](https://msdn.microsoft.com/library/Ee420943(v=VS.85).aspx)                                                                                                                                                                                       |
| D3DXVec3TransformNormal            | [**XMVector3TransformNormal**](https://msdn.microsoft.com/library/Ee420945(v=VS.85).aspx)                                                                                                                                                                                     |
| D3DXVec3TransformArray             | [**XMVector3TransformStream**](https://msdn.microsoft.com/library/Hh404780(v=VS.85).aspx)                                                                                                                                                                                     |
| D3DXVec3TransformCoordArray        | [**XMVector3TransformCoordStream**](https://msdn.microsoft.com/library/Hh404778(v=VS.85).aspx)                                                                                                                                                                           |
| D3DXVec3TransformNormalArray       | [**XMVector3TransformNormalStream**](https://msdn.microsoft.com/library/Hh404779(v=VS.85).aspx)                                                                                                                                                                         |
| D3DXVec3Project                    | [**XMVector3Project**](https://msdn.microsoft.com/library/Ee420934(v=VS.85).aspx)                                                                                                                                                                                                     |
| D3DXVec3Unproject                  | [**XMVector3Unproject**](https://msdn.microsoft.com/library/Ee420949(v=VS.85).aspx)                                                                                                                                                                                                 |
| D3DXVec3ProjectArray               | [**XMVector3ProjectStream**](https://msdn.microsoft.com/library/Hh404776(v=VS.85).aspx)                                                                                                                                                                                         |
| D3DXVec3UnprojectArray             | [**XMVector3UnprojectStream**](https://msdn.microsoft.com/library/Hh404782(v=VS.85).aspx)                                                                                                                                                                                     |
| D3DXVec4Length                     | [**XMVector4Length**](https://msdn.microsoft.com/library/Ee420970(v=VS.85).aspx) or [**XMVector4LengthEst**](https://msdn.microsoft.com/library/Ee420971(v=VS.85).aspx)                                                                                                                                                   |
| D3DXVec4LengthSq                   | [**XMVector4LengthSq**](https://msdn.microsoft.com/library/Ee420972(v=VS.85).aspx)                                                                                                                                                                                                   |
| D3DXVec4Dot                        | [**XMVector4Dot**](https://msdn.microsoft.com/library/Ee420957(v=VS.85).aspx)                                                                                                                                                                                                             |
| D3DXVec4Add                        | [**XMVectorAdd**](https://msdn.microsoft.com/library/Ee420991(v=VS.85).aspx)                                                                                                                                                                                                               |
| D3DXVec4Subtract                   | [**XMVectorSubtract**](https://msdn.microsoft.com/library/Ee421358(v=VS.85).aspx)                                                                                                                                                                                                     |
| D3DXVec4Minimize                   | [**XMVectorMin**](https://msdn.microsoft.com/library/Ee421181(v=VS.85).aspx)                                                                                                                                                                                                               |
| D3DXVec4Maximize                   | [**XMVectorMax**](https://msdn.microsoft.com/library/Ee421177(v=VS.85).aspx)                                                                                                                                                                                                               |
| D3DXVec4Scale                      | [**XMVectorScale**](https://msdn.microsoft.com/library/Ee421210(v=VS.85).aspx)                                                                                                                                                                                                           |
| D3DXVec4Lerp                       | [**XMVectorLerp**](https://msdn.microsoft.com/library/Ee421171(v=VS.85).aspx) or [**XMVectorLerpV**](https://msdn.microsoft.com/library/Ee421172(v=VS.85).aspx)                                                                                                                                                                   |
| D3DXVec4Cross                      | [**XMVector4Cross**](https://msdn.microsoft.com/library/Ee420956(v=VS.85).aspx)                                                                                                                                                                                                         |
| D3DXVec4Normalize                  | [**XMVector4Normalize**](https://msdn.microsoft.com/library/Ee420976(v=VS.85).aspx) or [**XMVector4NormalizeEst**](https://msdn.microsoft.com/library/Ee420977(v=VS.85).aspx)                                                                                                                                       |
| D3DXVec4Hermite                    | [**XMVectorHermite**](https://msdn.microsoft.com/library/Ee421159(v=VS.85).aspx) or [**XMVectorHermiteV**](https://msdn.microsoft.com/library/Ee421160(v=VS.85).aspx)                                                                                                                                                       |
| D3DXVec4CatmullRom                 | [**XMVectorCatmullRom**](https://msdn.microsoft.com/library/Ee421005(v=VS.85).aspx) or [**XMVectorCatmullRomV**](https://msdn.microsoft.com/library/Ee421006(v=VS.85).aspx)                                                                                                                                           |
| D3DXVec4BaryCentric                | [**XMVectorBaryCentric**](https://msdn.microsoft.com/library/Ee421003(v=VS.85).aspx) or [**XMVectorBaryCentricV**](https://msdn.microsoft.com/library/Ee421004(v=VS.85).aspx)                                                                                                                                       |
| D3DXVec4Transform                  | [**XMVector4Transform**](https://msdn.microsoft.com/library/Ee420986(v=VS.85).aspx)                                                                                                                                                                                                 |
| D3DXVec4TransformArray             | [**XMVector4TransformStream**](https://msdn.microsoft.com/library/Hh404783(v=VS.85).aspx)                                                                                                                                                                                     |
| D3DXMatrixIdentity                 | [**XMMatrixIdentity**](https://msdn.microsoft.com/library/Ee419964(v=VS.85).aspx)                                                                                                                                                                                                     |
| D3DXMatrixDeterminant              | [**XMMatrixDeterminant**](https://msdn.microsoft.com/library/Ee419963(v=VS.85).aspx)                                                                                                                                                                                               |
| D3DXMatrixDecompose                | [**XMMatrixDecompose**](https://msdn.microsoft.com/library/Ee419962(v=VS.85).aspx)                                                                                                                                                                                                   |
| D3DXMatrixTranspose                | [**XMMatrixTranspose**](https://msdn.microsoft.com/library/Ee420022(v=VS.85).aspx)                                                                                                                                                                                                   |
| D3DXMatrixMultiply                 | [**XMMatrixMultiply**](https://msdn.microsoft.com/library/Ee419973(v=VS.85).aspx)                                                                                                                                                                                                     |
| D3DXMatrixMultiplyTranspose        | [**XMMatrixMultiplyTranspose**](https://msdn.microsoft.com/library/Ee419974(v=VS.85).aspx)                                                                                                                                                                                   |
| D3DXMatrixInverse                  | [**XMMatrixInverse**](https://msdn.microsoft.com/library/Ee419965(v=VS.85).aspx)                                                                                                                                                                                                       |
| D3DXMatrixScaling                  | [**XMMatrixScaling**](https://msdn.microsoft.com/library/Ee420014(v=VS.85).aspx)                                                                                                                                                                                                       |
| D3DXMatrixTranslation              | [**XMMatrixTranslation**](https://msdn.microsoft.com/library/Ee420020(v=VS.85).aspx)                                                                                                                                                                                               |
| D3DXMatrixRotationX                | [**XMMatrixRotationX**](https://msdn.microsoft.com/library/Ee420011(v=VS.85).aspx)                                                                                                                                                                                                   |
| D3DXMatrixRotationY                | [**XMMatrixRotationY**](https://msdn.microsoft.com/library/Ee420012(v=VS.85).aspx)                                                                                                                                                                                                   |
| D3DXMatrixRotationZ                | [**XMMatrixRotationZ**](https://msdn.microsoft.com/library/Ee420013(v=VS.85).aspx)                                                                                                                                                                                                   |
| D3DXMatrixRotationAxis             | [**XMMatrixRotationAxis**](https://msdn.microsoft.com/library/Ee419986(v=VS.85).aspx)                                                                                                                                                                                             |
| D3DXMatrixRotationQuaternion       | [**XMMatrixRotationQuaternion**](https://msdn.microsoft.com/library/Ee419988(v=VS.85).aspx)                                                                                                                                                                                 |
| D3DXMatrixRotationYawPitchRoll     | [**XMMatrixRotationRollPitchYaw**](https://msdn.microsoft.com/library/Ee419989(v=VS.85).aspx) (Note the order of parameters is different: D3DXMatrixRotationYawPitchRoll takes yaw, pitch, roll, **XMMatrixRotationRollPitchYaw** takes pitch, yaw, roll)                 |
| D3DXMatrixTransformation           | [**XMMatrixTransformation**](https://msdn.microsoft.com/library/Ee420018(v=VS.85).aspx)                                                                                                                                                                                         |
| D3DXMatrixTransformation2D         | [**XMMatrixTransformation2D**](https://msdn.microsoft.com/library/Ee420019(v=VS.85).aspx)                                                                                                                                                                                     |
| D3DXMatrixAffineTransformation     | [**XMMatrixAffineTransformation**](https://msdn.microsoft.com/library/Ee419960(v=VS.85).aspx)                                                                                                                                                                             |
| D3DXMatrixAffineTransformation2D   | [**XMMatrixAffineTransformation2D**](https://msdn.microsoft.com/library/Ee419961(v=VS.85).aspx)                                                                                                                                                                         |
| D3DXMatrixLookAtRH                 | [**XMMatrixLookAtRH**](https://msdn.microsoft.com/library/Ee419970(v=VS.85).aspx)                                                                                                                                                                                                     |
| D3DXMatrixLookAtLH                 | [**XMMatrixLookAtLH**](https://msdn.microsoft.com/library/Ee419969(v=VS.85).aspx)                                                                                                                                                                                                     |
| D3DXMatrixPerspectiveRH            | [**XMMatrixPerspectiveRH**](https://msdn.microsoft.com/library/Ee419984(v=VS.85).aspx)                                                                                                                                                                                           |
| D3DXMatrixPerspectiveLH            | [**XMMatrixPerspectiveLH**](https://msdn.microsoft.com/library/Ee419981(v=VS.85).aspx)                                                                                                                                                                                           |
| D3DXMatrixPerspectiveFovRH         | [**XMMatrixPerspectiveFovRH**](https://msdn.microsoft.com/library/Ee419980(v=VS.85).aspx)                                                                                                                                                                                     |
| D3DXMatrixPerspectiveFovLH         | [**XMMatrixPerspectiveFovLH**](https://msdn.microsoft.com/library/Ee419979(v=VS.85).aspx)                                                                                                                                                                                     |
| D3DXMatrixPerspectiveOffCenterRH   | [**XMMatrixPerspectiveOffCenterRH**](https://msdn.microsoft.com/library/Ee419983(v=VS.85).aspx)                                                                                                                                                                         |
| D3DXMatrixPerspectiveOffCenterLH   | [**XMMatrixPerspectiveOffCenterLH**](https://msdn.microsoft.com/library/Ee419982(v=VS.85).aspx)                                                                                                                                                                         |
| D3DXMatrixOrthoRH                  | [**XMMatrixOrthographicRH**](https://msdn.microsoft.com/library/Ee419978(v=VS.85).aspx)                                                                                                                                                                                         |
| D3DXMatrixOrthoLH                  | [**XMMatrixOrthographicLH**](https://msdn.microsoft.com/library/Ee419975(v=VS.85).aspx)                                                                                                                                                                                         |
| D3DXMatrixOrthoOffCenterRH         | [**XMMatrixOrthographicOffCenterRH**](https://msdn.microsoft.com/library/Ee419977(v=VS.85).aspx)                                                                                                                                                                       |
| D3DXMatrixOrthoOffCenterLH         | [**XMMatrixOrthographicOffCenterLH**](https://msdn.microsoft.com/library/Ee419976(v=VS.85).aspx)                                                                                                                                                                       |
| D3DXMatrixShadow                   | [**XMMatrixShadow**](https://msdn.microsoft.com/library/Ee420017(v=VS.85).aspx)                                                                                                                                                                                                         |
| D3DXMatrixReflect                  | [**XMMatrixReflect**](https://msdn.microsoft.com/library/Ee419985(v=VS.85).aspx)                                                                                                                                                                                                       |
| D3DXQuaternionLength               | [**XMQuaternionLength**](https://msdn.microsoft.com/library/Ee420164(v=VS.85).aspx)                                                                                                                                                                                                 |
| D3DXQuaternionLengthSq             | [**XMQuaternionLengthSq**](https://msdn.microsoft.com/library/Ee420165(v=VS.85).aspx)                                                                                                                                                                                             |
| D3DXQuaternionDot                  | [**XMQuaternionDot**](https://msdn.microsoft.com/library/Ee420156(v=VS.85).aspx)                                                                                                                                                                                                       |
| D3DXQuaternionIdentity             | [**XMQuaternionIdentity**](https://msdn.microsoft.com/library/Ee420159(v=VS.85).aspx)                                                                                                                                                                                             |
| D3DXQuaternionIsIdentity           | [**XMQuaternionIsIdentity**](https://msdn.microsoft.com/library/Ee420161(v=VS.85).aspx)                                                                                                                                                                                         |
| D3DXQuaternionConjugate            | [**XMQuaternionConjugate**](https://msdn.microsoft.com/library/Ee420155(v=VS.85).aspx)                                                                                                                                                                                           |
| D3DXQuaternionToAxisAngle          | [**XMQuaternionToAxisAngle**](https://msdn.microsoft.com/library/Ee420182(v=VS.85).aspx)                                                                                                                                                                                       |
| D3DXQuaternionRotationMatrix       | [**XMQuaternionRotationMatrix**](https://msdn.microsoft.com/library/Ee420173(v=VS.85).aspx)                                                                                                                                                                                 |
| D3DXQuaternionRotationAxis         | [**XMQuaternionRotationAxis**](https://msdn.microsoft.com/library/Ee420172(v=VS.85).aspx)                                                                                                                                                                                     |
| D3DXQuaternionRotationYawPitchRoll | [**XMQuaternionRotationRollPitchYaw**](https://msdn.microsoft.com/library/Ee420175(v=VS.85).aspx) (Note the order of parameters is different: D3DXQuaternionRotationYawPitchRoll takes yaw, pitch, roll, **XMQuaternionRotationRollPitchYaw** takes pitch, yaw, roll) |
| D3DXQuaternionMultiply             | [**XMQuaternionMultiply**](https://msdn.microsoft.com/library/Ee420167(v=VS.85).aspx)                                                                                                                                                                                             |
| D3DXQuaternionNormalize            | [**XMQuaternionNormalize**](https://msdn.microsoft.com/library/Ee420168(v=VS.85).aspx) or [**XMQuaternionNormalizeEst**](https://msdn.microsoft.com/library/Ee420169(v=VS.85).aspx)                                                                                                                           |
| D3DXQuaternionInverse              | [**XMQuaternionInverse**](https://msdn.microsoft.com/library/Ee420160(v=VS.85).aspx)                                                                                                                                                                                               |
| D3DXQuaternionLn                   | [**XMQuaternionLn**](https://msdn.microsoft.com/library/Ee420166(v=VS.85).aspx)                                                                                                                                                                                                         |
| D3DXQuaternionExp                  | [**XMQuaternionExp**](https://msdn.microsoft.com/library/Ee420158(v=VS.85).aspx)                                                                                                                                                                                                       |
| D3DXQuaternionSlerp                | [**XMQuaternionSlerp**](https://msdn.microsoft.com/library/Ee420177(v=VS.85).aspx) or [**XMQuaternionSlerpV**](https://msdn.microsoft.com/library/Ee420178(v=VS.85).aspx)                                                                                                                                               |
| D3DXQuaternionSquad                | [**XMQuaternionSquad**](https://msdn.microsoft.com/library/Ee420179(v=VS.85).aspx) or [**XMQuaternionSquadV**](https://msdn.microsoft.com/library/Ee420181(v=VS.85).aspx)                                                                                                                                               |
| D3DXQuaternionSquadSetup           | [**XMQuaternionSquadSetup**](https://msdn.microsoft.com/library/Ee420180(v=VS.85).aspx)                                                                                                                                                                                         |
| D3DXQuaternionBaryCentric          | [**XMQuaternionBaryCentric**](https://msdn.microsoft.com/library/Ee420153(v=VS.85).aspx) or [**XMQuaternionBaryCentricV**](https://msdn.microsoft.com/library/Ee420154(v=VS.85).aspx)                                                                                                                       |
| D3DXPlaneDot                       | [**XMPlaneDot**](https://msdn.microsoft.com/library/Ee420137(v=VS.85).aspx)                                                                                                                                                                                                                 |
| D3DXPlaneDotCoord                  | [**XMPlaneDotCoord**](https://msdn.microsoft.com/library/Ee420138(v=VS.85).aspx)                                                                                                                                                                                                       |
| D3DXPlaneDotNormal                 | [**XMPlaneDotNormal**](https://msdn.microsoft.com/library/Ee420139(v=VS.85).aspx)                                                                                                                                                                                                     |
| D3DXPlaneScale                     | [**XMVectorScale**](https://msdn.microsoft.com/library/Ee421210(v=VS.85).aspx)                                                                                                                                                                                                           |
| D3DXPlaneNormalize                 | [**XMPlaneNormalize**](https://msdn.microsoft.com/library/Ee420148(v=VS.85).aspx) or [**XMPlaneNormalizeEst**](https://msdn.microsoft.com/library/Ee420149(v=VS.85).aspx)                                                                                                                                               |
| D3DXPlaneIntersectLine             | [**XMPlaneIntersectLine**](https://msdn.microsoft.com/library/Ee420143(v=VS.85).aspx)                                                                                                                                                                                             |
| D3DXPlaneFromPointNormal           | [**XMPlaneFromPointNormal**](https://msdn.microsoft.com/library/Ee420141(v=VS.85).aspx)                                                                                                                                                                                         |
| D3DXPlaneFromPoints                | [**XMPlaneFromPoints**](https://msdn.microsoft.com/library/Ee420142(v=VS.85).aspx)                                                                                                                                                                                                   |
| D3DXPlaneTransform                 | [**XMPlaneTransform**](https://msdn.microsoft.com/library/Ee420151(v=VS.85).aspx)                                                                                                                                                                                                     |
| D3DXPlaneTransformArray            | [**XMPlaneTransformStream**](https://msdn.microsoft.com/library/Hh404689(v=VS.85).aspx)                                                                                                                                                                                         |
| D3DXColorNegative                  | [**XMColorNegative**](https://msdn.microsoft.com/library/Ee419404(v=VS.85).aspx)                                                                                                                                                                                                       |
| D3DXColorAdd                       | [**XMVectorAdd**](https://msdn.microsoft.com/library/Ee420991(v=VS.85).aspx)                                                                                                                                                                                                               |
| D3DXColorSubtract                  | [**XMVectorSubtract**](https://msdn.microsoft.com/library/Ee421358(v=VS.85).aspx)                                                                                                                                                                                                     |
| D3DXColorScale                     | [**XMVectorScale**](https://msdn.microsoft.com/library/Ee421210(v=VS.85).aspx)                                                                                                                                                                                                           |
| D3DXColorModulate                  | [**XMColorModulate**](https://msdn.microsoft.com/library/Ee419403(v=VS.85).aspx)                                                                                                                                                                                                       |
| D3DXColorLerp                      | [**XMVectorLerp**](https://msdn.microsoft.com/library/Ee421171(v=VS.85).aspx) or [**XMVectorLerpV**](https://msdn.microsoft.com/library/Ee421172(v=VS.85).aspx)                                                                                                                                                                   |
| D3DXColorAdjustSaturation          | [**XMColorAdjustSaturation**](https://msdn.microsoft.com/library/Ee419294(v=VS.85).aspx)                                                                                                                                                                                       |
| D3DXColorAdjustContrast            | [**XMColorAdjustContrast**](https://msdn.microsoft.com/library/Ee419293(v=VS.85).aspx)                                                                                                                                                                                           |
| D3DXFresnelTerm                    | [**XMFresnelTerm**](https://msdn.microsoft.com/library/Ee419648(v=VS.85).aspx)                                                                                                                                                                                                           |



 

> [!Note]  
> [Spherical Harmonics](https://go.microsoft.com/fwlink/p/?LinkId=262885) functions for DirectXMath are available separately. There is no DirectXMath equivalent to **ID3DXMatrixStack**.

 

## Related topics

<dl> <dt>

[DirectXMath Programming Guide](ovw-xnamath-progguide.md)
</dt> </dl>

 

 




