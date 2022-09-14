---
title: Echo Sample Overview
description: Echo Sample Overview
ms.assetid: df9ad8f4-8c17-44b8-b5ee-c86de44788cf
keywords:
- Windows Media Player plug-ins,Echo sample overview
- plug-ins,Echo sample overview
- digital signal processing plug-ins,Echo sample overview
- DSP plug-ins,Echo sample overview
- Echo DSP plug-in sample,about
ms.topic: article
ms.date: 05/31/2018
---

# Echo Sample Overview

This guide builds a Windows Media Player DSP plug-in that creates an echo effect in PCM audio during playback. The goals for the plug-in are as follows:

-   The plug-in processes 8-bit or 16-bit PCM audio only.
-   It supports a delay time between 10 milliseconds (ms) and 2000 ms (2 seconds). This represents a practical range for most applications.
-   It supports mixing of the original signal with the delay signal.
-   It provides a property page implementation that allows the user to provide a value for the delay time and a value for the percentage of delay signal relative to the overall audio signal level.
-   The code is created by modifying the Windows Media Player Plug-in Wizard audio DSP plug-in sample.

The Echo sample is not included with the Windows Media Player SDK; it is a sample that you create. To create the Echo sample, you must start with the default project from the Windows Media Player Plug-in Wizard. You can name the project whatever you like; this documentation assumes the project is named Echo. For details about using the wizard, see [Building a DSP Plug-in](building-a-dsp-plug-in.md).

The following section provides an overview of how the sample creates an echo effect:

-   [How the Echo Sample Works](how-the-echo-sample-works.md)

## Related topics

<dl> <dt>

[**The Echo Sample**](the-echo-sample.md)
</dt> </dl>

 

 




