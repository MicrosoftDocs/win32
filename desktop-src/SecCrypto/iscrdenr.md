---
description: Represents the smart card enrollment control.
ms.assetid: ae872206-81e7-4627-b807-4222f75f8ab6
title: ISCrdEnr interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr interface

The **ISCrdEnr** interface represents the smart card enrollment control. It is primarily of interest to developers not using Automation. For programming in Visual Basic or another Automation language, see the [**CEnroll**](/previous-versions/windows/desktop/legacy/aa376007(v=vs.85)) object.

## Members

The **ISCrdEnr** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ISCrdEnr** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ISCrdEnr** interface has these methods.



| Method                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
|:--------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**enroll**](/previous-versions/windows/desktop/legacy/aa386564(v=vs.85))                                         | Requests a certificate on behalf of the user and stores the resulting [*certificate*](../secgloss/c-gly.md) on the user's [*smart card*](../secgloss/s-gly.md).<br/>                                                                                                                                                |
| [**enumCAName**](iscrdenr-enumcaname.md)                                 | Enumerates the names of the [*certification authorities*](../secgloss/c-gly.md) (CAs) for a given certificate template name.<br/>                                                                                                                                                                                                       |
| [**enumCertTemplateName**](iscrdenr-enumcerttemplatename.md)             | Enumerates the certificate template names.<br/>                                                                                                                                                                                                                                                                                                                                                               |
| [**enumCSPName**](iscrdenr-enumcspname.md)                               | Enumerates the name of the available [*cryptographic service providers*](../secgloss/c-gly.md) (CSPs).<br/>                                                                                                                                                                                                               |
| [**getCACount**](iscrdenr-getcacount.md)                                 | Returns the number of CAs willing to issue a certificate based on the specified certificate template.<br/>                                                                                                                                                                                                                                                                                                    |
| [**getCAName**](iscrdenr-getcaname.md)                                   | Retrieves the name of the specified CA for a given certificate template.<br/>                                                                                                                                                                                                                                                                                                                                 |
| [**getCertTemplateCount**](iscrdenr-getcerttemplatecount.md)             | Retrieves the number of certificate templates.<br/>                                                                                                                                                                                                                                                                                                                                                           |
| [**getCertTemplateName**](iscrdenr-getcerttemplatename.md)               | Retrieves the name of the certificate template.<br/>                                                                                                                                                                                                                                                                                                                                                          |
| [**getCertTemplateSMIME**](iscrdenr-getcerttemplatesmime.md)             | Determine whether a certificate template contains the szOID\_PKIX\_KP\_EMAIL\_PROTECTION key usage. If this key usage is part of the certificate template, the certificate template supports [*Secure/Multipurpose Internet Mail Extensions*](../secgloss/s-gly.md) (S/MIME) operations.<br/> |
| [**getEnrolledCertificateName**](iscrdenr-getenrolledcertificatename.md) | Retrieves the name of the certificate resulting from an earlier successful call to [**ISCrdEnr::enroll**](/previous-versions/windows/desktop/legacy/aa386564(v=vs.85)). This method can also be used to display the certificate in a dialog box.<br/>                                                                                                                                                                                                 |
| [**getSigningCertificateName**](iscrdenr-getsigningcertificatename.md)   | Retrieves the subject name from the signing certificate. This method can also be used to display the certificate in a dialog box. <br/>                                                                                                                                                                                                                                                                       |
| [**getUserName**](iscrdenr-getusername.md)                               | Retrieves the name of the user on whose behalf the certificate enrollment is intended.<br/>                                                                                                                                                                                                                                                                                                                   |
| [**resetUser**](iscrdenr-resetuser.md)                                   | Clears the user name from the smart card control.<br/>                                                                                                                                                                                                                                                                                                                                                        |
| [**selectSigningCertificate**](iscrdenr-selectsigningcertificate.md)     | Displays a **Select Certificate** dialog box allowing a signing certificate (also known as the *enrollment agent certificate*) to be selected.<br/>                                                                                                                                                                                                                                                           |
| [**selectUserName**](iscrdenr-selectusername.md)                         | Displays a **Select User** dialog box allowing a user name to be selected. The user name applies to the user on whose behalf the certificate enrollment is intended.<br/>                                                                                                                                                                                                                                     |
| [**setCAName**](iscrdenr-setcaname.md)                                   | Specifies the name of the CA.<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| [**setCertTemplateName**](iscrdenr-setcerttemplatename.md)               | Specifies the name of the certificate template.<br/>                                                                                                                                                                                                                                                                                                                                                          |
| [**setSigningCertificate**](iscrdenr-setsigningcertificate.md)           | Specifies a signing certificate (also known as the *enrollment agent certificate*).<br/>                                                                                                                                                                                                                                                                                                                      |
| [**setUserName**](iscrdenr-setusername.md)                               | Specifies the name of the user on whose behalf the certificate enrollment is intended.<br/>                                                                                                                                                                                                                                                                                                                   |



 

### Properties

The **ISCrdEnr** interface has these properties.



| Property                                         | Access type           | Description                                                          |
|:-------------------------------------------------|:----------------------|:---------------------------------------------------------------------|
| [**CSPCount**](iscrdenr-cspcount.md)<br/> | Read-only<br/>  | Specifies the number of CSPs. This property is read-only.<br/> |
| [**CSPName**](iscrdenr-cspname.md)<br/>   | Read/write<br/> | The name of the CSP. This property is read/write. <br/>        |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Scrdenrl.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCrdEnr is defined as 753988a1-1357-436d-9cf5-f089bdd67d64<br/>             |



 

 
