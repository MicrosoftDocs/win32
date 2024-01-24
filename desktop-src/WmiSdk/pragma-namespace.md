---
description: Requests that the compiler load the MOF file into the namespace specified as namespacepath. If both the MOF compiler -n namespace switch and the \#pragma namespace&\#32;namespacepath command are used, the command takes priority over the switch.
ms.assetid: d280f67a-a798-47c0-b8de-071c290dd216
ms.tgt_platform: multiple
title: pragma namespace
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

# pragma namespace

The **pragma namespace** preprocessor command requests that the compiler load the MOF file into the namespace specified as *namespacepath*. If both the MOF compiler **-n** namespace switch and the **\#pragma namespace** *namespacepath* command are used, the command takes priority over the switch.

The following describes the syntax:


```mof
#pragma namespace ("[Namespace]")
```



*\[Namespace\]* is the specified namespace.

If you do not specify this command or the equivalent command-line switch, the MOF compiler uses the root\\default namespace by default.

## Remarks

You can require that client scripts and applications use an encrypted connection for authentication by adding the **RequiresEncryption** qualifier to the .mof file that creates the namespace. You can also modify an existing namespace by adding this attribute and compile the MOF file again. For more information about how to use **RequiresEncryption**, see [Requiring an Encrypted Connection to a Namespace](requiring-an-encrypted-connection-to-a-namespace.md).

## Examples

The following example shows how place classes or instances in the "Root\\Test" namespace.


```mof
#pragma namespace ("\\\\.\\Root\\Test")
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dt>

[**Standard WMI Qualifiers**](standard-wmi-qualifiers.md)
</dt> <dt>

[Preprocessor Commands](preprocessor-commands.md)
</dt> </dl>

 

 




