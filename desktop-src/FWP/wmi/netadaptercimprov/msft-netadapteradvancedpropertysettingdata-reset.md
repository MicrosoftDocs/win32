---
description: Resets the advanced property of a network adapter to its factory default value.
ms.assetid: 7E5FE9C7-22BC-4F42-BF8E-7F57733FF385
title: Reset method of the MSFT\_NetAdapterAdvancedPropertySettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterAdvancedPropertySettingData.Reset
api_type: 
- COM
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# Reset method of the MSFT\_NetAdapterAdvancedPropertySettingData class

Resets the advanced property of a network adapter to its factory default value.

## Syntax


```mof
HRESULT Reset(
  [out] string CmdletOutput
);
```



## Parameters

<dl> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

On return, contains an embedded instance of the [**MSFT\_NetAdapterAdvancedPropertySettingData**](msft-netadapteradvancedpropertysettingdata.md) class.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetAdapterAdvancedPropertySettingData**](msft-netadapteradvancedpropertysettingdata.md)
</dt> </dl>

 

 




