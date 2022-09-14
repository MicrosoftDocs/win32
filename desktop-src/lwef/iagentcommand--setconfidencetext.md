---
title: IAgentCommand SetConfidenceText
description: IAgentCommand SetConfidenceText
ms.assetid: e776a2ba-3592-4f26-a3e3-2c044eed7f0c
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommand::SetConfidenceText

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetConfidenceText(
   BSTR bszTipText  // ConfidenceText setting for Command 
);
```

Sets the value of the Listening Tip text for a [**Command**](/windows/desktop/lwef/the-command-object).

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszTipText"></span><span id="bsztiptext"></span><span id="BSZTIPTEXT"></span>*bszTipText*
</dt> <dd>

A BSTR that specifies the text for the [**ConfidenceText**](confidencetext-property.md) property of a [**Command**](/windows/desktop/lwef/the-command-object).

</dd> </dl>

If the confidence value returned of the best match returned in the [**Command**](/windows/desktop/lwef/the-command-object) event does not exceed the value set for the [**ConfidenceThreshold**](/windows/desktop/lwef/confidence-property) property, the text supplied in *bszTipText* is displayed in the Listening Tip.

## See Also

[**IAgentCommand::SetConfidenceThreshold**](iagentcommand--setconfidencethreshold.md), [**IAgentCommand::GetConfidenceThreshold**](iagentcommand--getconfidencethreshold.md), [**IAgentCommand::GetConfidenceText**](iagentcommand--getconfidencetext.md), [**IAgentUserInput::GetItemConfidence**](iagentuserinput--getitemconfidence.md)


 

 