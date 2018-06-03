---
title: Formatting Functions
description: To format a variant into a string you must first tokenize the format string and then apply the format on that string.
ms.assetid: a00ee3c1-9799-4cd8-a13c-063c725aab68
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Formatting Functions

To format a variant into a string you must first tokenize the format string and then apply the format on that string. The formatting functions can be used to apply the format in one step and to apply the same format repeatedly. For example, you can call the [**VarFormat**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varformat) function to apply the formatting at once. If you are going to apply the same format over again you can call [**VarTokenizeFormatString**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vartokenizeformatstring) and use the tokens from [**VarFormatFromTokens**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varformatfromtokens) repeatedly.

The following table describes the formatting functions.

## In this section



| Topic                                                                 | Description                                                                                                                                                       |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VarFormat**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varformat)<br/>                             | Formats a variant into string form by parsing a format string.<br/>                                                                                         |
| [**VarFormatCurrency**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varformatcurrency)<br/>             | Formats a variant containing currency values into a string form.<br/>                                                                                       |
| [**VarFormatDateTime**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varformatdatetime)<br/>             | Formats a variant containing named date and time information into a string.<br/>                                                                            |
| [**VarFormatFromTokens**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varformatfromtokens)<br/>         | Takes a tokenized format string and applies it to a variant to produce a formatted output string.<br/>                                                      |
| [**VarFormatNumber**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varformatnumber)<br/>                 | Formats a variant containing numbers into a string form.<br/>                                                                                               |
| [**VarFormatPercent**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varformatpercent)<br/>               | Formats a variant containing percentages into a string form.<br/>                                                                                           |
| [**VarMonthName**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varmonthname)<br/>                       | Returns a string containing the localized month name.<br/>                                                                                                  |
| [**VarTokenizeFormatString**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-vartokenizeformatstring)<br/> | Parses the actual format string into a series of tokens which can be used to format variants using [**VarFormatFromTokens**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varformatfromtokens).<br/> |
| [**VarWeekdayName**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-varweekdayname)<br/>                   | Returns a string containing the localized name of the weekday.<br/>                                                                                         |



 

 

 





