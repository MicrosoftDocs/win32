---
title: RtmDeregisterClient function (Rtm.h)
description: The RtmDeregisterClient function deregisters the client, and frees resources associated with the client.
ms.assetid: 5d04f276-86a7-4e63-8266-e93f0d6e5241
keywords:
- RtmDeregisterClient function RAS
topic_type:
- apiref
api_name:
- RtmDeregisterClient
api_location:
- Rtm.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RtmDeregisterClient function

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **RtmDeregisterClient** function deregisters the client, and frees resources associated with the client.

## Syntax


```C++
DWORD RtmDeregisterClient(
  _In_ HANDLE ClientHandle
);
```



## Parameters

<dl> <dt>

*ClientHandle* \[in\]
</dt> <dd>

Handle that identifies the client to deregister. Obtain this handle by calling [**RtmRegisterClient**](rtmregisterclient.md).

</dd> </dl>

## Return value

If the function succeeds, the return value is NO\_ERROR.

If the function fails, the return value is one of the following error codes.



| Value                                                                                                       | Description                                                    |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_HANDLE**</dt> </dl>       | The *ClientHandle* parameter is not a valid handle.<br/> |
| <dl> <dt>**ERROR\_NO\_SYSTEM\_RESOURCES**</dt> </dl> | Insufficient resources to carry out the operation.<br/>  |



 

## Remarks

This function removes all routes that were added by the client.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| End of server support<br/>    | Windows Server 2003<br/>                                                     |
| Header<br/>                   | <dl> <dt>Rtm.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Rtm.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Rtm.dll</dt> </dl> |



## See also

<dl> <dt>

[Routing Table Manager Version 1 Reference](routing-table-manager-version-1-reference.md)
</dt> <dt>

[Routing Table Manager Version 1 Functions](routing-table-manager-version-1-functions.md)
</dt> <dt>

[**RtmRegisterClient**](rtmregisterclient.md)
</dt> </dl>

 

 





