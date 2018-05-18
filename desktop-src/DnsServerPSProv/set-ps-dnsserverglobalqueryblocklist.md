---
title: Set method of the PS\_DnsServerGlobalQueryBlockList class
description: Overwrites the list of names the server does not resolve.
audience: developer
ms.assetid: '226febcc-39cc-4c53-adde-71ea38024ab9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DnsServerGlobalQueryBlockList class", "PS_DnsServerGlobalQueryBlockList class, Set method"]
topic_type:
- apiref
api_name:
- PS_DnsServerGlobalQueryBlockList.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_DnsServerGlobalQueryBlockList class

Overwrites the list of names the server does not resolve.

## Syntax


```mof
uint32 Set(
  [in]  boolean                       Enable,
  [in]  string                        List[],
  [in]  string                        ComputerName,
  [in]  boolean                       PassThru,
  [out] DnsServerGlobalQueryBlockList cmdletOutput
);
```



## Parameters

<dl> <dt>

*Enable* \[in\]
</dt> <dd>

Enables or disables support for the global query block list that blocks name resolution for names in the list. The DNS Server service creates and enables the global query block list by default when the service starts the first time. 0: Disables support for the global query block list. When you set the value of this command to 0, the DNS Server service responds to queries for names in the block list. 1: Enables support for the global query block list. When you set the value of this command to 1, the DNS Server service does not respond to queries for names in the block list.

</dd> <dt>

*List* \[in\]
</dt> <dd>

Replaces the current global query block list with a list of the names that you specify. If you do not specify any names, this command clears the block list. By default, the global query block list contains the following items: isatap; wpad: The DNS Server service can remove either or both of these names when it starts the first time, if it finds these names in an existing zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerGlobalQueryBlockList**](ps-dnsserverglobalqueryblocklist.md)
</dt> </dl>

 

 





