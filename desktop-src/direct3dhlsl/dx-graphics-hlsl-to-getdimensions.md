---
title: GetDimensions (DirectX HLSL Texture Object)
description: Gets texture size information. The syntax block shows all the parameters that are possible in the method declaration. The table in the Remarks section shows which parameters are implemented for each texture-object type.
ms.assetid: b72e54da-382a-4b90-bbfe-0b32effc7c05
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# GetDimensions (DirectX HLSL Texture Object)

Gets texture size information. The syntax block shows all the parameters that are possible in the method declaration. The table in the Remarks section shows which parameters are implemented for each texture-object type.

void Object.GetDimensions( UINT MipLevel, typeX Width, typeX Height, typeX Elements, typeX Depth, typeX NumberOfLevels, typeX NumberOfSamples );



 

typeX denotes that there are two possible types: **uint** or **float**.

## Parameters



| Item                                                                                                                               | Description                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Object"></span><span id="object"></span><span id="OBJECT"></span>*Object*<br/>                                     | Any [texture-object](dx-graphics-hlsl-to-type.md) type except a **Buffer** object.<br/>                                       |
| <span id="MipLevel"></span><span id="miplevel"></span><span id="MIPLEVEL"></span>*MipLevel*<br/>                             | \[in\] A zero-based index that identifies the mipmap level. If this argument is not used, the first mip level is assumed.<br/> |
| <span id="Width"></span><span id="width"></span><span id="WIDTH"></span>*Width*<br/>                                         | \[out\] The texture width, in texels.<br/>                                                                                     |
| <span id="Height"></span><span id="height"></span><span id="HEIGHT"></span>*Height*<br/>                                     | \[out\] The texture height, in texels.<br/>                                                                                    |
| <span id="Elements"></span><span id="elements"></span><span id="ELEMENTS"></span>*Elements*<br/>                             | \[out\] The number of elements in an array.<br/>                                                                               |
| <span id="Depth"></span><span id="depth"></span><span id="DEPTH"></span>*Depth*<br/>                                         | \[out\] The texture depth, in texels.<br/>                                                                                     |
| <span id="NumberOfLevels"></span><span id="numberoflevels"></span><span id="NUMBEROFLEVELS"></span>*NumberOfLevels*<br/>     | \[out\] The number of mipmap levels.<br/>                                                                                      |
| <span id="NumberOfSamples"></span><span id="numberofsamples"></span><span id="NUMBEROFSAMPLES"></span>*NumberOfSamples*<br/> | \[out\] The number of samples.<br/>                                                                                            |



 

## Return Value

None

## Overloaded Methods

This table lists all the different versions of the method; versions differs by the number of input parameters. Notice that for every method that takes integer parameters, there is an overloaded method that takes floating-point parameters.



| Texture-Object Type | Input Parameters                                                               |
|---------------------|--------------------------------------------------------------------------------|
| Texture1D           | UINT MipLevel, UINT Width, UINT NumberOfLevels                                 |
| Texture1D           | UINT Width                                                                     |
| Texture1D           | UINT MipLevel, float Width, float NumberOfLevels                               |
| Texture1D           | float Width                                                                    |
| Texture1DArray      | UINT MipLevel, UINT Width, UINT Elements, UINT NumberOfLevels                  |
| Texture1DArray      | UINT Width, UINT Elements                                                      |
| Texture1DArray      | UINT MipLevel, float Width, float Elements, float NumberOfLevels               |
| Texture1DArray      | float Width, float Elements                                                    |
| Texture2D           | UINT MipLevel, UINT Width, UINT Height, UINT NumberOfLevels                    |
| Texture2D           | UINT Width, UINT Height                                                        |
| Texture2D           | UINT MipLevel, float Width, float Height, float NumberOfLevels                 |
| Texture2D           | float Width, float Height                                                      |
| Texture2DArray      | UINT MipLevel, UINT Width, UINT Height, UINT Elements, UINT NumberOfLevels     |
| Texture2DArray      | UINT Width, UINT Height, UINT Elements                                         |
| Texture2DArray      | UINT MipLevel, float Width, float Height, float Elements, float NumberOfLevels |
| Texture2DArray      | float Width, float Height, float Elements                                      |
| Texture3D           | UINT MipLevel, UINT Width, UINT Height, UINT Depth, UINT NumberOfLevels        |
| Texture3D           | UINT Width, UINT Height, UINT Depth                                            |
| Texture3D           | UINT MipLevel, float Width, float Height, float Depth, float NumberOfLevels    |
| Texture3D           | float Width, float Height, float Depth                                         |
| TextureCube         | UINT MipLevel, UINT Width, UINT Height, UINT NumberOfLevels                    |
| TextureCube         | UINT Width, UINT Height                                                        |
| TextureCube         | UINT MipLevel, float Width, float Height, UINT NumberOfLevels                  |
| TextureCube         | float Width, float Height                                                      |
| TextureCubeArray    | UINT MipLevel, UINT Width, UINT Height, UINT Elements, UINT NumberOfLevels     |
| TextureCubeArray    | UINT Width, UINT Height, UINT Elements                                         |
| TextureCubeArray    | UINT MipLevel, float Width, float Height, float Elements, float NumberOfLevels |
| TextureCubeArray    | float Width, float Height, float Elements                                      |
| Texture2DMS         | UINT Width, UINT Height, UINT Samples                                          |
| Texture2DMS         | float Width, float Height, float Samples                                       |
| Texture2DMSArray    | UINT Width, UINT Height, UINT Elements, UINT Samples                           |
| Texture2DMSArray    | float Width, float Height, float Elements, float Samples                       |



 

## Minimum Shader Model

This function is supported in the following shader models.



| vs\_4\_0 | vs\_4\_1  | ps\_4\_0 | ps\_4\_1  | gs\_4\_0 | gs\_4\_1  |
|----------|-----------|----------|-----------|----------|-----------|
| x        | x         | x        | x         | x        | x         |



 

1.  Returns dimensions for the largest (zeroth) mipmap level.
2.  TextureCubeArray is available in Shader Model 4.1 or higher.
3.  Shader Model 4.1 is available in Direct3D 10.1 or higher.

## Related topics

<dl> <dt>

[Texture-Object](dx-graphics-hlsl-to-type.md)
</dt> </dl>

 

 





