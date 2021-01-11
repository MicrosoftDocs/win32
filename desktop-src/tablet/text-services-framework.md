---
description: Overview of text services framework for the Tablet PC.
ms.assetid: f77fe77a-8625-47c5-bfc7-b473c8e8a8c6
title: Text Services Framework (Tablet PC)
ms.topic: article
ms.date: 05/31/2018
---

# Text Services Framework (Tablet PC)

When the [Text Services Framework (TSF)](../tsf/text-services-framework.md) is enabled on a control with a [PenInputPanel](/previous-versions/aa514041(v=msdn.10)) object attached, the PenInputPanel object can insert text directly. If the control does not support Text Services Framework (TSF), the PenInputPanel object must resort to using the [SendInput function](/windows/win32/api/winuser/nf-winuser-sendinput) to insert text.

The ability to insert text directly becomes very important for those inputting East Asian characters, where using the [SendInput function](/windows/win32/api/winuser/nf-winuser-sendinput) can produce incorrect characters.

TSF provides an interface for correcting recognition errors enabling the end user to correct, rewrite, or even dictate the proper text.

TSF is enabled by calling the [EnableTsf](/previous-versions/ms569656(v=vs.100)) method with the *enable* parameter set to **TRUE**.

\[C\#\]


```C++
PenInputPanel thePenInputPanel = new PenInputPanel(theControl);
//...
thePenInputPanel.EnableTsf(true);
```



A [PenInputPanel](/previous-versions/aa514041(v=msdn.10)) object attached to a [InkEdit](/previous-versions/ms552265(v=vs.100)) control provides a robust user experience because the InkEdit supports TSF. However, be sure to set the [InkMode](/previous-versions/ms835850(v=msdn.10)) property to [Microsoft.Ink.InkMode.Ink](/previous-versions/ms827399(v=msdn.10)) on the InkEdit control as mentioned in the [Best Practices](best-practices.md) topic.

The [PenInputPanel Sample](peninputpanel-sample.md) provides an example of enabling TSF.

## Related topics

<dl> <dt>

[Text Services Framework](../tsf/text-services-framework.md)
</dt> </dl>

 

 
