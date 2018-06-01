---
Description: Query Syntax Errors
ms.assetid: 287ec486-cf08-43c3-b975-b121e17e780d
title: Query Syntax Errors
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Query Syntax Errors

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following error messages can be returned when executing a query.



| Message                                                                                                            | Explanation                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Expecting closing parenthesis ')'.                                                                                 | Occurs when parentheses are mismatched.                                                                                                                                                                                              |
| Expecting closing square bracket '\]'.                                                                             | An opening square bracket was not followed by a closing square bracket. Usually the result of an ill-formed weight.                                                                                                                  |
| Expecting comma.                                                                                                   | Occurs when a reserved token or end-of-string occurs before the closing brace of a vector property. Example: @VectorString = {A1, B@}.                                                                                               |
| Expecting currency.                                                                                                | A currency value was expected but not found. Occurs when a property of type DBTYPE\_CY is fed incorrect input. Correct format for currency is \#.\#.                                                                                 |
| Expecting date.                                                                                                    | A date was expected but not found. Occurs when a property of type DBTYPE\_DATE is fed incorrect input. Allowed formats for dates are yyyy/mm/dd, yyyy/mm/dd hh:mm:ss, and relative dates (-\#y, -\#m, -\#w, -\#d, -\#h, -\#n, -\#s). |
| Expecting end of string.                                                                                           | A complete restriction has been parsed, and there is still more input. Example: (@size = 100) sample.                                                                                                                                |
| Expecting GUID.                                                                                                    | A GUID was expected but not found. Occurs when a property of DBTYPE\_GUID is fed incorrect input. Property format for a GUID is XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.                                                                |
| Expecting integer.                                                                                                 | An integer was expected but not found. Occurs when a property of an integer type (DBTYPE\_I4, and so on) is fed a non-numeric value, or a non-numeric vector weight is entered.                                                      |
| Expecting phrase.                                                                                                  | A textual phrase was expected and not found. This error occurs in a variety of situations where the query parser is expecting plain text and is given a special token instead.                                                       |
| Expecting property name.                                                                                           | Occurs when a correctly formed property name is not found after an @ sign.                                                                                                                                                           |
| Expecting real number.                                                                                             | A real number was expected but not found. Occurs when a property of a real type (DBTYPE\_R4, and so on) is fed a non-numeric value.                                                                                                  |
| Expecting regular expression.                                                                                      | Similar to Expecting phrase error. Used when in regular-expression parsing mode.                                                                                                                                                     |
| The file &lt;file&gt; is on a remote UNC share. .Idq, .ida, and .htx files cannot be placed on a remote UNC share. | An .idq, .ida, or .htx file was found on a remote UNC share. None of these files can be on a remote UNC share.                                                                                                                       |
| Invalid literal.                                                                                                   | Occurs only when a query property is formatted poorly. Almost all conditions are covered by the Expecting integer, Expecting date, and other errors.                                                                                 |
| No such property.                                                                                                  | Property specified after @, \#, or $ does not exist. It is not a default property and is not specified in the [Names section of the .idq file](names-section-of-idq-files.md).                                                      |
| Not yet implemented.                                                                                               | An unimplemented feature of Indexing Service.                                                                                                                                                                                        |
| Out of memory.                                                                                                     | The server ran out of memory processing the CiRestriction parameter.                                                                                                                                                                 |
| Regular expressions require a property of type string.                                                             | A property of a nontextual type (DBTYPE\_I4, DBTYPE\_GUID, and so on) was selected for regular-expression mode. For example, \#size 100\* will cause this error.                                                                     |
| Unexpected end of string.                                                                                          | There is a missing quotation mark in your query.                                                                                                                                                                                     |
| Unsupported property type.                                                                                         | For future expansion. Will occur when a display-only property type is used in a query restriction.                                                                                                                                   |
| Weight must be between 0 and 1000.                                                                                 | Occurs when a query term weight is outside the legal range of 0 to 1000.                                                                                                                                                             |



 

 

 



