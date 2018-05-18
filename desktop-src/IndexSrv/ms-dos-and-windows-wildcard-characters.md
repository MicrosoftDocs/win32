---
title: MS-DOS and Windows Wildcard Characters
description: MS-DOS and Windows Wildcard Characters
ms.assetid: '9091c137-2659-48e0-b7d3-0bc506e3b9cc'
---

# MS-DOS and Windows Wildcard Characters

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The asterisk (\*) and question mark (?) are used as wildcard characters, as they are in MS-DOS and Windows. The asterisk matches any sequence of characters, whereas the question mark matches any single character. In its long form, Dialect 2 uses the {regex} tag with the asterisk or the question mark to specify the wildcard characters. In its short form, Dialect 2 uses the equal sign (=) to indicate that wildcard characters are used. Essentially, "=" turns on the MS-DOS/Windows wildcard character mode. If no equal sign is used, a **CONTAINS** operator is assumed.



| To Search For                                                                | Example                                                                                                               | Results                                                                        |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Documents with any number of characters in the name.<br/>              | {prop name=filename} {regex} \*.doc {/regex}{/prop}<br/> —Or—<br/> \#filename = \*.doc<br/>         | Documents with any name and the extension *doc*.<br/>                    |
| Documents with any number of characters in the extension.<br/>         | {prop name=filename} {regex} readme.\* {/regex}{/prop}<br/> —Or—<br/> \#filename = readme.\*<br/>   | Documents with the name *readme* and any extension.<br/>                 |
| Documents with a specified number of characters in the extension.<br/> | {prop name=filename} {regex} readme.??? {/regex}{/prop}<br/> —Or—<br/> \#filename = readme.???<br/> | Documents with the name *readme* and any three-character extension.<br/> |



 

> [!Note]  
> In the Indexing Service query language, the syntax \#contents = *text* is invalid.t

 

 

 





