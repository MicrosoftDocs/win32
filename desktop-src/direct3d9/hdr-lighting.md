---
description: Lighting in the real world contains a very high dynamic range (HDR) of luminance values.
ms.assetid: 537700e2-802d-4fd1-b026-142d6f4f0559
title: HDR Lighting (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# HDR Lighting (Direct3D 9)

Lighting in the real world contains a very high dynamic range (HDR) of luminance values. The real world has about 10 orders of dynamic range (DR) for luminance values spread across the spectrum of darkness to brightness. On the other hand, a computer screen has a very limited display gamut (or range of luminance values): approximately two orders of dynamic range. The challenge to producing HDR rendered images is to map the real world HDR values into the limited gamut of a computer screen.

Tone mapping is the technique used by DirectX for mapping HDR information into a more limited range. Tone mapping applied to CGI rendering can dramatically improve the amount of lighting detail rendered, allowing details in the darkest areas to be seen, and providing contrast in areas that are so bright, they appear burned. The resulting scenes render with far more visible lighting detail.

[HDRLighting Sample](https://msdn.microsoft.com/library/Ee417769(v=VS.85).aspx) is a SDK sample that demonstrates HDR lighting.

## Tone Mapping

Tone mapping generally simulates optical phenomena that cannot be caused by the DR of the monitor. Examples of this are flares or blooming (which are mostly properties of lenses), the blue shift that happens in the human eye in low light conditions, and other adaptations that are a result of the biochemistry of the eye. If the DR of the display were large enough, tone mapping would not be as neccessary, except for providing artistic effects or some of the properties of a camera lens or a charge coupled device (CCD).

Tone mapping divides the range of luminance values in a scene into a set of zones. Each zone encompasses a range of luminance values.

HDR uses the following terms:

-   Zone - range of luminance values
-   Middle gray - middle brightness region of the scene
-   Dynamic range - ratio of the highest scene luminance to the lowest scene luminance
-   Key - subjective measurement of scene lighting: this varies from light to moderate to dark

To calculate luminance from RGB values, use this:


```
L = 0.27R + 0.67G + 0.06B;
```



The log-average luminance is a useful approximation for the key of a scene. A general equation looks like this:

L<sub>w</sub> = exp\[ 1 / N( sum\[ log( delta + L<sub>w</sub>( x, y ) ) \] ) \]

Where:

-   L<sub>w</sub> - log-average luminance
-   N - number of pixels in the image
-   delta - a small factor to avoid problems with black pixels
-   L<sub>w</sub>( x, y ) - the world space luminance for pixel ( x, y )

To map this to a middle-gray value, here is a luminance scaling operator:

L( x, y ) = a \* L<sub>w</sub>( x, y ) / L<sub>w</sub>

Where:

-   L( x, y ) - scaled luminance for pixel ( x, y )
-   a - image key value after applying the scaling

And finally, here is a simple tone mapping operator for compressing the high luminances:

L<sub>d</sub>( x, y ) = L( x, y ) / ( 1 + L( x, y ) )

Where:

-   L<sub>d</sub>( x, y ) - compressed and scaled luminance for pixel ( x, y )
-   a - image key value after applying the scaling

This operator scales high luminances by 1/L and low luminances by 1. For more details, see the following paper.

Reinhard, Erik, Mike Stark, Peter Shirley, and James Ferwerda. ["Photographic Tone Reproduction for Digital Images"](https://www.cs.utah.edu/~reinhard/cdrom/tonemap.pdf). ACM Transactions on Graphics (TOG), Proceedings of the 29th Annual Conference on Computer Graphics and Interactive Techniques (SIGGRAPH), pp. 267-276. New York, NY: ACM Press, 2002.

## Related topics

<dl> <dt>

[Advanced Topics](advanced-topics.md)
</dt> </dl>

 

 



