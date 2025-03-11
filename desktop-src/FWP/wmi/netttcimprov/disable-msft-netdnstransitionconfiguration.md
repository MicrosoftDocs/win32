---
description: Turns DNS 64 off.
ms.assetid: d5478d7f-0fb4-451e-948f-54f403fb7ff2
title: Disable method of the MSFT\_NetDnsTransitionConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetDnsTransitionConfiguration.Disable
api_type: 
- COM
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# Disable method of the MSFT\_NetDnsTransitionConfiguration class

Turns DNS 64 off.

## Syntax


```mof
uint32 Disable(
  [in]  boolean                            PassThru,
  [out] MSFT_NetDnsTransitionConfiguration OutputObject
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output the [**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md) object that results from turning DNS64 off in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives the [**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md) object that results from turning DNS64 off.

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

[**MSFT\_NetDnsTransitionConfiguration**](msft-netdnstransitionconfiguration.md)
</dt> </dl>

 

 




