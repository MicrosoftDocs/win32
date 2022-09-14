---
description: Retrieves the NPP status.
ms.assetid: 48682997-f641-4ae5-b5ad-64fd84f07ae3
title: IESP::QueryStatus method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IESP.QueryStatus
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IESP::QueryStatus method

The **QueryStatus** method retrieves the NPP status.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE QueryStatus(
  [out] NETWORKSTATUS *pNetworkStatus
);
```



## Parameters

<dl> <dt>

*pNetworkStatus* \[out\]
</dt> <dd>

A pointer to a returned [NETWORKSTATUS](networkstatus.md) structure that indicates the current state (capturing, paused, stopped, and so on) of the NPP. The user must allocate and free the memory for the NETWORKSTATUS structure.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is the following error code:



| Return code                                                                                              | Description                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_INVALID\_PARAMETER**</dt> </dl> | The *pNetworkStatus* parameter is not pointing to a valid [NETWORKSTATUS](networkstatus.md) structure. Allocate memory for this structure and call **IESP::QueryStatus** again.<br/> |



 

## Remarks

This method can be called at any time after the [CreateNPPInterface](createnppinterface.md) is called. You can call this method to see if the NPP is connected to the network, to find out the status of the current capture, and to see if any triggers are pending.

Before calling this method, allocate the memory required for the [NETWORKSTATUS](networkstatus.md) structure and free that memory when the structure is no longer required.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[IESP](iesp.md)
</dt> <dt>

[CreateNPPInterface](createnppinterface.md)
</dt> <dt>

[NETWORKSTATUS](networkstatus.md)
</dt> </dl>

 

 




