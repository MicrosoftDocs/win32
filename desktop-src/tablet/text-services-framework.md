---
Description: Overview of text services framework for the Tablet PC.
ms.assetid: f77fe77a-8625-47c5-bfc7-b473c8e8a8c6
title: Text Services Framework
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Text Services Framework

When the [Text Services Framework (TSF)](ecc34b2e-89e8-48a8-8a8e-442d2145fe24) is enabled on a control with a [PenInputPanel](https://www.bing.com/search?q=PenInputPanel) object attached, the PenInputPanel object can insert text directly. If the control does not support Text Services Framework (TSF), the PenInputPanel object must resort to using the [SendInput function](https://www.bing.com/search?q=SendInput+function) to insert text.

The ability to insert text directly becomes very important for those inputting East Asian characters, where using the [SendInput function](https://www.bing.com/search?q=SendInput+function) can produce incorrect characters.

TSF provides an interface for correcting recognition errors enabling the end user to correct, rewrite, or even dictate the proper text.

TSF is enabled by calling the [EnableTsf](https://www.bing.com/search?q=EnableTsf) method with the *enable* parameter set to **TRUE**.

\[C\#\]


```C++
PenInputPanel thePenInputPanel = new PenInputPanel(theControl);
//...
thePenInputPanel.EnableTsf(true);
```



A [PenInputPanel](https://www.bing.com/search?q=PenInputPanel) object attached to a [InkEdit](https://www.bing.com/search?q=InkEdit) control provides a robust user experience because the InkEdit supports TSF. However, be sure to set the [InkMode](https://www.bing.com/search?q=InkMode) property to [Microsoft.Ink.InkMode.Ink](https://www.bing.com/search?q=Microsoft.Ink.InkMode.Ink) on the InkEdit control as mentioned in the [Best Practices](best-practices.md) topic.

The [PenInputPanel Sample](peninputpanel-sample.md) provides an example of enabling TSF.

## Related topics

<dl> <dt>

[Text Services Framework](ecc34b2e-89e8-48a8-8a8e-442d2145fe24)
</dt> </dl>

 

 



