---
title: Resource Virtualization
description: Resource Virtualization
ms.assetid: ead0e99a-94da-4e80-bb68-d8f4b199173d
ms.topic: article
ms.date: 05/31/2018
---

# Resource Virtualization

The primary function of the TBS is to efficiently share certain limited TPM resources: keys, authorization, and transport sessions.

When an instance of one of these resources is created, the TBS creates a virtual instance of the resource, and returns a handle to this virtual instance in the result command stream (rather than the actual handle instance returned by the TPM). The TBS maintains a mapping between the virtual handle and the actual handle internally. If the TPM runs out of space to hold more resources of a given type, existing instances of the resource are selectively saved and evicted until the TPM can hold the new resource. When the old resources are required again, the TBS loads the saved contexts (saving and evicting other resources if necessary) before submitting the command.

All virtualization in the TBS is performed on behalf of a specific context. Each context is only allowed to access virtual resources created specifically on its behalf, as well as the physical resources on the TPM that corresponds to those virtual resources. By default, the total number of all virtualized resources is limited to 500. This number can be altered by creating or modifying a **DWORD** registry value named **MaxResources** under **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Tpm**. Real-time TBS resource usage can be observed by using the Performance Monitor tool to track the number of TBS resources. This restriction became obsolete with Windows 8 and Windows Server 2012.

Limited TPM resources that are not virtualized by the TBS (such as counters and NV store) must be cooperatively shared among software stacks.

> [!Note]  
> This handle virtualization causes commands that include key handles in the calculation of HMAC authorization parameters to fail. As a result, many commands deprecated in TPM version 1.2 cannot be used by application software in the TBS environment.

 

## Resource Limits

The TPM enables callers to query its capabilities to determine how much space is available for certain types of resources. Some of these resource limits, such as the amount of space available for keys, authorization sessions, and transport sessions, are effectively extended by the TBS through virtualization. TBS limitations, which are controlled by the **MaxResources** registry setting, are usually far larger than the actual limitations of the underlying TPM hardware. No mechanism is supplied for querying TBS limitations separately from the TPM hardware limits. This TBS limitation became obsolete with Windows 8 and Windows Server 2012.

## Keys

The TBS virtualizes key handles so that keys can be transparently unloaded from the TPM when they are not being used and loaded back onto the TPM when they are needed. When a key is created, the TBS associates a virtual handle with the loaded key. The same virtual handle is used for the lifetime of the resource. Virtual key handles are only valid in the context that created them, and the associated resources are not preserved beyond the life of the context.

-   Creating Keys with TPM\_LoadKey2

    If a key is created by using the TPM\_LoadKey2, TPM2\_CreatePrimary, TPM2\_Load, or TPM2\_LoadExternal command, the TBS replaces the handle in the return byte stream with a virtual key handle of its choosing. As a result, the TBS ensures that each virtual handle is unique. If the TBS detects a collision (an extremely unlikely event), the TBS unloads the key from the TPM and informs the calling software. The software can then resubmit the operation. This process can be repeated until the TBS gets a unique key handle.

-   Clearing Keys

    The TBS invalidates the virtual key handle when it receives a TPM\_FlushSpecific or TPM2\_FlushContext message for that virtual handle from the client context. If the key is physically present on the TPM when the flush message is received, the TBS flushes the key from the TPM at that time.

-   Temporarily Removing Keys

    When evicting a key from the TPM to make room for a new item, the TBS executes a TPM\_SaveContext or TPM2\_ContextSave command on the key before evicting it.

-   Restoring Keys

    When a command that references a loaded key is submitted to the TBS, it ensures that the key is physically present on the TPM. If the key is not present, the TBS restores it with a call to TPM\_LoadContext or TPM2\_ContextLoad. If a key cannot be restored to the TPM, the TBS returns TPM\_E\_INVALID\_KEYHANDLE as the TPM result.

The TBS replaces each virtual handle associated with a key in a command stream with the physical handle of the key loaded on the TPM. If a command is submitted with a virtual handle that is not recognized by the TBS in the context of the caller, the TBS formats an error stream for the caller with TPM\_E\_INVALID\_KEYHANDLE.

## Authorization Sessions

Authorization sessions are created by calling TPM\_OIAP, TPM\_OSAP, or TPM\_DSAP. In each case, the return byte stream contains the physical TPM handle of the newly created authorization session. The TBS replaces this with a virtual handle. When the authorization session is subsequently referenced, the TBS replaces the virtual handle in the command stream with the physical handle of the authorization session. The TBS ensures that the lifetime of the virtual authorization session matches that of the physical authorization session. If a client attempts to use an expired virtual handle, the TBS formats an error stream with error TPM\_INVALIDAUTHHANDLE.

Session slots are limited, and the TBS may run out of external slots in which to save authorization session contexts. If this happens, the TBS chooses an authorization session to invalidate so that the new context can be successfully saved. An application that attempts to use the old context will need to re-create the authorization session.

The TBS invalidates the virtual authorization session when any of the following cases occur:

-   The continue-use flag associated with the authorization session in the returned command stream from the TPM is **FALSE**.
-   A command that uses an authorization session fails.
-   A command is executed that invalidates the authorization session associated with the command (such as TPM\_CreateWrapKey).
-   A key associated with an OSAP or DSAP session is evicted from the TPM with a call to TPM\_FlushSpecific or TPM2\_FlushContext (without regard to whether this command originated with the TBS or with higher-level software).

    The TBS will automatically resynchronize the authorization sessions after successful execution of certain nondeterministic commands to ensure that the TBS state remains consistent with the TPM state. The affected commands are:

    -   TPM\_ORD\_Delegate\_Manage
    -   TPM\_ORD\_Delegate\_CreateOwnerDelegation
    -   TPM\_ORD\_Delegate\_LoadOwnerDelegation

In each of the following cases the authorization session on the TPM is flushed automatically by the TPM:

-   Creating Authorization Sessions

    Virtual authorization session handles are only valid in the context that created them, and the associated resources are not preserved beyond the life of the associated context.

-   Clearing Authorization Sessions

    The TBS invalidates the virtual authorization session if it receives a TPM\_FlushSpecific or TPM2\_FlushContext command for the virtual handle from the client context. If the authorization session is physically present on the TPM when the flush command is received, the TBS flushes the physical session from the TPM immediately.

-   Temporarily Removing Authorization Sessions

    When evicting an authorization session from the TPM to make room for a new entity, the TBS executes TPM\_SaveContext or TPM2\_ContextSave on that authorization session.

-   Restoring Authorization Sessions

    When an authorized TPM command is submitted to the TBS, the TBS ensures that all virtual authorization sessions referred to in the command are physically present on the TPM. If any of the authorization sessions are not present, the TBS restores them with a call to TPM\_LoadContext or TPM2\_ContextLoad. If an authorization session cannot be restored to the TPM, the TBS returns TPM\_E\_INVALID\_HANDLE as the TPM result.

The TBS replaces each virtual handle associated with an authorization session in a command stream with the physical handle of the authorization session loaded on the TPM.

If a command is submitted with a virtual handle that is not recognized by the TBS in the context of the caller, the TBS formats an error stream for the caller with the error TPM\_E\_INVALID\_HANDLE.

## Transport Sessions

> [!Note]  
> The handling of transport sessions as described here is specific to Windows Vista and Windows Server 2008.

 

Transport sessions are a mechanism provided by the TPM that enables a software stack to encrypt data in a command as it passes between the software and the TPM. This prevents an adversary from intercepting the data as it passes over the hardware bus.

> [!IMPORTANT]
> Only the payload data is encrypted. The commands being executed can still be identified.

 

Unfortunately, this mechanism also prevents the TBS from examining payload data. In most cases this is not an issue because the TBS only modifies handles, not payload data. However, in the case of TPM\_LoadContext for instance, the returned resource handle is covered by the encryption. Therefore, the TBS prevents attempts to perform a TPM\_LoadContext operation covered by a transport session.

The TBS blocks the following commands under transport session:

-   TPM\_EstablishTransport
-   TPM\_ExecuteTransport
-   TPM\_Terminate\_Handle
-   TPM\_LoadKey
-   TPM\_EvictKey
-   TPM\_SaveKeyContext
-   TPM\_LoadKeyContext
-   TPM\_SaveAuthContext
-   TPM\_LoadAuthContext
-   TPM\_SaveContext
-   TPM\_LoadContext
-   TPM\_FlushSpecific

When any one of these commands is covered by a transport session, the TBS returns TPM\_E\_EMBEDDED\_COMMAND\_UNSUPPORTED as the TPM result.

Transport session handles are virtualized in a manner similar to key handles and authorization handles. There are a limited number of saved transport session context slots available on the TPM.

The TBS invalidates the virtual transport session if any of the following cases occurs:

-   The continue-use flag associated with the transport session in the return command stream from the TPM is **FALSE**.

    As with authorization sessions above, the TBS will automatically resynchronize transport sessions after successful execution of certain nondeterministic commands to ensure that the TBS state remains consistent with the TPM state. The affected commands are:

    -   TPM\_ORD\_Delegate\_Manage
    -   TPM\_ORD\_Delegate\_CreateOwnerDelegation
    -   TPM\_ORD\_Delegate\_LoadOwnerDelegation

In each of these cases, the transport session on the TPM will be flushed automatically by the TPM:

-   Creating Transport Sessions

    The TBS creates a virtual handle for each transport session created by a client. Virtual transport handles are only valid in the context that created them, and the associated resources are not preserved beyond the life of the associated context.

-   Clearing Transport Sessions

    The TBS invalidates the virtual transport session if it receives a TPM\_FlushSpecific command for the virtual handle from the client context. If the transport session is physically present on the TPM when the flush command is received, the TBS flushes the physical session from the TPM immediately.

-   Temporarily Removing Transport Sessions

    When evicting a transport session from the TPM to make room for a new entity, the TBS executes TPM\_SaveContext on that transport session.

-   Restoring Transport Sessions

    When a TPM\_ExecuteTransport command is submitted to the TBS, the TBS ensures that the transport session referred to in the command is physically present on the TPM. If the transport session is not present, the TBS restores it with a call to TPM\_LoadContext.

The TBS replaces the virtual handle associated with the transport session in a command stream with the physical handle of the transport session loaded on the TPM. If a command is submitted with a virtual handle that is not recognized by the TBS in the context of the caller, the TBS formats an error stream for the caller by using TPM\_E\_INVALID\_HANDLE.

## Exclusive Transport Sessions

Exclusive wrapped transport sessions are a way for top-level software to determine whether any other software has accessed the TPM during a chain of commands. They do not prevent other software from accessing the TPM, they just give the creator of the transport session a means of determining that some other access occurred. The TBS does not do anything specific to hinder exclusive transport sessions, but it is somewhat incompatible with them. The TBS attempts to duplicate the natural behavior of the TPM by being transparent, so it does not favor commands from contexts that establish an exclusive transport session. For example, if client B submits a command when client A is in an exclusive transport session, then it will invalidate the exclusive transport session of client A.

Commands initiated by TBS can also terminate the exclusive transport session. This happens when client A is in an exclusive transport session, and a command executed by client A calls for a resource that is not physically present in the TPM. This situation triggers the TBS virtualization manager to execute a TPM\_LoadContext command to supply that resource, which terminates the exclusive transport session of client A.

 

 




