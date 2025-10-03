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
related to managing background user sessions.

This service is still experimental. The interface below will change on future
OS releases.


## Windows.AI.IsolationEnvironment.idl

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
    [interface_name("IIsolationEnvironmentCreationResult_Exp", ed8425e5-5d71-5f72-8b49-1689f1e0a744)]
    runtimeclass IsolationEnvironmentCreationResult_Exp
    {
        IsolationEnvironment_Exp Environment { get; };
        IsolationEnvironmentCreationStatus_Exp Status { get; };
        HRESULT ExtendedError { get; };
    }

    [contract(IsolationEnvironmentContract, 0.1)]
    [interface_name("IIsolationWorkerProcess_Exp", 44a1b74d-7fbb-5f27-aaee-e470474e325f)]
    runtimeclass IsolationWorkerProcess_Exp : Windows.Foundation.IClosable
    {
        String ProcessPath { get; };
        UInt32 ProcessId { get; };
    }

    [contract(IsolationEnvironmentContract, 0.1)]
    [interface_name("IIsolationProcessCreationResult_Exp", 31e09f76-8c5a-53d6-bac0-64226ec1a49f)]
    runtimeclass IsolationProcessCreationResult_Exp
    {
        IsolationWorkerProcess_Exp Process { get; };
        IsolationProcessCreationStatus_Exp Status { get; };
        HRESULT ExtendedError { get; };
    }

    [contract(IsolationEnvironmentContract, 0.1)]
    [interface_name("IIsolationEnvironment_Exp", 1e5b19a7-2376-5263-bb90-cb067dd21747)]
    [static_name("IIsolationEnvironment_ExpStatics", d5bfbc81-5d2b-5b49-919d-1df3344c6dbe)]
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
