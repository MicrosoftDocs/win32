---
title: EAP Peer Method Registry Values
description: Learn about the specific registry values that are required for EAP peer methods. See a list of registry values and view additional available resources.
ms.assetid: 16bdd6bf-9eab-40a8-a2d3-8942d2f5f37a
ms.topic: article
ms.date: 05/31/2018
---

# EAP Peer Method Registry Values

Specific registry values are required for EAP peer methods.

## EAP Peer Method DLL Paths

The following path specifies the registry location for regular EAP peer method DLLs.

**HKLM\\System\\CCS\\Services\\Eaphost\\Methods\\*&lt;AuthorId&gt;*\\*&lt;EapTypeId&gt;***

For example, an EAP method installation registration path given an **AuthorId** of "311" (indicating that "Microsoft" is the author) and a **EapTypeId** of "40", appears as follows.

**HKLM\\System\\CCS\\Services\\Eaphost\\Methods\\311\\40**

The following path specifies the registry location for extended EAP method DLLs.

> [!Note]  
> Extended EAP method DLLs are supported in Windows Vista with Service Pack 1 (SP1) or later.

 

**HKLM\\System\\CCS\\Services\\Eaphost\\Methods\\*&lt;AuthorId&gt;*\\254\\*&lt;VendorId&gt;*\\*&lt;EapTypeId&gt;***

For example, an EAP method installation registration path given an **AuthorId** of "311" (indicating that "Microsoft" is the author), a **VendorId** of "311", and a **EapTypeId** of "40", appears as follows.

**HKLM\\System\\CCS\\Services\\Eaphost\\Methods\\311\\254\\311\\40**

> [!Note]  
> For more information on the allocation of EAP method types, see section 6.2 of [RFC 3748](https://go.microsoft.com/fwlink/p/?linkid=84016).

 

## Registry Values

The following EAPHost peer method registry values are required.

-   [PeerDllPath](#peerdllpath)
-   [PeerFriendlyName](#peerfriendlyname)
-   [PeerInvokePasswordDialog](#peerinvokepassworddialog)
-   [PeerInvokeUsernameDialog](#peerinvokeusernamedialog)

The following AP peer method registry values are recommended.

-   [Properties](#properties)

The following AP peer method registry values are optional.

-   [PeerConfigUIPath](#peerconfiguipath)
-   [PeerIdentityPath](#peeridentitypath)
-   [PeerInteractiveUIPath](#peerinteractiveuipath)
-   [PeerRequireConfigUI](#peerrequireconfigui)

### PeerConfigUIPath



| Constant Value | PeerConfigUIPath                                                                                                                                       |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_EXPAND\_SZ                                                                                                                                        |
| Description    | The path to the DLL that contains the implementation of the user configuration dialog. For example, %SystemRoot%\\system32\\&lt;name\_of\_DLL&gt;.dll. |



 

### PeerDllPath



| Constant Value | PeerDllPath                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
| Type           | REG\_EXPAND\_SZ                                                                                 |
| Description    | The path to the EAP method DLL. For example, %SystemRoot%\\system32\\&lt;name\_of\_DLL&gt;.dll. |



 

### PeerFriendlyName



| Constant Value | PeerFriendlyName                                                     |
|----------------|----------------------------------------------------------------------|
| Type           | REG\_SZ                                                              |
| Description    | String that contains the friendly (display) name for the EAP method. |



 

### PeerIdentityPath



| Constant Value | PeerIdentityPath                                                                                                                                     |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_EXPAND\_SZ                                                                                                                                      |
| Description    | The path to the DLL that contains the implementation of the user identity functions. For example, %SystemRoot%\\system32\\&lt;name\_of\_DLL&gt;.dll. |



 

### PeerInteractiveUIPath



| Constant Value | PeerInteractiveUIPath                                                                                                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_EXPAND\_SZ                                                                                                                                                                                                            |
| Description    | The path to the DLL that contains the implementation of the interactive user interface used to obtain user information during execution of the EAP method. For example, %SystemRoot%\\system32\\&lt;name\_of\_DLL&gt;.dll. |



 

### PeerInvokePasswordDialog



| Constant Value | PeerInvokePasswordDialog                                                                                                                                                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_DWORD                                                                                                                                                                                                                                       |
| Description    | 1- to get credentials using the generic EAPHost password and domain dialog box. 0 - to use a custom dialog box. If the generic dialog box is used, credentials are set by the [**EapPeerSetCredentials**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetcredentials) method. |



 

### PeerInvokeUsernameDialog




| Constant Value | PeerInvokeUsernameDialog | 
|----------------|--------------------------|
| Type | REG_DWORD | 
| Description | <ul><li>1 - to get credentials using the generic EAPHost user name dialog box.</li><li>0- to use a custom dialog box.</li></ul>If the generic dialog box is used, credentials are set by the [<strong>EapPeerSetCredentials</strong>](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetcredentials) method. | 




 

### PeerRequireConfigUI



| Constant Value | PeerRequireConfigUI                                                                        |
|----------------|--------------------------------------------------------------------------------------------|
| Type           | REG\_DWORD                                                                                 |
| Description    | 0 if a configuration user interface dialog is implemented for this method; 1 if it is not. |



 

### Properties



| Constant Value | Properties                                                                                                                                                  |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_DWORD                                                                                                                                                  |
| Description    | Bits in the DWORD are set to indicate support for the property. For a list of supported values, see [**EAP Method Properties**](eap-method-properties.md). |



 

## Related topics

<dl> <dt>

[EAP Authenticator Method Registry Keys](eap-authenticator-method-registry-keys.md)
</dt> <dt>

[Registry Configuration for Expanded EAP Types](registry-keys-for-eap-methods.md)
</dt> <dt>

[Using EAPHost](using-eap-host.md)
</dt> <dt>

[RFC 3748](https://go.microsoft.com/fwlink/p/?linkid=84016)
</dt> </dl>

 

 
