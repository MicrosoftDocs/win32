---
description: You can use the AddAsString method of the SWbemPrivilegeSet object to add a privilege to an SWbemPrivilegeSet collection using a privilege string.
ms.assetid: 729ed4e3-2c5c-4bb4-acc6-cf9ad0d5eaf1
ms.tgt_platform: multiple
title: SWbemPrivilegeSet.AddAsString method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemPrivilegeSet.AddAsString
- ISWbemPrivilegeSet.AddAsString
- ISWbemPrivilegeSet.AddAsString
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemPrivilegeSet.AddAsString method

You can use the **AddAsString** method of the [**SWbemPrivilegeSet**](swbemprivilegeset.md) object to add a privilege to an **SWbemPrivilegeSet** collection using a privilege string. Use this method to add a privilege or to enable a privilege for [**SWbemSecurity**](swbemsecurity.md) objects. See [Executing Privileged Operations Using VBScript](executing-privileged-operations-using-vbscript.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objPrivilege = .AddAsString( _
  ByVal strPrivilege, _
  [ ByVal bIsEnabled ] _
)
```



## Parameters

<dl> <dt>

*strPrivilege* 
</dt> <dd>

Required. One of the privilege strings. For a complete list of these strings and the associated WMI constants, see [**Privilege Constants**](privilege-constants.md). Every privilege string represents a specific privilege. For example, to add the privilege that use to shut down a computer system, use the **SeShutdownPrivilege** string.

</dd> <dt>

*bIsEnabled* \[optional\]
</dt> <dd>

Boolean value that enables or disables this privilege. The default value is **True**.

</dd> </dl>

## Return value

If successful, this method returns an [**SWbemPrivilege**](swbemprivilege.md) object that represents the new privilege. Otherwise, a null object is returned.

## Error codes

Upon the completion of the **AddAsString** method, the **Err** object may contain the error code in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> </dl>

## Examples

The following VBScript code example creates a new port for a print server using [**Win32\_TCPIPPrinterPort**](/windows/desktop/CIMWin32Prov/win32-tcpipprinterport). The **SeLoadDriverPrivilege** is required for this operation. See [Executing Privileged Operations](executing-privileged-operations.md).


```VB
Set objWMIService = GetObject("Winmgmts:")
objWMIService.Security_.Privileges. _
    AddAsString "SeLoadDriverPrivilege", True
Set objNewPort = objWMIService.Get _
    ("Win32_TCPIPPrinterPort").SpawnInstance_
objNewPort.Name = "IP_111.222.111.11"
objNewPort.Protocol = 1
objNewPort.HostAddress = "111.222.111.11"
objNewPort.PortNumber = "9999"
objNewPort.SNMPEnabled = False
objNewPort.Put_
```



A code example using this method is also described in the [**SWbemPrivilegeSet**](swbemprivilegeset.md) topic.

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

[**SWbemPrivilegeSet.Add**](swbemprivilegeset-add.md)
</dt> <dt>

[**SWbemPrivilegeSet.Remove**](swbemprivilegeset-remove.md)
</dt> <dt>

[**WbemPrivilegeEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemprivilegeenum)
</dt> <dt>

[**Privilege Constants**](privilege-constants.md)
</dt> <dt>

[Executing Privileged Operations](executing-privileged-operations.md)
</dt> <dt>

[Executing Privileged Operations Using VBScript](executing-privileged-operations-using-vbscript.md)
</dt> </dl>

 

