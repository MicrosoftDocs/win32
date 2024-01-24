---
title: DirectComposition interfaces
description: This section describes the interfaces provided by the Microsoft DirectComposition \ 32;API.
ms.assetid: AE51F47F-4315-4DA2-959E-B256957BE6DA
ms.topic: reference
ms.date: 06/12/2023
---

# DirectComposition interfaces

This section describes the interfaces provided by the Microsoft DirectComposition API.

## In this section

| Topic | Description |
|-|-|
| [**IDCompositionAffineTransform2DEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositionaffinetransform2deffect) | The arithmetic composite effect is used to combine 2 images using a weighted sum of pixels from the input images. |
| [**IDCompositionAnimation**](/windows/desktop/api/DcompAnimation/nn-dcompanimation-idcompositionanimation) | Represents a function for animating one or more properties of one or more DirectComposition objects. |
| [**IDCompositionArithmeticCompositeEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositionarithmeticcompositeeffect) | The arithmetic composite effect is used to combine 2 images using a weighted sum of pixels from the input images. |
| [**IDCompositionBlendEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositionblendeffect) | The Blend Effect is used to combine 2 images. |
| [**IDCompositionBrightnessEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositionbrightnesseffect) | The brightness effect controls the brightness of the image. |
| [**IDCompositionClip**](/windows/win32/api/dcomp/nn-dcomp-idcompositionclip) | Represents a clip object that is used to restrict the rendering of a visual subtree to a rectangular area. |
| [**IDCompositionColorMatrixEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositioncolormatrixeffect) | The color matrix effect alters the RGBA values of a bitmap. |
| [**IDCompositionCompositeEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositioncompositeeffect) | The composite effect is used to combine 2 or more images. This effect has 13 different composite modes. The composite effect accepts 2 or more inputs. When you specify 2 images, destination is the first input (index 0) and the source is the second input (index 1). If you specify more than 2 inputs, the images are composited starting with the first input and the second and so on. |
| [**IDCompositionDesktopDevice**](/windows/win32/api/dcomp/nn-dcomp-idcompositiondesktopdevice) | An application must use the IDCompositionDesktopDevice interface in order to use DirectComposition in a Win32 desktop application. This interface allows the application to connect a visual tree to a window and to host layered child windows for composition |
| [**IDCompositionDevice**](/windows/win32/api/dcomp/nn-dcomp-idcompositiondevice) | Serves as a factory for all other DirectComposition objects and provides methods to control transactional composition. |
| [**IDCompositionDevice2**](/windows/win32/api/dcomp/nn-dcomp-idcompositiondevice2) | Serves as a factory for all other DirectComposition objects and provides methods to control transactional composition. |
| [**IDCompositionDevice3**](/windows/win32/api/dcomp/nn-dcomp-idcompositiondevice3) | Serves as a factory for all other DirectComposition objects and provides methods to control transactional composition. |
| [**IDCompositionDevice4**](/windows/win32/api/dcomp/nn-dcomp-idcompositiondevice4) | Serves as the root factory for composition textures. |
| [**IDCompositionDeviceDebug**](/windows/win32/api/dcomp/nn-dcomp-idcompositiondevicedebug) | Provides access to rendering features that help with application debugging and performance tuning. This interface can be queried from the DirectComposition device interface. |
| [**IDCompositionEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositioneffect) | Represents a bitmap effect that modifies the rasterization of a visual's subtree. |
| [**IDCompositionEffectGroup**](/windows/win32/api/dcomp/nn-dcomp-idcompositioneffectgroup) | Represents a group of bitmap effects that are applied together to modify the rasterization of a visual's subtree. |
| [**IDCompositionFilterEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositionfiltereffect) | Represents a filter effect. |
| [**IDCompositionFloodEffect**](/previous-versions/windows/desktop/legacy/dn919732(v=vs.85)) | The flood effect is used to generate a bitmap based on the specified color and alpha value. You can use this effect when you want a specific color as an input for an effect, like a background color. |
| [**IDCompositionGaussianBlurEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositiongaussianblureffect) | |
| [**IDCompositionHueRotationEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositionhuerotationeffect) | The hue rotate effect alters the hue of an image by applying a color matrix based on the rotation angle. |
| [**IDCompositionLinearTransferEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositionlineartransfereffect) | The linear transfer effect is used to map the color intensities of an image using a linear function created from a list of values you provide for each channel. |
| [**IDCompositionMatrixTransform**](/windows/win32/api/dcomp/nn-dcomp-idcompositionmatrixtransform) | Represents an arbitrary affine 2D transformation defined by a 3-by-2 matrix. |
| [**IDCompositionMatrixTransform3D**](/windows/win32/api/dcomp/nn-dcomp-idcompositionmatrixtransform3d) | Represents an arbitrary 3D transformation defined by a 4-by-4 matrix. |
| [**IDCompositionRectangleClip**](/windows/win32/api/dcomp/nn-dcomp-idcompositionrectangleclip) | Represents a clip object that restricts the rendering of a visual subtree to the specified rectangular region. Optionally, the clip object may have rounded corners specified. |
| [**IDCompositionRotateTransform**](/windows/win32/api/dcomp/nn-dcomp-idcompositionrotatetransform) | Represents a 2D transformation that affects the rotation of a visual around the z-axis. The coordinate system is rotated around the specified center point. |
| [**IDCompositionRotateTransform3D**](/windows/win32/api/dcomp/nn-dcomp-idcompositionrotatetransform3d) | Represents a 3D transformation that affects the rotation of a visual along an arbitrary axis in 3D space. The coordinate system is rotated around the specified center point. |
| [**IDCompositionSaturationEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositionsaturationeffect) | This effect is used to alter the saturation of an image. The saturation effect is a specialization of the color matrix effect. |
| [**IDCompositionScaleTransform**](/windows/win32/api/dcomp/nn-dcomp-idcompositionscaletransform) | Represents a 2D transformation that affects the scale of a visual along the x-axis and y-axis. The coordinate system is scaled from the specified center point. |
| [**IDCompositionScaleTransform3D**](/windows/win32/api/dcomp/nn-dcomp-idcompositionscaletransform3d) | Represents a 3D transformation effect that affects the scale of a visual along the x-axis, y-axis, and z-axis. The coordinate system is scaled from the specified center point. |
| [**IDCompositionShadowEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositionshadoweffect) | The shadow effect is used to generate a shadow from the alpha channel of an image. The shadow is more opaque for higher alpha values and more transparent for lower alpha values. You can set the amount of blur and the color of the shadow. |
| [**IDCompositionSkewTransform**](/windows/win32/api/dcomp/nn-dcomp-idcompositionskewtransform) | Represents a 2D transformation that affects the skew of a visual along the x-axis and y-axis. The coordinate system is skewed around the specified center point. |
| [**IDCompositionSurface**](/windows/win32/api/dcomp/nn-dcomp-idcompositionsurface) | Represents a physical bitmap that can be associated with a visual for composition in a visual tree. This interface can also be used to update the bitmap contents. |
| [**IDCompositionSurfaceFactory**](/windows/win32/api/dcomp/nn-dcomp-idcompositionsurfacefactory) | Creates surface and virtual surface objects associated with an application-provided rendering device. |
| [**IDCompositionTableTransferEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositiontabletransfereffect) | The table transfer effect is used to map the color intensities of an image using a transfer function created from interpolating a list of values you provide. |
| [**IDCompositionTarget**](/windows/win32/api/dcomp/nn-dcomp-idcompositiontarget) | Represents a binding between a DirectComposition visual tree and a destination on top of which the visual tree should be composed. |
| [**IDCompositionTexture**](/windows/win32/api/dcomp/nn-dcomp-idcompositiontexture) | The interface to an object that represents a raw Direct3D texture that can be bound to a DComp visual as content. |
| [**IDCompositionTransform**](/windows/win32/api/dcomp/nn-dcomp-idcompositiontransform) | Represents a 2D transformation that can be used to modify the coordinate space of a visual subtree. |
| [**IDCompositionTransform3D**](/windows/win32/api/dcomp/nn-dcomp-idcompositiontransform3d) | Represents a 3D transformation effect that can be used to modify the rasterization of a visual subtree. |
| [**IDCompositionTranslateTransform**](/windows/win32/api/dcomp/nn-dcomp-idcompositiontranslatetransform) | Represents a 2D transformation that affects only the offset of a visual along the x-axis and y-axis. |
| [**IDCompositionTranslateTransform3D**](/windows/win32/api/dcomp/nn-dcomp-idcompositiontranslatetransform3d) | Represents a 3D transformation that affects the offset of a visual along the x-axis, y-axis, and z-axis. |
| [**IDCompositionTurbulenceEffect**](/windows/win32/api/dcomp/nn-dcomp-idcompositionturbulenceeffect) | The turbulence effect is used to generate a bitmap based on the Perlin noise function. The turbulence effect has no input image. |
| [**IDCompositionVirtualSurface**](/windows/win32/api/dcomp/nn-dcomp-idcompositionvirtualsurface) | Represents a sparsely allocated bitmap that can be associated with a visual for composition in a visual tree. |
| [**IDCompositionVisual**](/windows/win32/api/dcomp/nn-dcomp-idcompositionvisual) | Represents a DirectComposition visual. |
| [**IDCompositionVisual2**](/windows/win32/api/dcomp/nn-dcomp-idcompositionvisual2) | Represents one DirectComposition visual in a visual tree. |
| [**IDCompositionVisual3**](/windows/win32/api/dcomp/nn-dcomp-idcompositionvisual3) | Represents one DirectComposition visual in a visual tree. |
| [**IDCompositionVisualDebug**](/windows/win32/api/dcomp/nn-dcomp-idcompositionvisualdebug) | Represents a debug visual. |

## Related topics

* [DirectComposition Reference](reference.md)
