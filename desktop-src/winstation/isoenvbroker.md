---
title: IsoEnvBroker interface
description: Isolation Environment Broker Service.
ms.assetid: a2c7fa29-47c7-443b-8357-d6782083fa94
ms.tgt_platform: multiple
keywords:
- IsoEnvBroker
topic_type:
- apiref
api_name:
- IsoEnvBroker
api_location:
- IsoEnvBroker.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/31/2025
---

# IsoEnvBroker interface

The Isolation Environment Broker is a windows service that performs tasks
related to managing background (or Agent) user sessions.

This service is still experimental. The interface described below is present
only in insider OS builds (not retail) and will change in future releases prior
to shipping on retail versions of the OS.


## Windows.AI.IsolationEnvironment.idl


TODO: need guids!
[interface_name("IBlah", uuid)]


```idl
namespace Windows.AI.IsolationEnvironment.Preview
{
    [contractversion(0.1)]
    apicontract IsolationEnvironmentContract{};

    [contract(IsolationEnvironmentContract, 0.1)]
    enum IsolationProcessCreationStatus_Exp
    {
        Succeeded,
        InvalidPath,
        PermissionDenied,
        AlreadyRunning,
        Failed
    };

    [contract(IsolationEnvironmentContract, 0.1)]
    enum IsolationEnvironmentCreationStatus_Exp
    {
        Succeeded,
        UserLimitReached,
        PermissionDenied,
        Failed
    };

    [contract(IsolationEnvironmentContract, 0.1)]
    enum IsIsolationSupportedResult_Exp
    {
        NotSupported,
        Supported,
        UserSettingDisabled
    };

    [contract(IsolationEnvironmentContract, 0.1)]
    runtimeclass IsolationEnvironmentCreationResult_Exp
    {
        IsolationEnvironment_Exp Environment { get; };
        IsolationEnvironmentCreationStatus_Exp Status { get; };
        HRESULT ExtendedError { get; };
    }

    [contract(IsolationEnvironmentContract, 0.1)]
    runtimeclass IsolationWorkerProcess_Exp : Windows.Foundation.IClosable
    {
        String ProcessPath { get; };
        UInt32 ProcessId { get; };
    }

    [contract(IsolationEnvironmentContract, 0.1)]
    runtimeclass IsolationProcessCreationResult_Exp
    {
        IsolationWorkerProcess_Exp Process { get; };
        IsolationProcessCreationStatus_Exp Status { get; };
        HRESULT ExtendedError { get; };
    }

    [contract(IsolationEnvironmentContract, 0.1)]
    runtimeclass IsolationEnvironment_Exp : Windows.Foundation.IClosable
    {
        static IsolationEnvironmentCreationResult_Exp Create();
        static IsIsolationSupportedResult_Exp IsSupported();

        String UserName { get; };
        String Password { get; };

        IsolationProcessCreationResult_Exp LaunchIsolatedProcess(String processPath, String arguments);
    }
}
```


## Requirements


| Requirement | Value |
|-------------------------------------|----------------------------------------|
| Minimum supported client<br/> | Windows 11<br/>                                                                 |
| Minimum supported server<br/> | <br/>                                                      |
| Type library<br/>             | <dl> <dt>IsoEnvBroker.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IsoEnvBroker.dll</dt> </dl> |
