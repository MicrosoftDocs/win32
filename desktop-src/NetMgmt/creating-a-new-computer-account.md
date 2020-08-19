---
title: Creating a New Computer Account
description: The following code sample demonstrates how to create a new computer account using the NetUserAdd function.
ms.assetid: 1e180b8e-b948-4836-b789-cb9dff0829e8
ms.topic: article
ms.date: 05/31/2018
---

# Creating a New Computer Account

The following code sample demonstrates how to create a new computer account using the [**NetUserAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuseradd) function.

The following are considerations for managing computer accounts:

-   The computer account name should be all uppercase for consistency with account management utilities.
-   A computer account name always has a trailing dollar sign ($). Any functions used to manage computer accounts must build the computer name such that the last character of the computer account name is a dollar sign ($). For interdomain trust, the account name is TrustingDomainName$.
-   The maximum computer name length is MAX\_COMPUTERNAME\_LENGTH (15). This length does not include the trailing dollar sign ($).
-   The password for a new computer account should be the lowercase representation of the computer account name, without the trailing dollar sign ($). For interdomain trust, the password can be an arbitrary value that matches the value specified on the trust side of the relationship.
-   The maximum password length is LM20\_PWLEN (14). The password should be truncated to this length if the computer account name exceeds this length.
-   The password provided at computer-account-creation time is valid only until the computer account becomes active on the domain. A new password is established during trust relationship activation.


```C++
#include <windows.h>
#include <lm.h>
#pragma comment(lib, "netapi32.lib")

BOOL AddMachineAccount(
    LPWSTR wTargetComputer,
    LPWSTR MachineAccount,
    DWORD AccountType
    )
{
    LPWSTR wAccount;
    LPWSTR wPassword;
    USER_INFO_1 ui;
    DWORD cbAccount;
    DWORD cbLength;
    DWORD dwError;

    //
    // Ensure a valid computer account type was passed.
    //
    if (AccountType != UF_WORKSTATION_TRUST_ACCOUNT &&
        AccountType != UF_SERVER_TRUST_ACCOUNT &&
        AccountType != UF_INTERDOMAIN_TRUST_ACCOUNT
        ) 
    {
        SetLastError(ERROR_INVALID_PARAMETER);
        return FALSE;
    }

    //
    // Obtain number of chars in computer account name.
    //
    cbLength = cbAccount = lstrlenW(MachineAccount);

    //
    // Ensure computer name doesn't exceed maximum length.
    //
    if(cbLength > MAX_COMPUTERNAME_LENGTH) {
        SetLastError(ERROR_INVALID_ACCOUNT_NAME);
        return FALSE;
    }

    //
    // Allocate storage to contain Unicode representation of
    // computer account name + trailing $ + NULL.
    //
    wAccount=(LPWSTR)HeapAlloc(GetProcessHeap(), 0,
        (cbAccount + 1 + 1) * sizeof(WCHAR)  // Account + '$' + NULL
        );

    if(wAccount == NULL) return FALSE;

    //
    // Password is the computer account name converted to lowercase;
    //  you will convert the passed MachineAccount in place.
    //
    wPassword = MachineAccount;

    //
    // Copy MachineAccount to the wAccount buffer allocated while
    //  converting computer account name to uppercase.
    //  Convert password (in place) to lowercase.
    //
    while(cbAccount--) {
        wAccount[cbAccount] = towupper( MachineAccount[cbAccount] );
        wPassword[cbAccount] = towlower( wPassword[cbAccount] );
    }

    //
    // Computer account names have a trailing Unicode '$'.
    //
    wAccount[cbLength] = L'$';
    wAccount[cbLength + 1] = L'\0'; // terminate the string

    //
    // If the password is greater than the max allowed, truncate.
    //
    if(cbLength > LM20_PWLEN) wPassword[LM20_PWLEN] = L'\0';

    //
    // Initialize the USER_INFO_1 structure.
    //
    ZeroMemory(&ui, sizeof(ui));

    ui.usri1_name = wAccount;
    ui.usri1_password = wPassword;

    ui.usri1_flags = AccountType | UF_SCRIPT;
    ui.usri1_priv = USER_PRIV_USER;

    dwError=NetUserAdd(
                wTargetComputer,    // target computer name
                1,                  // info level
                (LPBYTE) &ui,       // buffer
                NULL
                );

    //
    // Free allocated memory.
    //
    if(wAccount) HeapFree(GetProcessHeap(), 0, wAccount);

    //
    // Indicate whether the function was successful.
    //
    if(dwError == NO_ERROR)
        return TRUE;
    else {
        SetLastError(dwError);
        return FALSE;
    }
}
```



The user that calls the account management functions must have Administrator privilege on the target computer. In the case of existing computer accounts, the creator of the account can manage the account, regardless of administrative membership. For more information about calling functions that require administrator privileges, see [Running with Special Privileges](/windows/desktop/SecBP/running-with-special-privileges).

The SeMachineAccountPrivilege can be granted on the target computer to give specified users the ability to create computer accounts. This gives non-administrators the ability to create computer accounts. The caller needs to enable this privilege prior to adding the computer account. For more information about account privileges, see [Privileges](/windows/desktop/SecAuthZ/privileges) and [Authorization Constants](/windows/desktop/SecAuthZ/authorization-constants).

 

 