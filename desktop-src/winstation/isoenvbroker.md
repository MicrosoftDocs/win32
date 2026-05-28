---
title: IsolationSession interface
description: Isolation Session performs tasks related to managing background user sessions.
ms.tgt_platform: multiple
keywords:
- IsolationSession
topic_type:
- apiref
api_name:
- IsolationSession
api_location:
- IsolationSession.dll
api_type:
- COM
ms.topic: reference
ms.date: 10/24/2025
---

# IsolationSession interface

The Isolation Environment Broker is a windows service that performs tasks related to managing background user sessions.

This service is still experimental. The interface below will change on future OS releases.

## Windows.AI.IsolationSession.idl

```idl
namespace Windows.AI.IsolationSession
{
    // Structured error with remediation guidance. Every operation returns one.
    // Uses RoOriginateError internally for debugger/ETW visibility.
    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    runtimeclass IsoSessionError
    {
        // -- Construction --
        IsoSessionError();

        // -- Properties --
        HRESULT Code { get; };
        Boolean IsError { get; };
        String Message { get; };
        String Remediation { get; };

        // -- Methods --
        String Format();
    }

    // =====================================================================
    //  CONFIGURATION
    // =====================================================================

    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    enum IsoSessionConfigId
    {
        Small = 1,
        Medium = 2,
        Large = 3,
        Composable = 4,
    };


    // =====================================================================
    //  AGENT USER TYPES
    // =====================================================================

    // Result of AddUser / GetUser. Contains user info + structured error.
    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    runtimeclass IsoSessionUserResult
    {
        // -- Properties --
        String AgentName { get; };
        String AgentUserName { get; };
        String AgentUserSid { get; };
        IsoSessionError Error { get; };

        // Query extensions — new interface to avoid breaking existing consumers of the default IID.
        [interface_name("IIsoSessionUserResult2")]
        {
            String RegistrationId { get; };
        }
    }


    // =====================================================================
    //  PROCESS TYPES
    // =====================================================================

    // Options for creating an isolated process.
    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    runtimeclass IsoSessionProcessOptions
    {
        // -- Construction --
        IsoSessionProcessOptions();

        // -- Properties --
        Windows.Foundation.Collections.IMap<String, String> Environment { get; };
        Boolean InteractiveConsole;
        Boolean RedirectStandardError;
        Boolean RedirectStandardInput;
        Boolean RedirectStandardOutput;
        UInt32 TimeoutMilliseconds;
        String WorkingDirectory;
    }

    // A running process inside the isolation session.
    //
    // Owns ConPTY pipe handles for interactive I/O. The caller reads from OutputHandle and writes
    // to InputHandle using ReadFile/WriteFile. Close() releases the handles and detaches from the
    // process (the process itself continues running in the session).
    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    runtimeclass IsoSessionProcess : Windows.Foundation.IClosable
    {
        // -- Properties --
        Int32 ExitCode { get; };
        UInt64 ErrorHandle { get; };
        UInt64 InputHandle { get; };
        UInt64 OutputHandle { get; };
        UInt32 ProcessId { get; };
        String ProcessPath { get; };

        // -- Methods --
        void CloseStandardInput();
        void ResizeConsole(UInt16 columns, UInt16 rows);
        void SendCtrlClose();
        void Terminate();
        Int32 WaitForExit(UInt32 timeoutMs);
    }

    // =====================================================================
    //  FOLDER SHARING TYPES
    // =====================================================================

    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    enum IsoSessionFolderSharingAccessLevel
    {
        Read = 0,
        ReadWrite = 1,
        Remove = 2,
        Deny = 3,
    };

    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    enum IsoSessionFolderSharingStatus
    {
        Succeeded = 0,
        Failed = 1,
    };

    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    struct IsoSessionFolderSharingRequest
    {
        String FolderPath;
        IsoSessionFolderSharingAccessLevel AccessLevel;
    };

    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    runtimeclass IsoSessionFolderSharingResult
    {
        // -- Properties --
        String FolderPath { get; };
        IsoSessionFolderSharingStatus Status { get; };
        IsoSessionError Error { get; };
    }

    // =====================================================================
    //  RESULT TYPES
    // =====================================================================

    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    runtimeclass IsoSessionResult
    {
        IsoSessionError Error { get; };
    }

    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    runtimeclass IsoSessionProcessResult
    {
        // -- Properties --
        IsoSessionError Error { get; };
        IsoSessionProcess Process { get; };
    }



    // =====================================================================
    //  GRANULAR MANAGEMENT OPERATIONS
    //
    //  Instance class (not static) for better perf.
    //  Each method = one chunky call to server + structured error.
    // =====================================================================

    [contract(Windows.Foundation.UniversalApiContract, 19)]
    [feature(Feature_IsoBrokerSessionApis)]
    runtimeclass IsoSessionOps
    {
        // -- Construction --
        IsoSessionOps();

        // -- Methods --
        Windows.Foundation.IAsyncOperation<IsoSessionUserResult> AddUserAsync(
            String registrationId,
            String provisionId);

        IsoSessionUserResult GetUser(String agentName);

        IsoSessionResult RegisterApp(String registrationId);

        Windows.Foundation.IAsyncOperation<IsoSessionResult> RemoveUserAsync(String agentName);

        Windows.Foundation.IAsyncOperation<IsoSessionProcessResult> RunProcessAsync(
            String agentName,
            String processPath,
            String arguments);

        Windows.Foundation.IAsyncOperation<IsoSessionProcessResult> RunProcessWithOptionsAsync(
            String agentName,
            String processPath,
            String arguments,
            IsoSessionProcessOptions options);

        Windows.Foundation.IAsyncOperation<IsoSessionResult> StartSessionAsync(
            String agentName,
            IsoSessionConfigId configId);

        Windows.Foundation.IAsyncOperation<IsoSessionResult> StopSessionAsync(String agentName);

        Windows.Foundation.IAsyncOperation<IsoSessionResult> UnregisterAppAsync(String registrationId);

        Windows.Foundation.IAsyncOperation<
            Windows.Foundation.Collections.IVectorView<IsoSessionFolderSharingResult> >
        ShareFolderBatchAsync(
            String agentName,
            Windows.Foundation.Collections.IVectorView<IsoSessionFolderSharingRequest> requests);

        // Cloud (Entra) extensions — new interface so the default IID
        // is unchanged and existing consumers are not broken.
        [interface_name("IIsoSessionOps2")]
        {
            Windows.Foundation.IAsyncOperation<IsoSessionUserResult> AddUserAsync2(
                String registrationId,
                String entraAccountName,
                String wamToken);

            Windows.Foundation.IAsyncOperation<IsoSessionResult> StartSessionAsync2(
                String entraAccountName,
                IsoSessionConfigId configId,
                String wamToken);
        }

        // Query extensions — new interface to avoid breaking existing consumers of the default IID.
        [contract(Windows.Foundation.UniversalApiContract, 19)]
        [interface_name("IIsoSessionOps3")]
        {
            IsoSessionUserResult[] GetAgentUsers(
                String registrationId,
                Boolean includeInactive);

            IsoSessionUserResult[] GetAllAgentUsers(Boolean includeInactive);

            IsoSessionProcess[] GetProcesses(String agentName);
        }

        [contract(Windows.Foundation.UniversalApiContract, 19)]
        [interface_name("IIsoSessionOps5")]
        {
            Int32 BehaviorVersion { get; };
        }
    }
}
```


## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------|
| Minimum supported client | Windows 11 |
| Minimum supported server |  |
| Type library             | IsoSessionClient.dll |
| DLL                      | IsoSessionClient.dll |
