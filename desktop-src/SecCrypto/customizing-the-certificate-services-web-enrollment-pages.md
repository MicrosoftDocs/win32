---
description: Certificate Services provides web enrollment pages that can be used to request certificates.
ms.assetid: 1e198bc8-c712-4d0f-9e3a-35a295445acf
title: Customizing Certificate Services Web Enrollment Pages
ms.topic: article
ms.date: 05/31/2018
---

# Customizing Certificate Services Web Enrollment Pages

[*Certificate Services*](../secgloss/c-gly.md) provides web enrollment pages that can be used to request certificates. An administrator can customize some of the items that can be viewed in the web enrollment pages; however, you should be familiar with the web enrollment pages and web scripting before making any changes. For more information about web scripting, see [Scripting](/previous-versions/ms950396(v=msdn.10)).

The default values for the Distinguished Name fields for Organization, Organizational Unit, Locality, State, and Country/Region are the values specified for the [*certification authority*](../secgloss/c-gly.md) (CA) when Certificate Services is installed. These default values appear in the webpages and can be changed by the user during the certificate enrollment process. However, if you want other default values to appear in the webpages, you can edit the Certdat.inc file (in the path \\*WindowsDirectory*\\System32\\Certsrv\\); specifically, you can assign custom values to the following variables provided for customization.



| Variable            | Description                                                                                                                                                                                                                               |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sDefaultCompany     | Default company (appears in the [*certificate request*](../secgloss/c-gly.md) as the [*X.509*](../secgloss/x-gly.md) Organization field). |
| sDefaultOrgUnit     | Default department (appears in the certificate request as the X.509 Organizational Unit field).                                                                                                                                           |
| sDefaultLocality    | Default city (appears in the certificate request as the X.509 Location field).                                                                                                                                                            |
| sDefaultState       | Default state/province (appears in the certificate request as the X.509 State field).                                                                                                                                                     |
| sDefaultCountry     | Default country/region (appears in the certificate request as the X.509 Country/Region field).                                                                                                                                            |
| nPendingTimeoutDays | Number of days in which the user can retrieve a pending certificate after it has been requested.                                                                                                                                          |



 

No other variables should be changed in the Certdat.inc file.

The following example sets the default Organizational Unit to "Marketing".


```VB
sDefaultOrgUnit="Marketing"
```



Additionally, you can edit the Certrqtp.inc file to add, change, or remove [*certificate templates*](../secgloss/c-gly.md) or types available to the user. These templates and types, as well as related information, are contained in a dimensioned array called rgAvailReqTypes(*m*,5).

This array, like all Visual Basic Scripting Edition arrays, is zero based, and as a result, the array's first dimension, *m*, allocates memory for *m*+1 items. Therefore, if in customizing the webpages, you need to modify the number of items in the rgAvailReqTypes array, set the *m* dimension to one less than the total number of items you need. For example, if you will have seven certificate templates, change the declaration of rgAvailReqTypes as shown in the following example.


```VB
Dim rgAvailReqTypes(6,5)
```



The array's second dimension, which always has the value five, allocates the six fields that compose each item. These six fields represent the certificate template or type, the display name associated with this template or type, and whether the template requires [*Secure/Multipurpose Internet Mail Extensions*](../secgloss/s-gly.md) (S/MIME).

To make it easier to understand which of these fields is being accessed, Certrqtp.inc also provides the following constants you can use when setting field values.



| Constant                              | Description                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **FIELD\_OID**                        | (Applies to stand-alone CAs) Index to the item's first field; represents an [*object identifier*](../secgloss/o-gly.md) (OID) for a certificate type.<br/>                                                                                                           |
| **FIELD\_TEMPLATE**                   | (Applies to enterprise CAs) Index to the item's first field; represents a certificate template.<br/>                                                                                                                                                                                                                           |
| **FIELD\_FRIENDLYNAME**               | Index to the item's second field; represents the display name (which the user will see when enrolling) of the item in the first field.                                                                                                                                                                                               |
| **FIELD\_CSPLIST**                    | Index to the item's third field. A list of [*Cryptographic Service Provider*](../secgloss/c-gly.md) names allowed by the template. Each name in the list is separated by a question mark (?).                                                    |
| **FIELD\_CSPLIST2**                   | Index to the item's fourth field. A secondary list of [*Cryptographic Service Provider*](../secgloss/c-gly.md) names allowed by the template. Each name in the list is separated by a question mark (?). This list provides a different default. |
| **FIELD\_EXPORTABLE**                 | Index to the item's fifth field. Indicates whether the template specifies that the key should be exportable. If this field contains "True", the key is exportable. If this field contains "False", the key is not exportable.                                                                                                        |
| **FIELD\_NEEDS\_SMIME\_CAPABILITIES** | This constant is not supported.                                                                                                                                                                                                                                                                                                      |



 

For example, the following expressions assign the OID of 1.3.6.1.5.5.7.3.2 to the first item's first field and assign "Web Browser Certificate" to the first item's second field (the array value of zero indexes the first item).


```VB
rgAvailReqTypes(0, FIELD_OID) = "1.3.6.1.5.5.7.3.2"
rgAvailReqTypes(0, FIELD_FRIENDLYNAME) = "Web Browser Certificate"
```



The result of these assignments is that the user will see the text **Web Browser Certificate** when enrolling, and if the user selects **Web Browser Certificate**, the [*certificate request*](../secgloss/c-gly.md) will contain the OID 1.3.6.1.5.5.7.3.2.

The Certrqtp.inc file also contains constants that are used for the display names of the certificate templates or types. The following example shows the format.


```VB
' Strings for localization.
Const L_WebBrowserCert_Text="Web Browser Certificate"
Const L_EmailProtectionCert_Text="E-Mail Protection Certificate"
Const L_UserTemplateCert_Text="User Certificate"
```



These constants are defined in a block in the Certrqtp.inc file, and this grouping makes it easier to assign each of them a custom value. This is particularly helpful when you localize the display names for international versions of the webpages.

Finally, the Certrqtp.inc file contains a variable that represents the number of certificate templates or types in the rgAvailReqTypes array. In contrast to the *m* dimension of the array, set the value of the nAvailReqTypes variable to the actual number of certificate templates or types that your installation will use; this value must be no larger than *m*+1. Although declared near the top of the Certrqtp.inc file, nAvailReqTypes is assigned a value after the rgAvailReqTypes array is populated, making it easier to see how many elements are actually used by the array. The nAvailReqTypes value is used in an iteration elsewhere in the web enrollment pages, so it is important that this variable accurately reflect the number of certificate templates or types that you want to be viewable to the user.

Note that merely adding [*certificate templates*](../secgloss/c-gly.md) and types to the Certrqtp.inc file does not guarantee that the user will be able to get a certificate with those traits; the CA must be authorized to issue a certificate for the specified certificate template or type.

Installations can create their own applications or webpages to request and receive a certificate. The [**ICEnroll4**](/windows/desktop/api/Xenroll/nn-xenroll-icenroll4) and [**ICertRequest2**](/windows/desktop/api/Certcli/nn-certcli-icertrequest2) objects allow programmers or scripters to build [*certificate request*](../secgloss/c-gly.md) applications.

To request a certificate to be issued on a [*smart card*](../secgloss/s-gly.md), you can use the Smart Card Enrollment Control. For details and example code, see [**ISCrdEnr**](iscrdenr.md).

 

 
