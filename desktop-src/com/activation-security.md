---
title: Activation Security
description: Activation Security
ms.assetid: 0c13d473-a9f9-40b5-951b-731eab736fe6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Activation Security

Activation security (also called launch security) helps control who can launch a server. Activation security is automatically applied by the service control manager (SCM) of a particular computer. Upon receipt of a request from a client to activate an object (as described in [Instance Creation Helper Functions](instance-creation-helper-functions.md)), the SCM checks the request against activation-security information stored within its registry. (Activation security is also checked for same-computer activations.)

When determining the identity of the client, activation examines the cloaking flag set in the client's call to [**CoInitializeSecurity**](/windows/win32/combaseapi/nf-combaseapi-coinitializesecurity?branch=master). If the cloaking flag is set (for either dynamic or static cloaking), the thread token is used, if present, to determine the identity of the client. If no cloaking is set, the process token is used instead of the thread token.

For more information about activation security, see [**COAUTHINFO**](/windows/win32/wtypesbase/ns-wtypesbase-_coauthinfo?branch=master) and [**COSERVERINFO**](/windows/win32/objidlbase/ns-objidl-_coserverinfo?branch=master).

## Related topics

<dl> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




