---
title: Authentication Protocol Registry Values
description: The setup software for the EAP DLL may create the following registry values below eaptypeid .
ms.assetid: a5f6674d-77c8-4b88-af0e-bb62f84d8a2b
keywords:
- RAS_EAP_VALUENAME_PATH
- RAS_EAP_VALUENAME_FRIENDLY_NAME
- RAS_EAP_VALUENAME_CONFIGUI
- RAS_EAP_VALUENAME_DEFAULT_DATA
- RAS_EAP_VALUENAME_REQUIRE_CONFIGUI
- RAS_EAP_VALUENAME_CONFIG_CLSID
- RAS_EAP_VALUENAME_IDENTITY
- RAS_EAP_VALUENAME_INTERACTIVEUI
- RAS_EAP_VALUENAME_INVOKE_NAMEDLG
- RAS_EAP_VALUENAME_INVOKE_PWDDLG
- RAS_EAP_VALUENAME_ENCRYPTION
- RAS_EAP_VALUENAME_STANDALONE_SUPPORTED
- RAS_EAP_VALUENAME_ROLES_SUPPORTED
- RAS_EAP_VALUENAME_PER_POLICY_CONFIG
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Authentication Protocol Registry Values

The setup software for the EAP DLL may create the following registry values below **&lt;eaptypeid&gt;**. These registry values are defined in the Raseapif.h header file. The **RAS_EAP_VALUENAME_PATH** and **RAS_EAP_VALUENAME_FRIENDLY_NAME** values are required. The setup software may create other keys and values as well. These could be used by the authentication protocol itself. For more information and an example of registry configuration, see [Registry Values Example](registry-values-example.md).

[RAS_EAP_VALUENAME_PATH](#raseapvaluenamepath)

[RAS_EAP_VALUENAME_FRIENDLY_NAME](#raseapvaluenamefriendlyname)

[RAS_EAP_VALUENAME_CONFIGUI](#raseapvaluenameconfigui)

[RAS_EAP_VALUENAME_DEFAULT_DATA](#raseapvaluenamedefaultdata)

[RAS_EAP_VALUENAME_REQUIRE_CONFIGUI](#raseapvaluenamerequireconfigui)

[RAS_EAP_VALUENAME_CONFIG_CLSID](#raseapvaluenameconfigclsid)

[RAS_EAP_VALUENAME_IDENTITY](#raseapvaluenameidentity)

[RAS_EAP_VALUENAME_INTERACTIVEUI](#raseapvaluenameinteractiveui)

[RAS_EAP_VALUENAME_INVOKE_NAMEDLG](#raseapvaluenameinvokenamedlg)

[RAS_EAP_VALUENAME_INVOKE_PWDDLG](#raseapvaluenameinvokepwddlg)

[RAS_EAP_VALUENAME_ENCRYPTION](#raseapvaluenameencryption)

[RAS_EAP_VALUENAME_STANDALONE_SUPPORTED](#raseapvaluenamestandalonesupported)

[RAS_EAP_VALUENAME_ROLES_SUPPORTED](#raseapvaluenamerolessupported)

[RAS_EAP_VALUENAME_PER_POLICY_CONFIG](#raseapvaluenameperpolicyconfig)

## RAS_EAP_VALUENAME_PATH



| Constant value | Path                               |
|----------------|------------------------------------|
| Type           | REG_EXPAND_SZ                    |
| Description    | Specifies the path to the EAP DLL. |



 

## RAS_EAP_VALUENAME_FRIENDLY_NAME



| Constant value | FriendlyName                                                                                                                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG_SZ                                                                                                                                                           |
| Description    | Specifies a friendly name for the authentication protocol. This name appears in the EAP application user interface for both dial-up and wireless implementations. |



 

## RAS_EAP_VALUENAME_CONFIGUI



| Constant value | ConfigUIPath                                                                                                                      |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG_EXPAND_SZ                                                                                                                   |
| Description    | Specifies the path to the DLL that implements the configuration user interface on the client, because this UI is for client only. |



 

## RAS_EAP_VALUENAME_DEFAULT_DATA



| Constant value | ConfigData                                                            |
|----------------|-----------------------------------------------------------------------|
| Type           | REG_BINARY                                                           |
| Description    | Specifies default configuration data for the authentication protocol. |



 

## RAS_EAP_VALUENAME_REQUIRE_CONFIGUI



| Constant value | RequireConfigUI                                                                                                                                                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG_DWORD                                                                                                                                                                                                                                               |
| Description    | Specifies whether the user must provide configuration data in the EAP client application user interface. If this value is 1, the user is not allowed to exit the EAP client application UI without providing configuration data. The default value is 0. |



 

## RAS_EAP_VALUENAME_CONFIG_CLSID



| Constant value | ConfigCLSID                                                   |
|----------------|---------------------------------------------------------------|
| Type           | REG_SZ                                                       |
| Description    | Specifies the class ID of the configuration UI on the server. |



 

## RAS_EAP_VALUENAME_IDENTITY



| Constant value | IdentityPath                                                                                                                           |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG_EXPAND_SZ                                                                                                                        |
| Description    | Specifies the path to the DLL that implements functions to obtain the user identity on the client, because this UI is for client only. |



 

## RAS_EAP_VALUENAME_INTERACTIVEUI



| Constant value | InteractiveUIPath                                                                                                               |
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG_EXPAND_SZ                                                                                                                 |
| Description    | Specifies the path to the DLL that implements the interactive user interface on the client, because this UI is for client only. |



 

## RAS_EAP_VALUENAME_INVOKE_NAMEDLG



| Constant value | InvokeUsernameDialog                                                                                                                                                                                   |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG_DWORD                                                                                                                                                                                             |
| Description    | Specifies whether RAS should display the standard Windows NT/Windows 2000 user name dialog (value of 1) or invoke [**RasEapGetIdentity**](/previous-versions/windows/desktop/api/Raseapif/nf-raseapif-raseapgetidentity) (value of 0). The default value is 1. |



 

## RAS_EAP_VALUENAME_INVOKE_PWDDLG



| Constant value | InvokePasswordDialog                                                                                                                                                                        |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG_DWORD                                                                                                                                                                                  |
| Description    | Specifies whether RAS should display the standard Windows NT/Windows 2000 password dialog. If this value exists and is 0, RAS will not display the password dialog. The default value is 1. |



 

## RAS_EAP_VALUENAME_ENCRYPTION



| Constant value | MPPEEncryptionSupported                                                                                                                                                                       |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG_DWORD                                                                                                                                                                                    |
| Description    | If this value is 1, the authentication protocol can generate keys for the Microsoft Point-to-Point Encryption (MPPE) style of encryption. Possible values are 0 or 1. The default value is 0. |



 

## RAS_EAP_VALUENAME_STANDALONE_SUPPORTED



| Constant value | StandaloneSupported                                                                                                                                                            |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG_DWORD                                                                                                                                                                     |
| Description    | Specifies whether this authentication protocol is supported on a standalone Windows 2000 Server. A value of 0 indicates that the EAP is not supported. The default value is 1. |



 

## RAS_EAP_VALUENAME_ROLES_SUPPORTED



| Constant Value | RolesSupported                                                                                                                                                                                                                             |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG_DWORD                                                                                                                                                                                                                                 |
| Description    | Specifies the various roles the EAP supports. This indicates whether it can be used on a server or a client, whether it is supported for RAS connections (VPN) or PEAP. The default behavior is to show the EAP method in PEAP and in EAP. |



 

## RAS_EAP_VALUENAME_PER_POLICY_CONFIG



| Constant Value | PerPolicyConfig |
|----------------|-----------------|
| Type           | REG_DWORD      |
| Description    |                 |



 

## RAS_EAP_VALUENAME_ISTUNNEL_METHOD

This registry value is not in use.

## RAS_EAP_VALUENAME_FILTER_INNERMETHODS

This registry value is not in use.

 

 




