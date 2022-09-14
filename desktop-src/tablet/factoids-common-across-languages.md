---
description: A number of factoids describe input that is common to all language recognizers and need not have different formats for different languages. The following table lists factoids that are common across all languages.
ms.assetid: dae4a28d-0332-4bb2-b040-13a959c7945e
title: Factoids Common Across Languages
ms.topic: article
ms.date: 05/31/2018
---

# Factoids Common Across Languages

A number of factoids describe input that is common to all language recognizers and need not have different formats for different languages. The following table lists factoids that are common across all languages.




| Factoid | Definition | Examples | 
|---------|------------|----------|
| <strong>Digit</strong> | Sets bias for a single digit. The recognizer is biased toward returning only single digits when this factoid is set.<br /> | 0-9<br /> | 
| <strong>Email</strong> | Sets bias for an email address.<br /> | someone@example.com<br /> | 
| <strong>Web</strong> | Sets bias for various URL formats.<br /><blockquote>[!Note]<br />The default settings for the recognizer include the <strong>Web</strong> factoid. Because of this, you may not notice a large difference between the <strong>Web</strong> factoid and the default setting. However, the <strong>Web</strong> factoid does help eliminate spaces between words in a URL.</blockquote><br /> | http:\\microsoft.net<br /> `https://microsoft.us/`<br /> https:\\www.microsoft.au\<br /> https://microsoft.com<br /> www.microsoft_world.com<br /> www.microsoft.us\<br /> http:\\www.microsoft.com\myfile.htm<br /> http:\\www.microsoft.com\myfile.html<br /> http:\\www.microsoft.com\myfile.asp<br /> http:\\www.microsoft.uk<br /> http:\\www.microsoft.info<br /> www.microsoft.biz<br /> | 
| <strong>Default</strong> | Returns the recognizer to its default settings.<br /> | The default setting for factoids for western languages includes the system dictionary, user dictionary, various punctuations, and the <strong>Web</strong> and <strong>Number</strong> factoids.<br /> The default setting for factoids for East Asian languages includes all characters supported by the recognizer.<br /> | 
| <strong>None</strong> | Disables all factoids, dictionaries, and the language model.<br /> | This factoid should be used only when you do not want the recognizer to use any grammar rules or dictionaries, including the system dictionary. This factoid is useful for input of random strings such as product codes. Do not use the Coerce flag with this factoid.<br /> | 




 

 

 




