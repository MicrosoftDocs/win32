---
description: The LocalService account is a predefined local account used by the service control manager.
ms.assetid: 5409e2fe-a349-4739-a481-f8a35fd3c9b4
title: LocalService Account
ms.topic: article
ms.date: 05/31/2018
---

# LocalService Account

The LocalService account is a predefined local account used by the service control manager. It has minimum privileges on the local computer and presents anonymous credentials on the network.

This account can be specified in a call to the [**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea) and [**ChangeServiceConfig**](/windows/desktop/api/Winsvc/nf-winsvc-changeserviceconfiga) functions. Note that this account does not have a password, so any password information that you provide in this call is ignored. While the security subsystem localizes this account name, the SCM does not support localized names. Therefore, you will receive a localized name for this account from the [**LookupAccountSid**](/windows/desktop/api/winbase/nf-winbase-lookupaccountsida) function, but the name of the account must be NT AUTHORITY\\LocalService when you call **CreateService** or **ChangeServiceConfig**, regardless of the locale, or unexpected results can occur.

The user SID is created from the **SECURITY\_LOCAL\_SERVICE\_RID** value.

The LocalService account has its own subkey under the **HKEY\_USERS** registry key. Therefore, the **HKEY\_CURRENT\_USER** registry key is associated with the LocalService account.

The LocalService account has the following privileges:

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

 

 
