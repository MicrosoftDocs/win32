---
Description: The following methods are defined by the ICertSrvSetup interface. The property access methods are not shown here. To see the properties for ICertSrvSetup, see Properties of ICertSrvSetup.
ms.assetid: cb7f288b-30a0-4c3b-b7bc-3055166d2302
title: Methods of ICertSrvSetup
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Methods of ICertSrvSetup

The following methods are defined by the [**ICertSrvSetup**](/windows/win32/Casetup/nn-casetup-icertsrvsetup?branch=master) interface. The property access methods are not shown here. To see the properties for **ICertSrvSetup**, see [Properties of ICertSrvSetup](properties-of-icertsrvsetup.md).



| Method                                                                         | Description                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CAImportPFX**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-caimportpfx?branch=master)                               | Imports a Certification Authority (CA) certificate and its associated private key into the "LocalMachine" store.                                                                                                                                          |
| [**GetCASetupProperty**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-getcasetupproperty?branch=master)                 | Gets a property value for a CA configuration.                                                                                                                                                                                                             |
| [**GetExistingCACertificates**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-getexistingcacertificates?branch=master)   | Gets the collection of **CCertSrvSetupKeyInformation** objects that represent valid CA certificates currently installed on the computer.                                                                                                                  |
| [**GetHashAlgorithmList**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-gethashalgorithmlist?branch=master)             | Gets the list of hash algorithms supported by the specified [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) for an asymmetric key signature algorithm. |
| [**GetKeyLengthList**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-getkeylengthlist?branch=master)                     | Gets the list of key lengths supported by the specified CSP.                                                                                                                                                                                              |
| [**GetPrivateKeyContainerList**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-getprivatekeycontainerlist?branch=master) | Gets the list of key container names stored by the specified CSP for asymmetric signature key algorithms.                                                                                                                                                 |
| [**GetProviderNameList**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-getprovidernamelist?branch=master)               | Gets the list of CSPs that provide asymmetric key signature algorithms on the computer.                                                                                                                                                                   |
| [**GetSupportedCATypes**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-getsupportedcatypes?branch=master)               | Gets the types of CAs that can be installed on a computer under the caller context.                                                                                                                                                                       |
| [**InitializeDefaults**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-initializedefaults?branch=master)                 | Initializes a **CCertSrvSetup** object with default values to enable installation of a CA role.                                                                                                                                                           |
| [**Install**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-install?branch=master)                                       | Installs a CA role as configured in the **CCertSrvSetup** object.                                                                                                                                                                                         |
| [**IsPropertyEditable**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-ispropertyeditable?branch=master)                 | Indicates to the caller whether a specified property can be edited.                                                                                                                                                                                       |
| [**PostUnInstall**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-postuninstall?branch=master)                           | Is not implemented and is reserved for future use.                                                                                                                                                                                                        |
| [**PreUnInstall**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-preuninstall?branch=master)                             | Temporarily saves role-specific state-information.                                                                                                                                                                                                        |
| [**SetCADistinguishedName**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-setcadistinguishedname?branch=master)         | Sets a CA common name and an optional distinguished name suffix.                                                                                                                                                                                          |
| [**SetCASetupProperty**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-setcasetupproperty?branch=master)                 | Sets a property value for a CA configuration.                                                                                                                                                                                                             |
| [**SetDatabaseInformation**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-setdatabaseinformation?branch=master)         | Sets the database related information for the CA role.                                                                                                                                                                                                    |
| [**SetParentCAInformation**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-setparentcainformation?branch=master)         | Sets the parent CA information for a subordinate CA configuration.                                                                                                                                                                                        |
| [**SetWebCAInformation**](/windows/win32/Casetup/nf-casetup-icertsrvsetup-setwebcainformation?branch=master)               | Sets the CA information for the CA Web Enrollment role.                                                                                                                                                                                                   |



 

 

 



