---
Description: 'Enumerations that are used with authorization applications.'
ms.assetid: 'e2f22838-102e-432c-9c82-06a3e0741374'
title: Authorization Enumerations
---

# Authorization Enumerations

The following enumerations are used with authorization applications.

## In this section



| Topic                                                                                          | Description                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACCESS\_MODE**](access-mode.md)<br/>                                                 | Contains values that indicate how the access rights in an [**EXPLICIT\_ACCESS**](explicit-access.md) structure apply to the trustee.<br/>                                                                                                                                      |
| [**ACL\_INFORMATION\_CLASS**](acl-information-class.md)<br/>                            | Contains values that specify the type of information being assigned to or retrieved from an [access control list](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly) (ACL).<br/>                                                               |
| [**AUDIT\_EVENT\_TYPE**](audit-event-type.md)<br/>                                      | Defines values that indicate the type of object being audited. The [**AccessCheckByTypeAndAuditAlarm**](accesscheckbytypeandauditalarm.md) and [**AccessCheckByTypeResultListAndAuditAlarm**](accesscheckbytyperesultlistandauditalarm.md) functions use these values.<br/>   |
| [**AUDIT\_PARAM\_TYPE**](audit-param-type.md)<br/>                                      | Defines the type of audit parameters that are available.<br/>                                                                                                                                                                                                                   |
| [**AUTHZ\_CONTEXT\_INFORMATION\_CLASS**](authz-context-information-class.md)<br/>       | Specifies the type of information to be retrieved from an existing AuthzClientContext. This enumeration is used by the [**AuthzGetInformationFromContext**](authzgetinformationfromcontext.md) function.<br/>                                                                  |
| [**AUTHZ\_SECURITY\_ATTRIBUTE\_OPERATION**](authz-security-attribute-operation.md)<br/> | Indicates the type of modification to be made to security attributes by a call to the [**AuthzModifySecurityAttributes**](authzmodifysecurityattributes.md) function.<br/>                                                                                                     |
| [**AUTHZ\_SID\_OPERATION**](authz-sid-operation.md)<br/>                                | Indicates the type of SID operations that can be made by a call to the [**AuthzModifySids**](authzmodifysids.md) function.<br/>                                                                                                                                                |
| [**AZ\_PROP\_CONSTANTS**](az-prop-constants.md)<br/>                                    | Defines constants used by Authorization Manager.<br/>                                                                                                                                                                                                                           |
| [**MANDATORY\_LEVEL**](mandatory-level.md)<br/>                                         | Lists the possible security levels.<br/>                                                                                                                                                                                                                                        |
| [**MULTIPLE\_TRUSTEE\_OPERATION**](multiple-trustee-operation.md)<br/>                  | Contains values that indicate whether a [**TRUSTEE**](trustee.md) structure is an impersonation trustee.<br/>                                                                                                                                                                  |
| [**PROG\_INVOKE\_SETTING**](prog-invoke-setting.md)<br/>                                | Indicates the initial setting of the function used to track the progress of a call to the [**TreeSetNamedSecurityInfo**](treesetnamedsecurityinfo.md) or [**TreeResetNamedSecurityInfo**](treeresetnamedsecurityinfo.md) function.<br/>                                       |
| [**SE\_OBJECT\_TYPE**](se-object-type.md)<br/>                                          | Contains values that correspond to the types of Windows objects that support security.<br/>                                                                                                                                                                                     |
| [**SECURITY\_IMPERSONATION\_LEVEL**](security-impersonation-level.md)<br/>              | Contains values that specify security impersonation levels. Security impersonation levels govern the degree to which a server process can act on behalf of a client [process](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-process-gly).<br/>                                 |
| [**SI\_PAGE\_TYPE**](si-page-type.md)<br/>                                              | Contains values that indicate the types of property pages in an access control editor property sheet.<br/>                                                                                                                                                                      |
| [**SID\_NAME\_USE**](sid-name-use.md)<br/>                                              | Contains values that specify the type of a [security identifier](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SID).<br/>                                                                                                                |
| [**TOKEN\_ELEVATION\_TYPE**](token-elevation-type-.md)<br/>                             | Indicates the elevation type of token being queried by the [**GetTokenInformation**](gettokeninformation.md) function or set by the [**SetTokenInformation**](settokeninformation.md) function.<br/>                                                                          |
| [**TOKEN\_INFORMATION\_CLASS**](token-information-class.md)<br/>                        | Contains values that specify the type of information being assigned to or retrieved from an [access token](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly).<br/>                                                                                          |
| [**TOKEN\_TYPE**](token-type.md)<br/>                                                   | Contains values that differentiate between a [primary token](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-primary-token-gly) and an [impersonation token](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-impersonation-token-gly).<br/>                     |
| [**TRUSTEE\_FORM**](trustee-form.md)<br/>                                               | Values that indicate the type of data pointed to by the **ptstrName** member of the [**TRUSTEE**](trustee.md) structure.<br/>                                                                                                                                                  |
| [**TRUSTEE\_TYPE**](trustee-type.md)<br/>                                               | Values that indicate the type of trustee identified by a [**TRUSTEE**](trustee.md) structure.<br/>                                                                                                                                                                             |
| [**WELL\_KNOWN\_SID\_TYPE**](well-known-sid-type.md)<br/>                               | A list of commonly used [security identifiers](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SIDs). Programs can pass these values to the [**CreateWellKnownSid**](createwellknownsid.md) function to create a SID from this list.<br/> |



 

 

 




