---
description: Queries a previously created kernel-mode representation of a Microsoft DirectDraw object for its capabilities.
ms.assetid: ec07c7ef-4c57-4ed9-849b-f30692cc3181
title: NtGdiDdQueryDirectDrawObject function (Ntgdi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtGdiDdQueryDirectDrawObject
api_type: 
- DllExport
api_location: 
- Ntgdi.h
- Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll
- GDI32.dll
- GDI32Full.dll
---

# NtGdiDdQueryDirectDrawObject function

\[This function is subject to change with each operating system revision. Instead, use the DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Queries a previously created kernel-mode representation of a Microsoft DirectDraw object for its capabilities.

## Syntax


```C++
BOOL APIENTRY NtGdiDdQueryDirectDrawObject(
  _In_  HANDLE                      hDirectDrawLocal,
  _Out_ DD_HALINFO                  *pHalInfo,
        DWORD                       *pCallBackFlags,
  _Out_ LPD3DNTHAL_CALLBACKS        puD3dCallbacks,
  _Out_ LPD3DNTHAL_GLOBALDRIVERDATA puD3dDriverData,
  _Out_ PDD_D3DBUFCALLBACKS         puD3dBufferCallbacks,
  _Out_ LPDDSURFACEDESC             puD3dTextureFormats,
  _Out_ DWORD                       *puNumHeaps,
  _Out_ VIDEOMEMORY                 *puvmList,
  _Out_ DWORD                       *puNumFourCC,
  _Out_ DWORD                       *puFourCC
);
```



## Parameters

<dl> <dt>

*hDirectDrawLocal* \[in\]
</dt> <dd>

Handle to the previously-created kernel-mode DirectDraw device.

</dd> <dt>

*pHalInfo* \[out\]
</dt> <dd>

Pointer to a [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo) structure that will be filled with the device's capabilities. See DDK documentation for details.

</dd> <dt>

*pCallBackFlags* 
</dt> <dd>

Pointer to a caller-provided buffer that stores driver-reported callback flags. The buffer should be of size 3\*sizeof(DWORD) and stores callback flags in the following order: pCallBackFlags\[0\] for flags in [**DD\_CALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_callbacks), pCallBackFlags\[1\] for flags in [**DD\_SURFACECALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surfacecallbacks), and pCallBackFlags\[2\] for flags in [**DD\_PALETTECALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_palettecallbacks). See DDK documentation for details.

</dd> <dt>

*puD3dCallbacks* \[out\]
</dt> <dd>

Pointer to a table of Direct3D callback pointers. The table is filled with pointers to functions within Gdi32.dll that imitate a Direct3D display driver. This callback table is identical to the D3DHAL\_D3DCALLBACKS structure discussed in the DDK documentation.

</dd> <dt>

*puD3dDriverData* \[out\]
</dt> <dd>

Pointer to [**D3DHAL\_GLOBALDRIVERDATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_globaldriverdata) data, as described in the DDK documentation.

</dd> <dt>

*puD3dBufferCallbacks* \[out\]
</dt> <dd>

Pointer to a table of callback pointers. The table is filled with pointers to functions within Gdi32.dll that imitate a Direct3D display driver. This callback table is identical to the DDHAL\_DDEXEBUFCALLBACKS structure, which maps to the [**DD\_D3DBUFCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_d3dbufcallbacks) structure discussed in the DDK documentation, except that members XxxD3DBuffer in **DD\_D3DBUFCALLBACKS** are replaced with XxxExecuteBuffer in DDHAL\_DDEXEBUFCALLBACKS.

</dd> <dt>

*puD3dTextureFormats* \[out\]
</dt> <dd>

Pointer to an array of [**DDSURFACEDESC**](/windows/win32/api/ddraw/ns-ddraw-ddsurfacedesc) structures that define the set of permissible texture formats.

</dd> <dt>

*puNumHeaps* \[out\]
</dt> <dd>

Pointer to the **dwNumHeaps** member of [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo).**vmiData**. The **dwNumHeaps** member specifies the number of memory heaps in *puvmList*. See DDK documentation for details.

</dd> <dt>

*puvmList* \[out\]
</dt> <dd>

Pointer to a list of video memory heap descriptors. Can be **NULL**. This parameter is not used because video memory management is handled entirely within kernel mode.

</dd> <dt>

*puNumFourCC* \[out\]
</dt> <dd>

Pointer to the **puNumFourCCCodes** member of [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo).**ddCaps**. The **puNumFourCCCodes** member specifies the number of [Four-Character Codes (FOURCC)](../directshow/fourcc-codes.md) codes that the driver supports. See DDK documentation for details.

</dd> <dt>

*puFourCC* \[out\]
</dt> <dd>

Pointer to a list of supported [Four-Character Codes (FOURCC)](../directshow/fourcc-codes.md) surface formats. Can be **NULL**.

</dd> </dl>

## Return value

If successful, this function returns **TRUE**; otherwise it returns **FALSE**.

## Remarks

A call to this function is designed to be made in a two-step process. In the first step, *puFourCC*, *puvmList* and *puD3dTextureFormats* should be **NULL**, and [**DdQueryDirectDrawObject**](/windows/desktop/api/Ddrawgdi/nf-ddrawgdi-ddquerydirectdrawobject) will fill in [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo).**ddCaps**.**dwNumFourCCCodes**, **DD\_HALINFO**.**vmiData**.**dwNumHeaps**, and [**D3DHAL\_GLOBALDRIVERDATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_globaldriverdata).**dwNumTextureFormats** with the number of entries that are to be returned. In the second call, the caller should allocate arrays of the indicated size and pass those pointers instead of **NULL** values in the *puFourCC*, *puvmList* and *puD3dTextureFormats* parameters. The arrays will then be populated with appropriate data.

Applications are advised to use the DirectDraw and [Direct3D](../direct3d10/d3d10-graphics-reference.md) APIs to create and manage graphics device objects. These constructs abstract the device creation process in a simplified and operating-system-independent way.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Ntgdi.h</dt> </dl> |



## See also

<dl> <dt>

[Graphics Low Level Client Support](-dxgkernel-low-level-client-support.md)
</dt> <dt>

[**DdQueryDirectDrawObject**](/windows/desktop/api/Ddrawgdi/nf-ddrawgdi-ddquerydirectdrawobject)
</dt> <dt>

[**NtGdiDdCreateDirectDrawObject**](-dxgkernel-ntgdiddcreatedirectdrawobject.md)
</dt> </dl>

 

 
