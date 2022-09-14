---
title: Implementing CEcho DoProcessOutput
description: Implementing CEcho DoProcessOutput
ms.assetid: afd91022-4e2d-46a2-a0f4-cd2b558536d6
keywords:
- Windows Media Player plug-ins,Echo sample DoProcessOutput method
- plug-ins,Echo sample DoProcessOutput method
- digital signal processing plug-ins,Echo sample DoProcessOutput method
- DSP plug-ins,Echo sample DoProcessOutput method
- Echo DSP plug-in sample,DoProcessOutput method
ms.topic: article
ms.date: 05/31/2018
---

# Implementing CEcho::DoProcessOutput

The **DoProcessOutput** method performs the digital signal processing. This is the method that makes the changes to the data provided by Windows Media Player. It is the results of this method that you will hear as an echo effect when your Echo sample plug-in is complete.

For this sample, the plug-in will only process 8-bit or 16-bit audio. You will need to make some changes to the plug-in wizard sample code to remove the sections that process higher bit depth audio. It is worthwhile to study these sections, however, because you may decide to add your own echo implementation for those formats.

The following sections detail the changes you need to make to the code:

-   [Removing the Code to Process Greater than 16 Bits](removing-the-code-to-process-greater-than-16-bits.md)
-   [Processing the Audio Data](processing-the-audio-data.md)
-   [Variables to Perform Processing](variables-to-perform-processing.md)
-   [Creating the Echo Effect](creating-the-echo-effect.md)

## Related topics

<dl> <dt>

[**The Echo Sample**](the-echo-sample.md)
</dt> </dl>

 

 




