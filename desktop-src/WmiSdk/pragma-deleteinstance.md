---
description: Deletes an existing instance of a class from the repository.
ms.assetid: 4389f831-a60e-4198-a55a-79189d10a38a
ms.tgt_platform: multiple
title: pragma deleteinstance
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- pragma
api_type: 
- NA
api_location: 
---

# pragma deleteinstance

The **pragma deleteinstance** command deletes an existing instance of a class from the repository.

The following describes the syntax for this command:


```mof
#pragma deleteinstance("InstanceId", [Flag])
```



*InstanceId* is a unique identifier of the instance the MOF compiler deletes from the current namespace.

*\[Flag\]* must be one of the following arguments.



| Flag   | Description                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------|
| fail   | Causes the MOF compiler to quit with an error message if the class does not already exist in the repository. |
| nofail | Causes the MOF compiler to continue even if the class does not already exist.                                |



 

## Examples

The following example shows how to use this command.


```mof
#pragma deleteinstance(
    "MSFT_RisingFallingTemplate.id='TestRisingFallingCorrId'",
    nofail)
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[Preprocessor Commands](preprocessor-commands.md)
</dt> </dl>

 

 




