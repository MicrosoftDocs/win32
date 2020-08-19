---
title: IAgentCommand SetConfidenceThreshold
description: IAgentCommand SetConfidenceThreshold
ms.assetid: f62d646a-895d-468c-9397-0495680109a0
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommand::SetConfidenceThreshold

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetConfidenceThreshold(
   long lConfidence  // Confidence setting for Command
);
```

Sets the value of the [**Confidence**](confidence-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object).

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="lConfidence"></span><span id="lconfidence"></span><span id="LCONFIDENCE"></span>*lConfidence*
</dt> <dd>

The value for the [**Confidence**](confidence-property.md) property of a [**Command**](/windows/desktop/lwef/the-command-object).

</dd> </dl>

If the confidence value returned of the best match returned in the [**Command**](/windows/desktop/lwef/the-command-object) event does not exceed the value set for the [**ConfidenceThreshold**](/windows/desktop/lwef/confidence-property) property, the text supplied in [**SetConfidenceText**](iagentcommand--setconfidencetext.md) is displayed in the Listening Tip.

## See Also

[**IAgentCommand::GetConfidenceThreshold**](iagentcommand--getconfidencethreshold.md), [**IAgentCommand::SetConfidenceText**](iagentcommand--setconfidencetext.md), [**IAgentUserInput::GetItemConfidence**](iagentuserinput--getitemconfidence.md)


 

 