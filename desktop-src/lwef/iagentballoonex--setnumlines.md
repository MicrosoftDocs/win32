---
title: IAgentBalloonEx SetNumLines
description: IAgentBalloonEx SetNumLines
ms.assetid: 350fd273-a941-4454-a309-045d19ed8f59
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloonEx::SetNumLines

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetNumLines(
   long lLines,  // number of lines setting
);
```

Sets the number of lines of text output that can be displayed in the character's word balloon.

-   Returns S\_OK to indicate the operation was successful.
-   Returns E\_INVALIDARG if the parameter is zero.

<dl> <dt>

<span id="lLines"></span><span id="llines"></span><span id="LLINES"></span>*lLines*
</dt> <dd>

Number of lines to display in the word balloon.

</dd> </dl>

The minimum setting is 1 and maximum is 128. If the text specified in the [**Speak**](speak-method.md) or [**Think**](think-method.md) method exceeds the size of the current balloon, Agent automatically scrolls the text in the balloon.

This method will fail if the **SizeToText** balloon style bit is set.

The default setting is based on settings when the character is compiled with the Microsoft Agent Character Editor.

## See Also

[**IAgentBalloon::GetNumLines**](iagentballoon--getnumlines.md), [**IAgentBalloonEx::GetStyle**](iagentballoonex--getstyle.md), [**IAgentBalloonEx::SetStyle**](iagentballoonex--setstyle.md)


 

 




