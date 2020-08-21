---
title: EAP Authenticator Method Registry Values
description: Learn about EAP Authenticator method registry values. These specific registry values are required for EAP authenticator methods.
ms.assetid: 9374f9f7-b088-4e3a-ac96-8ccbeda87bb7
ms.topic: article
ms.date: 05/31/2018
---

# EAP Authenticator Method Registry Values

Specific registry values are required for EAP authenticator methods.

## EAP Authenticator Method DLL Paths

The following path specifies the registry location for regular EAP authenticator method DLLs.

**HKLM\\System\\CCS\\Services\\Eaphost\\Methods\\*&lt;AuthorId&gt;*\\*&lt;EapTypeId&gt;***

For example, an EAP authenticator method installation registration path given an **AuthorId** of "311" (indicating that "Microsoft" is the author) and a **EapTypeId** of "40", appears as follows.

**HKLM\\System\\CCS\\Services\\Eaphost\\Methods\\311\\40**

The following path specifies the registry location for extended EAP authenticator method DLLs.

**HKLM\\System\\CCS\\Services\\Eaphost\\Methods\\*&lt;AuthorId&gt;*\\254\\*&lt;VendorId&gt;*\\*&lt;VendorType&gt;***

For example, an EAP authenticator method installation registration path given an **AuthorId** of "311" (indicating that "Microsoft" is the author), a **VendorId** of "311", and a **EapTypeId** of "40", appears as follows.

**HKLM\\System\\CCS\\Services\\Eaphost\\Methods\\311\\254\\311\\40**

> [!Note]  
> For more information on the allocation of EAP method types, see section 6.2 of [RFC 3748](https://go.microsoft.com/fwlink/p/?linkid=84016).

 

## Registry Values

The following authenticator method registry values are required.

-   [AuthenticatorDllPath](#authenticatordllpath)
-   [AuthenticatorFriendlyName](#authenticatorfriendlyname)

Besides the above registry values, the following authenticator method registry value is recommended.

-   [Properties](#properties)

The remaining authenticator method registry values are optional.

-   [ConfigCLSID](#configclsid)
-   [StandaloneSupported](#standalonesupported)

## AuthenticatorDllPath



| Constant Value | AuthenticatorDllPath                                                                                          |
|----------------|---------------------------------------------------------------------------------------------------------------|
| Type           | REG\_EXPAND\_SZ                                                                                               |
| Description    | The path to the EAP authenticator method DLL. For example, %SystemRoot%\\system32\\&lt;name\_of\_DLL&gt;.dll. |



 

## AuthenticatorFriendlyName



| Constant Value | AuthenticatorFriendlyName                                                          |
|----------------|------------------------------------------------------------------------------------|
| Type           | REG\_SZ                                                                            |
| Description    | String that contains the friendly (display) name for the EAP authenticator method. |



 

## ConfigCLSID



| Constant Value | ConfigCLSID                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_SZ                                                                                                                               |
| Description    | String that contains the configuration class GUID for this authenticator method, in the format {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX} |



 

## Properties



| Constant Value | Properties                                                                                                                                                  |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type           | REG\_DWORD                                                                                                                                                  |
| Description    | Bits in the DWORD are set to indicate support for the property. For a list of supported values, see [**EAP Method Properties**](eap-method-properties.md). |



 

## StandaloneSupported



| Constant Value | StandaloneSupported                                             |
|----------------|-----------------------------------------------------------------|
| Type           | REG\_DWORD                                                      |
| Description    | 0 if this is a standalone authenticator method; 1 if it is not. |



 

## Related topics

<dl> <dt>

[EAP Peer Method Registry Keys](eap-peer-method-registry-keys.md)
</dt> <dt>

[Registry Configuration for Expanded EAP Types](registry-keys-for-eap-methods.md)
</dt> <dt>

[Using EAPHost](using-eap-host.md)
</dt> <dt>

[RFC 3748](https://go.microsoft.com/fwlink/p/?linkid=84016)
</dt> </dl>

 

 




