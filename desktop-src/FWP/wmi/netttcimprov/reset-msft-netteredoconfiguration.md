---
description: Reset the Teredo configuration.
ms.assetid: a4b52015-4a78-4b84-b2fd-3b9a22bbc1c2
title: Reset method of the MSFT\_NetTeredoConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetTeredoConfiguration.Reset
api_type: 
- COM
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# Reset method of the MSFT\_NetTeredoConfiguration class

Reset the Teredo configuration.

## Syntax


```mof
uint32 Reset(
  [in]  boolean                     Type,
  [in]  boolean                     ServerName,
  [in]  boolean RefreshInterval     In,
  [in]  boolean                     ServerVirtualIP,
  [in]  boolean                     DefaultQualified,
  [in]  boolean                     ServerShunt,
  [in]  boolean                     PassThru,
  [out] MSFT_NetTeredoConfiguration OutputObject
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

Specifies whether to reset the **Type** property of the [**MSFT\_NetTeredoConfiguration**](msft-netteredoconfiguration.md) object.

</dd> <dt>

*ServerName* \[in\]
</dt> <dd>

Specifies whether to reset the **ServerName** property of the [**MSFT\_NetTeredoConfiguration**](msft-netteredoconfiguration.md) object.

</dd> <dt>

*In* \[in\]
</dt> <dd>

Specifies whether to reset the **RefreshInterval** property of the [**MSFT\_NetTeredoConfiguration**](msft-netteredoconfiguration.md) object.

</dd> <dt>

*ServerVirtualIP* \[in\]
</dt> <dd>

Specifies whether to reset the **ServerVirtualIP** property of the [**MSFT\_NetTeredoConfiguration**](msft-netteredoconfiguration.md) object.

</dd> <dt>

*DefaultQualified* \[in\]
</dt> <dd>

Specifies whether to reset the **DefaultQualified** property of the [**MSFT\_NetTeredoConfiguration**](msft-netteredoconfiguration.md) object.

</dd> <dt>

*ServerShunt* \[in\]
</dt> <dd>

Specifies whether to reset the **ServerShunt** property of the [**MSFT\_NetTeredoConfiguration**](msft-netteredoconfiguration.md) object.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output the an object that represents the reset Teredo configuration in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives the reset [**MSFT\_NetTeredoConfiguration**](msft-netteredoconfiguration.md) object.

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

[**MSFT\_NetTeredoConfiguration**](msft-netteredoconfiguration.md)
</dt> </dl>

 

 




