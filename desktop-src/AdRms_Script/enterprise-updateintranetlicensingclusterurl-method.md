---
Description: 'Specifies an intranet URL for the licensing cluster.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '78359731-49f1-42e2-b1dd-6bbd61b145fe'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'Enterprise.UpdateIntranetLicensingClusterUrl method'
---

# Enterprise.UpdateIntranetLicensingClusterUrl method

The **UpdateIntranetLicensingClusterUrl** method specifies an intranet URL for the licensing cluster.

## Syntax


```VB
Enterprise.UpdateIntranetLicensingClusterUrl( _
  ByVal url _
)
```



## Parameters

<dl> <dt>

*url* 
</dt> <dd>

A string value that contains a URL in the format http: or https://*DomainName*/\_wmcs/licensing.

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
' Set the URL.

SUB Set URL()

  DIM enterprise

  ' Retrieve the Enterprise object.
  SET enterprise = config_manager.Enterprise
  CheckError()

  ' Set the intranet licensing URL.
  enterprise.UpdateIntranetLicensingClusterUrl( _
    "https://domain_name/_wmcs/licensing")
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**Enterprise**](enterprise-object.md)
</dt> </dl>

 

 




