---
description: The NetworkService account is a predefined local account used by the service control manager.
ms.assetid: f90d9346-10ed-4eba-bae2-9a1f1e6dc6b7
title: NetworkService Account
ms.topic: article
ms.date: 05/31/2018
---

# NetworkService Account

The NetworkService account is a predefined local account used by the service control manager. This account is not recognized by the security subsystem, so you cannot specify its name in a call to the [**LookupAccountName**](/windows/desktop/api/winbase/nf-winbase-lookupaccountnamea) function. It has minimum privileges on the local computer and acts as the computer on the network.

This account can be specified in a call to the [**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea) and [**ChangeServiceConfig**](/windows/desktop/api/Winsvc/nf-winsvc-changeserviceconfiga) functions. Note that this account does not have a password, so any password information that you provide in this call is ignored. While the security subsystem localizes this account name, the SCM does not support localized names. Therefore, you will receive a localized name for this account from the [**LookupAccountSid**](/windows/desktop/api/winbase/nf-winbase-lookupaccountsida) function, but the name of the account must be NT AUTHORITY\\NetworkService when you call **CreateService** or **ChangeServiceConfig**, regardless of the locale, or unexpected results can occur.

A service that runs in the context of the NetworkService account presents the computer's credentials to remote servers. By default, the remote token contains SIDs for the Everyone and Authenticated Users groups. The user SID is created from the **SECURITY\_NETWORK\_SERVICE\_RID** value.

The NetworkService account has its own subkey under the **HKEY\_USERS** registry key. Therefore, the **HKEY\_CURRENT\_USER** registry key is associated with the NetworkService account.

The NetworkService account has the following privileges:

-   **SE\_ASSIGNPRIMARYTOKEN\_NAME** (disabled)
-   **SE\_AUDIT\_NAME** (disabled)
-   **SE\_CHANGE\_NOTIFY\_NAME** (enabled)
-   **SE\_CREATE\_GLOBAL\_NAME** (enabled)
-   **SE\_IMPERSONATE\_NAME** (enabled)
-   **SE\_INCREASE\_QUOTA\_NAME** (disabled)
-   **SE\_SHUTDOWN\_NAME** (disabled)
-   **SE\_UNDOCK\_NAME** (disabled)
-   Any privileges assigned to users and authenticated users

For more information, see [Service Security and Access Rights](service-security-and-access-rights.md).

 

 
