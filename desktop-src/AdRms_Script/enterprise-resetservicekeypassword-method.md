---
Description: 'Specifies a password used to encrypt the server licensor private key.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'ff9fe56d-8d5b-401b-9f20-3a1a4f9e6bb7'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'Enterprise.ResetServiceKeyPassword method'
---

# Enterprise.ResetServiceKeyPassword method

The **ResetServiceKeyPassword** method specifies a password used to encrypt the server licensor private key.

## Syntax


```VB
Enterprise.ResetServiceKeyPassword( _
  ByVal password _
)
```



## Parameters

<dl> <dt>

*password* 
</dt> <dd>

A string value that contains the password.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The password is used to encrypt the private key. The encrypted data is then saved in the configuration database and the registry of the local computer. The key is saved by using the current user logon account. This method does not support remote access.

## Examples


```VB
DIM config_manager
DIM admin_role

' *******************************************************************
' Create and initialize a ConfigurationManager object.

SUB InitObject()

  CALL WScript.Echo( "Create ConfigurationManager object...")
  SET config_manager = CreateObject _
    ("Microsoft.RightsManagementServices.Admin.ConfigurationManager")      
  CheckError()
    
  CALL WScript.Echo( "Initialize...")
  admin_role=config_manager.Initialize(false,"localhost",80,"","","")
  CheckError()

END SUB

' *******************************************************************
' Reset the password.

SUB SetPassword()

  DIM enterprise

  ' Retrieve the Enterprise object.
  SET enterprise = config_manager.Enterprise
  CheckError()

  ' Reset the password.
  IF config_manager.IsServerOnLocalMachine THEN
    enterprise.ResetServiceKeyPassword("some_password")
    CheckError()
  ELSE
    CALL RaiseError(-504, "Server must be local computer.")
  END IF

END SUB

' *******************************************************************
' Error checking function.

FUNCTION CheckError()
  CheckError = Err.number
  IF Err.number <> 0 THEN
    CALL WScript.Echo( vbTab & "*****Error Number: " _
                       & Err.number _
                       & " Desc:" _
                       & Err.Description _
                       & "*****")
    WScript.StdErr.Write(Err.Description)
    WScript.Quit( Err.number )
  END IF
END FUNCTION

' *******************************************************************
' Generate a runtime error.

SUB RaiseError(errId, desc)
  CALL Err.Raise( errId, "", desc )
  CheckError()
END SUB
```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**Enterprise**](enterprise-object.md)
</dt> </dl>

 

 




