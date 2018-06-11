---
Description: Destroys a previously allocated kernel-mode Microsoft DirectDraw surface object that was created with the dwCaps member of the DDSCAPS structure set to DDSCAPS\_EXECUTEBUFFER.
ms.assetid: c737b706-25be-49b8-8d8c-35f48aea2889
title: NtGdiDdDestroyD3DBuffer function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NtGdiDdDestroyD3DBuffer function

\[This function is subject to change with each operating system revision. Instead, use the DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Destroys a previously allocated kernel-mode Microsoft DirectDraw surface object that was created with the **dwCaps** member of the [**DDSCAPS**](https://msdn.microsoft.com/windows/desktop/e1ed1fa2-2f3c-4d04-a601-c11fb77eb5cc) structure set to DDSCAPS\_EXECUTEBUFFER.

## Syntax


```C++
DWORD APIENTRY NtGdiDdDestroyD3DBuffer(
  _In_ HANDLE hSurface
);
```



## Parameters

<dl> <dt>

*hSurface* \[in\]
</dt> <dd>

Handle to a [**DD\_DESTROYSURFACEDATA**](https://msdn.microsoft.com/windows/desktop/77d9544d-72df-4e7d-ba57-644aeee34a88) structure that contains the information needed to destroy a Direct3D command or vertex buffer.

</dd> </dl>

## Return value

**NtGdiDdDestroyD3DBuffer** returns one of the following callback codes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDHAL\_DRIVER\_HANDLED**</dt> </dl>    | The driver has performed the operation and returned a valid return code for that operation. If this code is DD\_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function.<br/>                                                                                 |
| <dl> <dt>**DDHAL\_DRIVER\_NOTHANDLED**</dt> </dl> | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation.<br/> |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Ntgdi.h</dt> </dl> |



## See also

<dl> <dt>

[Graphics Low Level Client Support](-dxgkernel-low-level-client-support.md)
</dt> </dl>

 

 




