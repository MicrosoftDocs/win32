---
Description: 'Attaches a surface to another surface.'
ms.assetid: '4fd757c7-9e32-4737-b666-3226f6cf29fa'
title: NtGdiDdCreateSurface function
---

# NtGdiDdCreateSurface function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Attaches a surface to another surface.

## Syntax


```C++
DWORD APIENTRY NtGdiDdCreateSurface(
  _In_    HANDLE               hDirectDraw,
  _In_    HANDLE               *hSurface,
  _Inout_ DDSURFACEDESC        *puSurfaceDescription,
  _Inout_ DD_SURFACE_GLOBAL    *puSurfaceGlobalData,
  _Inout_ DD_SURFACE_LOCAL     *puSurfaceLocalData,
  _Inout_ DD_SURFACE_MORE      *puSurfaceMoreData,
  _Inout_ DD_CREATESURFACEDATA *puCreateSurfaceData,
  _Out_   HANDLE               *puhSurface
);
```



## Parameters

<dl> <dt>

*hDirectDraw* \[in\]
</dt> <dd>

Handle to the [**DD\_DIRECTDRAW\_GLOBAL**](ddstrcts_d176c3e5-1e8b-4ff6-ba62-2fcfc42a9e5b.xml) structure representing the driver.

</dd> <dt>

*hSurface* \[in\]
</dt> <dd>

Previous handle to the same surface. Used if the surface is being re-created after a mode switch.

</dd> <dt>

*puSurfaceDescription* \[in, out\]
</dt> <dd>

Pointer to the [**DDSURFACEDESC**](ddstrcts_99443119-6641-4a66-8c77-e9ab2c271009.xml) structure describing the surface or buffer that the driver should create.

</dd> <dt>

*puSurfaceGlobalData* \[in, out\]
</dt> <dd>

Pointer to the [**DD\_SURFACE\_GLOBAL**](ddstrcts_83ae0625-9b08-4380-bd3a-d8d67675a48b.xml) structure containing surface data that is shared globally with multiple surfaces.

</dd> <dt>

*puSurfaceLocalData* \[in, out\]
</dt> <dd>

Pointer to a list of [**DD\_SURFACE\_LOCAL**](ddstrcts_07a504fc-c8bb-4b48-b825-4da3012e4f95.xml) structures describing the surface objects created by the driver.

</dd> <dt>

*puSurfaceMoreData* \[in, out\]
</dt> <dd>

Pointer to a [**DD\_SURFACE\_MORE**](ddstrcts_b86749f9-edbf-4e8b-ae17-27840ad4e5d5.xml) structure that contains additional local surface data.

</dd> <dt>

*puCreateSurfaceData* \[in, out\]
</dt> <dd>

Pointer to a [**DD\_CREATESURFACEDATA**](ddstrcts_bd51b416-f5b7-4a68-833b-7102de67488c.xml) structure that contains the information required to create a surface.

</dd> <dt>

*puhSurface* \[out\]
</dt> <dd>

Is used by the DirectDraw  API and should not be filled in by the driver.

</dd> </dl>

## Return value

**NtGdiDdCreateSurface** returns one of the following callback codes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDHAL\_DRIVER\_HANDLED**</dt> </dl>    | The driver has performed the operation and returned a valid return code for that operation. If this code is DD\_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function.<br/>                                                                                 |
| <dl> <dt>**DDHAL\_DRIVER\_NOTHANDLED**</dt> </dl> | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation.<br/> |



 

## Remarks

It is recommended that your application call [IDirectDraw7::CreateSurface](directdraw.idirectdraw7_createsurface) instead of using this function.

When creating a chain of attached surfaces, such as a swap chain or chain or mipmaps, [**NtGdiDdCreateSurfaceObject**](-dxgkernel-ntgdiddcreatesurfaceobject.md) should be called for each surface first. Then call [**NtGdiDdAttachSurface**](-dxgkernel-ntgdiddattachsurface.md) to attach them. Finally, call **NtGdiDdCreateSurface** for the first surface in the chain only. In this case, *hSurface* would be the handle returned by **NtGdiDdCreateSurfaceObject** for the first surface in the chain.

**NtGdiDdCreateSurface** should only be called to create surfaces in local and non-local video memory. It should never be called to create system memory surfaces. To create system memory surfaces, use [**NtGdiDdCreateSurfaceObject**](-dxgkernel-ntgdiddcreatesurfaceobject.md) instead.

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

 

 




