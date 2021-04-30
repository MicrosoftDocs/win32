---
description: Aspect Ratio Correction
ms.assetid: 0ed6010b-9168-44b1-be49-0c9d5d77ce3f
title: Aspect Ratio Correction
ms.topic: article
ms.date: 05/31/2018
---

# Aspect Ratio Correction

This topic applies to Windows XP Service Pack 2 or later.

In mixing mode, the VMR sizes the video to the correct aspect ratio. (Exception: See [Non-Square Mixing](non-square-mixing.md).) This may require stretching the video if the preferred aspect ratio is not the same as the image's physical aspect ratio. For example, digital video (DV) format is 720 x 480 pixels (3:2) but should be displayed at a 4:3 aspect ratio.

The VMR supports two different behaviors for aspect ratio correction:

-   Adjust either the horizontal or vertical size, so that the image is always stretched, never shrunk. This is now the default behavior.
-   Adjust the horizontal size, either stretching or shrinking the video.

Because the second behavior (horizontal adjustment only) may entail shrinking the video, the output image may have less resolution. For this reason, the first behavior is preferred. For example, in the case of 720 x 480 video at 4:3 aspect ratio, the default behavior produces a 720 x 550 image, while horizontal adjustment produces a smaller 640 x 480 image.

**VMR-7**: To set the aspect ratio correction preference, call [**IVMRMixerControl::SetMixingPrefs**](/windows/desktop/api/Strmif/nf-strmif-ivmrmixercontrol-setoutputrect). Set the MixerPref\_ARAdjustXorY flag for the default behavior, or clear this flag for horizontal adjustment only.

**VMR-9**: To set the aspect ratio correction preference, call [**IVMRMixerControl9::SetMixingPrefs**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrmixercontrol9-setmixingprefs). Set the MixerPref9\_ARAdjustXorY flag for the default behavior, or clear this flag for horizontal adjustment only.

## Related topics

<dl> <dt>

[Using VMR Mixing Mode](using-vmr-mixing-mode.md)
</dt> </dl>

 

 



