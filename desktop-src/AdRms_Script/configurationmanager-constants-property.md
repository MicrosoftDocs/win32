---
Description: Retrieves a Constants object that contains common constant values supported by the AD RMS service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 2e279834-45e9-4aa6-b7a9-e306df5df81d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ConfigurationManager.Constants property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ConfigurationManager.Constants property

The **Constants** property retrieves a [**Constants**](constants-object.md) object that contains common constant values supported by the AD RMS service.

This property is read-only.

## Syntax


```VB
ConfigurationManager.Constants
```



## Property value

This property returns a [**Constants**](constants-object.md) object. The property is read-only.

## Remarks

You can use the [**Constants**](constants-object.md) object to retrieve the following values:

-   Role constants:<dl> RoleAuditor  
    RoleTemplateEditor  
    RoleAdministrator  
    </dl>
-   Rights constants:<dl> TemplateRightFullControl  
    TemplateRightExport  
    TemplateRightView  
    TemplateRightExtract  
    TemplateRightAllowMacros  
    TemplateRightReply  
    TemplateRightViewRights  
    TemplateRightSave  
    TemplateRightPrint  
    TemplateRightEdit  
    TemplateRightForward  
    TemplateRightReplyAll  
    </dl>
-   Rights template expiration constants:<dl> TemplateExpirationTypeNever  
    TemplateExpirationTypeOnDate  
    TemplateExpirationTypeUntilDays  
    </dl>
-   Key hierarchy constants:<dl> KeyHierarchyPreproduction  
    KeyHierarchyProduction  
    KeyHierarchyOther  
    </dl>
-   Cluster type constants:<dl> ClusterTypeLicensing  
    ClusterTypeCertification  
    </dl>
-   Proxy scheme constants:<dl> ProxySchemeBasic  
    ProxySchemeDigest  
    ProxySchemeWindowsIntegrated  
    </dl>
-   Service account type constants:<dl> ServiceAccountTypeUnknown  
    ServiceAccountTypeDomainIdentity  
    ServiceAccountTypeLocalSystem  
    ServiceAccountTypeLocalService  
    ServiceAccountTypeNetworkService  
    </dl>

## Examples


```VB
' *******************************************************************
' Use the Constants object to filter on a role.

SUB TestRole(testCaseName)
 
  SELECT CASE testCaseName
    CASE "UT_TestGetRoles"
      IF admin_role<config_manager.Constants.RoleAdministrator  THEN
        CALL RaiseError(-100, "The Admin role " _
        & admin_role & " is invalid.")
      END IF
      ' TODO: Perform an action.
        
    CASE "UT_TestGetClusterInformation"
      IF admin_role < config_manager.Constants.RoleAuditor THEN
        CALL RaiseError(-101, "Invalid role operation")
      END IF
     ' TODO: Perform an action.

    CASE ELSE
      CALL RaiseError(-1, "Unknown test case of " & testCaseName)

  END SELECT

END SUB

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ConfigurationManager**](configurationmanager-object.md)
</dt> </dl>

 

 




