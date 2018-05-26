---
Description: Authz API allows applications to perform customizable access checks with better performance and more simplified development than Low-level Access Control.
ms.assetid: 83df96ff-f3d6-43f8-88b2-6387914b3503
title: Using Authz API
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Authz API

Authz API allows applications to perform customizable access checks with better performance and more simplified development than [Low-level Access Control](low-level-access-control.md).

Authz API allows applications to cache access checks for improved performance, to query and modify client contexts, and to define business rules that can be used to evaluate access permission dynamically.

## In This Section



| Topic                                                                             | Description                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Initializing a Client Context](initializing-a-client-context.md)<br/>     | An application must create a client context before it can use Authz API to perform access checks or auditing.<br/>                                                                                                                                            |
| [Querying a Client Context](querying-a-client-context.md)<br/>             | Applications can call the [**AuthzGetInformationFromContext**](/windows/win32/Authz/nf-authz-authzgetinformationfromcontext?branch=master) function to query information about an existing client context.<br/>                                                                                       |
| [Adding SIDs to a Client Context](adding-sids-to-a-client-context.md)<br/> | An application can add [*security identifiers*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SIDs) to an existing client context by calling the [**AuthzAddSidsToContext**](/windows/win32/Authz/nf-authz-authzaddsidstocontext?branch=master) function.<br/> |
| [Checking Access with Authz API](checking-access-with-authz-api.md)<br/>   | Applications determine whether to grant access to securable objects by calling the [**AuthzAccessCheck**](/windows/win32/Authz/nf-authz-authzaccesscheck?branch=master) function.<br/>                                                                                                                |
| [Caching Access Checks](caching-access-checks.md)<br/>                     | When an application performs an access check by calling the [**AuthzAccessCheck**](/windows/win32/Authz/nf-authz-authzaccesscheck?branch=master) function, the results of that access check can be cached.<br/>                                                                                       |



 

 

 




