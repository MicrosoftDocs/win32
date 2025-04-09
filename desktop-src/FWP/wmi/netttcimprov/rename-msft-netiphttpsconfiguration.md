---
description: Renames the IP-HTTPs profile.
ms.assetid: 2486f26a-a336-4c22-97bd-96f7ff86852a
title: Rename method of the MSFT\_NetIPHttpsConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIPHttpsConfiguration.Rename
api_type: 
- COM
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# Rename method of the MSFT\_NetIPHttpsConfiguration class

Renames the IP-HTTPs profile.

## Syntax


```mof
uint32 Rename(
  [in]  string                       NewName,
  [in]  boolean                      PassThru,
  [out] MSFT_NetIPHttpsConfiguration OutputObject
);
```



## Parameters

<dl> <dt>

*NewName* \[in\]
</dt> <dd>

Specifies the new name for the profile.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output the an object that represents the renamed profile in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives the [**MSFT\_NetIPHttpsConfiguration**](msft-netiphttpsconfiguration.md) object for the renamed profile.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetIPHttpsConfiguration**](msft-netiphttpsconfiguration.md)
</dt> </dl>

 

 




