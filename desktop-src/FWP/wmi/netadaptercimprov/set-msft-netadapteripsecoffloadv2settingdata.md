---
description: Set the IPsec Task Offload v2 properties on the network adapter.
ms.assetid: 531c876d-bfe2-4f32-a437-74e092b2252f
title: Set method of the MSFT\_NetAdapterIPsecOffloadV2SettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterIPsecOffloadV2SettingData.Set
api_type: 
- COM
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# Set method of the MSFT\_NetAdapterIPsecOffloadV2SettingData class

Set the IPsec Task Offload v2 properties on the network adapter.

## Syntax


```mof
uint32 Set(
  [in]  boolean Enabled,
  [in]  boolean NoRestart,
  [in]  boolean PassThru,
  [out] string  cmdletOutput
);
```



## Parameters

<dl> <dt>

*Enabled* \[in\]
</dt> <dd>

**true** to enable the properties on the adapter.

</dd> <dt>

*NoRestart* \[in\]
</dt> <dd>

**true** to not restart the adapter after being disabled. By default, the adapter will restart.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return an object in the *cmdletOutput* parameter; otherwise, false. The default value is **false.**

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

if **PssThru** is **true**, returns an embedded [**MSFT\_NetAdapterIPsecOffloadV2SettingData**](msft-netadapteripsecoffloadv2settingdata.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetAdapterIPsecOffloadV2SettingData**](msft-netadapteripsecoffloadv2settingdata.md)
</dt> </dl>

 

 




