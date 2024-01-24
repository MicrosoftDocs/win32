---
description: The purpose of the Central Authorization Policy Rule (CAPR) is to provide a domain-wide definition of an isolated aspect of the organizations authorization policy.
ms.assetid: 51436332-F06A-4929-B3C1-AD2F66C3273B
title: Central Authorization Policy Rule
ms.topic: article
ms.date: 05/31/2018
---

# Central Authorization Policy Rule

The purpose of the Central Authorization Policy Rule (CAPR) is to provide a domain-wide definition of an isolated aspect of the organization's authorization policy. The administrator defines the CAPR to enforce one of the specific authorization requirements. Since the CAPR defines only one specific desired requirement of the authorization policy it can be more simply defined and understood than if all the authorization policy requirements of the organization are compiled into a single policy definition.

The CAPR has the following attributes:

-   Name – identifies the CAPR to the administrators.
-   Description – defines the purpose of the CAPR and any information that may be needed by consumers of the CAPR.
-   Applicability Expression – defines the resources or situations in which the policy will be applied.
-   ID – identifier for use in auditing of changes to the CAPR.
-   Effective Access Control Policy – a Windows security descriptor containing a DACL that defines the effective authorization policy.
-   Exception Expression – one or more expressions that provide a means to override the policy and grant access to a principal according to the evaluation of the expression.
-   Staging Policy – an optional Windows security descriptor containing a DACL that defines a proposed authorization policy (list of access control entries) that will be tested against the effective policy but not enforced. If there is a difference between the results of the effective policy and the staging policy the difference will be recorded in the audit event log.
    -   Since staging can have an unpredictable effect on system performance, a Group Policy administrator must be able to select specific machines on which staging will be in effect. This allows the existing policy to be in place on most machines in an OU while staging is happening on a subset of the machines.
    -   P2 – A local administrator on a particular machine should be able to disable staging if staging on that machine is causing too much of a performance degradation.
-   Backlink to CAP – A list of backlinks to any CAPs that may be referring to this CAPR.

During access check, the CAPR is be evaluated for applicability based on the applicability expression. If a CAPR is applicable, it is evaluated for whether it provides the requesting user the requested access to the identified resource. The results of the CAPE evaluation is then logically joined by **AND** with the results of the DACL on the resource and any other applicable CAPRs in effect on the resource.

Example CAPRs:

``` syntax
[HBI-POLICY]
APPLIES-TO="(@resource.confidentiality == HBI"
SD ="D:(A;;FA;;;AU;(@memberOf("Smartcard Logon")))"
StagingSD = "D:(A;;FA;;;AU;(@memberOf("Smartcard Logon") AND memberOfAny(Resource.ProjectGroups)))"
description="Control access to sensitive information"
 
[RETENTION-POLICY]
Applies-To="@resource.retention == true"
SD ="D:(A;;;FA;;BA)(A;;FR;;;WD)"
description="If the document is marked for retention, then it is read-only for everyone however Local Admins have 
full control to them to put them out of retention when the time comes"
 
[TEST-FINANCE-POLICY]
Applies-To="@resource.label == 'finance'"
SD="D:(A;;FA;;;AU;(member_of(FinanceGroup))"
description="Department: Only employees of the finance department should be able to read documents labeled as finance"
```

## Deny ACEs in CAPEs

In Windows 8 deny ACEs will not be supported in a CAPR. The CAPR authoring UX will not allow creation of a deny ACE. Additionally, when the LSA retrieves the CAP from Active Directory, LSA will verify that no CAPRs have deny ACEs. If a deny ACE is found in a CAPR then the CAP will be treated as invalid and not be copied to the registry or SRM.

> [!Note]  
> The access check will not enforce that no deny ACEs are present. Deny ACEs in a CAPR will be applied. It is expected that authoring tools will prevent this from happening.

 

## CAPE Definition

CAPRs are created though a new UX provided in Active Directory Administrative Center (ADAC.) In ADAC a new task option is provided to create a CAPR. When this task is selected, ADAC will prompt the user with a dialog asking the user for a CAPR name and a description. When these are provided, the controls to define any of the remaining CAPR elements become enabled. For each of the remaining CAPR elements, the UX will call out to the ACL-UI to allow definition of expression and/or ACLs.

## Related topics

<dl> <dt>

[**AccessCheck**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-accesscheck)
</dt> <dt>

[Dynamic Access Control (DAC) scenario](/previous-versions/windows/desktop/dacx/dynamic-access-control-developer-extensibility-roadmap)
</dt> </dl>

 

 
