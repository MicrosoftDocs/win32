---
Description: Specifies an extranet URL for the certification or licensing cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 178146cc-945a-45f6-b7aa-6aa254b23e7b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Enterprise.UpdateExtranetLicensingClusterUrl method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enterprise.UpdateExtranetLicensingClusterUrl method

The **UpdateExtranetLicensingClusterUrl** method specifies an extranet URL for the certification or licensing cluster.

## Syntax


```VB
Enterprise.UpdateExtranetLicensingClusterUrl( _
  ByVal url _
)
```



## Parameters

<dl> <dt>

*url* 
</dt> <dd>

A string value that contains a URL in the format http or https://*DomainName*/\_wmcs/licensing.

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

  ' Set the extranet licensing URL.
  enterprise.UpdateExtranetLicensingClusterUrl( _
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**Enterprise**](enterprise-object.md)
</dt> </dl>

 

 




