---
title: CBCreateClientInstance function (Cbclient.h)
description: Creates an instance of the Remote Desktop Connection Broker RPC client.
ms.assetid: 700E47BC-C547-44AB-8607-B9797D542AA7
ms.tgt_platform: multiple
keywords:
- CBCreateClientInstance function Remote Desktop Services
topic_type:
- apiref
api_name:
- CBCreateClientInstance
api_location:
- Cbclient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# CBCreateClientInstance function

Creates an instance of the Remote Desktop Connection Broker RPC client.

## Syntax


```C++
HRESULT CBCreateClientInstance(
  _In_  DWORD                   Version,
  _Out_ IConnectionBrokerClient **ppCbClient
);
```



## Parameters

<dl> <dt>

*Version* \[in\]
</dt> <dd>

Specifies the version of the Remote Desktop Connection Broker client interface being requested. This must be the following value.

<dt>

1
</dt> <dd>

Version 1 of the Remote Desktop Connection Broker client.

</dd> </dl> </dd> <dt>

*ppCbClient* \[out\]
</dt> <dd>

The address of an [**IConnectionBrokerClient**](iconnectionbrokerclient.md) interface pointer that receives the Remote Desktop Connection Broker client object.

</dd> </dl>

## Return value

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cbclient.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Cbclient.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Cbclient.dll</dt> </dl> |



 

 





