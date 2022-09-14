---
description: The SWbemSecurity object gets or sets security settings, such as privileges, COM impersonations, and authentication levels assigned to an object.
ms.assetid: 794587fa-5feb-455b-be28-ecfaa25625ad
ms.tgt_platform: multiple
title: SWbemSecurity object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemSecurity
- ISWbemSecurity
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemSecurity object

The **SWbemSecurity** object gets or sets security settings, such as privileges, COM impersonations, and authentication levels assigned to an object. The [**SWbemLocator**](swbemlocator.md), [**SWbemServices**](swbemservices.md), [**SWbemObject**](swbemobject.md), [**SWbemObjectSet**](swbemobjectset.md), [**SWbemObjectPath**](swbemobjectpath.md), [**SWbemLastError**](swbemlasterror.md), and [**SWbemEventSource**](swbemeventsource.md) objects have a **Security\_** property, which is the **SWbemSecurity** object. When you retrieve an instance or view the WMI security log, you might need to set the properties of the **Security\_** object.

The VBScript [CreateObject](/previous-versions//xzysf6hc(v=vs.85)) call cannot create the Security object. The security settings in this object do not identify the authentication, impersonation, or privilege settings on a connection to WMI, or the security in effect for the proxy when an object is delivered to a sink in an asynchronous call. For more information, see [Maintaining WMI Security](maintaining-wmi-security.md).

## Members

The **SWbemSecurity** object has these types of members:

-   [Properties](#properties)

### Properties

The **SWbemSecurity** object has these properties.



| Property                                                                    | Access type           | Description                                                                                                                                                                                                                            |
|:----------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AuthenticationLevel**](swbemsecurity-authenticationlevel.md)<br/> | Read/write<br/> | Numeric value that defines the COM Authentication level that is assigned to this object. This setting determines how you protect information sent from WMI.<br/>                                                                 |
| [**ImpersonationLevel**](swbemsecurity-impersonationlevel.md)<br/>   | Read/write<br/> | Numeric value that defines the COM Impersonation level that is assigned to this object. This setting determines if processes owned by WMI can detect or use your security credentials when making calls to other processes.<br/> |
| [**Privileges**](swbemsecurity-privileges.md)<br/>                   | Read-only<br/>  | An [**SWbemPrivilegeSet**](swbemprivilegeset.md) object that defines privileges for this object. For more information, see [Running with Special Privileges](/windows/desktop/SecBP/running-with-special-privileges).<br/>                    |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemSecurity<br/>                                                         |
| IID<br/>                      | IID\_ISWbemSecurity<br/>                                                          |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> <dt>

[Setting Client\_Application\_Process Security](setting-client-application-process-security.md)
</dt> <dt>

[**WbemAuthenticationLevelEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemauthenticationlevelenum)
</dt> <dt>

[**WbemImpersonationLevelEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemimpersonationlevelenum)
</dt> <dt>

[**WbemPrivilegeEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemprivilegeenum)
</dt> </dl>

 

