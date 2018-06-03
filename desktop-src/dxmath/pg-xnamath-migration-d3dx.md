---
Description: D3DXMath is a math helper library for Direct3D applications.
ms.assetid: 3067d47f-9b1d-2051-fa24-2094418ea272
title: Working with D3DXMath
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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

Both DirectXMath and D3DXMath are optional when working with Direct3D. Direct3D 9 defined D3DMATRIX and D3DCOLOR as part of the Direct3D API in support of the (now legacy) fixed-function pipeline. D3DXMath in D3DX9 extends these Direct3D 9 types with common graphics math operations. For Direct3D 10.x and Direct3D 11, the API uses only the programmable pipeline so there is no API-specific structure for either matrices or color values. When the newer APIs require a color value, they take an explicit array of float values or a generic buffer of constant data that is interpreted by the HLSL shader. HLSL itself can support either row-major or column-major matrix formats, so the layout is entirely up to you (for more info, see HLSL, [Matrix Ordering](https://www.bing.com/search?q=Matrix Ordering); if you use column-major matrix formats in your shaders, you need to transpose the DirectXMath matrix data as you place it into your constant buffer structures). While optional, the DirectXMath and D3DXMath libraries both provide common graphics related functionality, and are therefore extremely convenient when doing Direct3D programming.

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
<td>[<strong>HALF</strong>](half-data-type.md)</td>
</tr>
<tr class="even">
<td>D3DXMATRIX</td>
<td>[<strong>XMFLOAT4X4</strong>](/windows/desktop/api/DirectXMath/)</td>
</tr>
<tr class="odd">
<td>D3DXMATRIXA16</td>
<td>[<strong>XMMATRIX</strong>](/windows/desktop/api/DirectXMath/) or [<strong>XMFLOAT4X4A</strong>](/windows/desktop/api/DirectXMath/)</td>
</tr>
<tr class="even">
<td>D3DXQUATERNION<br/> D3DXPLANE<br/> D3DXCOLOR<br/></td>
<td>[<strong>XMVECTOR</strong>](xmvector-data-type.md) is used rather than having unique types, so you will likely need to use an [<strong>XMFLOAT4</strong>](/windows/desktop/api/DirectXMath/)
<blockquote>
[!Note]<br />
[<strong>D3DXQUATERNION::operator *</strong>](https://msdn.microsoft.com/windows/desktop/a49975a4-a9a7-4183-91b3-3d56f70747ef) calls the [<strong>D3DXQuaternionMultiply</strong>](https://msdn.microsoft.com/windows/desktop/11072fc9-dae8-4f63-b07d-b709eed381df) function, which multiplies two quaternions. But, unless you explicitly use the [<strong>XMQuaternionMultiply</strong>](/windows/desktop/api/DirectXMath/) function, you get an incorrect answer when you use [<strong>XMVECTOR::operator *</strong>](xmvector-operator-mul.md) on a quaternion.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>D3DXVECTOR2</td>
<td>[<strong>XMFLOAT2</strong>](/windows/desktop/api/DirectXMath/)</td>
</tr>
<tr class="even">
<td>D3DXVECTOR2_16F</td>
<td>[<strong>XMHALF2</strong>](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmhalf2)</td>
</tr>
<tr class="odd">
<td>D3DXVECTOR3</td>
<td>[<strong>XMFLOAT3</strong>](/windows/desktop/api/DirectXMath/)</td>
</tr>
<tr class="even">
<td>D3DXVECTOR4</td>
<td>[<strong>XMFLOAT4</strong>](/windows/desktop/api/DirectXMath/)(or if you can guarantee the data is 16-byte aligned, [<strong>XMVECTOR</strong>](xmvector-data-type.md) or [<strong>XMFLOAT4A</strong>](/windows/desktop/api/DirectXMath/) )<br/></td>
</tr>
<tr class="odd">
<td>D3DXVECTOR4_16F</td>
<td>[<strong>XMHALF4</strong>](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmhalf4)</td>
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
| D3DXBoxBoundProbe                  | [**BoundingBox::Intersects(XMVECTOR, XMVECTOR, float&)**](https://www.bing.com/search?q=**BoundingBox::Intersects(XMVECTOR, XMVECTOR, float&)**)                                                                                                                                                          |
| D3DXComputeBoundingBox             | [**BoundingBox::CreateFromPoints**](https://www.bing.com/search?q=**BoundingBox::CreateFromPoints**)                                                                                                                                                                          |
| D3DXComputeBoundingSphere          | [**BoundingSphere::CreateFromPoints**](/windows/desktop/api/DirectXCollision/nf-directxcollision-boundingbox-createfrompoints(boundingbox &,size_t,const xmfloat3,size_t))                                                                                                                                                                      |
| D3DXSphereBoundProbe               | [**BoundingSphere::Intersects(XMVECTOR, XMVECTOR, float&)**](https://www.bing.com/search?q=**BoundingSphere::Intersects(XMVECTOR, XMVECTOR, float&)**)                                                                                                                                                    |
| D3DXIntersectTriFunction           | [**TriangleTests::Intersects**](ovw-xnamath-triangletests.md)                                                                                                                                                                                   |
| D3DXFloat32To16Array               | [**XMConvertFloatToHalfStream**](https://www.bing.com/search?q=**XMConvertFloatToHalfStream**)                                                                                                                                                                                 |
| D3DXFloat16To32Array               | [**XMConvertHalfToFloatStream**](https://www.bing.com/search?q=**XMConvertHalfToFloatStream**)                                                                                                                                                                                 |
| D3DXVec2Length                     | [**XMVector2Length**](https://www.bing.com/search?q=**XMVector2Length**) or [**XMVector2LengthEst**](https://www.bing.com/search?q=**XMVector2LengthEst**)                                                                                                                                                   |
| D3DXVec2LengthSq                   | [**XMVector2LengthSq**](https://www.bing.com/search?q=**XMVector2LengthSq**)                                                                                                                                                                                                   |
| D3DXVec2Dot                        | [**XMVector2Dot**](https://www.bing.com/search?q=**XMVector2Dot**)                                                                                                                                                                                                             |
| D3DXVec2CCW                        | [**XMVector2Cross**](https://www.bing.com/search?q=**XMVector2Cross**)                                                                                                                                                                                                         |
| D3DXVec2Add                        | [**XMVectorAdd**](https://www.bing.com/search?q=**XMVectorAdd**)                                                                                                                                                                                                               |
| D3DXVec2Subtract                   | [**XMVectorSubtract**](https://www.bing.com/search?q=**XMVectorSubtract**)                                                                                                                                                                                                     |
| D3DXVec2Minimize                   | [**XMVectorMin**](https://www.bing.com/search?q=**XMVectorMin**)                                                                                                                                                                                                               |
| D3DXVec2Maximize                   | [**XMVectorMax**](https://www.bing.com/search?q=**XMVectorMax**)                                                                                                                                                                                                               |
| D3DXVec2Scale                      | [**XMVectorScale**](https://www.bing.com/search?q=**XMVectorScale**)                                                                                                                                                                                                           |
| D3DXVec2Lerp                       | [**XMVectorLerp**](https://www.bing.com/search?q=**XMVectorLerp**) or [**XMVectorLerpV**](https://www.bing.com/search?q=**XMVectorLerpV**)                                                                                                                                                                   |
| D3DXVec2Normalize                  | [**XMVector2Normalize**](https://www.bing.com/search?q=**XMVector2Normalize**) or [**XMVector2NormalizeEst**](https://www.bing.com/search?q=**XMVector2NormalizeEst**)                                                                                                                                       |
| D3DXVec2Hermite                    | [**XMVectorHermite**](https://www.bing.com/search?q=**XMVectorHermite**) or [**XMVectorHermiteV**](https://www.bing.com/search?q=**XMVectorHermiteV**)                                                                                                                                                       |
| D3DXVec2CatmullRom                 | [**XMVectorCatmullRom**](https://www.bing.com/search?q=**XMVectorCatmullRom**) or [**XMVectorCatmullRomV**](https://www.bing.com/search?q=**XMVectorCatmullRomV**)                                                                                                                                           |
| D3DXVec2BaryCentric                | [**XMVectorBaryCentric**](https://www.bing.com/search?q=**XMVectorBaryCentric**) or [**XMVectorBaryCentricV**](https://www.bing.com/search?q=**XMVectorBaryCentricV**)                                                                                                                                       |
| D3DXVec2Transform                  | [**XMVector2Transform**](https://www.bing.com/search?q=**XMVector2Transform**)                                                                                                                                                                                                 |
| D3DXVec2TransformCoord             | [**XMVector2TransformCoord**](https://www.bing.com/search?q=**XMVector2TransformCoord**)                                                                                                                                                                                       |
| D3DXVec2TransformNormal            | [**XMVector2TransformNormal**](https://www.bing.com/search?q=**XMVector2TransformNormal**)                                                                                                                                                                                     |
| D3DXVec2TransformArray             | [**XMVector2TransformStream**](https://www.bing.com/search?q=**XMVector2TransformStream**)                                                                                                                                                                                     |
| D3DXVec2TransformCoordArray        | [**XMVector2TransformCoordStream**](https://www.bing.com/search?q=**XMVector2TransformCoordStream**)                                                                                                                                                                           |
| D3DXVec2TransformNormalArray       | [**XMVector2TransformNormalStream**](https://www.bing.com/search?q=**XMVector2TransformNormalStream**)                                                                                                                                                                         |
| D3DXVec3Length                     | [**XMVector3Length**](https://www.bing.com/search?q=**XMVector3Length**) or [**XMVector3LengthEst**](https://www.bing.com/search?q=**XMVector3LengthEst**)                                                                                                                                                   |
| D3DXVec3LengthSq                   | [**XMVector3LengthSq**](https://www.bing.com/search?q=**XMVector3LengthSq**)                                                                                                                                                                                                   |
| D3DXVec3Dot                        | [**XMVector3Dot**](https://www.bing.com/search?q=**XMVector3Dot**)                                                                                                                                                                                                             |
| D3DXVec3Cross                      | [**XMVector3Cross**](https://www.bing.com/search?q=**XMVector3Cross**)                                                                                                                                                                                                         |
| D3DXVec3Add                        | [**XMVectorAdd**](https://www.bing.com/search?q=**XMVectorAdd**)                                                                                                                                                                                                               |
| D3DXVec3Subtract                   | [**XMVectorSubtract**](https://www.bing.com/search?q=**XMVectorSubtract**)                                                                                                                                                                                                     |
| D3DXVec3Minimize                   | [**XMVectorMin**](https://www.bing.com/search?q=**XMVectorMin**)                                                                                                                                                                                                               |
| D3DXVec3Maximize                   | [**XMVectorMax**](https://www.bing.com/search?q=**XMVectorMax**)                                                                                                                                                                                                               |
| D3DXVec3Scale                      | [**XMVectorScale**](https://www.bing.com/search?q=**XMVectorScale**)                                                                                                                                                                                                           |
| D3DXVec3Lerp                       | [**XMVectorLerp**](https://www.bing.com/search?q=**XMVectorLerp**) or [**XMVectorLerpV**](https://www.bing.com/search?q=**XMVectorLerpV**)                                                                                                                                                                   |
| D3DXVec3Normalize                  | [**XMVector3Normalize**](https://www.bing.com/search?q=**XMVector3Normalize**) or [**XMVector3NormalizeEst**](https://www.bing.com/search?q=**XMVector3NormalizeEst**)                                                                                                                                       |
| D3DXVec3Hermite                    | [**XMVectorHermite**](https://www.bing.com/search?q=**XMVectorHermite**) or [**XMVectorHermiteV**](https://www.bing.com/search?q=**XMVectorHermiteV**)                                                                                                                                                       |
| D3DXVec3CatmullRom                 | [**XMVectorCatmullRom**](https://www.bing.com/search?q=**XMVectorCatmullRom**) or [**XMVectorCatmullRomV**](https://www.bing.com/search?q=**XMVectorCatmullRomV**)                                                                                                                                           |
| D3DXVec3BaryCentric                | [**XMVectorBaryCentric**](https://www.bing.com/search?q=**XMVectorBaryCentric**) or [**XMVectorBaryCentricV**](https://www.bing.com/search?q=**XMVectorBaryCentricV**)                                                                                                                                       |
| D3DXVec3Transform                  | [**XMVector3Transform**](https://www.bing.com/search?q=**XMVector3Transform**)                                                                                                                                                                                                 |
| D3DXVec3TransformCoord             | [**XMVector3TransformCoord**](https://www.bing.com/search?q=**XMVector3TransformCoord**)                                                                                                                                                                                       |
| D3DXVec3TransformNormal            | [**XMVector3TransformNormal**](https://www.bing.com/search?q=**XMVector3TransformNormal**)                                                                                                                                                                                     |
| D3DXVec3TransformArray             | [**XMVector3TransformStream**](https://www.bing.com/search?q=**XMVector3TransformStream**)                                                                                                                                                                                     |
| D3DXVec3TransformCoordArray        | [**XMVector3TransformCoordStream**](https://www.bing.com/search?q=**XMVector3TransformCoordStream**)                                                                                                                                                                           |
| D3DXVec3TransformNormalArray       | [**XMVector3TransformNormalStream**](https://www.bing.com/search?q=**XMVector3TransformNormalStream**)                                                                                                                                                                         |
| D3DXVec3Project                    | [**XMVector3Project**](https://www.bing.com/search?q=**XMVector3Project**)                                                                                                                                                                                                     |
| D3DXVec3Unproject                  | [**XMVector3Unproject**](https://www.bing.com/search?q=**XMVector3Unproject**)                                                                                                                                                                                                 |
| D3DXVec3ProjectArray               | [**XMVector3ProjectStream**](https://www.bing.com/search?q=**XMVector3ProjectStream**)                                                                                                                                                                                         |
| D3DXVec3UnprojectArray             | [**XMVector3UnprojectStream**](https://www.bing.com/search?q=**XMVector3UnprojectStream**)                                                                                                                                                                                     |
| D3DXVec4Length                     | [**XMVector4Length**](https://www.bing.com/search?q=**XMVector4Length**) or [**XMVector4LengthEst**](https://www.bing.com/search?q=**XMVector4LengthEst**)                                                                                                                                                   |
| D3DXVec4LengthSq                   | [**XMVector4LengthSq**](https://www.bing.com/search?q=**XMVector4LengthSq**)                                                                                                                                                                                                   |
| D3DXVec4Dot                        | [**XMVector4Dot**](https://www.bing.com/search?q=**XMVector4Dot**)                                                                                                                                                                                                             |
| D3DXVec4Add                        | [**XMVectorAdd**](https://www.bing.com/search?q=**XMVectorAdd**)                                                                                                                                                                                                               |
| D3DXVec4Subtract                   | [**XMVectorSubtract**](https://www.bing.com/search?q=**XMVectorSubtract**)                                                                                                                                                                                                     |
| D3DXVec4Minimize                   | [**XMVectorMin**](https://www.bing.com/search?q=**XMVectorMin**)                                                                                                                                                                                                               |
| D3DXVec4Maximize                   | [**XMVectorMax**](https://www.bing.com/search?q=**XMVectorMax**)                                                                                                                                                                                                               |
| D3DXVec4Scale                      | [**XMVectorScale**](https://www.bing.com/search?q=**XMVectorScale**)                                                                                                                                                                                                           |
| D3DXVec4Lerp                       | [**XMVectorLerp**](https://www.bing.com/search?q=**XMVectorLerp**) or [**XMVectorLerpV**](https://www.bing.com/search?q=**XMVectorLerpV**)                                                                                                                                                                   |
| D3DXVec4Cross                      | [**XMVector4Cross**](https://www.bing.com/search?q=**XMVector4Cross**)                                                                                                                                                                                                         |
| D3DXVec4Normalize                  | [**XMVector4Normalize**](https://www.bing.com/search?q=**XMVector4Normalize**) or [**XMVector4NormalizeEst**](https://www.bing.com/search?q=**XMVector4NormalizeEst**)                                                                                                                                       |
| D3DXVec4Hermite                    | [**XMVectorHermite**](https://www.bing.com/search?q=**XMVectorHermite**) or [**XMVectorHermiteV**](https://www.bing.com/search?q=**XMVectorHermiteV**)                                                                                                                                                       |
| D3DXVec4CatmullRom                 | [**XMVectorCatmullRom**](https://www.bing.com/search?q=**XMVectorCatmullRom**) or [**XMVectorCatmullRomV**](https://www.bing.com/search?q=**XMVectorCatmullRomV**)                                                                                                                                           |
| D3DXVec4BaryCentric                | [**XMVectorBaryCentric**](https://www.bing.com/search?q=**XMVectorBaryCentric**) or [**XMVectorBaryCentricV**](https://www.bing.com/search?q=**XMVectorBaryCentricV**)                                                                                                                                       |
| D3DXVec4Transform                  | [**XMVector4Transform**](https://www.bing.com/search?q=**XMVector4Transform**)                                                                                                                                                                                                 |
| D3DXVec4TransformArray             | [**XMVector4TransformStream**](https://www.bing.com/search?q=**XMVector4TransformStream**)                                                                                                                                                                                     |
| D3DXMatrixIdentity                 | [**XMMatrixIdentity**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                     |
| D3DXMatrixDeterminant              | [**XMMatrixDeterminant**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                               |
| D3DXMatrixDecompose                | [**XMMatrixDecompose**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                   |
| D3DXMatrixTranspose                | [**XMMatrixTranspose**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                   |
| D3DXMatrixMultiply                 | [**XMMatrixMultiply**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                     |
| D3DXMatrixMultiplyTranspose        | [**XMMatrixMultiplyTranspose**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                   |
| D3DXMatrixInverse                  | [**XMMatrixInverse**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                       |
| D3DXMatrixScaling                  | [**XMMatrixScaling**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                       |
| D3DXMatrixTranslation              | [**XMMatrixTranslation**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                               |
| D3DXMatrixRotationX                | [**XMMatrixRotationX**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                   |
| D3DXMatrixRotationY                | [**XMMatrixRotationY**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                   |
| D3DXMatrixRotationZ                | [**XMMatrixRotationZ**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                   |
| D3DXMatrixRotationAxis             | [**XMMatrixRotationAxis**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                             |
| D3DXMatrixRotationQuaternion       | [**XMMatrixRotationQuaternion**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                 |
| D3DXMatrixRotationYawPitchRoll     | [**XMMatrixRotationRollPitchYaw**](/windows/desktop/api/DirectXMath/) (Note the order of parameters is different: D3DXMatrixRotationYawPitchRoll takes yaw, pitch, roll, **XMMatrixRotationRollPitchYaw** takes pitch, yaw, roll)                 |
| D3DXMatrixTransformation           | [**XMMatrixTransformation**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                         |
| D3DXMatrixTransformation2D         | [**XMMatrixTransformation2D**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                     |
| D3DXMatrixAffineTransformation     | [**XMMatrixAffineTransformation**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                             |
| D3DXMatrixAffineTransformation2D   | [**XMMatrixAffineTransformation2D**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                         |
| D3DXMatrixLookAtRH                 | [**XMMatrixLookAtRH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                     |
| D3DXMatrixLookAtLH                 | [**XMMatrixLookAtLH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                     |
| D3DXMatrixPerspectiveRH            | [**XMMatrixPerspectiveRH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                           |
| D3DXMatrixPerspectiveLH            | [**XMMatrixPerspectiveLH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                           |
| D3DXMatrixPerspectiveFovRH         | [**XMMatrixPerspectiveFovRH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                     |
| D3DXMatrixPerspectiveFovLH         | [**XMMatrixPerspectiveFovLH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                     |
| D3DXMatrixPerspectiveOffCenterRH   | [**XMMatrixPerspectiveOffCenterRH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                         |
| D3DXMatrixPerspectiveOffCenterLH   | [**XMMatrixPerspectiveOffCenterLH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                         |
| D3DXMatrixOrthoRH                  | [**XMMatrixOrthographicRH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                         |
| D3DXMatrixOrthoLH                  | [**XMMatrixOrthographicLH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                         |
| D3DXMatrixOrthoOffCenterRH         | [**XMMatrixOrthographicOffCenterRH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                       |
| D3DXMatrixOrthoOffCenterLH         | [**XMMatrixOrthographicOffCenterLH**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                       |
| D3DXMatrixShadow                   | [**XMMatrixShadow**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                         |
| D3DXMatrixReflect                  | [**XMMatrixReflect**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                       |
| D3DXQuaternionLength               | [**XMQuaternionLength**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                 |
| D3DXQuaternionLengthSq             | [**XMQuaternionLengthSq**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                             |
| D3DXQuaternionDot                  | [**XMQuaternionDot**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                       |
| D3DXQuaternionIdentity             | [**XMQuaternionIdentity**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                             |
| D3DXQuaternionIsIdentity           | [**XMQuaternionIsIdentity**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                         |
| D3DXQuaternionConjugate            | [**XMQuaternionConjugate**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                           |
| D3DXQuaternionToAxisAngle          | [**XMQuaternionToAxisAngle**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                       |
| D3DXQuaternionRotationMatrix       | [**XMQuaternionRotationMatrix**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                 |
| D3DXQuaternionRotationAxis         | [**XMQuaternionRotationAxis**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                     |
| D3DXQuaternionRotationYawPitchRoll | [**XMQuaternionRotationRollPitchYaw**](/windows/desktop/api/DirectXMath/) (Note the order of parameters is different: D3DXQuaternionRotationYawPitchRoll takes yaw, pitch, roll, **XMQuaternionRotationRollPitchYaw** takes pitch, yaw, roll) |
| D3DXQuaternionMultiply             | [**XMQuaternionMultiply**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                             |
| D3DXQuaternionNormalize            | [**XMQuaternionNormalize**](/windows/desktop/api/DirectXMath/) or [**XMQuaternionNormalizeEst**](/windows/desktop/api/DirectXMath/)                                                                                                                           |
| D3DXQuaternionInverse              | [**XMQuaternionInverse**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                               |
| D3DXQuaternionLn                   | [**XMQuaternionLn**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                         |
| D3DXQuaternionExp                  | [**XMQuaternionExp**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                       |
| D3DXQuaternionSlerp                | [**XMQuaternionSlerp**](/windows/desktop/api/DirectXMath/) or [**XMQuaternionSlerpV**](/windows/desktop/api/DirectXMath/)                                                                                                                                               |
| D3DXQuaternionSquad                | [**XMQuaternionSquad**](/windows/desktop/api/DirectXMath/) or [**XMQuaternionSquadV**](/windows/desktop/api/DirectXMath/)                                                                                                                                               |
| D3DXQuaternionSquadSetup           | [**XMQuaternionSquadSetup**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                         |
| D3DXQuaternionBaryCentric          | [**XMQuaternionBaryCentric**](/windows/desktop/api/DirectXMath/) or [**XMQuaternionBaryCentricV**](/windows/desktop/api/DirectXMath/)                                                                                                                       |
| D3DXPlaneDot                       | [**XMPlaneDot**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                                 |
| D3DXPlaneDotCoord                  | [**XMPlaneDotCoord**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                       |
| D3DXPlaneDotNormal                 | [**XMPlaneDotNormal**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                     |
| D3DXPlaneScale                     | [**XMVectorScale**](https://www.bing.com/search?q=**XMVectorScale**)                                                                                                                                                                                                           |
| D3DXPlaneNormalize                 | [**XMPlaneNormalize**](/windows/desktop/api/DirectXMath/) or [**XMPlaneNormalizeEst**](/windows/desktop/api/DirectXMath/)                                                                                                                                               |
| D3DXPlaneIntersectLine             | [**XMPlaneIntersectLine**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                             |
| D3DXPlaneFromPointNormal           | [**XMPlaneFromPointNormal**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                         |
| D3DXPlaneFromPoints                | [**XMPlaneFromPoints**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                   |
| D3DXPlaneTransform                 | [**XMPlaneTransform**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                     |
| D3DXPlaneTransformArray            | [**XMPlaneTransformStream**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                         |
| D3DXColorNegative                  | [**XMColorNegative**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                       |
| D3DXColorAdd                       | [**XMVectorAdd**](https://www.bing.com/search?q=**XMVectorAdd**)                                                                                                                                                                                                               |
| D3DXColorSubtract                  | [**XMVectorSubtract**](https://www.bing.com/search?q=**XMVectorSubtract**)                                                                                                                                                                                                     |
| D3DXColorScale                     | [**XMVectorScale**](https://www.bing.com/search?q=**XMVectorScale**)                                                                                                                                                                                                           |
| D3DXColorModulate                  | [**XMColorModulate**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                       |
| D3DXColorLerp                      | [**XMVectorLerp**](https://www.bing.com/search?q=**XMVectorLerp**) or [**XMVectorLerpV**](https://www.bing.com/search?q=**XMVectorLerpV**)                                                                                                                                                                   |
| D3DXColorAdjustSaturation          | [**XMColorAdjustSaturation**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                       |
| D3DXColorAdjustContrast            | [**XMColorAdjustContrast**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                           |
| D3DXFresnelTerm                    | [**XMFresnelTerm**](/windows/desktop/api/DirectXMath/)                                                                                                                                                                                                           |



 

> [!Note]  
> [Spherical Harmonics](http://go.microsoft.com/fwlink/p/?LinkId=262885) functions for DirectXMath are available separately. There is no DirectXMath equivalent to **ID3DXMatrixStack**.

 

## Related topics

<dl> <dt>

[DirectXMath Programming Guide](ovw-xnamath-progguide.md)
</dt> </dl>

 

 




