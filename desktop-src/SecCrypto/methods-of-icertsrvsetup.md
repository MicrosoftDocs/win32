---
Description: 'The following methods are defined by the ICertSrvSetup interface. The property access methods are not shown here. To see the properties for ICertSrvSetup, see Properties of ICertSrvSetup.'
ms.assetid: 'cb7f288b-30a0-4c3b-b7bc-3055166d2302'
title: Methods of ICertSrvSetup
---

# Methods of ICertSrvSetup

The following methods are defined by the [**ICertSrvSetup**](icertsrvsetup.md) interface. The property access methods are not shown here. To see the properties for **ICertSrvSetup**, see [Properties of ICertSrvSetup](properties-of-icertsrvsetup.md).



| Method                                                                         | Description                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CAImportPFX**](icertsrvsetup-caimportpfx.md)                               | Imports a Certification Authority (CA) certificate and its associated private key into the "LocalMachine" store.                                                                                                                                          |
| [**GetCASetupProperty**](icertsrvsetup-getcasetupproperty.md)                 | Gets a property value for a CA configuration.                                                                                                                                                                                                             |
| [**GetExistingCACertificates**](icertsrvsetup-getexistingcacertificates.md)   | Gets the collection of **CCertSrvSetupKeyInformation** objects that represent valid CA certificates currently installed on the computer.                                                                                                                  |
| [**GetHashAlgorithmList**](icertsrvsetup-gethashalgorithmlist.md)             | Gets the list of hash algorithms supported by the specified [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) for an asymmetric key signature algorithm. |
| [**GetKeyLengthList**](icertsrvsetup-getkeylengthlist.md)                     | Gets the list of key lengths supported by the specified CSP.                                                                                                                                                                                              |
| [**GetPrivateKeyContainerList**](icertsrvsetup-getprivatekeycontainerlist.md) | Gets the list of key container names stored by the specified CSP for asymmetric signature key algorithms.                                                                                                                                                 |
| [**GetProviderNameList**](icertsrvsetup-getprovidernamelist.md)               | Gets the list of CSPs that provide asymmetric key signature algorithms on the computer.                                                                                                                                                                   |
| [**GetSupportedCATypes**](icertsrvsetup-getsupportedcatypes.md)               | Gets the types of CAs that can be installed on a computer under the caller context.                                                                                                                                                                       |
| [**InitializeDefaults**](icertsrvsetup-initializedefaults.md)                 | Initializes a **CCertSrvSetup** object with default values to enable installation of a CA role.                                                                                                                                                           |
| [**Install**](icertsrvsetup-install.md)                                       | Installs a CA role as configured in the **CCertSrvSetup** object.                                                                                                                                                                                         |
| [**IsPropertyEditable**](icertsrvsetup-ispropertyeditable.md)                 | Indicates to the caller whether a specified property can be edited.                                                                                                                                                                                       |
| [**PostUnInstall**](icertsrvsetup-postuninstall.md)                           | Is not implemented and is reserved for future use.                                                                                                                                                                                                        |
| [**PreUnInstall**](icertsrvsetup-preuninstall.md)                             | Temporarily saves role-specific state-information.                                                                                                                                                                                                        |
| [**SetCADistinguishedName**](icertsrvsetup-setcadistinguishedname.md)         | Sets a CA common name and an optional distinguished name suffix.                                                                                                                                                                                          |
| [**SetCASetupProperty**](icertsrvsetup-setcasetupproperty.md)                 | Sets a property value for a CA configuration.                                                                                                                                                                                                             |
| [**SetDatabaseInformation**](icertsrvsetup-setdatabaseinformation.md)         | Sets the database related information for the CA role.                                                                                                                                                                                                    |
| [**SetParentCAInformation**](icertsrvsetup-setparentcainformation.md)         | Sets the parent CA information for a subordinate CA configuration.                                                                                                                                                                                        |
| [**SetWebCAInformation**](icertsrvsetup-setwebcainformation.md)               | Sets the CA information for the CA Web Enrollment role.                                                                                                                                                                                                   |



 

 

 



