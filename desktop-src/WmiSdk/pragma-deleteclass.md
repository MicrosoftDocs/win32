---
description: Deletes an existing class and its instances from the repository.
ms.assetid: 6f96d14a-16ab-4e83-a75f-5dbf162d1692
ms.tgt_platform: multiple
title: pragma deleteclass
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

# pragma deleteclass

The **pragma deleteclass** preprocessor command deletes an existing class and its instances from the repository.

The following describes the syntax:


```mof
#pragma deleteclass("ClassName", [Flag])
```



*ClassName* is the name of the class that the MOF compiler deletes from the current namespace.

*\[Flag\]* must be one of the following arguments.



| Flag   | Description                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------|
| fail   | Causes the MOF compiler to quit with an error message if the class does not already exist in the repository. |
| nofail | Causes the MOF compiler to continue even if the class does not already exist.                                |



 

## Examples

The following example shows how to use this command.


```mof
#pragma deleteclass("MyClass1",FAIL)
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

 

 




