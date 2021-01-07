---
description: The LSA provides several functions that applications can call to enumerate or set privileges for user, group, and local group accounts.
ms.assetid: c28c03f0-4638-42ed-8dad-1e934cf99273
title: Managing Account Permissions
ms.topic: article
ms.date: 05/31/2018
---

# Managing Account Permissions

The LSA provides several functions that applications can call to enumerate or set [*privileges*](/windows/desktop/SecGloss/p-gly) for user, group, and local group accounts.

Before you can manage account information, your application must get a handle to the local [**Policy**](policy-object.md) object, as demonstrated in [Opening a Policy Object Handle](opening-a-policy-object-handle.md). In addition, to enumerate or edit permissions for an account, you must have the [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID) for that account. Your application can locate a SID given the account name, as described in [Translating Between Names and SIDs](translating-between-names-and-sids.md).

To access all accounts that have a particular permission, call [**LsaEnumerateAccountsWithUserRight**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaenumerateaccountswithuserright). This function populates an array with the SIDs of all accounts that have the specified permission.

After you have obtained the SID of an account, you can modify its permissions. Call [**LsaAddAccountRights**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaaddaccountrights) to add permissions to the account. If the specified account does not exist, **LsaAddAccountRights** creates it. To remove permissions from an account, call [**LsaRemoveAccountRights**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaremoveaccountrights). If you remove all permissions from an account, **LsaRemoveAccountRights** also deletes the account.

Your application can check the permissions currently assigned to an account by calling [**LsaEnumerateAccountRights**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaenumerateaccountrights). This function populates an array of [**LSA\_UNICODE\_STRING**](/windows/desktop/api/lsalookup/ns-lsalookup-lsa_unicode_string) structures. Each structure contains the name of a privilege held by the specified account.

The following example adds the SeServiceLogonRight permission to an account. In this example, the AccountSID variable specifies the SID of the account. For more information about how to lookup an account SID, see [Translating Between Names and SIDs](translating-between-names-and-sids.md).


```C++
#include <windows.h>
#include <ntsecapi.h>

void AddPrivileges(PSID AccountSID, LSA_HANDLE PolicyHandle)
{
  LSA_UNICODE_STRING lucPrivilege;
  NTSTATUS ntsResult;

  // Create an LSA_UNICODE_STRING for the privilege names.
  if (!InitLsaString(&lucPrivilege, L"SeServiceLogonRight"))
  {
         wprintf(L"Failed InitLsaString\n");
         return;
  }

  ntsResult = LsaAddAccountRights(
    PolicyHandle,  // An open policy handle.
    AccountSID,    // The target SID.
    &lucPrivilege, // The privileges.
    1              // Number of privileges.
  );                
  if (ntsResult == STATUS_SUCCESS) 
  {
    wprintf(L"Privilege added.\n");
  }
  else
  {
    wprintf(L"Privilege was not added - %lu \n",
      LsaNtStatusToWinError(ntsResult));
  }
} 
```



In the preceding example, the function InitLsaString converts a [*Unicode*](/windows/desktop/SecGloss/u-gly) string to an [**LSA\_UNICODE\_STRING**](/windows/desktop/api/lsalookup/ns-lsalookup-lsa_unicode_string) structure. The code for this function is shown in [Using LSA Unicode Strings](using-lsa-unicode-strings.md).

 

 
