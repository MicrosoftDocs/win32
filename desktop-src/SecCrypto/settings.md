---
description: Used to configure CAPICOM components.
title: Settings object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Settings
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Settings object (Cryptography)

\[The **Settings** object is available for use in the operating systems specified in the Requirements section.\]

The **Settings** object is used to configure CAPICOM components.

## Members

The **Settings** object has these types of members:

-   [Properties](#properties)

### Properties

The **Settings** object has these properties.




| Property | Access type | Description | 
|----------|-------------|-------------|
| <a href="settings-activedirectorysearchlocation.md"><strong>ActiveDirectorySearchLocation</strong></a><br /> | Read/write<br /> | Sets or retrieves the Active Directory search location. The initial location is unspecified by default. When the location is unspecified, the global catalog is searched, then the default domain is searched. The search determines whether the user certificate attribute is published at that location.<br /> | 
| <a href="settings-enablepromptforcertificateui.md"><strong>EnablePromptForCertificateUI</strong></a><br /> | Read/write<br /> | Sets or retrieves a Boolean value that indicates whether user interface prompts for a signer or sender's identity can be used. <br /><blockquote>[!Note]<br />Setting this property does not disable warnings that are generated before any private key usage is done from a web-based application.</blockquote><br /> | 




 

## Remarks

The **Settings** object can be created, and it is safe for scripting. The ProgID for the **Settings** object is CAPICOM.Settings.1.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 




