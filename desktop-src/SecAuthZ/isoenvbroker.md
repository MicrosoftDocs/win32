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
- IsoSessionApp.dll
api_type:
- COM
ms.topic: reference
ms.date: 6/1/2026
---

# IsolationSession interface

The Isolation Environment Broker is a Windows service that performs tasks related to managing background user sessions.

> [!IMPORTANT]
> This service is experimental. The interface below is subject to change in future OS releases.

## Windows.AI.IsolationSession.idl

```idl
namespace Windows.AI.IsolationSession
{
    runtimeclass IsoSessionError
    {
        IsoSessionError();

        HRESULT Code { get; };
        Boolean IsError { get; };
        String Message { get; };
        String Remediation { get; };

        String Format();
    }

    enum IsoSessionConfigId
    {
        Small = 1,
        Medium = 2,
        Large = 3,
        Composable = 4,
    };

    runtimeclass IsoSessionUserResult
    {
        String AgentName { get; };
        String AgentUserName { get; };
        String AgentUserSid { get; };
        IsoSessionError Error { get; };

        [interface_name("IIsoSessionUserResult2")]
        {
            String RegistrationId { get; };
        }
    }

    runtimeclass IsoSessionProcessOptions
    {
        IsoSessionProcessOptions();

        Windows.Foundation.Collections.IMap<String, String> Environment { get; };
        Boolean InteractiveConsole;
        Boolean RedirectStandardError;
        Boolean RedirectStandardInput;
        Boolean RedirectStandardOutput;
        UInt32 TimeoutMilliseconds;
        String WorkingDirectory;
    }

    runtimeclass IsoSessionProcess : Windows.Foundation.IClosable
    {
        Int32 ExitCode { get; };
        UInt64 ErrorHandle { get; };
        UInt64 InputHandle { get; };
        UInt64 OutputHandle { get; };
        UInt32 ProcessId { get; };
        String ProcessPath { get; };

        void CloseStandardInput();
        void ResizeConsole(UInt16 columns, UInt16 rows);
        void SendCtrlClose();
        void Terminate();
        Int32 WaitForExit(UInt32 timeoutMs);
    }

    enum IsoSessionFolderSharingAccessLevel
    {
        Read = 0,
        ReadWrite = 1,
        Remove = 2,
    };

    enum IsoSessionFolderSharingStatus
    {
        Succeeded = 0,
        Failed = 1,
    };

    struct IsoSessionFolderSharingRequest
    {
        String FolderPath;
        IsoSessionFolderSharingAccessLevel AccessLevel;
    };

    runtimeclass IsoSessionFolderSharingResult
    {
        String FolderPath { get; };
        IsoSessionFolderSharingStatus Status { get; };
        IsoSessionError Error { get; };
    }

    runtimeclass IsoSessionResult
    {
        IsoSessionError Error { get; };
    }

    runtimeclass IsoSessionProcessResult
    {
        IsoSessionError Error { get; };
        IsoSessionProcess Process { get; };
    }

    runtimeclass IsoSessionAppConfig
    {
        IsoSessionAppConfig();

        IsoSessionConfigId ConfigId;
        String RegistrationId;

        [interface_name("IIsoSessionAppConfig2")]
        {
            String ProvisionId;
            String WamToken;
        }
    }

    runtimeclass IsoSessionAppConnectResult
    {
        String AgentName { get; };
        String AgentUserName { get; };
        IsoSessionError Error { get; };
    }

    runtimeclass IsoSessionApp : Windows.Foundation.IClosable
    {
        IsoSessionApp();

        String AgentName { get; };
        String AgentUserName { get; };
        Boolean IsConnected { get; };

        Windows.Foundation.IAsyncOperation<IsoSessionAppConnectResult> ConnectAsync(IsoSessionAppConfig config);

        Windows.Foundation.IAsyncOperation<IsoSessionProcessResult> LaunchProcessAsync(String processPath, String arguments);

        Windows.Foundation.IAsyncOperation<IsoSessionProcessResult> LaunchProcessWithOptionsAsync(
            String processPath,
            String arguments,
            IsoSessionProcessOptions options);

        Windows.Foundation.IAsyncAction TeardownAsync();
    }

    runtimeclass IsoSessionOps
    {
        IsoSessionOps();

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

        [interface_name("IIsoSessionOps3")]
        {
            IsoSessionUserResult[] GetAgentUsers(
                String registrationId,
                Boolean includeInactive);

            IsoSessionUserResult[] GetAllAgentUsers(Boolean includeInactive);

            IsoSessionProcess[] GetProcesses(String agentName);
        }
    }
}
```

## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------|
| Minimum supported client | **Windows 11 (Insiders Channel)** |
| Minimum supported server |  |
| Type library             | IsoSessionApp.dll |
| DLL                      | IsoSessionApp.dll |
