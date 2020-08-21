---
title: Confidence Property
description: Confidence Property
ms.assetid: 28a57970-4649-4a9a-9fb2-bf3f0b2f54ce
ms.topic: article
ms.date: 05/31/2018
---

# Confidence Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets whether the client's **Confidence** appears in the Listening Tip.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Commands("***name***")**.**Confidence** \[ = *Number*\]



| Part     | Description                                                                                                                        |
|----------|------------------------------------------------------------------------------------------------------------------------------------|
| *Number* | A numeric expression that evaluates to a Long integer that identifies confidence value for the [**Command**](/windows/desktop/lwef/the-command-object). |



 

</dd> </dl>

## Remarks

If the returned confidence value of the best match (UserInput.Confidence) does not exceed value you set for the **Confidence** property, the text supplied in [**ConfidenceText**](confidencetext-property.md) is displayed in the Listening Tip.

 

 