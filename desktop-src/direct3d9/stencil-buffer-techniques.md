---
description: Applications use the stencil buffer to mask pixels in an image. The mask controls whether the pixel is drawn or not. Some of the more common effects are shown below.
ms.assetid: 984f0a98-4a74-44c3-a9d0-f5d3f12f7e4e
title: Stencil Buffer Techniques (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Stencil Buffer Techniques (Direct3D 9)

Applications use the stencil buffer to mask pixels in an image. The mask controls whether the pixel is drawn or not. Some of the more common effects are shown below.

-   [Compositing](compositing.md)
-   [Decaling](decaling.md)
-   [Dissolves, Fades, and Swipes](dissolves--fades--and-swipes.md)
-   [Outlines and Silhouettes](outlines-and-silhouettes.md)
-   [Two-Sided Stencil](two-sided-stencil.md)

The stencil buffer enables or disables drawing to the rendering target surface on a pixel-by-pixel basis. At its most fundamental level, it enables applications to mask sections of the rendered image so that they are not displayed. Applications often use stencil buffers for special effects such as dissolves, decaling, and outlining.

Stencil buffer information is embedded in the z-buffer data. Your application can use the [**IDirect3D9::CheckDeviceFormat**](/windows/desktop/api) method to check for hardware stencil support, as shown in the following code example.


```
// Reject devices that cannot perform 8-bit stencil buffering. 
// The following example assumes that pCaps is a valid pointer 
// to an initialized D3DCAPS9 structure. 

if( FAILED( m_pD3D->CheckDeviceFormat( pCaps->AdapterOrdinal,
                                       pCaps->DeviceType,  
                                       Format,  
                                       D3DUSAGE_DEPTHSTENCIL, 
                                       D3DRTYPE_SURFACE,
                                       D3DFMT_D24S8 ) ) )
return E_FAIL;
```



[**IDirect3D9::CheckDeviceFormat**](/windows/desktop/api) allows you to choose a device to create based on the capabilities of that device. In this case, devices that do not support 8-bit stencil buffers are rejected. Note that this is only one possible use for **IDirect3D9::CheckDeviceFormat**; for details see [Determining Hardware Support (Direct3D 9)](determining-hardware-support.md).

## How the Stencil Buffer Works

Direct3D performs a test on the contents of the stencil buffer on a pixel-by-pixel basis. For each pixel in the target surface, it performs a test using the corresponding value in the stencil buffer, a stencil reference value, and a stencil mask value. If the test passes, Direct3D performs an action. The test is performed using the following steps.

1.  Perform a bitwise AND operation of the stencil reference value with the stencil mask.
2.  Perform a bitwise AND operation of the stencil buffer value for the current pixel with the stencil mask.
3.  Compare the result of step 1 to the result of step 2, using the comparison function.

These steps are shown in the following code example.


```
(StencilRef & StencilMask) CompFunc (StencilBufferValue & StencilMask)
```




```
StencilBufferValue
```



is the contents of the stencil buffer for the current pixel. This code example uses the ampersand (&) symbol to represent the bitwise AND operation.


```
StencilMask
```



represents the value of the stencil mask, and


```
StencilRef
```



represents the stencil reference value.


```
CompFunc
```



is the comparison function.

The current pixel is written to the target surface if the stencil test passes, and is ignored otherwise. The default comparison behavior is to write the pixel, no matter how each bitwise operation turns out (D3DCMP\_ALWAYS). You can change this behavior by changing the value of the D3DRS\_STENCILFUNC render state, passing a member of the [**D3DCMPFUNC**](./d3dcmpfunc.md) enumerated type to identify the desired comparison function.

Your application can customize the operation of the stencil buffer. It can set the comparison function, the stencil mask, and the stencil reference value. It can also control the action that Direct3D takes when the stencil test passes or fails. For more information, see [Stencil Buffer State (Direct3D 9)](stencil-buffer-state.md).

## Examples

The following code examples demonstrate setting up the stencil buffer.


```
// Enable stencil testing
pDevice->SetRenderState(D3DRS_STENCILENABLE, TRUE);

// Specify the stencil comparison function
pDevice->SetRenderState(D3DRS_STENCILFUNC, D3DCMP_EQUAL);

// Set the comparison reference value
pDevice->SetRenderState(D3DRS_STENCILREF, 0);

//  Specify a stencil mask 
pDevice->SetRenderState(D3DRS_STENCILMASK, 0);
```



By default, the stencil reference value is zero. Any integer value is valid. Direct3D performs a bitwise AND of the stencil reference value and a stencil mask value before the stencil test.

You can control what pixel information is written out depending on the stencil comparison.


```
// A write mask controls what is written
pDevice->SetRenderState(D3DRS_STENCILWRITEMASK, D3DSTENCILOP_KEEP);
// Specify when to write stencil data
pDevice->SetRenderState(D3DRS_STENCILFAIL, D3DSTENCILOP_KEEP);
```



You can write your own formula for the value you want written into the stencil buffer as shown in the following example.


```
NewStencilBufferValue = (StencilBufferValue & ~StencilWriteMask) | 
                        (StencilWriteMask & StencilOp(StencilBufferValue))
```



## Related topics

<dl> <dt>

[Pixel Pipeline](pixel-pipeline.md)
</dt> </dl>

 

 
