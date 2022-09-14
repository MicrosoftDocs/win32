---
title: IMsTscAxEvents OnRemoteProgramResult method
description: Called when a RemoteApp program returns a result to the client control.
ms.assetid: 5bc9570f-14fb-4b6f-a7dd-c1bce3ef19e0
ms.tgt_platform: multiple
keywords:
- OnRemoteProgramResult method Remote Desktop Services
- OnRemoteProgramResult method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnRemoteProgramResult method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnRemoteProgramResult
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnRemoteProgramResult method

Called when a RemoteApp program returns a result to the client control.

## Syntax


```C++
VOID OnRemoteProgramResult(
  [in] BSTR                bstrRemoteProgram,
  [in] RemoteProgramResult lError,
  [in] VARIANT_BOOL        vbIsExecutable
);
```



## Parameters

<dl> <dt>

*bstrRemoteProgram* \[in\]
</dt> <dd>

The name of the RemoteApp program.

</dd> <dt>

*lError* \[in\]
</dt> <dd>

The result of the attempt to launch the RemoteApp program.

<dt>

<span id="remoteAppResultOk"></span><span id="remoteappresultok"></span><span id="REMOTEAPPRESULTOK"></span>

<span id="remoteAppResultOk"></span><span id="remoteappresultok"></span><span id="REMOTEAPPRESULTOK"></span>**remoteAppResultOk** (0 (0x0))


</dt> <dd>

The RemoteApp program launched successfully.

</dd> <dt>

<span id="remoteAppResultLocked"></span><span id="remoteappresultlocked"></span><span id="REMOTEAPPRESULTLOCKED"></span>

<span id="remoteAppResultLocked"></span><span id="remoteappresultlocked"></span><span id="REMOTEAPPRESULTLOCKED"></span>**remoteAppResultLocked** (1 (0x1))


</dt> <dd>

The remote session is locked and the RemoteApp program cannot be launched. The user must enter their credentials to unlock the session, and then launch the RemoteApp program.

</dd> <dt>

<span id="remoteAppResultProtocolError"></span><span id="remoteappresultprotocolerror"></span><span id="REMOTEAPPRESULTPROTOCOLERROR"></span>

<span id="remoteAppResultProtocolError"></span><span id="remoteappresultprotocolerror"></span><span id="REMOTEAPPRESULTPROTOCOLERROR"></span>**remoteAppResultProtocolError** (2 (0x2))


</dt> <dd>

The RemoteApp program returned a protocol error.

</dd> <dt>

<span id="remoteAppResultNotInWhitelist"></span><span id="remoteappresultnotinwhitelist"></span><span id="REMOTEAPPRESULTNOTINWHITELIST"></span>

<span id="remoteAppResultNotInWhitelist"></span><span id="remoteappresultnotinwhitelist"></span><span id="REMOTEAPPRESULTNOTINWHITELIST"></span>**remoteAppResultNotInWhitelist** (3 (0x3))


</dt> <dd>

The RemoteApp program is not in the approved list of the RD Session Host server.

</dd> <dt>

<span id="remoteAppResultNetworkPathDenied"></span><span id="remoteappresultnetworkpathdenied"></span><span id="REMOTEAPPRESULTNETWORKPATHDENIED"></span>

<span id="remoteAppResultNetworkPathDenied"></span><span id="remoteappresultnetworkpathdenied"></span><span id="REMOTEAPPRESULTNETWORKPATHDENIED"></span>**remoteAppResultNetworkPathDenied** (4 (0x4))


</dt> <dd>

The network path to the RemoteApp program was denied.

</dd> <dt>

<span id="remoteAppResultFileNotFound"></span><span id="remoteappresultfilenotfound"></span><span id="REMOTEAPPRESULTFILENOTFOUND"></span>

<span id="remoteAppResultFileNotFound"></span><span id="remoteappresultfilenotfound"></span><span id="REMOTEAPPRESULTFILENOTFOUND"></span>**remoteAppResultFileNotFound** (5 (0x5))


</dt> <dd>

The RemoteApp program file was not found.

</dd> <dt>

<span id="remoteAppResultFailure"></span><span id="remoteappresultfailure"></span><span id="REMOTEAPPRESULTFAILURE"></span>

<span id="remoteAppResultFailure"></span><span id="remoteappresultfailure"></span><span id="REMOTEAPPRESULTFAILURE"></span>**remoteAppResultFailure** (6 (0x6))


</dt> <dd>

The RemoteApp program failed to launch.

</dd> <dt>

<span id="remoteAppResultHookNotLoaded"></span><span id="remoteappresulthooknotloaded"></span><span id="REMOTEAPPRESULTHOOKNOTLOADED"></span>

<span id="remoteAppResultHookNotLoaded"></span><span id="remoteappresulthooknotloaded"></span><span id="REMOTEAPPRESULTHOOKNOTLOADED"></span>**remoteAppResultHookNotLoaded** (7 (0x7))


</dt> <dd>

The RemoteApp program cannot be launched because the session is currently displaying the secure desktop.

</dd> </dl> </dd> <dt>

*vbIsExecutable* \[in\]
</dt> <dd>

Indicates whether the RemoteApp program was launched directly, by using the executable name or indirectly, by using a file association.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Implement this method in your event sink to receive notification that a RemoteApp program returned a result.

This method is called immediately after the ActiveX control attempts to launch the RemoteApp program, and the *lError* parameter indicates the result of the attempt.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





