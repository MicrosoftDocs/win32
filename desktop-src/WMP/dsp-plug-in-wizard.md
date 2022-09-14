---
title: DSP Plug-in Wizard
description: DSP Plug-in Wizard
ms.assetid: 3d1ae5ef-12c4-4db3-815a-2adc73353f20
keywords:
- Windows Media Player plug-ins,plug-in wizard
- plug-ins,plug-in wizard
- digital signal processing plug-ins,plug-in wizard
- DSP plug-ins,plug-in wizard
- plug-in wizard
- Visual Studio,DSP plug-in wizard
ms.topic: article
ms.date: 05/31/2018
---

# DSP Plug-in Wizard

The Windows Media Player SDK provides a plug-in wizard that you can add to Visual Studio. The wizard can generate sample code for a variety of plug-ins, including the following types of DSP plug-ins:

-   Audio DSP plug-in
-   Audio DSP plug-in (dual mode)
-   Video DSP plug-in
-   Video DSP plug-in (dual mode)

Each of the two basic sample plug-ins, Audio DSP and Video DSP, functions as a DirectX Media Object (DMO). That is, each sample plug-in implements the **IMediaObject** interface. Each of the two dual-mode sample plug-ins can function either as a DMO or as a Media Foundation Transform (MFT). That is, each dual-mode sample plug-in implements both the **IMediaObject** interface and the **IMFTransform** interface.

You can compile, link, register, and test the sample plug-in code. Then you can modify the generated sample code to create your own DSP plug-in.

## Related topics

<dl> <dt>

[**Building a DSP Plug-in**](building-a-dsp-plug-in.md)
</dt> <dt>

[**DSP Plug-in Developer Overview**](dsp-plug-in-developer-overview.md)
</dt> <dt>

[**Updates to the DSP Plug-in Wizard for Windows Media Player 11**](updates-to-the-dsp-plug-in-wizard-for-windows-media-player-11.md)
</dt> </dl>

 

 




