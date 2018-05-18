---
title: Authentication Protocol Registry Values
description: The setup software for the EAP DLL may create the following registry values below eaptypeid .
ms.assetid: 'a5f6674d-77c8-4b88-af0e-bb62f84d8a2b'
keywords: ["RAS_EAP_VALUENAME_PATH", "RAS_EAP_VALUENAME_FRIENDLY_NAME", "RAS_EAP_VALUENAME_CONFIGUI", "RAS_EAP_VALUENAME_DEFAULT_DATA", "RAS_EAP_VALUENAME_REQUIRE_CONFIGUI", "RAS_EAP_VALUENAME_CONFIG_CLSID", "RAS_EAP_VALUENAME_IDENTITY", "RAS_EAP_VALUENAME_INTERACTIVEUI", "RAS_EAP_VALUENAME_INVOKE_NAMEDLG", "RAS_EAP_VALUENAME_INVOKE_PWDDLG", "RAS_EAP_VALUENAME_ENCRYPTION", "RAS_EAP_VALUENAME_STANDALONE_SUPPORTED", "RAS_EAP_VALUENAME_ROLES_SUPPORTED", "RAS_EAP_VALUENAME_PER_POLICY_CONFIG"]
---

# Authentication Protocol Registry Values

The setup software for the EAP DLL may create the following registry values below **&lt;eaptypeid&gt;**. These registry values are defined in the Raseapif.h header file. The **RAS\_EAP\_VALUENAME\_PATH** and **RAS\_EAP\_VALUENAME\_FRIENDLY\_NAME** values are required. The setup software may create other keys and values as well. These could be used by the authentication protocol itself. For more information and an example of registry configuration, see [Registry Values Example](registry-values-example.md).

[RAS\_EAP\_VALUENAME\_PATH](#ras-eap-valuename-path)

[RAS\_EAP\_VALUENAME\_FRIENDLY\_NAME](#ras-eap-valuename-friendly-name)

[RAS\_EAP\_VALUENAME\_CONFIGUI](#ras-eap-valuename-configui)

[RAS\_EAP\_VALUENAME\_DEFAULT\_DATA](#ras-eap-valuename-default-data)

[RAS\_EAP\_VALUENAME\_REQUIRE\_CONFIGUI](#ras-eap-valuename-require-configui)

[RAS\_EAP\_VALUENAME\_CONFIG\_CLSID](#ras-eap-valuename-config-clsid)

[RAS\_EAP\_VALUENAME\_IDENTITY](#ras-eap-valuename-identity)

[RAS\_EAP\_VALUENAME\_INTERACTIVEUI](#ras-eap-valuename-interactiveui)

[RAS\_EAP\_VALUENAME\_INVOKE\_NAMEDLG](#ras-eap-valuename-invoke-namedlg)

[RAS\_EAP\_VALUENAME\_INVOKE\_PWDDLG](#ras-eap-valuename-invoke-pwddlg)

[RAS\_EAP\_VALUENAME\_ENCRYPTION](#ras-eap-valuename-encryption)

[RAS\_EAP\_VALUENAME\_STANDALONE\_SUPPORTED](#ras-eap-valuename-standalone-supported)

[RAS\_EAP\_VALUENAME\_ROLES\_SUPPORTED](#ras-eap-valuename-roles-supported)

[RAS\_EAP\_VALUENAME\_PER\_POLICY\_CONFIG](#ras-eap-valuename-per-policy-config)

## RAS\_EAP\_VALUENAME\_PATH



| Constant value | Path                               |
|----------------|------------------------------------|
| Type           | REG\_EXPAND\_SZ                    |
| Description    | Specifies the path to the EAP DLL. |



 

## RAS\_EAP\_VALUENAME\_FRIENDLY\_NAME



| Constant value | FriendlyName                                                                                                                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_SZ                                                                                                                                                           |
| Description    | Specifies a friendly name for the authentication protocol. This name appears in the EAP application user interface for both dial-up and wireless implementations. |



 

## RAS\_EAP\_VALUENAME\_CONFIGUI



| Constant value | ConfigUIPath                                                                                                                      |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_EXPAND\_SZ                                                                                                                   |
| Description    | Specifies the path to the DLL that implements the configuration user interface on the client, because this UI is for client only. |



 

## RAS\_EAP\_VALUENAME\_DEFAULT\_DATA



| Constant value | ConfigData                                                            |
|----------------|-----------------------------------------------------------------------|
| Type           | REG\_BINARY                                                           |
| Description    | Specifies default configuration data for the authentication protocol. |



 

## RAS\_EAP\_VALUENAME\_REQUIRE\_CONFIGUI



| Constant value | RequireConfigUI                                                                                                                                                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_DWORD                                                                                                                                                                                                                                               |
| Description    | Specifies whether the user must provide configuration data in the EAP client application user interface. If this value is 1, the user is not allowed to exit the EAP client application UI without providing configuration data. The default value is 0. |



 

## RAS\_EAP\_VALUENAME\_CONFIG\_CLSID



| Constant value | ConfigCLSID                                                   |
|----------------|---------------------------------------------------------------|
| Type           | REG\_SZ                                                       |
| Description    | Specifies the class ID of the configuration UI on the server. |



 

## RAS\_EAP\_VALUENAME\_IDENTITY



| Constant value | IdentityPath                                                                                                                           |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_EXPAND\_SZ                                                                                                                        |
| Description    | Specifies the path to the DLL that implements functions to obtain the user identity on the client, because this UI is for client only. |



 

## RAS\_EAP\_VALUENAME\_INTERACTIVEUI



| Constant value | InteractiveUIPath                                                                                                               |
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_EXPAND\_SZ                                                                                                                 |
| Description    | Specifies the path to the DLL that implements the interactive user interface on the client, because this UI is for client only. |



 

## RAS\_EAP\_VALUENAME\_INVOKE\_NAMEDLG



| Constant value | InvokeUsernameDialog                                                                                                                                                                                   |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_DWORD                                                                                                                                                                                             |
| Description    | Specifies whether RAS should display the standard Windows NT/Windows 2000 user name dialog (value of 1) or invoke [**RasEapGetIdentity**](raseapgetidentity.md) (value of 0). The default value is 1. |



 

## RAS\_EAP\_VALUENAME\_INVOKE\_PWDDLG



| Constant value | InvokePasswordDialog                                                                                                                                                                        |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_DWORD                                                                                                                                                                                  |
| Description    | Specifies whether RAS should display the standard Windows NT/Windows 2000 password dialog. If this value exists and is 0, RAS will not display the password dialog. The default value is 1. |



 

## RAS\_EAP\_VALUENAME\_ENCRYPTION



| Constant value | MPPEEncryptionSupported                                                                                                                                                                       |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_DWORD                                                                                                                                                                                    |
| Description    | If this value is 1, the authentication protocol can generate keys for the Microsoft Point-to-Point Encryption (MPPE) style of encryption. Possible values are 0 or 1. The default value is 0. |



 

## RAS\_EAP\_VALUENAME\_STANDALONE\_SUPPORTED



| Constant value | StandaloneSupported                                                                                                                                                            |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_DWORD                                                                                                                                                                     |
| Description    | Specifies whether this authentication protocol is supported on a standalone Windows 2000 Server. A value of 0 indicates that the EAP is not supported. The default value is 1. |



 

## RAS\_EAP\_VALUENAME\_ROLES\_SUPPORTED



| Constant Value | RolesSupported                                                                                                                                                                                                                             |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_DWORD                                                                                                                                                                                                                                 |
| Description    | Specifies the various roles the EAP supports. This indicates whether it can be used on a server or a client, whether it is supported for RAS connections (VPN) or PEAP. The default behavior is to show the EAP method in PEAP and in EAP. |



 

## RAS\_EAP\_VALUENAME\_PER\_POLICY\_CONFIG



| Constant Value | PerPolicyConfig |
|----------------|-----------------|
| Type           | REG\_DWORD      |
| Description    |                 |



 

## RAS\_EAP\_VALUENAME\_ISTUNNEL\_METHOD

This registry value is not in use.

## RAS\_EAP\_VALUENAME\_FILTER\_INNERMETHODS

This registry value is not in use.

 

 




