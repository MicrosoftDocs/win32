---
title: ConnectionOptions object (WSManDisp.h)
description: The ConnectionOptions object is passed to the CreateSession method to provide the user name and password associated with the local account on the remote computer.
ms.assetid: 7a87a5f7-78ed-452c-9b9f-ad48811a3339
ms.tgt_platform: multiple
keywords:
- ConnectionOptions object Windows Remote Management
- ConnectionOptions object Windows Remote Management , described
topic_type:
- apiref
api_name:
- ConnectionOptions
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ConnectionOptions object

The **ConnectionOptions** object is passed to the [**CreateSession**](wsman-createsession.md) method to provide the user name and password associated with the local account on the remote computer. If no parameters are supplied, then the credentials of the account running the script are set to the default values.

## Members

The **ConnectionOptions** object has these types of members:

-   [Properties](#properties)

### Properties

The **ConnectionOptions** object has these properties.



| Property                                                  | Access type           | Description                                                                                 |
|:----------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------|
| [**Password**](connectionoptions-password.md)<br/> | Write-only<br/> | Sets the password of a local or domain account on the remote computer.<br/>           |
| [**UserName**](connectionoptions-username.md)<br/> | Read/write<br/> | Sets and gets the user name of a local or domain account on the remote computer.<br/> |



 

## Remarks

The **ConnectionOptions** object corresponds to the [**IWSManConnectionOptions**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanconnectionoptions) interface.

If a Windows Remote Management client application is running under impersonation, then a failure occurs if you set the [**Password**](connectionoptions-password.md) property. A client application is a script or other program that sends a request to WinRM on the local or a remote computer. The client application may be running under impersonation because it called a function like [**ImpersonateClient**](/previous-versions/windows/desktop/legacy/aa375494(v=vs.85)). An Active Server Page (ASP) or service cannot request a user name and password if the ASP process runs under an account that impersonates a client.

The **WSManFlagCredUserNamePassword** flag should be set on the [**WSman.CreateSession**](wsman-createsession.md) call when using the [**UserName**](connectionoptions-username.md) and [**Password**](connectionoptions-password.md) for authentication.

## Examples

The following VBScript code example shows how to create a **ConnectionOptions** object, set the properties for the account on the remote computer, and use it in creating a [**Session**](session.md) object.


```VB
Set objWsman = CreateObject( "Wsman.Automation" )
'Create ConnectionOptions object.
Set objConnectionOptions = objWsman.CreateConnectionOptions
objConnectionOptions.UserName = "johns "
objConnectionOptions.Password = "Dtf#4542?98"
iFlags = objWsman.SessionFlagUseBasic Or _
  objWsman.SessionFlagCredUserNamePassword
Set objSession = objWsman.CreateSession _
  ("https://172.30.168.2", iFlags, objConnectionOptions)
strResource = objSession.Get("winrm/config")
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

[Authentication for Remote Connections](authentication-for-remote-connections.md)
</dt> <dt>

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

 

