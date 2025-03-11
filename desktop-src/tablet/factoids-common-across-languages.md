---
description: A number of factoids describe input that is common to all language recognizers and need not have different formats for different languages. The following table lists factoids that are common across all languages.
ms.assetid: dae4a28d-0332-4bb2-b040-13a959c7945e
title: Factoids Common Across Languages
ms.topic: reference
ms.date: 11/06/2023
---

# Factoids Common Across Languages

A number of factoids describe input that is common to all language recognizers and need not have different formats for different languages. The following table lists factoids that are common across all languages.

| Factoid | Definition | Examples |
|---------|------------|----------|
| **Digit** | Sets bias for a single digit. The recognizer is biased toward returning only single digits when this factoid is set.<br /> | 0-9<br /> |
| **Email** | Sets bias for an email address.<br /> | `someone@example.com`<br /> |
| **Web** | Sets bias for various URL formats.<br> **Note:** The default settings for the recognizer include the **Web** factoid. Because of this, you may not notice a large difference between the **Web** factoid and the default setting. However, the **Web** factoid does help eliminate spaces between words in a URL.<br> | `http://microsoft.net`<br> `https://microsoft.us/`<br> `https://www.microsoft.au`<br> `https://microsoft.com`<br> `www.microsoft_world.com`<br> `www.microsoft.us`<br> `http://www.microsoft.com/myfile.htm`<br> `http://www.microsoft.com/myfile.html`<br> `http://www.microsoft.com/myfile.asp`<br> `http://www.microsoft.uk`<br> `http://www.microsoft.info`<br> `www.microsoft.biz`<br> |
| **Default** | Returns the recognizer to its default settings.<br /> | The default setting for factoids for western languages includes the system dictionary, user dictionary, various punctuations, and the **Web** and **Number** factoids.<br /> The default setting for factoids for East Asian languages includes all characters supported by the recognizer.<br /> |
| **None** | Disables all factoids, dictionaries, and the language model.<br /> | This factoid should be used only when you do not want the recognizer to use any grammar rules or dictionaries, including the system dictionary. This factoid is useful for input of random strings such as product codes. Do not use the Coerce flag with this factoid.<br /> |
