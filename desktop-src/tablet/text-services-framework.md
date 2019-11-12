---
Description: Overview of text services framework for the Tablet PC.
ms.assetid: f77fe77a-8625-47c5-bfc7-b473c8e8a8c6
title: Text Services Framework (Tablet PC)
ms.topic: article
ms.date: 05/31/2018
---

# Text Services Framework

When the [Text Services Framework (TSF)](https://msdn.microsoft.com/en-us/library/ms629032(v=VS.85).aspx) is enabled on a control with a [PenInputPanel](https://msdn.microsoft.com/library/Aa514041(v=MSDN.10).aspx) object attached, the PenInputPanel object can insert text directly. If the control does not support Text Services Framework (TSF), the PenInputPanel object must resort to using the [SendInput function](https://msdn.microsoft.com/library/ms646310(v=VS.85).aspx) to insert text.

The ability to insert text directly becomes very important for those inputting East Asian characters, where using the [SendInput function](https://msdn.microsoft.com/library/ms646310(v=VS.85).aspx) can produce incorrect characters.

TSF provides an interface for correcting recognition errors enabling the end user to correct, rewrite, or even dictate the proper text.

TSF is enabled by calling the [EnableTsf](https://msdn.microsoft.com/library/ms569656(v=VS.90).aspx) method with the *enable* parameter set to **TRUE**.

\[C\#\]


```C++
PenInputPanel thePenInputPanel = new PenInputPanel(theControl);
//...
thePenInputPanel.EnableTsf(true);
```



A [PenInputPanel](https://msdn.microsoft.com/library/Aa514041(v=MSDN.10).aspx) object attached to a [InkEdit](https://msdn.microsoft.com/library/ms552265(v=VS.100).aspx) control provides a robust user experience because the InkEdit supports TSF. However, be sure to set the [InkMode](https://msdn.microsoft.com/library/ms835850(v=MSDN.10).aspx) property to [Microsoft.Ink.InkMode.Ink](https://msdn.microsoft.com/library/ms827399(v=MSDN.10).aspx) on the InkEdit control as mentioned in the [Best Practices](best-practices.md) topic.

The [PenInputPanel Sample](peninputpanel-sample.md) provides an example of enabling TSF.

## Related topics

<dl> <dt>

[Text Services Framework](https://msdn.microsoft.com/en-us/library/ms629032(v=VS.85).aspx)
</dt> </dl>

 

 



