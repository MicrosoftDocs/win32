---
title: PxeProviderRecvRequest callback function
description: Called when a request is received from a client.
ms.assetid: 704972d5-177a-490e-881f-d2b3025babda
keywords:
- PxeProviderRecvRequest callback function Windows Deployment Services
topic_type:
- apiref
api_name:
- PxeProviderRecvRequest
api_type:
- UserDefined
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PxeProviderRecvRequest callback function

Called when a request is received from a client. This function is registered by calling the [**PxeRegisterCallback**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeregistercallback) function with the *CallbackType* parameter set to **PXE\_CALLBACK\_RECV\_REQUEST**.

## Syntax


```C++
DWORD PXEAPI PxeProviderRecvRequest(
  _In_  HANDLE          hClientRequest,
  _In_  PVOID           pPacket,
  _In_  ULONG           uPacketLen,
  _In_  PXE_ADDRESS     *pLocalAddress,
  _In_  PXE_ADDRESS     *pRemoteAddress,
  _Out_ PXE_BOOT_ACTION pAction,
  _In_  PVOID           pContext
);
```



## Parameters

<dl> <dt>

*hClientRequest* \[in\]
</dt> <dd>

Handle to a request received from a client.

</dd> <dt>

*pPacket* \[in\]
</dt> <dd>

Pointer to the memory buffer that contains the received packet.

</dd> <dt>

*uPacketLen* \[in\]
</dt> <dd>

Length, in bytes, of the buffer pointed to by the *pPacket* parameter.

</dd> <dt>

*pLocalAddress* \[in\]
</dt> <dd>

Pointer to a [**PXE\_ADDRESS**](/windows/win32/api/wdspxe/ns-wdspxe-pxe_address) structure that contains the local address on which the packet was received.

</dd> <dt>

*pRemoteAddress* \[in\]
</dt> <dd>

Pointer to a [**PXE\_ADDRESS**](/windows/win32/api/wdspxe/ns-wdspxe-pxe_address) structure that contains the source address of the packet.

</dd> <dt>

*pAction* \[out\]
</dt> <dd>

Specifies the action that the system should take.



| Value                                                                                                                                                                                                                       | Meaning                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PXE_BA_NBP"></span><span id="pxe_ba_nbp"></span><dl> <dt>**PXE\_BA\_NBP**</dt> <dt>1</dt> </dl>                | The provider replied to a client with a standard DHCP response packet that contains a path to the Network Boot Program. Returning this action means that the provider successfully completed the client request by calling the [**PxeSendReply**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxesendreply) function at least once.<br/>                        |
| <span id="PXE_BA_CUSTOM"></span><span id="pxe_ba_custom"></span><dl> <dt>**PXE\_BA\_CUSTOM**</dt> <dt>2</dt> </dl>       | The provider replied to a client by using a custom response that does not conform to DHCP specifications. Returning this action means that the provider successfully completed the client request by calling the [**PxeSendReply**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxesendreply) function at least once.<br/>                                      |
| <span id="PXE_BA_IGNORE"></span><span id="pxe_ba_ignore"></span><dl> <dt>**PXE\_BA\_IGNORE**</dt> <dt>3</dt> </dl>       | The provider does not want to service the client request and the request should not be passed to the next provider. All resources associated with the client request are released and the client request is ignored. Providers can also use this value if they recognize the client but the request was malformed.<br/> |
| <span id="PXE_BA_REJECTED"></span><span id="pxe_ba_rejected"></span><dl> <dt>**PXE\_BA\_REJECTED**</dt> <dt>4</dt> </dl> | The provider does not want to service the client request. The system passes the request to the next provider in the list of registered providers. If this was the last provider in the list, then all resources associated with the client request are released and client request is ignored.<br/>                     |



 

</dd> <dt>

*pContext* \[in\]
</dt> <dd>

Context value passed to the [**PxeRegisterCallback**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeregistercallback) function.

</dd> </dl>

## Return value

If the provider successfully processed the client request, the callback should return **ERROR\_SUCCESS** and the **PXE\_BOOT\_ACTION** pointed to by the *pAction* parameter contains the appropriate boot action for this request. If the provider will process the client request asynchronously, the callback should return **ERROR\_IO\_PENDING** and call the [**PxeAsyncRecvDone**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeasyncrecvdone) function when the client request has been processed. In case of failure, an appropriate error code should be returned and the system will proceed as if the **PXE\_BA\_REJECTED** boot action was specified.

## Remarks

The type of packets seen by a provider can be changed with the [**PxeProviderSetAttribute**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeprovidersetattribute) function.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2008, Windows Server 2003 with SP2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Windows Deployment Services Server Functions](windows-deployment-services-server-functions.md)
</dt> <dt>

[**PxeRegisterCallback**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeregistercallback)
</dt> <dt>

[**PxeSendReply**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxesendreply)
</dt> <dt>

[**PxeProviderSetAttribute**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeprovidersetattribute)
</dt> </dl>

 

 





