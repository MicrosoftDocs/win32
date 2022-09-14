---
description: Renders primitives and returns the updated render state.
ms.assetid: ef28ee62-a7ad-406c-a892-ffee14123d16
title: NtGdiD3DDrawPrimitives2 function (Ntgdi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtGdiD3DDrawPrimitives2
api_type: 
- HeaderDef
api_location: 
- Ntgdi.h
---

# NtGdiD3DDrawPrimitives2 function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Renders primitives and returns the updated render state.

## Syntax


```C++
DWORD APIENTRY NtGdiD3DDrawPrimitives2(
  _In_    HANDLE                         hCmdBuf,
  _In_    HANDLE                         hVBuf,
  _Inout_ LPD3DNTHAL_DRAWPRIMITIVES2DATA pded,
  _Inout_ FLATPTR                        *pfpVidMemCmd,
  _Inout_ DWORD                          *pdwSizeCmd,
  _Inout_ FLATPTR                        *pfpVidMemVtx,
  _Inout_ DWORD                          *pdwSizeVtx
);
```



## Parameters

<dl> <dt>

*hCmdBuf* \[in\]
</dt> <dd>

Handle to the [**DD\_SURFACE\_LOCAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_local) structure that identifies the DirectDraw surface containing the command data.

</dd> <dt>

*hVBuf* \[in\]
</dt> <dd>

Handle to the [**DD\_SURFACE\_LOCAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_local) structure that identifies the DirectDraw surface containing the vertex data.

</dd> <dt>

*pded* \[in, out\]
</dt> <dd>

Pointer to a [**D3DNTHAL\_DRAWPRIMITIVES2DATA**](/windows-hardware/drivers/ddi/) structure that contains the information required for the driver to render one or more primitives.

</dd> <dt>

*pfpVidMemCmd* \[in, out\]
</dt> <dd>

New pointer to video memory if the driver swapped the command buffer.

</dd> <dt>

*pdwSizeCmd* \[in, out\]
</dt> <dd>

Specifies the minimum number of bytes that the driver must increase the swap command buffer by.

</dd> <dt>

*pfpVidMemVtx* \[in, out\]
</dt> <dd>

New pointer to video memory if the driver swapped the vertex buffer.

</dd> <dt>

*pdwSizeVtx* \[in, out\]
</dt> <dd>

Specifies the minimum number of bytes that the driver must allocate for the swap vertex buffer.

</dd> </dl>

## Return value

**NtGdiD3DDrawPrimitives2** returns one of the following callback codes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDHAL\_DRIVER\_HANDLED**</dt> </dl>    | The driver has performed the operation and returned a valid return code for that operation. If this code is DD\_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function.<br/>                                                                                 |
| <dl> <dt>**DDHAL\_DRIVER\_NOTHANDLED**</dt> </dl> | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Ntgdi.h</dt> </dl> |



## See also

<dl> <dt>

[Graphics Low Level Client Support](-dxgkernel-low-level-client-support.md)
</dt> </dl>

 

 
