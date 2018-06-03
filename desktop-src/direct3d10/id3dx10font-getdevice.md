---
Description: Retrieve the Direct3D device associated with the font object.
ms.assetid: aad2406e-9461-4a84-9875-74b53d68ef40
title: ID3DX10Font::GetDevice method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DX10Font::GetDevice method

Retrieve the Direct3D device associated with the font object.

## Syntax


```C++
HRESULT GetDevice(
  [out] ID3D10Device **ppDevice
);
```



## Parameters

<dl> <dt>

*ppDevice* \[out\]
</dt> <dd>

Type: **[**ID3D10Device**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device)\*\***

Address of a pointer to an ID3D10Device interface, representing the Direct3D device object associated with the font object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

> [!Note]  
> Calling this method will increase the internal reference count on the ID3D10Device interface. Be sure to call IUnknown when you are done using this ID3D10Device interface or you will have a memory leak.

 

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Font](id3dx10font.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




