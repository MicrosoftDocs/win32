---
description: Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost, or before resetting a device.
ms.assetid: 1abc4e01-65c6-4034-8cbb-891a2234ad33
title: ID3DXFont::OnLostDevice method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFont.OnLostDevice
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXFont::OnLostDevice method

Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost, or before resetting a device.

## Syntax


```C++
HRESULT OnLostDevice();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

This method should be called whenever the device is lost or before the user calls [**Reset**](/windows/desktop/api). Even if the device was not actually lost, **OnLostDevice** is responsible for freeing stateblocks and other resources that may need to be released before resetting the device. As a result, the font object cannot be used again before calling **Reset** and then [**OnResetDevice**](id3dxfont--onresetdevice.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXFont](id3dxfont.md)
</dt> </dl>

 

 




