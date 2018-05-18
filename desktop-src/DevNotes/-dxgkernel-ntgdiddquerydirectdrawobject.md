---
Description: 'Queries a previously created kernel-mode representation of a Microsoft DirectDraw object for its capabilities.'
ms.assetid: 'ec07c7ef-4c57-4ed9-849b-f30692cc3181'
title: NtGdiDdQueryDirectDrawObject function
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

Pointer to a [**DD\_HALINFO**](display.dd_halinfo) structure that will be filled with the device's capabilities. See DDK documentation for details.

</dd> <dt>

*pCallBackFlags* 
</dt> <dd>

Pointer to a caller-provided buffer that stores driver-reported callback flags. The buffer should be of size 3\*sizeof(DWORD) and stores callback flags in the following order: pCallBackFlags\[0\] for flags in [**DD\_CALLBACKS**](ddstrcts_c4da6934-e140-40db-b7dc-686c205cb877.xml), pCallBackFlags\[1\] for flags in [**DD\_SURFACECALLBACKS**](ddstrcts_868cb884-02fc-4df4-a3ec-1fde158e42b0.xml), and pCallBackFlags\[2\] for flags in [**DD\_PALETTECALLBACKS**](ddstrcts_def94357-6d48-46e6-848a-ef85f13de99e.xml). See DDK documentation for details.

</dd> <dt>

*puD3dCallbacks* \[out\]
</dt> <dd>

Pointer to a table of Direct3D callback pointers. The table is filled with pointers to functions within Gdi32.dll that imitate a Direct3D display driver. This callback table is identical to the D3DHAL\_D3DCALLBACKS structure discussed in the DDK documentation.

</dd> <dt>

*puD3dDriverData* \[out\]
</dt> <dd>

Pointer to [**D3DHAL\_GLOBALDRIVERDATA**](d3dstrct_95940eeb-e317-455f-bd8c-0e7d1937197e.xml) data, as described in the DDK documentation.

</dd> <dt>

*puD3dBufferCallbacks* \[out\]
</dt> <dd>

Pointer to a table of callback pointers. The table is filled with pointers to functions within Gdi32.dll that imitate a Direct3D display driver. This callback table is identical to the DDHAL\_DDEXEBUFCALLBACKS structure, which maps to the [**DD\_D3DBUFCALLBACKS**](ddstrcts_cfe891c1-2660-460f-ac58-79f243ee902e.xml) structure discussed in the DDK documentation, except that members XxxD3DBuffer in **DD\_D3DBUFCALLBACKS** are replaced with XxxExecuteBuffer in DDHAL\_DDEXEBUFCALLBACKS.

</dd> <dt>

*puD3dTextureFormats* \[out\]
</dt> <dd>

Pointer to an array of [**DDSURFACEDESC**](display.ddsurfacedesc) structures that define the set of permissible texture formats.

</dd> <dt>

*puNumHeaps* \[out\]
</dt> <dd>

Pointer to the **dwNumHeaps** member of [**DD\_HALINFO**](display.dd_halinfo).**vmiData**. The **dwNumHeaps** member specifies the number of memory heaps in *puvmList*. See DDK documentation for details.

</dd> <dt>

*puvmList* \[out\]
</dt> <dd>

Pointer to a list of video memory heap descriptors. Can be **NULL**. This parameter is not used because video memory management is handled entirely within kernel mode.

</dd> <dt>

*puNumFourCC* \[out\]
</dt> <dd>

Pointer to the **puNumFourCCCodes** member of [**DD\_HALINFO**](display.dd_halinfo).**ddCaps**. The **puNumFourCCCodes** member specifies the number of [Four-Character Codes (FOURCC)](dshow.fourcc_codes) codes that the driver supports. See DDK documentation for details.

</dd> <dt>

*puFourCC* \[out\]
</dt> <dd>

Pointer to a list of supported [Four-Character Codes (FOURCC)](dshow.fourcc_codes) surface formats. Can be **NULL**.

</dd> </dl>

## Return value

If successful, this function returns **TRUE**; otherwise it returns **FALSE**.

## Remarks

A call to this function is designed to be made in a two-step process. In the first step, *puFourCC*, *puvmList* and *puD3dTextureFormats* should be **NULL**, and [**DdQueryDirectDrawObject**](-dxgkernel-ddquerydirectdrawobject.md) will fill in [**DD\_HALINFO**](display.dd_halinfo).**ddCaps**.**dwNumFourCCCodes**, **DD\_HALINFO**.**vmiData**.**dwNumHeaps**, and [**D3DHAL\_GLOBALDRIVERDATA**](d3dstrct_95940eeb-e317-455f-bd8c-0e7d1937197e.xml).**dwNumTextureFormats** with the number of entries that are to be returned. In the second call, the caller should allocate arrays of the indicated size and pass those pointers instead of **NULL** values in the *puFourCC*, *puvmList* and *puD3dTextureFormats* parameters. The arrays will then be populated with appropriate data.

Applications are advised to use the DirectDraw and [Direct3D](http://msdn.microsoft.com/en-us/library/bb205147(VS.85).aspx) APIs to create and manage graphics device objects. These constructs abstract the device creation process in a simplified and operating-system-independent way.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Ntgdi.h</dt> </dl> |



## See also

<dl> <dt>

[Graphics Low Level Client Support](-dxgkernel-low-level-client-support.md)
</dt> <dt>

[**DdQueryDirectDrawObject**](-dxgkernel-ddquerydirectdrawobject.md)
</dt> <dt>

[**NtGdiDdCreateDirectDrawObject**](-dxgkernel-ntgdiddcreatedirectdrawobject.md)
</dt> </dl>

 

 




