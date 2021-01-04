---
title: IMsTscAxEvents OnFatalError method
description: Called when the client control encounters a fatal error.
ms.assetid: 13a5eb2e-d847-4561-b30b-3f23a0579b4d
ms.tgt_platform: multiple
keywords:
- OnFatalError method Remote Desktop Services
- OnFatalError method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnFatalError method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnFatalError
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnFatalError method

Called when the client control encounters a fatal error.

## Syntax


```C++
void OnFatalError(
  [in] long errorCode
);
```



## Parameters

<dl> <dt>

*errorCode* \[in\]
</dt> <dd>

Indicates the error code.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

An unknown error has occurred.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Internal error code 1.

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

An out-of-memory error has occurred.

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3**


</dt> <dd>

A window-creation error has occurred.

</dd> <dt>

<span id="4"></span>

<span id="4"></span>**4**


</dt> <dd>

Internal error code 2.

</dd> <dt>

<span id="5"></span>

<span id="5"></span>**5**


</dt> <dd>

Internal error code 3. This is not a valid state.

</dd> <dt>

<span id="6"></span>

<span id="6"></span>**6**


</dt> <dd>

Internal error code 4.

</dd> <dt>

<span id="7"></span>

<span id="7"></span>**7**


</dt> <dd>

An unrecoverable error has occurred during client connection.

</dd> <dt>

<span id="100"></span>

<span id="100"></span>**100**


</dt> <dd>

Winsock initialization error.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Remarks

In response to this event, the container displays an error message and shuts down.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





