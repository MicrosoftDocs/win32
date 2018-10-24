---
title: Converting Domain Account Name Formats
description: The Microsoft Win32 functions for working with the service control manager (SCM) on a host server use the \ 0034; domain \\ username \ 0034; format for service accounts.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a8bb6331-5070-4f46-b03d-615a004b3982
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Converting Domain Account Name Formats

The Microsoft Win32 functions for working with the service control manager (SCM) on a host server use the "<domain>\\<username>" format for service accounts. For example, if you call the [**QueryServiceConfig**](https://msdn.microsoft.com/library/windows/desktop/ms684932) function to retrieve the user account under which your service runs, the function returns the name in "Fabrikam\\jeffsmith" format. To bind to the user account in the directory, for example to change the account password, the distinguished name of the account is required, which has the format "CN=Jeff Smith,CN=Users,DC=Fabrikam,DC=COM".

To convert between the various name formats, use the [**TranslateName**](https://msdn.microsoft.com/library/windows/desktop/ms725484) function, which can convert a name to other formats, such as a user principal name (UPN).

 

 




