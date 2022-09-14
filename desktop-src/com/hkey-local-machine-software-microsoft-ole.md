---
title: HKEY_LOCAL_MACHINESOFTWAREMicrosoftOle
description: The registry values associated with the HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Ole key control the default launch and access permission settings and call-level security capabilities for COM-based applications that do not call CoInitializeSecurity.
ms.assetid: 871ae88f-ed2c-4078-8160-b0a490390426
ms.topic: article
ms.date: 05/31/2018
---

# HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Ole

The registry values associated with the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Ole** key control the default launch and access permission settings and call-level security capabilities for COM-based applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity).

Only administrators, the object creator, and the system have full access to this portion of the registry. All other users have read-only access.



| Registry value                                                                         | Description                                                                                                                                                                   |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActivationFailureLoggingLevel**](activationfailurelogginglevel.md)                 | Sets the verbosity of event log entries about failed requests for component launch and activation.                                                                            |
| [**CallFailureLoggingLevel**](callfailurelogginglevel.md)                             | Sets the verbosity of event log entries about failed calls to components.                                                                                                     |
| [**DCOMSCMRemoteCallFlags**](dcomscmremotecallflags.md)                               | Controls the behavior of calls from the local DCOM Service Control Manager (DCOMSCM) to a remote DCOMSCM.                                                                     |
| [**DefaultAccessPermission**](defaultaccesspermission.md)                             | Defines default access permission list for the computer.                                                                                                                      |
| [**DefaultLaunchPermission**](defaultlaunchpermission.md)                             | Defines default launch ACL for the computer.                                                                                                                                  |
| [**EnableDCOM**](enabledcom.md)                                                       | Sets the global activation policy for the computer.                                                                                                                           |
| [**InvalidSecurityDescriptorLoggingLevel**](invalidsecuritydescriptorlogginglevel.md) | Sets the verbosity of event log entries about invalid security descriptors for component launch and access permissions.                                                       |
| [**LegacyAuthenticationLevel**](legacyauthenticationlevel.md)                         | Sets the default authentication level.                                                                                                                                        |
| [**LegacyImpersonationLevel**](legacyimpersonationlevel.md)                           | Sets the default impersonation level.                                                                                                                                         |
| [**LegacySecureReferences**](legacysecurereferences.md)                               | Determines security level of **AddRef**/**Release** invocations.                                                                                                              |
| [**MachineAccessRestriction**](machineaccessrestriction.md)                           | Sets the computer-wide restriction policy for component access.                                                                                                               |
| [**MachineLaunchRestriction**](machinelaunchrestriction.md)                           | Sets the computer-wide restriction policy for component launch and activation.                                                                                                |
| [**NonRedist**](nonredist.md)                                                         | Adds names to the list of files that should not be exported when COM+ applications are packaged for installation on other computers. Note that this is a subkey, not a value. |
| [**SRPActivateAsActivatorChecks**](srpactivateasactivatorchecks.md)                   | Determines whether software restriction policy (SRP) trust levels are used during ActivateAsActivator activations.                                                            |
| [**SRPRunningObjectChecks**](srprunningobjectchecks.md)                               | Determines whether attempts to connect to running objects are screened for compatible software restriction policy (SRP) trust levels.                                         |



 

 

 




