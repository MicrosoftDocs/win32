---
description: Lists and describes the access types of the Policy object.
ms.assetid: 592dea65-9da1-4e49-82e4-8e08c451e026
title: Policy Object Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# Policy Object Access Rights

The [**Policy**](policy-object.md) object has the following object-specific access types:



| Access type                         | Description                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| POLICY\_VIEW\_LOCAL\_INFORMATION    | This access type is needed to read the target system's miscellaneous security policy information. This includes the default quota, auditing, server state and role information, and trust information. This access type is also needed to enumerate trusted domains, accounts, and [*privileges*](/windows/desktop/SecGloss/p-gly). |
| POLICY\_GET\_PRIVATE\_INFORMATION   | This access type is needed to view sensitive information, such as the names of accounts established for trusted domain relationships.                                                                                                                                                                                                                              |
| POLICY\_TRUST\_ADMIN                | This access type is needed to change the account domain or primary domain information.                                                                                                                                                                                                                                                                             |
| POLICY\_SET\_DEFAULT\_QUOTA\_LIMITS | Set the default system quotas that are applied to user accounts.                                                                                                                                                                                                                                                                                                   |
| POLICY\_CREATE\_SECRET              | This access type is needed to create a new Private Data object.                                                                                                                                                                                                                                                                                                    |
| POLICY\_CREATE\_ACCOUNT             | This access type is needed to create a new [**Account**](account-object.md) object.                                                                                                                                                                                                                                                                               |
| POLICY\_SET\_AUDIT\_REQUIREMENTS    | This access type is needed to update the auditing requirements of the system.                                                                                                                                                                                                                                                                                      |
| POLICY\_AUDIT\_LOG\_ADMIN           | This access type is needed to change the characteristics of the audit trail such as its maximum size or the retention period for audit records, or to clear the log.                                                                                                                                                                                               |
| POLICY\_VIEW\_AUDIT\_INFORMATION    | This access type is needed to view audit trail or audit requirements information.                                                                                                                                                                                                                                                                                  |
| POLICY\_SERVER\_ADMIN               | This access type is needed to modify the server state or role (master/replica) information. It is also needed to change the replica source and account name information.                                                                                                                                                                                           |
| POLICY\_LOOKUP\_NAMES               | This access type is needed to translate between names and SIDs.                                                                                                                                                                                                                                                                                                    |
| POLICY\_CREATE\_PRIVILEGE           | Not yet supported.                                                                                                                                                                                                                                                                                                                                                 |



 

## Generic Access Masks

The [**Policy**](policy-object.md) object publishes the following mappings from generic access types to specific access types:

``` syntax
    GENERIC_READ    STANDARD_RIGHTS_READ |
                    POLICY_VIEW_AUDIT_INFORMATION |
                    POLICY_GET_PRIVATE_INFORMATION

    GENERIC_WRITE   STANDARD_RIGHTS_WRITE |
                    POLICY_TRUST_ADMIN |
                    POLICY_CREATE_ACCOUNT |
                    POLICY_CREATE_SECRET |
                    POLICY_CREATE_PRIVILEGE |
                    POLICY_SET_DEFAULT_QUOTA_LIMITS |
                    POLICY_SET_AUDIT_REQUIREMENTS |
                    POLICY_AUDIT_LOG_ADMIN |
                                        POLICY_SERVER_ADMIN

    GENERIC_EXECUTE STANDARD_RIGHTS_EXECUTE |
                    POLICY_VIEW_LOCAL_INFORMATION |
                    POLICY_LOOKUP_NAMES
```

## Standard Access Types

This object does not support the (optional) SYNCHRONIZE standard access type. All required access types are supported. The mask of all supported access types for this object type is:

``` syntax
    POLICY_ALL_ACCESS STANDARD_RIGHTS_REQUIRED |
                    POLICY_VIEW_LOCAL_INFORMATION |
                    POLICY_VIEW_AUDIT_INFORMATION |
                    POLICY_GET_PRIVATE_INFORMATION |
                    POLICY_TRUST_ADMIN |
                    POLICY_CREATE_ACCOUNT |
                    POLICY_CREATE_SECRET |
                    POLICY_CREATE_PRIVILEGE |
                    POLICY_SET_DEFAULT_QUOTA_LIMITS |
                    POLICY_SET_AUDIT_REQUIREMENTS |
                    POLICY_AUDIT_LOG_ADMIN |
                    POLICY_SERVER_ADMIN
                    POLICY_LOOKUP_NAMES
```

 

 
