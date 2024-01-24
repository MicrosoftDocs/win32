---
description: The SWbemPrivilege object represents a single privilege. This object cannot be created by the VBScript CreateObject call.
ms.assetid: 18ee4587-6347-4075-b5e9-c5fb02f3cbf7
ms.tgt_platform: multiple
title: SWbemPrivilege object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemPrivilege
- ISWbemPrivilege
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemPrivilege object

The **SWbemPrivilege** object represents a single privilege. This object cannot be created by the VBScript **CreateObject** call.

## Members

The **SWbemPrivilege** object has these types of members:

-   [Properties](#properties)

### Properties

The **SWbemPrivilege** object has these properties.



| Property                                                     | Access type           | Description                                                                      |
|:-------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------|
| [**Displayname**](swbemprivilege-displayname.md)<br/> | Read-only<br/>  | Display name of this privilege.<br/>                                       |
| [**Identifier**](swbemprivilege-identifier.md)<br/>   | Read/write<br/> | Integer that represents the privilege that is being set or retrieved.<br/> |
| [**IsEnabled**](swbemprivilege-isenabled.md)<br/>     | Read/write<br/> | Boolean value that indicates if this privilege is enabled.<br/>            |
| [**Name**](swbemprivilege-name.md)<br/>               | Read-only<br/>  | Name of this privilege.<br/>                                               |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemPrivilege<br/>                                                        |
| IID<br/>                      | IID\_ISWbemPrivilege<br/>                                                         |



## See also

<dl> <dt>

[Executing Privileged Operations](executing-privileged-operations.md)
</dt> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




