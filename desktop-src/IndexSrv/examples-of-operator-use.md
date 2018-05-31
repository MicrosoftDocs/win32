---
title: Examples of Operator Use
description: Examples of Operator Use
ms.assetid: 4eec337b-fe62-421c-8d58-801fd1eb9510
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Examples of Operator Use

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following examples illustrate the use of the Boolean and proximity operators.



| To Search For                                                                 | Example                                                                                                                                                                                                                     | Results                                                                                                    |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Both terms in the same document.<br/>                                   | red **AND** dog<br/>  Or <br/> red & dog<br/>                                                                                                                                                             | Documents with both the words *red* and *dog*.<br/>                                                  |
| Either term in a document.<br/>                                         | red **OR** dog<br/>  Or <br/> red \| dog<br/>                                                                                                                                                             | Documents with either of the words red or dog.<br/>                                                  |
| The first term without the second term.<br/>                            | red **AND NOT** dog<br/>  Or <br/> red & ! dog<br/>                                                                                                                                                       | Documents with the word *red* but not *dog*.<br/>                                                    |
| Several terms in the same document, close together.<br/>                | red {**NEAR** dist = 50, unit = word} dog {**NEAR** dist = 50, unit = word} cat<br/>  Or <br/> red **NEAR** dog **NEAR** cat<br/>  Or <br/> (red ~ dog) ~ cat<br/>                            | Documents with the word *red* near the word *dog* and that combination near the word *cat*. <br/>    |
| Several terms in the same document, but not others close together.<br/> | (red **OR** dog) **AND NOT** (black {**NEAR** dist = 50, unit = word} cat)<br/>  Or <br/> (red **OR** dog) **AND NOT** (black **NEAR** cat)<br/>  Or <br/> (red \| dog) &! (black ~ cat)<br/> | Documents with the word *red* or the word *dog*, but not the word *black* near the word *cat*. <br/> |
| Documents not matching a value-type property.<br/>                      | **NOT** @size = 100<br/>  Or <br/> ! @size = 100<br/>                                                                                                                                                     | Documents that are not 100 bytes. <br/>                                                              |



 

 

 





