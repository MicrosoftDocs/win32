---
Description: Specifies an extranet URL for the certification cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 89b52c8a-474f-4f52-a6d9-1c8d5dd7eeac
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Enterprise.UpdateExtranetCertificationClusterUrl method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enterprise.UpdateExtranetCertificationClusterUrl method

The **UpdateExtranetCertificationClusterUrl** method specifies an extranet URL for the certification cluster.

## Syntax


```VB
Enterprise.UpdateExtranetCertificationClusterUrl( _
  ByVal url _
)
```



## Parameters

<dl> <dt>

*url* 
</dt> <dd>

A string value that contains a URL in the format http or https://*DomainName*/\_wmcs/certification.

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

  ' Set the extranet certificate URL.
  enterprise.UpdateExtranetCertificationClusterUrl( _
    "https://domain_name/_wmcs/certification")
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

 

 




