---
Description: The DeleteAll method of the SWbemPrivilegeSet object removes all privileges from the collection, thus emptying it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 368caa14-1c53-4090-8569-97ea743905de
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: SWbemPrivilegeSet.DeleteAll method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SWbemPrivilegeSet.DeleteAll method

The **DeleteAll** method of the [**SWbemPrivilegeSet**](swbemprivilegeset.md) object removes all privileges from the collection, thus emptying it.

## Syntax


```VB
SWbemPrivilegeSet.DeleteAll()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Error codes

Upon the completion of the **DeleteAll** method, the **Err** object may contain the error code below.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
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

[**SWbemPrivilegeSet.Remove**](swbemprivilegeset-remove.md)
</dt> </dl>

 

 




