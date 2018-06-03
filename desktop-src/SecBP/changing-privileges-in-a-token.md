---
Description: Explains how to change privileges in a token by using the AdjustTokenPrivileges and CreateRestrictedToken functions.
ms.assetid: b8e47d04-07c1-4d57-8209-6b0c397476e5
title: Changing Privileges in a Token
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Changing Privileges in a Token

You can change the privileges in either a primary or an impersonation token in two ways:

-   Enable or disable privileges by using the [**AdjustTokenPrivileges**](https://msdn.microsoft.com/library/windows/desktop/aa375202) function.
-   Restrict or remove privileges by using the [**CreateRestrictedToken**](https://msdn.microsoft.com/library/windows/desktop/aa446583) function.

[**AdjustTokenPrivileges**](https://msdn.microsoft.com/library/windows/desktop/aa375202) cannot add or remove privileges from the token. It can only enable existing privileges that are currently disabled or disable existing privileges that are currently enabled. For examples, see [Enabling and Disabling Privileges in C++](https://msdn.microsoft.com/library/windows/desktop/aa446619).

To assign privileges to a user account, see [Assigning Privileges to an Account](assigning-privileges-to-an-account.md).

[**CreateRestrictedToken**](https://msdn.microsoft.com/library/windows/desktop/aa446583) has more extensive capabilities as follows:

-   Removing a privilege. Note that removing a privilege is not the same as disabling one. After a privilege is removed from a token, it cannot be put back.
-   Attaching the deny-only attribute to SIDs in the token. This has the effect of disallowing specific groups or accounts, for example, denying the Everyone group delete access to a particular file. For more information on restricting SIDs, see [SID Attributes in an Access Token](https://msdn.microsoft.com/library/windows/desktop/aa379596).
-   Specifying a list of restricting SIDs in the token. For information about restricting SIDs, see [Restricted Tokens](https://msdn.microsoft.com/library/windows/desktop/aa379316).

 

 



