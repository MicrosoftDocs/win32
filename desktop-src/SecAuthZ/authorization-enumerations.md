---
Description: Enumerations that are used with authorization applications.
ms.assetid: e2f22838-102e-432c-9c82-06a3e0741374
title: Authorization Enumerations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Authorization Enumerations

The following enumerations are used with authorization applications.

## In this section



| Topic                                                                                          | Description                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACCESS\_MODE**](access-mode.md)<br/>                                                 | Contains values that indicate how the access rights in an [**EXPLICIT\_ACCESS**](/windows/win32/AccCtrl/ns-accctrl-_explicit_access_a?branch=master) structure apply to the trustee.<br/>                                                                                                                                      |
| [**ACL\_INFORMATION\_CLASS**](/windows/win32/Winnt/ne-winnt-_acl_information_class?branch=master)<br/>                            | Contains values that specify the type of information being assigned to or retrieved from an [access control list](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly) (ACL).<br/>                                                               |
| [**AUDIT\_EVENT\_TYPE**](/windows/win32/Winnt/ne-winnt-_audit_event_type?branch=master)<br/>                                      | Defines values that indicate the type of object being audited. The [**AccessCheckByTypeAndAuditAlarm**](/windows/win32/Winbase/nf-winbase-accesscheckbytypeandauditalarma?branch=master) and [**AccessCheckByTypeResultListAndAuditAlarm**](/windows/win32/Winbase/nf-winbase-accesscheckbytyperesultlistandauditalarma?branch=master) functions use these values.<br/>   |
| [**AUDIT\_PARAM\_TYPE**](/windows/win32/Adtgen/ne-adtgen-_audit_param_type?branch=master)<br/>                                      | Defines the type of audit parameters that are available.<br/>                                                                                                                                                                                                                   |
| [**AUTHZ\_CONTEXT\_INFORMATION\_CLASS**](/windows/win32/Authz/ne-authz-_authz_context_information_class?branch=master)<br/>       | Specifies the type of information to be retrieved from an existing AuthzClientContext. This enumeration is used by the [**AuthzGetInformationFromContext**](/windows/win32/Authz/nf-authz-authzgetinformationfromcontext?branch=master) function.<br/>                                                                  |
| [**AUTHZ\_SECURITY\_ATTRIBUTE\_OPERATION**](/windows/win32/Authz/ne-authz-authz_security_attribute_operation?branch=master)<br/> | Indicates the type of modification to be made to security attributes by a call to the [**AuthzModifySecurityAttributes**](/windows/win32/Authz/nf-authz-authzmodifysecurityattributes?branch=master) function.<br/>                                                                                                     |
| [**AUTHZ\_SID\_OPERATION**](/windows/win32/Authz/ne-authz-authz_sid_operation?branch=master)<br/>                                | Indicates the type of SID operations that can be made by a call to the [**AuthzModifySids**](/windows/win32/Authz/nf-authz-authzmodifysids?branch=master) function.<br/>                                                                                                                                                |
| [**AZ\_PROP\_CONSTANTS**](/windows/win32/Azroles/ne-azroles-tagaz_prop_constants?branch=master)<br/>                                    | Defines constants used by Authorization Manager.<br/>                                                                                                                                                                                                                           |
| [**MANDATORY\_LEVEL**](/windows/win32/Winnt/ne-winnt-_mandatory_level?branch=master)<br/>                                         | Lists the possible security levels.<br/>                                                                                                                                                                                                                                        |
| [**MULTIPLE\_TRUSTEE\_OPERATION**](/windows/win32/AccCtrl/ne-accctrl-_multiple_trustee_operation?branch=master)<br/>                  | Contains values that indicate whether a [**TRUSTEE**](/windows/win32/AccCtrl/ns-accctrl-_trustee_a?branch=master) structure is an impersonation trustee.<br/>                                                                                                                                                                  |
| [**PROG\_INVOKE\_SETTING**](/windows/win32/AccCtrl/ne-accctrl-_progress_invoke_setting?branch=master)<br/>                                | Indicates the initial setting of the function used to track the progress of a call to the [**TreeSetNamedSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-treesetnamedsecurityinfoa?branch=master) or [**TreeResetNamedSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-treeresetnamedsecurityinfoa?branch=master) function.<br/>                                       |
| [**SE\_OBJECT\_TYPE**](/windows/win32/AccCtrl/ne-accctrl-_se_object_type?branch=master)<br/>                                          | Contains values that correspond to the types of Windows objects that support security.<br/>                                                                                                                                                                                     |
| [**SECURITY\_IMPERSONATION\_LEVEL**](/windows/win32/Winnt/ne-winnt-_security_impersonation_level?branch=master)<br/>              | Contains values that specify security impersonation levels. Security impersonation levels govern the degree to which a server process can act on behalf of a client [process](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-process-gly).<br/>                                 |
| [**SI\_PAGE\_TYPE**](/windows/win32/Aclui/ne-aclui-_si_page_type?branch=master)<br/>                                              | Contains values that indicate the types of property pages in an access control editor property sheet.<br/>                                                                                                                                                                      |
| [**SID\_NAME\_USE**](/windows/win32/Winnt/ne-winnt-_sid_name_use?branch=master)<br/>                                              | Contains values that specify the type of a [security identifier](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SID).<br/>                                                                                                                |
| [**TOKEN\_ELEVATION\_TYPE**](/windows/win32/Winnt/ne-winnt-_token_elevation_type?branch=master)<br/>                             | Indicates the elevation type of token being queried by the [**GetTokenInformation**](gettokeninformation.md) function or set by the [**SetTokenInformation**](settokeninformation.md) function.<br/>                                                                          |
| [**TOKEN\_INFORMATION\_CLASS**](/windows/win32/Winnt/ne-winnt-_token_information_class?branch=master)<br/>                        | Contains values that specify the type of information being assigned to or retrieved from an [access token](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly).<br/>                                                                                          |
| [**TOKEN\_TYPE**](/windows/win32/Winnt/ne-winnt-_token_type?branch=master)<br/>                                                   | Contains values that differentiate between a [primary token](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-primary-token-gly) and an [impersonation token](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-impersonation-token-gly).<br/>                     |
| [**TRUSTEE\_FORM**](/windows/win32/AccCtrl/ne-accctrl-_trustee_form?branch=master)<br/>                                               | Values that indicate the type of data pointed to by the **ptstrName** member of the [**TRUSTEE**](/windows/win32/AccCtrl/ns-accctrl-_trustee_a?branch=master) structure.<br/>                                                                                                                                                  |
| [**TRUSTEE\_TYPE**](/windows/win32/AccCtrl/ne-accctrl-_trustee_type?branch=master)<br/>                                               | Values that indicate the type of trustee identified by a [**TRUSTEE**](/windows/win32/AccCtrl/ns-accctrl-_trustee_a?branch=master) structure.<br/>                                                                                                                                                                             |
| [**WELL\_KNOWN\_SID\_TYPE**](/windows/win32/Winnt/ne-winnt-well_known_sid_type?branch=master)<br/>                               | A list of commonly used [security identifiers](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SIDs). Programs can pass these values to the [**CreateWellKnownSid**](createwellknownsid.md) function to create a SID from this list.<br/> |



 

 

 




