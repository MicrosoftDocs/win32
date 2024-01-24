---
description: The Add method of the SWbemPrivilegeSet object adds an SWbemPrivilege object to the SWbemPrivilegeSet collection. If a privilege with the same name already exists in the collection, it is replaced.
ms.assetid: 7d44193f-60e1-4e83-8640-31d8df509d98
ms.tgt_platform: multiple
title: SWbemPrivilegeSet.Add method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemPrivilegeSet.Add
- ISWbemPrivilegeSet.Add
- ISWbemPrivilegeSet.Add
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemPrivilegeSet.Add method

The **Add** method of the [**SWbemPrivilegeSet**](swbemprivilegeset.md) object adds an [**SWbemPrivilege**](swbemprivilege.md) object to the **SWbemPrivilegeSet** collection. If a privilege with the same name already exists in the collection, it is replaced.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objPrivilege = .Add( _
  ByVal iPrivilege, _
  [ ByVal bIsEnabled ] _
)
```



## Parameters

<dl> <dt>

*iPrivilege* 
</dt> <dd>

Required. One of the WMI constants from the [**WbemPrivilegeEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemprivilegeenum) group. These constants are essentially integers that represent specific privileges. For example, to add the privilege that allows you to shut down a computer system, use the **wbemPrivilegeShutdown** constant. In a script, you must use the numeric equivalent of 23 (0x17). For a complete list of these constants and the associated privilege strings, see [**Privilege Constants**](privilege-constants.md).

</dd> <dt>

*bIsEnabled* \[optional\]
</dt> <dd>

Boolean value that enables or disables this privilege. The default value is **TRUE**.

</dd> </dl>

## Return value

If successful, the method returns an [**SWbemPrivilege**](swbemprivilege.md) object that represents the new privilege. Otherwise, a null object is returned.

## Error codes

Upon the completion of the **Add** method, the **Err** object may contain the error code in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> </dl>

## Examples

A code example using this method is described in the [**SWbemPrivilegeSet**](swbemprivilegeset.md) topic.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemPrivilegeSet<br/>                                                     |
| IID<br/>                      | IID\_ISWbemPrivilegeSet<br/>                                                      |



## See also

<dl> <dt>

[**SWbemPrivilegeSet**](swbemprivilegeset.md)
</dt> <dt>

[Executing Privileged Operations](executing-privileged-operations.md)
</dt> <dt>

[Executing Privileged Operations Using VBScript](executing-privileged-operations-using-vbscript.md)
</dt> <dt>

[**SWbemPrivilegeSet.AddAsString**](swbemprivilegeset-addasstring.md)
</dt> <dt>

[**SWbemPrivilegeSet.Remove**](swbemprivilegeset-remove.md)
</dt> <dt>

[**WbemPrivilegeEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemprivilegeenum)
</dt> <dt>

[**Privilege Constants**](privilege-constants.md)
</dt> </dl>

 

 




