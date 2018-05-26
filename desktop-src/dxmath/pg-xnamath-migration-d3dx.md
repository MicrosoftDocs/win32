---
Description: D3DXMath is a math helper library for Direct3D applications.
ms.assetid: 3067d47f-9b1d-2051-fa24-2094418ea272
title: Working with D3DXMath
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Both DirectXMath and D3DXMath are optional when working with Direct3D. Direct3D 9 defined D3DMATRIX and D3DCOLOR as part of the Direct3D API in support of the (now legacy) fixed-function pipeline. D3DXMath in D3DX9 extends these Direct3D 9 types with common graphics math operations. For Direct3D 10.x and Direct3D 11, the API uses only the programmable pipeline so there is no API-specific structure for either matrices or color values. When the newer APIs require a color value, they take an explicit array of float values or a generic buffer of constant data that is interpreted by the HLSL shader. HLSL itself can support either row-major or column-major matrix formats, so the layout is entirely up to you (for more info, see HLSL, [Matrix Ordering](direct3dhlsl.dx_graphics_hlsl_per_component_math#matrix-ordering); if you use column-major matrix formats in your shaders, you need to transpose the DirectXMath matrix data as you place it into your constant buffer structures). While optional, the DirectXMath and D3DXMath libraries both provide common graphics related functionality, and are therefore extremely convenient when doing Direct3D programming.

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
<td>[<strong>XMFLOAT4X4</strong>](/windows/win32/DirectXMath/?branch=master)</td>
</tr>
<tr class="odd">
<td>D3DXMATRIXA16</td>
<td>[<strong>XMMATRIX</strong>](/windows/win32/DirectXMath/?branch=master) or [<strong>XMFLOAT4X4A</strong>](/windows/win32/DirectXMath/?branch=master)</td>
</tr>
<tr class="even">
<td>D3DXQUATERNION<br/> D3DXPLANE<br/> D3DXCOLOR<br/></td>
<td>[<strong>XMVECTOR</strong>](xmvector-data-type.md) is used rather than having unique types, so you will likely need to use an [<strong>XMFLOAT4</strong>](/windows/win32/DirectXMath/?branch=master)
<blockquote>
[!Note]<br />
[<strong>D3DXQUATERNION::operator *</strong>](direct3d9.d3dxquaternion_extensions) calls the [<strong>D3DXQuaternionMultiply</strong>](direct3d9.d3dxquaternionmultiply) function, which multiplies two quaternions. But, unless you explicitly use the [<strong>XMQuaternionMultiply</strong>](/windows/win32/DirectXMath/?branch=master) function, you get an incorrect answer when you use [<strong>XMVECTOR::operator *</strong>](xmvector-operator-mul.md) on a quaternion.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>D3DXVECTOR2</td>
<td>[<strong>XMFLOAT2</strong>](/windows/win32/DirectXMath/?branch=master)</td>
</tr>
<tr class="even">
<td>D3DXVECTOR2_16F</td>
<td>[<strong>XMHALF2</strong>](/windows/win32/DirectXPackedVector/ns-directxpackedvector-xmhalf2?branch=master)</td>
</tr>
<tr class="odd">
<td>D3DXVECTOR3</td>
<td>[<strong>XMFLOAT3</strong>](/windows/win32/DirectXMath/?branch=master)</td>
</tr>
<tr class="even">
<td>D3DXVECTOR4</td>
<td>[<strong>XMFLOAT4</strong>](/windows/win32/DirectXMath/?branch=master)(or if you can guarantee the data is 16-byte aligned, [<strong>XMVECTOR</strong>](xmvector-data-type.md) or [<strong>XMFLOAT4A</strong>](/windows/win32/DirectXMath/?branch=master) )<br/></td>
</tr>
<tr class="odd">
<td>D3DXVECTOR4_16F</td>
<td>[<strong>XMHALF4</strong>](/windows/win32/DirectXPackedVector/ns-directxpackedvector-xmhalf4?branch=master)</td>
</tr>
</tbody>
</table>



 

> [!Note]  
> There is no direct equivalent to D3DXVECTOR3\_16F in XNAMath.

 



| D3DXMath Macro | DirectXMath Equivalent                            |
|----------------|---------------------------------------------------|
| D3DX\_PI       | [XM\_PI](ovw-xnamath-reference-constants.md)     |
| D3DX\_1BYPI    | [XM\_1DIVPI](ovw-xnamath-reference-constants.md) |
| D3DXToRadian   | [**XMConvertToRadians**](/windows/win32/DirectXMath/nf-directxmath-xmconverttoradians?branch=master)  |
| D3DXToDegree   | [**XMConvertToDegrees**](/windows/win32/DirectXMath/nf-directxmath-xmconverttodegrees?branch=master)  |



 



| D3DXMath Function                  | DirectXMath Equivalent                                                                                                                                                                                                                           |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DXBoxBoundProbe                  | [**BoundingBox::Intersects(XMVECTOR, XMVECTOR, float&)**](boundingbox-intersects-2.md)                                                                                                                                                          |
| D3DXComputeBoundingBox             | [**BoundingBox::CreateFromPoints**](boundingbox-createfrompoints-2.md)                                                                                                                                                                          |
| D3DXComputeBoundingSphere          | [**BoundingSphere::CreateFromPoints**](/windows/win32/DirectXCollision/?branch=master)                                                                                                                                                                      |
| D3DXSphereBoundProbe               | [**BoundingSphere::Intersects(XMVECTOR, XMVECTOR, float&)**](boundingsphere-intersects-2.md)                                                                                                                                                    |
| D3DXIntersectTriFunction           | [**TriangleTests::Intersects**](ovw-xnamath-triangletests.md)                                                                                                                                                                                   |
| D3DXFloat32To16Array               | [**XMConvertFloatToHalfStream**](xmconvertfloattohalfstream.md)                                                                                                                                                                                 |
| D3DXFloat16To32Array               | [**XMConvertHalfToFloatStream**](xmconverthalftofloatstream.md)                                                                                                                                                                                 |
| D3DXVec2Length                     | [**XMVector2Length**](xmvector2length.md) or [**XMVector2LengthEst**](xmvector2lengthest.md)                                                                                                                                                   |
| D3DXVec2LengthSq                   | [**XMVector2LengthSq**](xmvector2lengthsq.md)                                                                                                                                                                                                   |
| D3DXVec2Dot                        | [**XMVector2Dot**](xmvector2dot.md)                                                                                                                                                                                                             |
| D3DXVec2CCW                        | [**XMVector2Cross**](xmvector2cross.md)                                                                                                                                                                                                         |
| D3DXVec2Add                        | [**XMVectorAdd**](xmvectoradd.md)                                                                                                                                                                                                               |
| D3DXVec2Subtract                   | [**XMVectorSubtract**](xmvectorsubtract.md)                                                                                                                                                                                                     |
| D3DXVec2Minimize                   | [**XMVectorMin**](xmvectormin.md)                                                                                                                                                                                                               |
| D3DXVec2Maximize                   | [**XMVectorMax**](xmvectormax.md)                                                                                                                                                                                                               |
| D3DXVec2Scale                      | [**XMVectorScale**](xmvectorscale.md)                                                                                                                                                                                                           |
| D3DXVec2Lerp                       | [**XMVectorLerp**](xmvectorlerp.md) or [**XMVectorLerpV**](xmvectorlerpv.md)                                                                                                                                                                   |
| D3DXVec2Normalize                  | [**XMVector2Normalize**](xmvector2normalize.md) or [**XMVector2NormalizeEst**](xmvector2normalizeest.md)                                                                                                                                       |
| D3DXVec2Hermite                    | [**XMVectorHermite**](xmvectorhermite.md) or [**XMVectorHermiteV**](xmvectorhermitev.md)                                                                                                                                                       |
| D3DXVec2CatmullRom                 | [**XMVectorCatmullRom**](xmvectorcatmullrom.md) or [**XMVectorCatmullRomV**](xmvectorcatmullromv.md)                                                                                                                                           |
| D3DXVec2BaryCentric                | [**XMVectorBaryCentric**](xmvectorbarycentric.md) or [**XMVectorBaryCentricV**](xmvectorbarycentricv.md)                                                                                                                                       |
| D3DXVec2Transform                  | [**XMVector2Transform**](xmvector2transform.md)                                                                                                                                                                                                 |
| D3DXVec2TransformCoord             | [**XMVector2TransformCoord**](xmvector2transformcoord.md)                                                                                                                                                                                       |
| D3DXVec2TransformNormal            | [**XMVector2TransformNormal**](xmvector2transformnormal.md)                                                                                                                                                                                     |
| D3DXVec2TransformArray             | [**XMVector2TransformStream**](xmvector2transformstream.md)                                                                                                                                                                                     |
| D3DXVec2TransformCoordArray        | [**XMVector2TransformCoordStream**](xmvector2transformcoordstream.md)                                                                                                                                                                           |
| D3DXVec2TransformNormalArray       | [**XMVector2TransformNormalStream**](xmvector2transformnormalstream.md)                                                                                                                                                                         |
| D3DXVec3Length                     | [**XMVector3Length**](xmvector3length.md) or [**XMVector3LengthEst**](xmvector3lengthest.md)                                                                                                                                                   |
| D3DXVec3LengthSq                   | [**XMVector3LengthSq**](xmvector3lengthsq.md)                                                                                                                                                                                                   |
| D3DXVec3Dot                        | [**XMVector3Dot**](xmvector3dot.md)                                                                                                                                                                                                             |
| D3DXVec3Cross                      | [**XMVector3Cross**](xmvector3cross.md)                                                                                                                                                                                                         |
| D3DXVec3Add                        | [**XMVectorAdd**](xmvectoradd.md)                                                                                                                                                                                                               |
| D3DXVec3Subtract                   | [**XMVectorSubtract**](xmvectorsubtract.md)                                                                                                                                                                                                     |
| D3DXVec3Minimize                   | [**XMVectorMin**](xmvectormin.md)                                                                                                                                                                                                               |
| D3DXVec3Maximize                   | [**XMVectorMax**](xmvectormax.md)                                                                                                                                                                                                               |
| D3DXVec3Scale                      | [**XMVectorScale**](xmvectorscale.md)                                                                                                                                                                                                           |
| D3DXVec3Lerp                       | [**XMVectorLerp**](xmvectorlerp.md) or [**XMVectorLerpV**](xmvectorlerpv.md)                                                                                                                                                                   |
| D3DXVec3Normalize                  | [**XMVector3Normalize**](xmvector3normalize.md) or [**XMVector3NormalizeEst**](xmvector3normalizeest.md)                                                                                                                                       |
| D3DXVec3Hermite                    | [**XMVectorHermite**](xmvectorhermite.md) or [**XMVectorHermiteV**](xmvectorhermitev.md)                                                                                                                                                       |
| D3DXVec3CatmullRom                 | [**XMVectorCatmullRom**](xmvectorcatmullrom.md) or [**XMVectorCatmullRomV**](xmvectorcatmullromv.md)                                                                                                                                           |
| D3DXVec3BaryCentric                | [**XMVectorBaryCentric**](xmvectorbarycentric.md) or [**XMVectorBaryCentricV**](xmvectorbarycentricv.md)                                                                                                                                       |
| D3DXVec3Transform                  | [**XMVector3Transform**](xmvector3transform.md)                                                                                                                                                                                                 |
| D3DXVec3TransformCoord             | [**XMVector3TransformCoord**](xmvector3transformcoord.md)                                                                                                                                                                                       |
| D3DXVec3TransformNormal            | [**XMVector3TransformNormal**](xmvector3transformnormal.md)                                                                                                                                                                                     |
| D3DXVec3TransformArray             | [**XMVector3TransformStream**](xmvector3transformstream.md)                                                                                                                                                                                     |
| D3DXVec3TransformCoordArray        | [**XMVector3TransformCoordStream**](xmvector3transformcoordstream.md)                                                                                                                                                                           |
| D3DXVec3TransformNormalArray       | [**XMVector3TransformNormalStream**](xmvector3transformnormalstream.md)                                                                                                                                                                         |
| D3DXVec3Project                    | [**XMVector3Project**](xmvector3project.md)                                                                                                                                                                                                     |
| D3DXVec3Unproject                  | [**XMVector3Unproject**](xmvector3unproject.md)                                                                                                                                                                                                 |
| D3DXVec3ProjectArray               | [**XMVector3ProjectStream**](xmvector3projectstream.md)                                                                                                                                                                                         |
| D3DXVec3UnprojectArray             | [**XMVector3UnprojectStream**](xmvector3unprojectstream.md)                                                                                                                                                                                     |
| D3DXVec4Length                     | [**XMVector4Length**](xmvector4length.md) or [**XMVector4LengthEst**](xmvector4lengthest.md)                                                                                                                                                   |
| D3DXVec4LengthSq                   | [**XMVector4LengthSq**](xmvector4lengthsq.md)                                                                                                                                                                                                   |
| D3DXVec4Dot                        | [**XMVector4Dot**](xmvector4dot.md)                                                                                                                                                                                                             |
| D3DXVec4Add                        | [**XMVectorAdd**](xmvectoradd.md)                                                                                                                                                                                                               |
| D3DXVec4Subtract                   | [**XMVectorSubtract**](xmvectorsubtract.md)                                                                                                                                                                                                     |
| D3DXVec4Minimize                   | [**XMVectorMin**](xmvectormin.md)                                                                                                                                                                                                               |
| D3DXVec4Maximize                   | [**XMVectorMax**](xmvectormax.md)                                                                                                                                                                                                               |
| D3DXVec4Scale                      | [**XMVectorScale**](xmvectorscale.md)                                                                                                                                                                                                           |
| D3DXVec4Lerp                       | [**XMVectorLerp**](xmvectorlerp.md) or [**XMVectorLerpV**](xmvectorlerpv.md)                                                                                                                                                                   |
| D3DXVec4Cross                      | [**XMVector4Cross**](xmvector4cross.md)                                                                                                                                                                                                         |
| D3DXVec4Normalize                  | [**XMVector4Normalize**](xmvector4normalize.md) or [**XMVector4NormalizeEst**](xmvector4normalizeest.md)                                                                                                                                       |
| D3DXVec4Hermite                    | [**XMVectorHermite**](xmvectorhermite.md) or [**XMVectorHermiteV**](xmvectorhermitev.md)                                                                                                                                                       |
| D3DXVec4CatmullRom                 | [**XMVectorCatmullRom**](xmvectorcatmullrom.md) or [**XMVectorCatmullRomV**](xmvectorcatmullromv.md)                                                                                                                                           |
| D3DXVec4BaryCentric                | [**XMVectorBaryCentric**](xmvectorbarycentric.md) or [**XMVectorBaryCentricV**](xmvectorbarycentricv.md)                                                                                                                                       |
| D3DXVec4Transform                  | [**XMVector4Transform**](xmvector4transform.md)                                                                                                                                                                                                 |
| D3DXVec4TransformArray             | [**XMVector4TransformStream**](xmvector4transformstream.md)                                                                                                                                                                                     |
| D3DXMatrixIdentity                 | [**XMMatrixIdentity**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                     |
| D3DXMatrixDeterminant              | [**XMMatrixDeterminant**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                               |
| D3DXMatrixDecompose                | [**XMMatrixDecompose**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                   |
| D3DXMatrixTranspose                | [**XMMatrixTranspose**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                   |
| D3DXMatrixMultiply                 | [**XMMatrixMultiply**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                     |
| D3DXMatrixMultiplyTranspose        | [**XMMatrixMultiplyTranspose**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                   |
| D3DXMatrixInverse                  | [**XMMatrixInverse**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                       |
| D3DXMatrixScaling                  | [**XMMatrixScaling**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                       |
| D3DXMatrixTranslation              | [**XMMatrixTranslation**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                               |
| D3DXMatrixRotationX                | [**XMMatrixRotationX**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                   |
| D3DXMatrixRotationY                | [**XMMatrixRotationY**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                   |
| D3DXMatrixRotationZ                | [**XMMatrixRotationZ**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                   |
| D3DXMatrixRotationAxis             | [**XMMatrixRotationAxis**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                             |
| D3DXMatrixRotationQuaternion       | [**XMMatrixRotationQuaternion**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                 |
| D3DXMatrixRotationYawPitchRoll     | [**XMMatrixRotationRollPitchYaw**](/windows/win32/DirectXMath/?branch=master) (Note the order of parameters is different: D3DXMatrixRotationYawPitchRoll takes yaw, pitch, roll, **XMMatrixRotationRollPitchYaw** takes pitch, yaw, roll)                 |
| D3DXMatrixTransformation           | [**XMMatrixTransformation**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                         |
| D3DXMatrixTransformation2D         | [**XMMatrixTransformation2D**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                     |
| D3DXMatrixAffineTransformation     | [**XMMatrixAffineTransformation**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                             |
| D3DXMatrixAffineTransformation2D   | [**XMMatrixAffineTransformation2D**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                         |
| D3DXMatrixLookAtRH                 | [**XMMatrixLookAtRH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                     |
| D3DXMatrixLookAtLH                 | [**XMMatrixLookAtLH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                     |
| D3DXMatrixPerspectiveRH            | [**XMMatrixPerspectiveRH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                           |
| D3DXMatrixPerspectiveLH            | [**XMMatrixPerspectiveLH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                           |
| D3DXMatrixPerspectiveFovRH         | [**XMMatrixPerspectiveFovRH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                     |
| D3DXMatrixPerspectiveFovLH         | [**XMMatrixPerspectiveFovLH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                     |
| D3DXMatrixPerspectiveOffCenterRH   | [**XMMatrixPerspectiveOffCenterRH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                         |
| D3DXMatrixPerspectiveOffCenterLH   | [**XMMatrixPerspectiveOffCenterLH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                         |
| D3DXMatrixOrthoRH                  | [**XMMatrixOrthographicRH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                         |
| D3DXMatrixOrthoLH                  | [**XMMatrixOrthographicLH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                         |
| D3DXMatrixOrthoOffCenterRH         | [**XMMatrixOrthographicOffCenterRH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                       |
| D3DXMatrixOrthoOffCenterLH         | [**XMMatrixOrthographicOffCenterLH**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                       |
| D3DXMatrixShadow                   | [**XMMatrixShadow**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                         |
| D3DXMatrixReflect                  | [**XMMatrixReflect**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                       |
| D3DXQuaternionLength               | [**XMQuaternionLength**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                 |
| D3DXQuaternionLengthSq             | [**XMQuaternionLengthSq**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                             |
| D3DXQuaternionDot                  | [**XMQuaternionDot**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                       |
| D3DXQuaternionIdentity             | [**XMQuaternionIdentity**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                             |
| D3DXQuaternionIsIdentity           | [**XMQuaternionIsIdentity**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                         |
| D3DXQuaternionConjugate            | [**XMQuaternionConjugate**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                           |
| D3DXQuaternionToAxisAngle          | [**XMQuaternionToAxisAngle**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                       |
| D3DXQuaternionRotationMatrix       | [**XMQuaternionRotationMatrix**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                 |
| D3DXQuaternionRotationAxis         | [**XMQuaternionRotationAxis**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                     |
| D3DXQuaternionRotationYawPitchRoll | [**XMQuaternionRotationRollPitchYaw**](/windows/win32/DirectXMath/?branch=master) (Note the order of parameters is different: D3DXQuaternionRotationYawPitchRoll takes yaw, pitch, roll, **XMQuaternionRotationRollPitchYaw** takes pitch, yaw, roll) |
| D3DXQuaternionMultiply             | [**XMQuaternionMultiply**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                             |
| D3DXQuaternionNormalize            | [**XMQuaternionNormalize**](/windows/win32/DirectXMath/?branch=master) or [**XMQuaternionNormalizeEst**](/windows/win32/DirectXMath/?branch=master)                                                                                                                           |
| D3DXQuaternionInverse              | [**XMQuaternionInverse**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                               |
| D3DXQuaternionLn                   | [**XMQuaternionLn**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                         |
| D3DXQuaternionExp                  | [**XMQuaternionExp**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                       |
| D3DXQuaternionSlerp                | [**XMQuaternionSlerp**](/windows/win32/DirectXMath/?branch=master) or [**XMQuaternionSlerpV**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                               |
| D3DXQuaternionSquad                | [**XMQuaternionSquad**](/windows/win32/DirectXMath/?branch=master) or [**XMQuaternionSquadV**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                               |
| D3DXQuaternionSquadSetup           | [**XMQuaternionSquadSetup**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                         |
| D3DXQuaternionBaryCentric          | [**XMQuaternionBaryCentric**](/windows/win32/DirectXMath/?branch=master) or [**XMQuaternionBaryCentricV**](/windows/win32/DirectXMath/?branch=master)                                                                                                                       |
| D3DXPlaneDot                       | [**XMPlaneDot**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                                 |
| D3DXPlaneDotCoord                  | [**XMPlaneDotCoord**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                       |
| D3DXPlaneDotNormal                 | [**XMPlaneDotNormal**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                     |
| D3DXPlaneScale                     | [**XMVectorScale**](xmvectorscale.md)                                                                                                                                                                                                           |
| D3DXPlaneNormalize                 | [**XMPlaneNormalize**](/windows/win32/DirectXMath/?branch=master) or [**XMPlaneNormalizeEst**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                               |
| D3DXPlaneIntersectLine             | [**XMPlaneIntersectLine**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                             |
| D3DXPlaneFromPointNormal           | [**XMPlaneFromPointNormal**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                         |
| D3DXPlaneFromPoints                | [**XMPlaneFromPoints**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                   |
| D3DXPlaneTransform                 | [**XMPlaneTransform**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                     |
| D3DXPlaneTransformArray            | [**XMPlaneTransformStream**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                         |
| D3DXColorNegative                  | [**XMColorNegative**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                       |
| D3DXColorAdd                       | [**XMVectorAdd**](xmvectoradd.md)                                                                                                                                                                                                               |
| D3DXColorSubtract                  | [**XMVectorSubtract**](xmvectorsubtract.md)                                                                                                                                                                                                     |
| D3DXColorScale                     | [**XMVectorScale**](xmvectorscale.md)                                                                                                                                                                                                           |
| D3DXColorModulate                  | [**XMColorModulate**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                       |
| D3DXColorLerp                      | [**XMVectorLerp**](xmvectorlerp.md) or [**XMVectorLerpV**](xmvectorlerpv.md)                                                                                                                                                                   |
| D3DXColorAdjustSaturation          | [**XMColorAdjustSaturation**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                       |
| D3DXColorAdjustContrast            | [**XMColorAdjustContrast**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                           |
| D3DXFresnelTerm                    | [**XMFresnelTerm**](/windows/win32/DirectXMath/?branch=master)                                                                                                                                                                                                           |



 

> [!Note]  
> [Spherical Harmonics](http://go.microsoft.com/fwlink/p/?LinkId=262885) functions for DirectXMath are available separately. There is no DirectXMath equivalent to **ID3DXMatrixStack**.

 

## Related topics

<dl> <dt>

[DirectXMath Programming Guide](ovw-xnamath-progguide.md)
</dt> </dl>

 

 




