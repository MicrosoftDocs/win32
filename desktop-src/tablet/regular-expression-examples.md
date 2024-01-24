---
description: The following examples show some handwriting regular expressions that you can create.
ms.assetid: b4954e05-64d0-434a-96fd-6185671252d0
title: Regular Expression Examples
ms.topic: article
ms.date: 05/31/2018
---

# Regular Expression Examples

The following examples show some handwriting regular expressions that you can create.



| Expression                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                               | Matches                                                                          | Non-matches                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-------------------------------------------|
| s(!IS\_ONECHAR)+p<br/>                                                                                                                                                                                                                                                                | Matches any word that begins with lower case "s", contains one or more characters (as defined by the IS\_ONECHAR input scope), and ends with a lower case "p".<br/> | stop<br/> soup<br/> schlep<br/> s234p<br/>               | Stop<br/> sp<br/>             |
| (0\|1\|2\|3\|4\|5\|6\|7\|8\|9)<br/>                                                                                                                                                                                                                                                   | Matches any single digit, 1 through 9.<br/>                                                                                                                         | 1<br/> 6<br/> 0<br/>                                           | 42<br/> One<br/>              |
| (0\|1\|2\|3\|4\|5\|6\|7\|8\|9\|,\|-)+<br/>                                                                                                                                                                                                                                            | Matches one or more single digits, commas, or dashes. Useful for limiting input to a range or set of numbers, such as a range of pages to print.<br/>               | 1<br/> 1-6<br/> 2,4,7<br/> 2-6,9,135<br/> ,,,<br/> | Three<br/> 7 through 9<br/>   |
| (0\|1\|2\|3\|4\|5\|6\|7\|8\|9)(0\|1\|2\|3\|4\|5\|6\|7\|8\|9)(0\|1\|2\|3\|4\|5\|6\|7\|8\|9)-(0\|1\|2\|3\|4\|5\|6\|7\|8\|9)(0\|1\|2\|3\|4\|5\|6\|7\|8\|9)-(0\|1\|2\|3\|4\|5\|6\|7\|8\|9)(0\|1\|2\|3\|4\|5\|6\|7\|8\|9)(0\|1\|2\|3\|4\|5\|6\|7\|8\|9)(0\|1\|2\|3\|4\|5\|6\|7\|8\|9)<br/> | A social security number. The format of a social security number is *nnn* - *nn* - *nnnn*.<br/>                                                                     | 123-45-6789<br/>                                                           | 12-123-12<br/> 12-2-3456<br/> |



 

 

 




