---
description: The VSS infrastructure requires writer processes to be able to function both as COM clients and as servers.
ms.assetid: 59bb7a86-e874-45ce-abd6-cafd18802c4d
title: Security Considerations for Writers
ms.topic: article
ms.date: 05/31/2018
---

# Security Considerations for Writers

The VSS infrastructure requires writer processes to be able to function both as COM clients and as servers.

When acting as servers, VSS writers expose COM interfaces (for example, the VSS event handlers such as [**CVssWriter::OnIdentify**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onidentify)) and receive incoming COM calls from VSS processes (such as requesters and the VSS service) or RPC calls from processes that are external to VSS, typically when these processes generate VSS events (for example, when a requester calls [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata)). Therefore, a VSS writer needs to securely manage which COM clients are able to make incoming COM calls into its process.

Similarly, VSS writers may also act as COM clients, making outgoing COM calls to callbacks supplied by the VSS infrastructure or RPC calls to processes that are external to VSS. These callbacks that are provided either by a backup application or by the VSS service allow the writer to perform tasks such as updating the Backup Components Document through the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface. Therefore, VSS security settings must allow writers to make outgoing COM calls into other VSS processes.

The simplest mechanism for managing writer security issues involves the proper selection of the user account under which it runs. A writer typically needs to run under a user who is a member of either the Administrators group or the Backup Operators group, or it needs to run as the Local System account.

By default, when a writer is acting as a COM client, if it does not run under these accounts, any COM call it makes is automatically rejected with **E\_ACCESSDENIED** without even getting to the COM method implementation.

## Disabling COM Exception Handling

When developing a writer, set the COM COMGLB\_EXCEPTION\_DONOT\_HANDLE global options flag to disable COM exception handling. It is important to do this because COM exception handling can mask fatal errors in a VSS application. The error that is masked can leave the process in an unstable and unpredictable state, which can lead to corruptions and hangs. For more information about this flag, see [IGlobalOptions](/windows/win32/api/objidlbase/nn-objidlbase-iglobaloptions).

## Setting Writer Default COM Access Check Permission

Writers need to be aware that when their processes act as a server (for example, to handle VSS events), they must allow incoming calls from other VSS participants, such as requesters or the VSS service.

However, by default, a process will allow only COM clients that are running under the same logon session the SELF SID) or running under the Local System account. This is a potential problem because these defaults are not sufficient to support the VSS infrastructure. For example, requesters may run as a "Backup Operator" user account that is neither in the same logon session as the writer process nor a Local System account.

To handle this type of problem, every COM server process can exercise further control over whether an RPC or COM client is allowed to perform a COM method the server (a writer in this case) implements by using [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) to set a process-wide default COM access check permission.

Writers can explicitly do the following:

-   Allow all processes access to call into the writer process.

    This option may be adequate for many writers, and is used by other COM servers—for example, all SVCHOST-based Windows services are already using this option, as are all COM+ Services by default.

    Allowing all processes to perform incoming COM calls is not necessarily a security weakness. A writer acting as a COM server, like all other COM servers, always retains the option of authorizing its clients on every COM method implemented in its process.

    To allow all processes COM access to a writer, you can pass a **NULL** security descriptor as the first parameter of [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity). (Note that **CoInitializeSecurity** must be called at most once for the entire process. Please see the COM documentation for more details on **CoInitializeSecurity**.)

    The following is a code example that includes a call to [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity):

    ``` syntax
    // Initialize COM security.
    hr = CoInitializeSecurity(
           NULL,                          // PSECURITY_DESCRIPTOR          pSecDesc,
           -1,                            // LONG                          cAuthSvc,
           NULL,                          // SOLE_AUTHENTICATION_SERVICE  *asAuthSvc,
           NULL,                          // void                         *pReserved1,
           RPC_C_AUTHN_LEVEL_PKT_PRIVACY, // DWORD                         dwAuthnLevel,
           RPC_C_IMP_LEVEL_IDENTIFY,      // DWORD                         dwImpLevel,
           NULL,                          // void                         *pAuthList,
           EOAC_NONE,                     // DWORD                         dwCapabilities,
           NULL                           // void                         *pReserved3
        );
    ```

    When explicitly setting a writer's COM-level security with [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity), you should do the following:

    -   Set the authentication level to at least **RPC\_C\_AUTHN\_LEVEL\_CONNECT**.

        For better security, consider using **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**.

    -   Set the impersonation level to **RPC\_C\_IMP\_LEVEL\_IDENTIFY** unless the writer process needs to allow impersonation for specific RPC or COM calls that are unrelated to VSS.

-   Allow only specified processes access to call into the writer process.

    A COM server (such as a writer) that is calling [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) with a non-**NULL** security descriptor can use the descriptor to configure itself to accept incoming calls only from users that belong to a specific set of accounts.

    A writer must ensure that COM clients running under valid users are authorized to call into its process. A writer that specifies a Security Descriptor in the first parameter must allow the following users to perform incoming calls into the requester process:

    -   Local System
    -   Members of the local Administrators group
    -   Members of the local Backup Operators group
    -   The account under which the writer is running

## Explicitly Controlling User Account Access to a Writer

There are cases where restricting access to a writer to processes running as Local System, or under the local Administrators or local Backup Operators local groups, may be too restrictive.

For example, a writer process (perhaps a third-party non-system writer) might not ordinarily need to be run under an Administrator or Backup Operator account. For security reasons, it would be best not to artificially promote the process's privileges to support VSS.

In these cases, the **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**\\**VSS**\\**VssAccessControl** registry key must be modified to instruct VSS that a specified user is safe to run a VSS writer.

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
                  MyDomain\MyUser = 1<dl>
<dt>

                  Data type
</dt>
<dd>                  REG_DWORD</dd>
</dl>
```

This mechanism can also be used to explicitly restrict an otherwise permitted user from running a VSS writer. The following example will restrict access from the "ThatDomain\\Administrator" account:

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

The user ThatDomain\\Administrator would not be able to run a VSS writer.

 

 
