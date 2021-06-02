---
title: Session object (WSManDisp.h)
description: Defines operations and session settings.
ms.assetid: b98ca759-71cb-492e-8645-8766b202eb36
ms.tgt_platform: multiple
keywords:
- Session object Windows Remote Management
- Session object Windows Remote Management , described
topic_type:
- apiref
api_name:
- Session
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Session object (WSManDisp.h)

Defines operations and session settings. Any Windows Remote Management operations require creation of a **Session** that connects to a remote computer, [*base management controller*](windows-remote-management-glossary.md) (BMC), or the local computer. WinRM network operations include getting, writing, or enumerating data, or invoking methods. The methods of the **Session** object mirror the basic operations defined in the WS-Management protocol.

## Members

The **Session** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Session** object has these methods.



| Method                                 | Description                                                                                                                 |
|:---------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**Create**](session-create.md)       | Creates a new instance of a resource and returns the URI of the new object.<br/>                                      |
| [**Delete**](session-delete.md)       | Deletes the resource specified in the resource URI.<br/>                                                              |
| [**Enumerate**](session-enumerate.md) | Enumerates a collection, table, or message log resource.<br/>                                                         |
| [**Get**](session-get.md)             | Retrieves a resource from the service and returns an XML representation of the current instance of the resource.<br/> |
| [**Identify**](session-identify.md)   | Queries a remote computer to determine if it supports the WS-Management protocol<br/>                                 |
| [**Invoke**](session-invoke.md)       | Invokes a method that returns the results of the method call.<br/>                                                    |
| [**Put**](session-put.md)             | Updates a resource.<br/>                                                                                              |



 

### Properties

The **Session** object has these properties.



| Property                                            | Access type           | Description                                                                                                                                                                                                                 |
|:----------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BatchItems**](session-batchitems.md)<br/> | Read/write<br/> | Sets and gets the number of items in each enumeration batch. This value cannot be changed during an enumeration. By default, the default is an unlimited number of items. The resource provider may set a limit.<br/> |
| [**Error**](session-error.md)<br/>           | Read-only<br/>  | Gets additional error information in an XML stream.<br/>                                                                                                                                                              |
| [**Timeout**](session-timeout.md)<br/>       | Read/write<br/> | Sets and gets the maximum amount of time (in milliseconds) for the client application to wait.<br/>                                                                                                                   |



 

## Remarks

The **Session** object corresponds to the [**IWSManSession**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmansession) interface.

## Examples

The following VBScript code example shows how to create a **Session** object.


```VB
' Create a WSMan object.
Dim objWsman 
Set objWsman = CreateObject( "WSMAN.Automation" )

' Create Session object.
Dim objSession
Set objSession = objWsman.CreateSession
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[WinRM Scripting API](winrm-scripting-api.md)
</dt> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[Using Windows Remote Management](using-windows-remote-management.md)
</dt> <dt>

[Scripting in Windows Remote Management](scripting-in-windows-remote-management.md)
</dt> <dt>

[Obtaining Data from the Local Computer](obtaining-data-from-the-local-computer.md)
</dt> <dt>

[Obtaining Data from a Remote Computer](obtaining-data-from-a-remote-computer.md)
</dt> </dl>

 

 





