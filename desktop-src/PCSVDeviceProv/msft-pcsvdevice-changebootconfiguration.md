---
Description: 'A wrapper method to set either the one time boot source or persistent boot source order.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'F222CA22-78AB-4E07-AB04-F67C4E8A45C5'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'ChangeBootConfiguration method of the MSFT\_PCSVDevice class'
---

# ChangeBootConfiguration method of the MSFT\_PCSVDevice class

A wrapper method to set either the one time boot source or persistent boot source order.

## Syntax


```mof
uint32 ChangeBootConfiguration(
  [in]      string              OneTimeBootSource,
  [in]      string              PersistentBootSource[],
  [in, out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*OneTimeBootSource* \[in\]
</dt> <dd>

The boot source for next boot.

</dd> <dt>

*PersistentBootSource* \[in\]
</dt> <dd>

An ordered array of strings representing the order of boot sources.

</dd> <dt>

*Job* \[in, out\]
</dt> <dd>

A reference to the job that may be created by this method. **NULL** if the job completed before this method returns.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Reserved** (3–4095)
</dt> <dt>

**Job Started** (4096)
</dt> <dt>

**DMTF Reserved** (4097–32767)
</dt> <dt>

**Vendor Reserved** (32768–65535)
</dt> </dl>

## Remarks

> \[!Warning\]  
> This method will only change one setting at a time. This method will fail if you set both the *OneTimeBootSource* and *PersistentBootSource* parameters.

 

Internally, this method simply calls either the [**SetOneTimeBootSource**](setonetimebootsource-msft-pcsvdevice.md) or [**ModifyPersistentBootConfigOrder**](modifypersistentbootconfigorder-msft-pcsvdevice.md) method. If you are using this class programmatically you should call the other methods directly.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>PCSVDevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVDevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_PCSVDevice**](msft-pcsvdevice.md)
</dt> </dl>

 

 




