---
title: INapSystemHealthAgentCallback CompareSoHRequests method (NapSystemHealthAgent.h)
description: Is used by the SHA to compare SoH requests.
ms.assetid: 14ba189a-e745-44b0-b729-522087d4e08b
keywords:
- CompareSoHRequests method NAP
- CompareSoHRequests method NAP , INapSystemHealthAgentCallback interface
- INapSystemHealthAgentCallback interface NAP , CompareSoHRequests method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentCallback.CompareSoHRequests
api_location:
- NapSystemHealthAgent.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentCallback::CompareSoHRequests method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentCallback::CompareSoHRequests** method is used by the SHA to compare SoH requests.

## Syntax


```C++
HRESULT CompareSoHRequests(
  [in]  const SoHRequest *lhs,
  [in]  const SoHRequest *rhs,
  [out]       BOOL       *isEqual
);
```



## Parameters

<dl> <dt>

*lhs* \[in\]
</dt> <dd>

A pointer to the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) on the left of the comparison operation.

</dd> <dt>

*rhs* \[in\]
</dt> <dd>

A pointer to the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) on the right of the comparison operation.

</dd> <dt>

*isEqual* \[out\]
</dt> <dd>

A pointer to a **BOOL** that is **TRUE** if *lhs* and *rhs* are semantically equal, and **FALSE** otherwise.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                               | Description                                           |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Indicates success.<br/>                         |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method was not implemented by the SHA.<br/> |



 

## Remarks

This callback method is declared by the NAP system and is to be implemented by the SHA writer.

The SHA should compare the SoHs and return **TRUE** if the SoHs are semantically equal. The NapAgent uses this information to determine if an SoH exchange should be initiated due to change of state of the client machine.

If SHAs have put incremental IDs or time-stamps into their SoH, then SoHs may be semantically equal (i.e. they may convey the same health information), but they may be byte-wise unequal. SHAs should implement this function to check for semantic equality of SoHs.

If SHAs have not put any time-stamps or Ids into their SoHs, they may choose to not implement this function and return **E\_NOTIMPL**. In this case, the NapAgent performs a byte-wise comparison on the [**SoHRequests**](/windows/win32/api/naptypes/ns-naptypes-soh).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapSystemHealthAgent.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthAgent.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapSystemHealthAgentCallback**](inapsystemhealthagentcallback.md)
</dt> <dt>

[**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh)
</dt> </dl>

 

 





