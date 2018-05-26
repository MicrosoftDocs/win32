---
Description: Specifies an email contact address.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7943d569-4f79-4a53-b048-42cf50adca1e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Enterprise.UpdateAdminContactEmail method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enterprise.UpdateAdminContactEmail method

The **UpdateAdminContactEmail** method specifies an email contact address.

## Syntax


```VB
Enterprise.UpdateAdminContactEmail( _
  ByVal email _
)
```



## Parameters

<dl> <dt>

*email* 
</dt> <dd>

A string that contains the email address in the format *someone@example.com*.

</dd> </dl>

## Return value

This method does not return a value.

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
' Update the contact address.

SUB GetEnterprise()

  DIM enterprise

  ' Retrieve the Enterprise object.
  SET enterprise = config_manager.Enterprise
  CheckError()

  ' Update the address.
  enterprise.UpdateAdminContactEmail("someone@example.com")
  CheckError()

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
```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**Enterprise**](enterprise-object.md)
</dt> </dl>

 

 




