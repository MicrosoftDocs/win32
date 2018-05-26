---
title: Formatting Functions
description: To format a variant into a string you must first tokenize the format string and then apply the format on that string.
ms.assetid: a00ee3c1-9799-4cd8-a13c-063c725aab68
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Formatting Functions

To format a variant into a string you must first tokenize the format string and then apply the format on that string. The formatting functions can be used to apply the format in one step and to apply the same format repeatedly. For example, you can call the [**VarFormat**](/windows/previous-versions/OleAuto/nf-oleauto-varformat?branch=master) function to apply the formatting at once. If you are going to apply the same format over again you can call [**VarTokenizeFormatString**](/windows/previous-versions/OleAuto/nf-oleauto-vartokenizeformatstring?branch=master) and use the tokens from [**VarFormatFromTokens**](/windows/previous-versions/OleAuto/nf-oleauto-varformatfromtokens?branch=master) repeatedly.

The following table describes the formatting functions.

## In this section



| Topic                                                                 | Description                                                                                                                                                       |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VarFormat**](/windows/previous-versions/OleAuto/nf-oleauto-varformat?branch=master)<br/>                             | Formats a variant into string form by parsing a format string.<br/>                                                                                         |
| [**VarFormatCurrency**](/windows/previous-versions/OleAuto/nf-oleauto-varformatcurrency?branch=master)<br/>             | Formats a variant containing currency values into a string form.<br/>                                                                                       |
| [**VarFormatDateTime**](/windows/previous-versions/OleAuto/nf-oleauto-varformatdatetime?branch=master)<br/>             | Formats a variant containing named date and time information into a string.<br/>                                                                            |
| [**VarFormatFromTokens**](/windows/previous-versions/OleAuto/nf-oleauto-varformatfromtokens?branch=master)<br/>         | Takes a tokenized format string and applies it to a variant to produce a formatted output string.<br/>                                                      |
| [**VarFormatNumber**](/windows/previous-versions/OleAuto/nf-oleauto-varformatnumber?branch=master)<br/>                 | Formats a variant containing numbers into a string form.<br/>                                                                                               |
| [**VarFormatPercent**](/windows/previous-versions/OleAuto/nf-oleauto-varformatpercent?branch=master)<br/>               | Formats a variant containing percentages into a string form.<br/>                                                                                           |
| [**VarMonthName**](/windows/previous-versions/OleAuto/nf-oleauto-varmonthname?branch=master)<br/>                       | Returns a string containing the localized month name.<br/>                                                                                                  |
| [**VarTokenizeFormatString**](/windows/previous-versions/OleAuto/nf-oleauto-vartokenizeformatstring?branch=master)<br/> | Parses the actual format string into a series of tokens which can be used to format variants using [**VarFormatFromTokens**](/windows/previous-versions/OleAuto/nf-oleauto-varformatfromtokens?branch=master).<br/> |
| [**VarWeekdayName**](/windows/previous-versions/OleAuto/nf-oleauto-varweekdayname?branch=master)<br/>                   | Returns a string containing the localized name of the weekday.<br/>                                                                                         |



 

 

 





