---
title: CMM Transform Creation Flags
description: CMMs use transform creation flags as hints for how to create a color transform. It is up to the CMM to determine how best to use these flags.
ms.assetid: f3942929-272c-4f08-98ac-a4d14d2f6ac4
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# CMM Transform Creation Flags

CMMs use transform creation flags as hints for how to create a color transform. It is up to the CMM to determine how best to use these flags.

All of the functions that use these flags pass or receive flag values through a parameter called *dwFlags*. The high-order **WORD** of *dwFlags* should be set to a value from the following table.



| Constant                    | Description                                                                                                                                  |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ENABLE\_GAMUT\_CHECKING     | Use this transform for gamut checking.                                                                                                       |
| USE\_RELATIVE\_COLORIMETRIC | Do not preserve the white point. If the output gamut does not support a given color, use the nearest supported color. See Rendering Intents. |
| FAST\_TRANSLATE             | Look up color only. Do not interpolate the color.                                                                                            |
| PRESERVEBLACK               | Inserts the appropriate black generation GMMP as the last GMMP in the transform sequence                                                     |
| WCS\_ALWAYS                 | Use the WCS code path even for ICC transforms.                                                                                               |
| SEQUENTIAL\_TRANSFORM       | Transform creation flag for creating a sequential (non-optimized) color transform.                                                           |



 

The low-order **WORD** can have one of the following constant values.



| Constant     | Description                                                                                        |
|--------------|----------------------------------------------------------------------------------------------------|
| PROOF\_MODE  | Transform will be used to preview the image. Low image quality.                                    |
| NORMAL\_MODE | Transform will be used for normal image display. Average image quality.                            |
| BEST\_MODE   | Transform will be used for the display of the highest-quality image possible on the target device. |



 

Moving from PROOF\_MODE to BEST\_MODE, output quality generally improves and transform speed declines.

## Related topics

<dl> <dt>

[Basic color management concepts](basic-color-management-concepts.md)
</dt> <dt>

[ICM Constants](wcs-constants.md)
</dt> </dl>

 

 




