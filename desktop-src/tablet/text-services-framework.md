---
Description: Overview of text services framework for the Tablet PC.
ms.assetid: f77fe77a-8625-47c5-bfc7-b473c8e8a8c6
title: Text Services Framework
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Text Services Framework

When the [Text Services Framework (TSF)](_tsf_tsf_start_page) is enabled on a control with a [PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic) object attached, the PenInputPanel object can insert text directly. If the control does not support Text Services Framework (TSF), the PenInputPanel object must resort to using the [SendInput function](_win32_SendInput_cpp) to insert text.

The ability to insert text directly becomes very important for those inputting East Asian characters, where using the [SendInput function](_win32_SendInput_cpp) can produce incorrect characters.

TSF provides an interface for correcting recognition errors enabling the end user to correct, rewrite, or even dictate the proper text.

TSF is enabled by calling the [EnableTsf](frlrfMicrosoftInkPenInputPanelClassEnableTsfTopic) method with the *enable* parameter set to **TRUE**.

\[C\#\]


```C++
PenInputPanel thePenInputPanel = new PenInputPanel(theControl);
//...
thePenInputPanel.EnableTsf(true);
```



A [PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic) object attached to a [InkEdit](frlrfMicrosoftInkInkEditClassTopic) control provides a robust user experience because the InkEdit supports TSF. However, be sure to set the [InkMode](frlrfMicrosoftInkInkEditClassInkModeTopic) property to [Microsoft.Ink.InkMode.Ink](frlrfMicrosoftInkInkModeClassTopic) on the InkEdit control as mentioned in the [Best Practices](best-practices.md) topic.

The [PenInputPanel Sample](peninputpanel-sample.md) provides an example of enabling TSF.

## Related topics

<dl> <dt>

[Text Services Framework](_tsf_tsf_start_page)
</dt> </dl>

 

 



