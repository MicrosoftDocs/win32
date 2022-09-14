---
title: Direct3D 11 on Downlevel Hardware
description: This section discusses how Direct3D 11 is designed to support both new and existing hardware, from DirectX 9 to DirectX 11.
ms.assetid: 9a1ca4ff-df3d-46e5-8895-37199523343e
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 11 on Downlevel Hardware

This section discusses how Direct3D 11 is designed to support both new and existing hardware, from DirectX 9 to DirectX 11.

This diagram shows how Direct3D 11 supports new and existing hardware.

![diagram of the hardware that direct3d 11 supports](images/d3d11-on-downlevel-hardware.png)

With Direct3D 11, a new paradigm is introduced called feature levels. A feature level is a well defined set of GPU functionality. Using a feature level, you can target a Direct3D application to run on a downlevel version of Direct3D hardware.

The [10Level9 Reference](d3d11-graphics-reference-10level9.md) section lists the differences between how various [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) and [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext) methods behave at various 10Level9 feature levels.


## In this section



| Topic                                                                                                                  | Description                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Direct3D feature levels](overviews-direct3d-11-devices-downlevel-intro.md)<br/>                                | This topic discusses Direct3D feature levels.<br/>                                                                                                                       |
| [Exceptions](overviews-direct3d-11-devices-downlevel-exceptions.md)<br/>                                        | This topic describes exceptions when using Direct3D 11 on downlevel hardware. <br/>                                                                                      |
| [Compute Shaders on Downlevel Hardware](overviews-direct3d-11-devices-downlevel-compute-shaders.md)<br/>        | This topic discusses how to make use of [compute shaders](direct3d-11-advanced-stages-compute-shader.md) in a Direct3D 11 app on Direct3D 10 hardware.<br/>             |
| [Preventing Unwanted NULL Pixel Shader SRVs](overviews-direct3d-11-devices-downlevel-prevent-null-srvs.md)<br/> | This topic discusses how to work around the driver receiving **NULL** shader-resource views (SRVs) even when non-**NULL** SRVs are bound to the pixel shader stage.<br/> |



 

## How to topics about feature levels



| Topic                                                                                                                                                                                                                                                                   | Description                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| <span id="How_To__Get_the_Device_Feature_Level"></span><span id="how_to__get_the_device_feature_level"></span><span id="HOW_TO__GET_THE_DEVICE_FEATURE_LEVEL"></span>[How To: Get the Device Feature Level](overviews-direct3d-11-devices-downlevel-get.md)<br/> | How to get a feature level.<br/> |



 

## Related topics

<dl> <dt>

[Devices](overviews-direct3d-11-devices.md)
</dt> </dl>

 

 





