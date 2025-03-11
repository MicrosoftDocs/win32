---
description: Enable IPsec Task Offload v2 on the network adapter.
ms.assetid: 211f8485-6580-42d9-8022-ae3941a3824c
title: Enable method of the MSFT\_NetAdapterIPsecOffloadV2SettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterIPsecOffloadV2SettingData.Enable
api_type: 
- COM
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# Enable method of the MSFT\_NetAdapterIPsecOffloadV2SettingData class

Enable IPsec Task Offload v2 on the network adapter.

## Syntax


```mof
uint32 Enable(
  [in]  boolean NoRestart,
  [in]  boolean PassThru,
  [out] string  cmdletOutput
);
```



## Parameters

<dl> <dt>

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

 

 




