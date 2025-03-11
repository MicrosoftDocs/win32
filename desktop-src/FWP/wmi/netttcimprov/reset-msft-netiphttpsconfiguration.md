---
description: Resets the configuration of IP-HTTPs.
ms.assetid: 64bd2391-72c3-4209-b2e5-588577bccfb7
title: Reset method of the MSFT\_NetIPHttpsConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIPHttpsConfiguration.Reset
api_type: 
- COM
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# Reset method of the MSFT\_NetIPHttpsConfiguration class

Resets the configuration of IP-HTTPs.

## Syntax


```mof
uint32 Reset(
  [in]  boolean                      State,
  [in]  boolean                      AuthMode,
  [in]  boolean                      StrongCRLRequired,
  [in]  boolean                      PassThru,
  [out] MSFT_NetIPHttpsConfiguration OutputObject
);
```



## Parameters

<dl> <dt>

*State* \[in\]
</dt> <dd>

Specifies whether to reset the **State** property of the [**MSFT\_NetIPHttpsConfiguration**](msft-netiphttpsconfiguration.md) object.

</dd> <dt>

*AuthMode* \[in\]
</dt> <dd>

Specifies whether to reset the **AuthMode** property of the [**MSFT\_NetIPHttpsConfiguration**](msft-netiphttpsconfiguration.md) object.

</dd> <dt>

*StrongCRLRequired* \[in\]
</dt> <dd>

Specifies whether to reset the **StrongCRLRequired** property of the [**MSFT\_NetIPHttpsConfiguration**](msft-netiphttpsconfiguration.md) object.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output the an object that represents the reset IP-HTTPs configuration in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives the reset [**MSFT\_NetIPHttpsConfiguration**](msft-netiphttpsconfiguration.md) object.

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

 

 




