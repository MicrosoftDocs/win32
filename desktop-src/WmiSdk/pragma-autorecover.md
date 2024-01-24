---
description: Adds a MOF file to the list of files compiled during repository recovery.
ms.assetid: 8901c04e-f8c1-45b0-b69d-e2ebc948f088
ms.tgt_platform: multiple
title: pragma autorecover
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

# pragma autorecover

The **pragma autorecover** preprocessor command adds a MOF file to the list of files compiled during repository recovery. The list of **autorecover** MOF files is stored in this registry key:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**CIMOM**\\**autorecover mofs**

WMI checks the integrity of the WMI repository when the operating system starts WMI. If the repository is damaged, WMI automatically rebuilds the repository and recompiles any MOF files listed in this key in the registry.

The following describes the syntax for the pragma autorecover command:


```mof
#pragma autorecover
```



However, you must observe the following restrictions when using this command:

-   WMI cannot recover MOF files located on a remote computer.

    Therefore, the MOF files listed in this registry key must reside on the local computer.

-   You cannot specify the command-line switches that the MOF compiler uses when WMI recovers a MOF file.

    Therefore, you should include [pragma](-pragma.md) commands in your MOF file that make command-line switches unnecessary. The following example describes a common command-line switch that WMI does not use when recovering a MOF file from this registry key: **mofcomp -N:Root\\Test mymof.mof**

    However, you can specify the namespace using a [pragma](-pragma.md) command in the MOF file.

    ```mof
    #pragma namespace ("\\\\.\\Root\\test")
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

 

 




