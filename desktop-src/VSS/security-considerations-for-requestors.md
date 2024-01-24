---
description: The VSS infrastructure requires VSS requesters, such as backup applications, to be able to function both as COM clients and as a server.
ms.assetid: b01145c6-76ba-4a81-bca6-59c4ca488dac
title: Security Considerations for Requesters
ms.topic: article
ms.date: 05/31/2018
---

# Security Considerations for Requesters

The VSS infrastructure requires VSS requesters, such as backup applications, to be able to function both as COM clients and as a server.

When acting as a server, a requester exposes a set of COM callback interfaces that can be invoked from external processes (such as writers or the VSS service). Therefore, requesters need to securely manage which COM clients are able to make incoming COM calls into its process.

Similarly, requesters can act as a COM client for the COM APIs supplied by a VSS writer or by the VSS service. The requester-specific security settings must allow outgoing COM calls from the requester to these other processes.

The simplest mechanism for managing a requester's security issues involves proper selection of the user account under which it runs.

A requester typically needs to run under a user that is a member of either the Administrators group or the Backup Operators group, or run as the Local System account.

By default, when a requester is acting as a COM client, if it does not run under these accounts, any COM call is automatically rejected with **E\_ACCESSDENIED**, without even getting to the COM method implementation.

## Disabling COM Exception Handling

When developing a requester, set the COM COMGLB\_EXCEPTION\_DONOT\_HANDLE global options flag to disable COM exception handling. It is important to do this because COM exception handling can mask fatal errors in a VSS application. The error that is masked can leave the process in an unstable and unpredictable state, which can lead to corruptions and hangs. For more information about this flag, see [IGlobalOptions](/windows/win32/api/objidlbase/nn-objidlbase-iglobaloptions).

## Setting Requester Default COM Access Check Permission

Requesters need to be aware that when their process acts as a server (for example, allowing writers to modify the Backup Components Document), they must allow incoming calls from other VSS participants, such as writers or the VSS service.

However, by default, a Windows process will allow only COM clients that are running under the same logon session (the SELF SID) or running under the Local System account. This is a potential problem because these defaults are not adequate for the VSS infrastructure. For example, writers might run as a "Backup Operator" user account that is neither in the same logon session as the requester process nor a Local System account.

To handle this type of problem, every COM server process can exercise further control over whether an RPC or COM client is allowed to perform a COM method implemented by the server (a requester in this case) by using [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) to set a process-wide "Default COM Access Check Permission".

Requesters can explicitly do the following:

-   Allow all processes access to call into the requester process.

    This option may be adequate for the vast majority of requesters, and is used by other COM servers—for example, all SVCHOST-based Windows services are already using this option, as are all COM+ Services by default.

    Allowing all processes to perform incoming COM calls is not necessarily a security weakness. A requester acting as a COM server, like all other COM servers, always retains the option to authorize its clients on every COM method implemented in its process.

    Note that internal COM callbacks implemented by VSS are secured by default.

    To allow all processes COM access to a requester, you can pass a **NULL** security descriptor as the first parameter of [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity). (Note that **CoInitializeSecurity** must be called at most once for the entire process. Please see the COM documentation or MSDN for more information on **CoInitializeSecurity** calls.)

    The following code example shows how a requester should call [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) in Windows 8 and Windows Server 2012 and later, in order to be compatible with VSS for remote file shares (RVSS):

    ``` syntax
    // Initialize COM security.
       hr = CoInitializeSecurity(
            NULL,                          //  PSECURITY_DESCRIPTOR         pSecDesc,
            -1,                            //  LONG                         cAuthSvc,
            NULL,                          //  SOLE_AUTHENTICATION_SERVICE *asAuthSvc,
            NULL,                          //  void                        *pReserved1,
            RPC_C_AUTHN_LEVEL_PKT_PRIVACY, //  DWORD                        dwAuthnLevel,
            RPC_C_IMP_LEVEL_IMPERSONATE,   //  DWORD                        dwImpLevel,
            NULL,                          //  void                        *pAuthList,
            EOAC_STATIC,                   //  DWORD                        dwCapabilities,
            NULL                           //  void                        *pReserved3
            );
    ```

    When explicitly setting a requester's COM level security with [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity), you should do the following:

    -   Set the authentication level to at least **RPC\_C\_AUTHN\_LEVEL\_PKT\_INTEGRITY**. For better security, consider using **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**.
    -   Set the impersonation level to **RPC\_C\_IMP\_LEVEL\_IMPERSONATE**.
    -   Set the cloaking security capabilities to **EOAC\_STATIC**. For more information about cloaking security, see [Cloaking](../com/cloaking.md).

    The following code example shows how a requester should call [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) in Windows 7 and Windows Server 2008 R2 and earlier (or in Windows 8 and Windows Server 2012 and later, if RVSS compatibility is not needed):

    ``` syntax
    // Initialize COM security.
       hr = CoInitializeSecurity(
            NULL,                          //  PSECURITY_DESCRIPTOR         pSecDesc,
            -1,                            //  LONG                         cAuthSvc,
            NULL,                          //  SOLE_AUTHENTICATION_SERVICE *asAuthSvc,
            NULL,                          //  void                        *pReserved1,
            RPC_C_AUTHN_LEVEL_PKT_PRIVACY, //  DWORD                        dwAuthnLevel,
            RPC_C_IMP_LEVEL_IDENTIFY,      //  DWORD                        dwImpLevel,
            NULL,                          //  void                        *pAuthList,
            EOAC_NONE,                     //  DWORD                        dwCapabilities,
            NULL                           //  void                        *pReserved3
            );
    ```

    When explicitly setting a requester's COM level security with [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity), you should do the following:

    -   Set the authentication level to at least **RPC\_C\_AUTHN\_LEVEL\_CONNECT**. For better security, consider using **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**.
    -   Set the impersonation level to **RPC\_C\_IMP\_LEVEL\_IDENTIFY** unless the requester process needs to allow impersonation for specific RPC or COM calls that are unrelated to VSS.

-   Allow only specified processes access to call into the requester process.

    A COM server (such as a requester) that is calling [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) with a non-**NULL** security descriptor as the first parameter can use the descriptor to configure itself to accept incoming calls only from users that belong to a specific set of accounts.

    A requester must ensure that COM clients running under valid users are authorized to call into its process. A requester that specifies a Security Descriptor in the first parameter must allow the following users to perform incoming calls into the requester process:

    -   Local System
    -   Local Service

        **Windows XP:** This value is not supported until Windows Server 2003.

    -   Network Service

        **Windows XP:** This value is not supported until Windows Server 2003.

    -   Members of the local Administrators group
    -   Members of the local Backup Operators group
    -   Special users that are specified in the registry location below, with "1" as their REG\_DWORD value

## Explicitly Controlling User Account Access to a Requester

There are cases where restricting access to a requester to processes running as Local System, or under the local Administrators or local Backup Operators groups, may be too restrictive.

For example, a specified requester process might not ordinarily need to be run under an Administrator or Backup Operator account. For security reasons, it would be best not to artificially promote the processes privileges to support VSS.

In these cases, the **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**\\**VSS**\\**VssAccessControl** registry key must be modified to instruct VSS that a specified user is safe to run a VSS requester.

Under this key, you must create a subkey that has the same name as the account that is to be granted or denied access. This subkey must be set to one of the values in the following table.

| Value | Meaning                                             |
|-------|-----------------------------------------------------|
| 0     | Deny the user access to your writer and requester.  |
| 1     | Grant the user access to your writer.               |
| 2     | Grant the user access to your requester.            |
| 3     | Grant the user access to your writer and requester. |



 

The following example grants access to the "MyDomain\\MyUser" account:

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Services
            VSS
               VssAccessControl
                  MyDomain\MyUser = 2<dl>
<dt>

                  Data type
</dt>
<dd>                  REG_DWORD</dd>
</dl>
```

This mechanism can also be used to explicitly restrict an otherwise permitted user from running a VSS requester. The following example will restrict access from the "ThatDomain\\Administrator" account:

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Services
            VSS
               VssAccessControl
                  ThatDomain\Administrator = 0<dl>
<dt>

                  Data type
</dt>
<dd>                  REG_DWORD</dd>
</dl>
```

The user ThatDomain\\Administrator would not be able to run a VSS requester.

## Performing a File Backup of the System State

If a requester performs system-state backup by backing up individual files instead of using a volume image for the backup, it must call the [**FindFirstFileNameW**](/windows/win32/api/fileapi/nf-fileapi-findfirstfilenamew) and [**FindNextFileNameW**](/windows/win32/api/fileapi/nf-fileapi-findnextfilenamew) functions to enumerate hard links on files that are located in the following directories:

-   Windows\\system32\\WDI\\perftrack\\
-   Windows\\WINSXS\\

These directories can only be accessed by members of the Administrators group. For this reason, such a requester must run under the system account or a user account that is a member of the Administrators group.

**Windows XP and Windows Server 2003:** The [**FindFirstFileNameW**](/windows/win32/api/fileapi/nf-fileapi-findfirstfilenamew) and [**FindNextFileNameW**](/windows/win32/api/fileapi/nf-fileapi-findnextfilenamew) functions are not supported until Windows Vista and Windows Server 2008.

 

 
