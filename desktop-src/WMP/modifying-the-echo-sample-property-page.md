---
title: Modifying the Echo Sample Property Page
description: Modifying the Echo Sample Property Page
ms.assetid: a7ebf7d7-1f70-421f-862f-bc60655bb242
keywords:
- Windows Media Player plug-ins,Echo sample property pages
- plug-ins,Echo sample property pages
- digital signal processing plug-ins,Echo sample property pages
- DSP plug-ins,Echo sample property pages
- Echo DSP plug-in sample,property pages
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Modifying the Echo Sample Property Page

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The default property page implementation provided by the Windows Media Player Plug-in Wizard DSP plug-in sample contains a single edit box control that receives the scale factor from the user. You need to modify the property page to receive the two property values used by the Echo sample.

For an overview of DSP plug-in property pages, see [Implementing an Audio DSP Plug-in](implementing-an-audio-dsp-plug-in.md).

The following sections step you through the process of modifying the sample property page:

-   [Modifying the Echo Dialog Resource](modifying-the-echo-dialog-resource.md)
-   [Adding and Modifying the Events](adding-and-modifying-the-events.md)
-   [How the Echo Sample Persists Data](how-the-echo-sample-persists-data.md)
-   [Implementing CEchoPropPage::OnInitDialog](implementing-cechoproppage--oninitdialog.md)
-   [Implementing CEchoPropPage::Apply](implementing-cechoproppage--apply.md)
-   [Implementing CEcho::FinalConstruct](implementing-cecho--finalconstruct.md)

## Related topics

<dl> <dt>

[**The Echo Sample**](the-echo-sample.md)
</dt> </dl>

 

 




