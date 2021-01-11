---
description: Validate a configuration text for correctness without setting it active. Returns 1 on success, 0 on error.
ms.assetid: baeabed0-7717-498a-9886-e49e4a101711
ms.tgt_platform: multiple
title: ValidateConfiguration method of the Control class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Control.ValidateConfiguration
api_type: 
- COM
api_location: 
- BEvtCol.exe
---

# ValidateConfiguration method of the Control class

Validate a configuration text for correctness without setting it active. Returns 1 on success, 0 on error.

## Syntax


```mof
Uint32 ValidateConfiguration(
  [in]  string Config,
  [out] string ErrorString,
  [out] string WarningString,
  [out] string InfoString,
  [out] uint32 ErrorType
);
```



## Parameters

<dl> <dt>

*Config* \[in\]
</dt> <dd>

The configuration to check.

</dd> <dt>

*ErrorString* \[out\]
</dt> <dd>

When this method returns, if there was a error, this parameter contains a description of the validation error for the operation.

</dd> <dt>

*WarningString* \[out\]
</dt> <dd>

When this method returns, this parameter contains a description of any validation warnings for the operation.

The text string with warnings.

</dd> <dt>

*InfoString* \[out\]
</dt> <dd>

When this method returns, this parameter contains a set of information about the configuration.

</dd> <dt>

*ErrorType* \[out\]
</dt> <dd>

When this method returns, if there was a validation error, this parameter indicates the error type.

The possible values are:

<dt>

0
</dt> <dd>

The argument is missing.

</dd> <dt>

1
</dt> <dd>

The argument format is invalid.

</dd> <dt>

2
</dt> <dd>

A configuration argument is invalid.

</dd> </dl> </dd> </dl>

## Return value

<dl> <dt>


</dt> <dd>

0

Failure

</dd> <dt>


</dt> <dd>

1

Success

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\BootEventCollector<br/>                                              |
| MOF<br/>                      | <dl> <dt>BootEventCollectorWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>BEvtCol.exe</dt> </dl>               |



## See also

<dl> <dt>

[**Control**](control.md)
</dt> </dl>

 

 




