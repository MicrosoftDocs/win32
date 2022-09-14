---
description: Working with Direct3D Render Targets
ms.assetid: 271b919c-421b-4484-8e60-afbf3cbdca44
title: Working with Direct3D Render Targets
ms.topic: article
ms.date: 05/31/2018
---

# Working with Direct3D Render Targets

Several media subtypes for Direct3D render targets are defined for use with the VMR-7 and the VMR-9. When an upstream filter proposes a connection with one of these subtypes, it indicates to the VMR that the rendering is to be performed on a Direct3D render target. For VMR-7, this will be a DirectX 7 Direct3D render target, and for VMR-9 this will be a DirectX 9 Direct3D render target. If the VMR is in mixing mode, the surface will also be a Direct3D texture surface. If the VMR is not in mixing mode, the surface will be a regular Direct3D surface. The ARGB pixel formats are only supported when the VMR is in mixing mode. The render target subtypes are:



| VMR-7                                | VMR-9                                |
|--------------------------------------|--------------------------------------|
| MEDIASUBTYPE\_RGB32\_D3D\_DX7\_RT    | MEDIASUBTYPE\_RGB32\_D3D\_DX9\_RT    |
| MEDIASUBTYPE\_RGB16\_D3D\_DX7\_RT    | MEDIASUBTYPE\_RGB16\_D3D\_DX9\_RT    |
| MEDIASUBTYPE\_ARGB32\_D3D\_DX7\_RT   | MEDIASUBTYPE\_ARGB32\_D3D\_DX9\_RT   |
| MEDIASUBTYPE\_ARGB4444\_D3D\_DX7\_RT | MEDIASUBTYPE\_ARGB4444\_D3D\_DX9\_RT |
| MEDIASUBTYPE\_ARGB1555\_D3D\_DX7\_RT | MEDIASUBTYPE\_ARGB1555\_D3D\_DX9\_RT |



 

These types are defined in the header file uuids.h. The MEDIASUBTYPE\_RGB32 media types are an RGBx888 format and MEDIASUBTYPE\_RGB16 media types are an RGB565 format. For more information on these pixel formats, see the DirectX Graphics documentation.

**Requesting an Unlocked Surface**

Locking and unlocking DirectDraw surfaces are computationally expensive operations. When using the Direct3D render target media subtypes, the upstream filter needs the surfaces to be unlocked so that it can operate on them with the graphics hardware. To avoid an unnecessary locking-unlocking operation, the VMR supports a new flag on the [**IMemAllocator::GetBuffer**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-getbuffer) method, AM\_GBF\_NODDSURFACELOCK, that instructs the VMR not to lock the DirectDraw surface before passing a sample to the upstream filter. When this flag is used, calls to [**IMediaSample::GetPointer**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getpointer) will fail because there is no locked pointer. To obtain access to the DirectDraw surface, the filter must call **QueryInterface** on the returned [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) object and request the [**IVMRSurface**](/windows/desktop/api/Strmif/nn-strmif-ivmrsurface) interface. Obviously, the upstream filter must ensure that the surface is not locked when it releases the sample back to the free list.

 

 



