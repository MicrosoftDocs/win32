---
description: GetAccessMask method of the Win32_Share class - Returns a uint32 bitmap with the access rights to the share held by the user or group on whose behalf the instance is returned.
ms.assetid: 234f44a4-ffff-431d-a973-98f2bd313c7d
ms.tgt_platform: multiple
title: GetAccessMask method of the Win32_Share class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Share.GetAccessMask
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# GetAccessMask method of the Win32\_Share class

The **GetAccessMask** method returns a uint32 bitmap with the access rights to the share held by the user or group on whose behalf the instance is returned.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 GetAccessMask();
```



## Parameters

This method has no parameters.

## Return value

Access rights to the share held by the user or group.

<dl> <dt>

**FILE\_LIST\_DIRECTORY**
</dt> <dd>

1 (0x1)

Grants the right to read data from the file. For a directory, this value grants the right to list the contents of the directory.

</dd> <dt>

**FILE\_ADD\_FILE**
</dt> <dd>

2 (0x2)

Grants the right to write data to the file. For a directory, this value grants the right to create a file in the directory.

</dd> <dt>

**FILE\_ADD\_SUBDIRECTORY**
</dt> <dd>

4 (0x4)

Grants the right to append data to the file. For a directory, this value grants the right to create a subdirectory.

</dd> <dt>

**FILE\_READ\_EA**
</dt> <dd>

8 (0x8)

Grants the right to read extended attributes.

</dd> <dt>

**FILE\_WRITE\_EA**
</dt> <dd>

16 (0x10)

Grants the right to write extended attributes.

</dd> <dt>

**FILE\_TRAVERSE**
</dt> <dd>

32 (0x20)

Grants the right to execute a file. For a directory, the directory can be traversed.

</dd> <dt>

**FILE\_DELETE\_CHILD**
</dt> <dd>

64 (0x40)

Grants the right to delete a directory and all of the files it contains (its children), even if the files are read-only.

</dd> <dt>

**FILE\_READ\_ATTRIBUTES**
</dt> <dd>

128 (0x80)

Grants the right to read file attributes.

</dd> <dt>

**FILE\_WRITE\_ATTRIBUTES**
</dt> <dd>

256 (0x100)

Grants the right to change file attributes.

</dd> <dt>

**DELETE**
</dt> <dd>

65536 (0x10000)

Grants delete access.

</dd> <dt>

**READ\_CONTROL**
</dt> <dd>

131072 (0x20000)

Grants read access to the security descriptor and owner.

</dd> <dt>

**WRITE\_DAC**
</dt> <dd>

262144 (0x40000)

Grants write access to the discretionary access control list (DACL).

</dd> <dt>

**WRITE\_OWNER**
</dt> <dd>

524288 (0x80000)

Assigns the write owner.

</dd> <dt>

**SYNCHRONIZE**
</dt> <dd>

1048576 (0x100000)

Synchronizes access and allows a process to wait for an object to enter the signaled state.

</dd> </dl>

## Remarks

**GetAccessMask** method is an object method and is used on an occurrence of this class.

## Examples

The following VBScript code example creates a share folder and then gets the value of the access mask in the security descriptor that secures the share folder.


```VB
Const FILE_SHARE = 0
Const MAXIMUM_CONNECTIONS = 4000 
strComputer = "."

Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set objNewShare = objWMIService.Get("Win32_Share")
Return = objNewShare.Create ("C:\Temp", "TestShare", FILE_SHARE, MAXIMUM_CONNECTIONS, "test share")

If Return <> 0 Then
          WScript.Echo Return
          WScript.Quit
End If

Set objShare = objWMIService.Get("Win32_Share.Name='TestShare'")
Return = objShare.GetAccessMask
WScript.Echo Return
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Share**](win32-share.md)
</dt> </dl>

 

