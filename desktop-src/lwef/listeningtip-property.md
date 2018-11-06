---
title: ListeningTip Property
description: ListeningTip Property
ms.assetid: 02a678bb-5eb6-495f-b339-35170a44b15e
ms.topic: article
ms.date: 05/31/2018
---

# ListeningTip Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns a Boolean indicating the current user setting for the Listening Tip.

</dd> <dt>

<span id="Syntax_"></span><span id="syntax_"></span><span id="SYNTAX_"></span>**Syntax** 
</dt> <dd>

*agent***.SpeechInput.ListeningTip**



| Value     | Description                    |
|-----------|--------------------------------|
| **True**  | The Listening Tip is enabled.  |
| **False** | The Listening Tip is disabled. |



 

</dd> </dl>

## Remarks

The **ListeningTip** property indicates whether the Display Listening Tip option in the Microsoft Agent property sheet (Advanced Character Options) is enabled. When **ListeningTip** returns **True** and speech input is enabled, the server displays the tip window when the user presses the Listening key.

## See Also

[**AgentPropertyChange event**](agentpropertychange-event.md)


 

 




