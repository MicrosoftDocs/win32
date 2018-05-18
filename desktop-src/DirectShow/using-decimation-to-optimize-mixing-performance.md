---
Description: Using Decimation to Optimize Mixing Performance
ms.assetid: '94d4ce86-9d60-4fd4-ab01-851dc073680b'
title: Using Decimation to Optimize Mixing Performance
---

# Using Decimation to Optimize Mixing Performance

> \[!Important\]  
> The optimization described in this section is highly dependent on the underlying hardware. Unless you can guarantee what type of graphics hardware will be used with the application, it may seriously degrade the appearance of the video image.

 

HDTV requires a lot of processing power, which on newer systems is provided mostly by the graphics card. But even if the graphics card and the decoder can support resolutions of 1920x1080, the user may not always have their monitor set to this resolution. In this case, the graphics chip is required to create a 1920 x 1080 image, and then reduce the resolution before sending it to the frame buffer.

Since this is a waste of processing power, the VMR provides a way to decimate (reduce) the image at the time it is being rendered onto the DirectDraw surface. This eliminates the extra memory copy required if the image has to be resized after it has been rendered.

**VMR-7:** To enable decimation, call [**IVMRMixerControl::SetMixingPrefs**](ivmrmixercontrol-setoutputrect.md) with the MixerPref\_DecimateOutput flag.

**VMR-9:** To enable decimation, call [**IVMRMixerControl9::SetMixingPrefs**](ivmrmixercontrol9-setmixingprefs.md) with the MixerPref9\_DecimateOutput flag.

The **SetMixingPrefs** method must be called before the VMR is connected. The mixing preference flags cannot be changed once the graph is running.

## Related topics

<dl> <dt>

[Using VMR Mixing Mode](using-vmr-mixing-mode.md)
</dt> </dl>

 

 



