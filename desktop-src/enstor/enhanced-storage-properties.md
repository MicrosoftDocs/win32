---
title: Enhanced Storage Properties
description: The following Windows Portable Device Enhanced Storage properties are utilized by the Enhanced Storage Portable Device Commands through the IEnhancedStorageSilo SendCommand method.
ms.assetid: 99cedad3-df4a-4a7b-9873-69a134d7d3a9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enhanced Storage Properties

The following Windows Portable Device Enhanced Storage properties are utilized by the [Enhanced Storage Portable Device Commands](enhanced-storage-portable-device-commands.md) through the [**IEnhancedStorageSilo::SendCommand**](/previous-versions/windows/desktop/api/EhStorAPI/nf-ehstorapi-ienhancedstoragesilo-sendcommand) method.



| WPD Enhanced Storage Properties                                            | Variable Type             | Description                                                                                                                                                                                                        |
|----------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ENHANCED\_STORAGE\_PROPERTY\_AUTHENTICATION\_STATE<br/>              | **VT\_UI4**               | Authentication status of the Enhanced Storage Silo.<br/>                                                                                                                                                     |
| ENHANCED\_STORAGE\_PROPERTY\_IS\_AUTHENTICATION\_SILO<br/>           | **VT\_BOOL**              | VARIANT\_TRUE if an Authentication Silo; otherwise, VARIANT\_FALSE.<br/>                                                                                                                                     |
| Password Silo Properties                                                   | Variable Types            | Description                                                                                                                                                                                                        |
| ENHANCED\_STORAGE\_PROPERTY\_MAX\_AUTH\_FAILURES<br/>                | **VT\_UI4**               | Maximum number of allowed password authentication failures.<br/>                                                                                                                                             |
| ENHANCED\_STORAGE\_PROPERTY\_PASSWORD<br/>                           | **VT\_VECTOR \| VT\_UI1** | The password to send or set.<br/>                                                                                                                                                                            |
| ENHANCED\_STORAGE\_PROPERTY\_PASSWORD\_INDICATOR<br/>                | **VT\_UI4**               | Non-zero identifies it as a User password; 0 as Admin.<br/>                                                                                                                                                  |
| ENHANCED\_STORAGE\_PROPERTY\_NEW\_PASSWORD\_INDICATOR<br/>           | **VT\_UI4**               | Non-zero identifies it as a User password; 0 as Admin. <br/>                                                                                                                                                 |
| ENHANCED\_STORAGE\_PROPERTY\_NEW\_PASSWORD<br/>                      | **VT\_VECTOR \| VT\_UI1** | The new password. This property is used to reset a password.<br/>                                                                                                                                            |
| ENHANCED\_STORAGE\_PROPERTY\_USER\_HINT<br/>                         | **VT\_LPWSTR**            | The User password 'hint'.<br/>                                                                                                                                                                               |
| ENHANCED\_STORAGE\_PROPERTY\_USER\_NAME<br/>                         | **VT\_LPWSTR**            | The 'friendly' User name.<br/>                                                                                                                                                                               |
| ENHANCED\_STORAGE\_PROPERTY\_ADMIN\_HINT<br/>                        | **VT\_LPWSTR**            | The Admin password 'hint'.<br/>                                                                                                                                                                              |
| ENHANCED\_STORAGE\_PROPERTY\_SILO\_NAME<br/>                         | **VT\_LPWSTR**            | The 'friendly' Silo name.<br/>                                                                                                                                                                               |
| ENHANCED\_STORAGE\_PROPERTY\_SILO\_FRIENDLYNAME\_SPECIFIED<br/>      | **VT\_UI4**               | Non-zero if a 'friendly' silo name is provided; otherwise, 0.<br/>                                                                                                                                           |
| ENHANCED\_STORAGE\_PROPERTY\_PASSWORD\_SILO\_INFO<br/>               | **VT\_VECTOR \| VT\_UI1** | An [**ENHANCED\_STORAGE\_PASSWORD\_SILO\_INFORMATION**](/previous-versions/windows/desktop/api/EhStorExtensions/ns-ehstorextensions-_enhanced_storage_password_silo_information) structure containing specific requirements and configuration information for the password silo.<br/> |
| ENHANCED\_STORAGE\_PROPERTY\_SECURITY\_IDENTIFIER<br/>               | **VT\_VECTOR \| VT\_UI1** | The security identifier for the device.<br/>                                                                                                                                                                 |
| ENHANCED\_STORAGE\_PROPERTY\_QUERY\_SILO\_TYPE<br/>                  | **VT\_UI4**               | The Query Silo type. For possible values, see PDO\_TYPE.<br/>                                                                                                                                                |
| ENHANCED\_STORAGE\_PROPERTY\_QUERY\_SILO\_RESULTS<br/>               | **VT\_VECTOR \| VT\_UI1** | Query silo properties result returned as an ENUM\_PDO\_RESULTS structure.<br/>                                                                                                                               |
| Certificate Silo Properties                                                | Variable Types            | Description                                                                                                                                                                                                        |
| ENHANCED\_STORAGE\_PROPERTY\_MAX\_CERTIFICATE\_COUNT<br/>            | **VT\_UI4**               | The maximum number of allowed certificate slots on the device.<br/>                                                                                                                                          |
| ENHANCED\_STORAGE\_PROPERTY\_STORED\_CERTIFICATE\_COUNT<br/>         | **VT\_UI4**               | The number of certificate slots in use on the device.<br/>                                                                                                                                                   |
| ENHANCED\_STORAGE\_PROPERTY\_CERTIFICATE\_INDEX<br/>                 | **VT\_UI4**               | An index of certificate slots on the device.<br/>                                                                                                                                                            |
| ENHANCED\_STORAGE\_PROPERTY\_CERTIFICATE\_TYPE<br/>                  | **VT\_UI4**               | The type of certificate. For possible values, see the [**CERT\_TYPE**](cert-type.md) documentation.<br/>                                                                                                    |
| ENHANCED\_STORAGE\_PROPERTY\_VALIDATION\_POLICY<br/>                 | **VT\_UI4**               | The validation policy for the certificate. For possible values, see the [**CERT\_VALIDATION\_POLICY**](cert-validation-policy.md) documentation.<br/>                                                       |
| ENHANCED\_STORAGE\_PROPERTY\_NEXT\_CERTIFICATE\_INDEX<br/>           | **VT\_UI4**               | The indexed location of the next valid certificate.<br/>                                                                                                                                                     |
| ENHANCED\_STORAGE\_PROPERTY\_NEXT\_CERTIFICATE\_OF\_TYPE\_INDEX<br/> | **VT\_UI4**               | The indexed location of the next valid certificate of the same type.<br/>                                                                                                                                    |
| ENHANCED\_STORAGE\_PROPERTY\_CERTIFICATE\_LENGTH<br/>                | **VT\_UI4**               | Length, in bytes, of the certificate.<br/>                                                                                                                                                                   |
| ENHANCED\_STORAGE\_PROPERTY\_CERTIFICATE<br/>                        | **VT\_VECTOR \| VT\_UI1** | The certificate buffer in X.509 format.<br/>                                                                                                                                                                 |
| ENHANCED\_STORAGE\_PROPERTY\_CERTIFICATE\_REQUEST<br/>               | **VT\_VECTOR \| VT\_UI1** | The certificate request buffer in PKCS 10 format.<br/>                                                                                                                                                       |
| ENHANCED\_STORAGE\_PROPERTY\_CERTIFICATE\_CAPABILITY\_TYPE<br/>      | **VT\_UI4**               | Silo capability type. For possible values, see [**CERT\_CAPABILITY**](cert-capability.md).<br/>                                                                                                             |
| ENHANCED\_STORAGE\_PROPERTY\_CERTIFICATE\_SILO\_CAPABILITY<br/>      | **VT\_VECTOR \| VT\_UI1** | The "raw" capability data returned from the silo.<br/>                                                                                                                                                       |
| ENHANCED\_STORAGE\_PROPERTY\_CERTIFICATE\_SILO\_CAPABILITIES<br/>    | **VT\_UNKNOWN**           | The certificate silo capabilities returned in a property collection. For possible values, see [**CERT\_CAPABILITY**](cert-capability.md) and refer to the Silo Capability properties documented below.<br/> |
| ENHANCED\_STORAGE\_PROPERTY\_CERTIFICATE\_ACT\_FRIENDLY\_NAME<br/>   | **VT\_LPWSTR**            | The "friendly" name of the ACT associated with the certificate silo.<br/>                                                                                                                                    |
| ENHANCED\_STORAGE\_PROPERTY\_CERTIFICATE\_SILO\_GUID<br/>            | **VT\_LPWSTR**            | The GUID associated with the certificate silo.<br/>                                                                                                                                                          |
| ENHANCED\_STORAGE\_PROPERTY\_SIGNER\_CERTIFICATE\_INDEX<br/>         | **VT\_UI4**               | The index for the signer certificate slot on the device.<br/>                                                                                                                                                |
| Silo Capability Properties                                                 | Variable Type             | Description                                                                                                                                                                                                        |
| ENHANCED\_STORAGE\_CAPABILITY\_HASH\_ALGS<br/>                       | **VT\_LPWSTR**            | Semi-colon delimited string of hash algorithm identifiers.<br/>                                                                                                                                              |
| ENHANCED\_STORAGE\_CAPABILITY\_ASYMMETRIC\_KEY\_CRYPTOGRAPHY<br/>    | **VT\_LPWSTR**            | Semi-colon delimited string of asymmetric key cryptography identifiers.<br/>                                                                                                                                 |
| ENHANCED\_STORAGE\_CAPABILITY\_SIGNING\_ALGS<br/>                    | **VT\_LPWSTR**            | Semi-colon delimited string of signing algorithm identifiers.<br/>                                                                                                                                           |
| ENHANCED\_STORAGE\_CAPABILITY\_RENDER\_USER\_DATA\_UNUSABLE<br/>     | **VT\_BOOL**              | VARIANT\_TRUE if the silo is capable of rendering User data unreadable; otherwise, VARIANT\_FALSE.<br/>                                                                                                      |
| ENHANCED\_STORAGE\_CAPABILITY\_CERTIFICATE\_EXTENSION\_PARSING<br/>  | **VT\_BOOL**              | VARIANT\_TRUE if certificate extension fields are supported; otherwise, VARIANT\_FALSE.<br/>                                                                                                                 |



 

 

 





