---
description: IRTC::QueryStatus method - The QueryStatus method retrieves the status of the NPP.
ms.assetid: 4517eb34-087a-491c-97b5-cbe9190fa7a2
title: IRTC::QueryStatus method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRTC.QueryStatus
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IRTC::QueryStatus method

The **QueryStatus** method retrieves the status of the NPP.

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

Pointer to a returned [NETWORKSTATUS](networkstatus.md) structure that indicates the current state (capturing, paused, stopped, and so on) of the NPP. It is the application's responsibility to allocate and free the memory for the **NETWORKSTATUS** structure.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is the following error code:



| Return code                                                                                              | Description                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_INVALID\_PARAMETER**</dt> </dl> | The *pNetworkStatus* parameter is not pointing to a valid [NETWORKSTATUS](networkstatus.md) structure. Allocate memory for this structure and call **IRTC::QueryStatus** again.<br/> |



 

## Remarks

This method can be called at any time after the [CreateNPPInterface](createnppinterface.md) method is called. You can call this method to see if the NPP is connected to the network, to find out the status of the current capture, and to see if any triggers are pending. Before calling this method, however, you must allocate the memory needed for the [NETWORKSTATUS](networkstatus.md) structure and free that memory when the structure is no longer needed.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[IRTC](irtc.md)
</dt> <dt>

[CreateNPPInterface](createnppinterface.md)
</dt> <dt>

[NETWORKSTATUS](networkstatus.md)
</dt> </dl>

 

 




