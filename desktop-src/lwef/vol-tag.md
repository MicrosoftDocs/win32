---
title: Vol Tag
description: Vol Tag
ms.assetid: a6444eb2-79c2-4c86-8474-846d908479df
ms.topic: article
ms.date: 05/31/2018
---

# Vol Tag

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Sets the baseline speaking volume of the speech output.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**\\Vol=***number***\\**



| Part     | Description                                                         |
|----------|---------------------------------------------------------------------|
| *number* | Baseline speaking volume: 0 is silence and 65535 is maximum volume. |



 

</dd> </dl>

### Remarks

The volume setting affects both left and right channels. You cannot set the volume of each channel separately. This tag is supported only for TTS-generated output.

 

 




