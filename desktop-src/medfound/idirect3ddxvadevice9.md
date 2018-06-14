---
Description: Represents a hardware accelerator for DirectX Video Acceleration (DXVA) 1.0.
ms.assetid: 63f77cf9-4c04-4ddb-9582-cfcf86f66a2a
title: IDirect3DDXVADevice9 interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IDirect3DDXVADevice9 interface

Represents a hardware accelerator for DirectX Video Acceleration (DXVA) 1.0.

## Members

The **IDirect3DDXVADevice9** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface. **IDirect3DDXVADevice9** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDirect3DDXVADevice9** interface has these methods.



| Method                                                  | Description                                                           |
|:--------------------------------------------------------|:----------------------------------------------------------------------|
| [**BeginFrame**](idirect3ddxvadevice9-beginframe.md)   | Begins the processing to create a decoded picture.<br/>         |
| [**EndFrame**](idirect3ddxvadevice9-endframe.md)       | Ends the processing to create a decoded picture.<br/>           |
| [**Execute**](idirect3ddxvadevice9-execute.md)         | Performs a DXVA decoding operation. <br/>                       |
| [**QueryStatus**](idirect3ddxvadevice9-querystatus.md) | Queries the read/write status of a DXVA decoding surface. <br/> |



 

## Remarks

To get a pointer to this interface, call [**IDirect3DVideoDevice9::CreateDXVADevice**](idirect3dvideodevice9-createdxvadevice.md).

## Requirements



|                                     |                                                                                   |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Dxva.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Video Interfaces](direct3d-video-interfaces.md)
</dt> </dl>

 

 




