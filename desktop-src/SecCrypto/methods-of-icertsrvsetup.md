---
description: The following methods are defined by the ICertSrvSetup interface. The property access methods are not shown here. To see the properties for ICertSrvSetup, see Properties of ICertSrvSetup.
ms.assetid: cb7f288b-30a0-4c3b-b7bc-3055166d2302
title: Methods of ICertSrvSetup
ms.topic: article
ms.date: 05/31/2018
---

# Methods of ICertSrvSetup

The following methods are defined by the [**ICertSrvSetup**](/windows/desktop/api/Casetup/nn-casetup-icertsrvsetup) interface. The property access methods are not shown here. To see the properties for **ICertSrvSetup**, see [Properties of ICertSrvSetup](properties-of-icertsrvsetup.md).



| Method                                                                         | Description                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CAImportPFX**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-caimportpfx)                               | Imports a Certification Authority (CA) certificate and its associated private key into the "LocalMachine" store.                                                                                                                                          |
| [**GetCASetupProperty**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-getcasetupproperty)                 | Gets a property value for a CA configuration.                                                                                                                                                                                                             |
| [**GetExistingCACertificates**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-getexistingcacertificates)   | Gets the collection of **CCertSrvSetupKeyInformation** objects that represent valid CA certificates currently installed on the computer.                                                                                                                  |
| [**GetHashAlgorithmList**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-gethashalgorithmlist)             | Gets the list of hash algorithms supported by the specified [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) for an asymmetric key signature algorithm. |
| [**GetKeyLengthList**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-getkeylengthlist)                     | Gets the list of key lengths supported by the specified CSP.                                                                                                                                                                                              |
| [**GetPrivateKeyContainerList**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-getprivatekeycontainerlist) | Gets the list of key container names stored by the specified CSP for asymmetric signature key algorithms.                                                                                                                                                 |
| [**GetProviderNameList**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-getprovidernamelist)               | Gets the list of CSPs that provide asymmetric key signature algorithms on the computer.                                                                                                                                                                   |
| [**GetSupportedCATypes**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-getsupportedcatypes)               | Gets the types of CAs that can be installed on a computer under the caller context.                                                                                                                                                                       |
| [**InitializeDefaults**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-initializedefaults)                 | Initializes a **CCertSrvSetup** object with default values to enable installation of a CA role.                                                                                                                                                           |
| [**Install**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-install)                                       | Installs a CA role as configured in the **CCertSrvSetup** object.                                                                                                                                                                                         |
| [**IsPropertyEditable**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-ispropertyeditable)                 | Indicates to the caller whether a specified property can be edited.                                                                                                                                                                                       |
| [**PostUnInstall**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-postuninstall)                           | Is not implemented and is reserved for future use.                                                                                                                                                                                                        |
| [**PreUnInstall**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-preuninstall)                             | Temporarily saves role-specific state-information.                                                                                                                                                                                                        |
| [**SetCADistinguishedName**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-setcadistinguishedname)         | Sets a CA common name and an optional distinguished name suffix.                                                                                                                                                                                          |
| [**SetCASetupProperty**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-setcasetupproperty)                 | Sets a property value for a CA configuration.                                                                                                                                                                                                             |
| [**SetDatabaseInformation**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-setdatabaseinformation)         | Sets the database related information for the CA role.                                                                                                                                                                                                    |
| [**SetParentCAInformation**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-setparentcainformation)         | Sets the parent CA information for a subordinate CA configuration.                                                                                                                                                                                        |
| [**SetWebCAInformation**](/windows/desktop/api/Casetup/nf-casetup-icertsrvsetup-setwebcainformation)               | Sets the CA information for the CA Web Enrollment role.                                                                                                                                                                                                   |



 

 

 
