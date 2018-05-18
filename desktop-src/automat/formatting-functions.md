---
title: Formatting Functions
description: To format a variant into a string you must first tokenize the format string and then apply the format on that string.
ms.assetid: 'a00ee3c1-9799-4cd8-a13c-063c725aab68'
---

# Formatting Functions

To format a variant into a string you must first tokenize the format string and then apply the format on that string. The formatting functions can be used to apply the format in one step and to apply the same format repeatedly. For example, you can call the [**VarFormat**](varformat.md) function to apply the formatting at once. If you are going to apply the same format over again you can call [**VarTokenizeFormatString**](vartokenizeformatstring.md) and use the tokens from [**VarFormatFromTokens**](varformatfromtokens.md) repeatedly.

The following table describes the formatting functions.

## In this section



| Topic                                                                 | Description                                                                                                                                                       |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VarFormat**](varformat.md)<br/>                             | Formats a variant into string form by parsing a format string.<br/>                                                                                         |
| [**VarFormatCurrency**](varformatcurrency.md)<br/>             | Formats a variant containing currency values into a string form.<br/>                                                                                       |
| [**VarFormatDateTime**](varformatdatetime.md)<br/>             | Formats a variant containing named date and time information into a string.<br/>                                                                            |
| [**VarFormatFromTokens**](varformatfromtokens.md)<br/>         | Takes a tokenized format string and applies it to a variant to produce a formatted output string.<br/>                                                      |
| [**VarFormatNumber**](varformatnumber.md)<br/>                 | Formats a variant containing numbers into a string form.<br/>                                                                                               |
| [**VarFormatPercent**](varformatpercent.md)<br/>               | Formats a variant containing percentages into a string form.<br/>                                                                                           |
| [**VarMonthName**](varmonthname.md)<br/>                       | Returns a string containing the localized month name.<br/>                                                                                                  |
| [**VarTokenizeFormatString**](vartokenizeformatstring.md)<br/> | Parses the actual format string into a series of tokens which can be used to format variants using [**VarFormatFromTokens**](varformatfromtokens.md).<br/> |
| [**VarWeekdayName**](varweekdayname.md)<br/>                   | Returns a string containing the localized name of the weekday.<br/>                                                                                         |



 

 

 





