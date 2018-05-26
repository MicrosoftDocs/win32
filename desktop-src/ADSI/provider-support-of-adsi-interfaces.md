---
title: Provider Support of ADSI Interfaces
description: The following table lists a brief description of the interfaces supported by the providers included with ADSI for Windows 2000 and DS Client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8eb9a88c-cf18-4fe4-b256-1d6fcaf96c62
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Provider Support of ADSI Interfaces ADSI
- ADSI ADSI , service providers, interfaces supported by each provider
- Provider Support for IADsUser
- Provider Support for IADsComputer
- Provider Support for IADsComputerOperations
- Provider Support for IADsDomain
- Provider Support for IADsFileService
- Provider Support for IADsGroup
- Provider Support for IADsClass
- Provider Support for IADsProperty
- Provider Support for IADsSyntax
- Provider Support for IADsContainer
- Provider Support for IADsNamespaces
- Provider Support for IADsAccessControlEntry
- Provider Support for IADsAccessControlList
- Provider Support for IADsSecurityDescriptor
- Provider Support for IADsObjectOptions
- Provider Support for IADsCollection
- Provider Support for IADsMembers
- Provider Support for IADsPathname
- Provider Support for IADsPrintQueue
- Provider Support for IADsPrintQueueOperations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Provider Support of ADSI Interfaces

The following table lists a brief description of the interfaces supported by the providers included with ADSI for Windows 2000 and DS Client. An entry marked with "Yes" indicates that at least one ADSI object of the specified provider supports the associated interface. "No" indicates that no object of the provider supports the interface in this release. In the future, currently unsupported interfaces may become supported by the system-supplied providers.

For more information about ADSI provider-specific implementation details, see:

-   [ADSI LDAP Provider](adsi-ldap-provider.md)
-   [ADSI WinNT Provider](adsi-winnt-provider.md)
-   [ADSI ROUTER](adsi-router.md)

For more information about which property or method is supported for each interface, click the appropriate interface name in the first column of the table.



| Interface Name                                                 | LDAP | WinNT |
|----------------------------------------------------------------|------|-------|
| [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master)                                           | Yes  | Yes   |
| [**IADsAccessControlEntry**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master)       | Yes  | No    |
| [**IADsAccessControlList**](/windows/win32/Iads/nn-iads-iadsaccesscontrollist?branch=master)         | Yes  | No    |
| [**IADsAcl**](/windows/win32/Iads/nn-iads-iadsacl?branch=master)                                     | No   | No    |
| [**IADsBackLink**](/windows/win32/Iads/nn-iads-iadsbacklink?branch=master)                           | No   | No    |
| [**IADsCaseIgnoreList**](/windows/win32/Iads/nn-iads-iadscaseignorelist?branch=master)               | No   | No    |
| [**IADsClass**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)                                 | Yes  | Yes   |
| [**IADsCollection**](/windows/win32/Iads/nn-iads-iadscollection?branch=master)                       | No   | Yes   |
| [**IADsComputer**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)                           | No   | Yes   |
| [**IADsComputerOperations**](/windows/win32/Iads/nn-iads-iadscomputeroperations?branch=master)       | No   | Yes   |
| [**IADsContainer**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master)                         | Yes  | Yes   |
| [**IADsDeleteOps**](/windows/win32/Iads/nn-iads-iadsdeleteops?branch=master)                         | Yes  | No    |
| [**IADsDomain**](/windows/win32/Iads/nn-iads-iadsdomain?branch=master)                               | No   | Yes   |
| [**IADsEmail**](/windows/win32/Iads/nn-iads-iadsemail?branch=master)                                 | No   | No    |
| [**IADsExtension**](/windows/win32/Iads/nn-iads-iadsextension?branch=master)                         | Yes  | Yes   |
| [**IADsFaxNumber**](/windows/win32/Iads/nn-iads-iadsfaxnumber?branch=master)                         | No   | No    |
| [**IADsFileService**](/windows/win32/Iads/nn-iads-iadsfileservice?branch=master)                     | No   | Yes   |
| [**IADsFileServiceOperations**](/windows/win32/Iads/nn-iads-iadsfileserviceoperations?branch=master) | No   | Yes   |
| [**IADsFileShare**](/windows/win32/Iads/nn-iads-iadsfileshare?branch=master)                         | No   | Yes   |
| [**IADsGroup**](/windows/win32/Iads/nn-iads-iadsgroup?branch=master)                                 | Yes  | Yes   |
| [**IADsHold**](/windows/win32/Iads/nn-iads-iadshold?branch=master)                                   | No   | No    |
| [**IADsLargeInteger**](/windows/win32/Iads/nn-iads-iadslargeinteger?branch=master)                   | Yes  | No    |
| [**IADsLocality**](/windows/win32/Iads/nn-iads-iadslocality?branch=master)                           | Yes  | No    |
| [**IADsMembers**](/windows/win32/Iads/nn-iads-iadsmembers?branch=master)                             | Yes  | Yes   |
| [**IADsNamespaces**](/windows/win32/Iads/nn-iads-iadsnamespaces?branch=master)                       | Yes  | Yes   |
| [**IADsNetAddress**](/windows/win32/Iads/nn-iads-iadsnetaddress?branch=master)                       | No   | No    |
| [**IADsO**](/windows/win32/Iads/nn-iads-iadso?branch=master)                                         | Yes  | No    |
| [**IADsObjectOptions**](/windows/win32/Iads/nn-iads-iadsobjectoptions?branch=master)                 | Yes  | No    |
| [**IADsOctetList**](/windows/win32/Iads/nn-iads-iadsoctetlist?branch=master)                         | No   | No    |
| [**IADsOpenDSObject**](/windows/win32/Iads/nn-iads-iadsopendsobject?branch=master)                   | Yes  | Yes   |
| [**IADsOU**](/windows/win32/Iads/nn-iads-iadsou?branch=master)                                       | Yes  | No    |
| [**IADsPath**](/windows/win32/Iads/nn-iads-iadspath?branch=master)                                   | No   | No    |
| [**IADsPathName**](/windows/win32/Iads/nn-iads-iadspathname?branch=master)                           | Yes  | Yes   |
| [**IADsPostalAddress**](/windows/win32/Iads/nn-iads-iadspostaladdress?branch=master)                 | No   | No    |
| [**IADsPrintJob**](/windows/win32/Iads/nn-iads-iadsprintjob?branch=master)                           | No   | Yes   |
| [**IADsPrintJobOperations**](/windows/win32/Iads/nn-iads-iadsprintjoboperations?branch=master)       | No   | Yes   |
| [**IADsPrintQueue**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)                       | Yes  | Yes   |
| [**IADsPrintQueueOperations**](/windows/win32/Iads/nn-iads-iadsprintqueueoperations?branch=master)   | Yes  | Yes   |
| [**IADsProperty**](/windows/win32/Iads/nn-iads-iadsproperty?branch=master)                           | Yes  | Yes   |
| [**IADsPropertyEntry**](/windows/win32/Iads/nn-iads-iadspropertyentry?branch=master)                 | Yes  | Yes   |
| [**IADsPropertyList**](/windows/win32/Iads/nn-iads-iadspropertylist?branch=master)                   | Yes  | Yes   |
| [**IADsPropertyValue**](/windows/win32/Iads/nn-iads-iadspropertyvalue?branch=master)                 | Yes  | Yes   |
| [**IADsPropertyValue2**](/windows/win32/Iads/nn-iads-iadspropertyvalue2?branch=master)               | Yes  | Yes   |
| [**IADsReplicaPointer**](/windows/win32/Iads/nn-iads-iadsreplicapointer?branch=master)               | No   | No    |
| [**IADsResource**](/windows/win32/Iads/nn-iads-iadsresource?branch=master)                           | No   | Yes   |
| [**IADsSecurityDescriptor**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)       | Yes  | No    |
| [**IADsService**](/windows/win32/Iads/nn-iads-iadsservice?branch=master)                             | No   | Yes   |
| [**IADsServiceOperations**](/windows/win32/Iads/nn-iads-iadsserviceoperations?branch=master)         | No   | Yes   |
| [**IADsSession**](/windows/win32/Iads/nn-iads-iadssession?branch=master)                             | No   | Yes   |
| [**IADsSyntax**](/windows/win32/Iads/nn-iads-iadssyntax?branch=master)                               | Yes  | Yes   |
| [**IADsTimestamp**](/windows/win32/Iads/nn-iads-iadstimestamp?branch=master)                         | No   | No    |
| [**IADsTypedName**](/windows/win32/Iads/nn-iads-iadstypedname?branch=master)                         | No   | No    |
| [**IADsUser**](/windows/win32/Iads/nn-iads-iadsuser?branch=master)                                   | Yes  | Yes   |
| [**IDirectoryObject**](/windows/win32/Iads/nn-iads-idirectoryobject?branch=master)                   | Yes  | No    |
| [**IDirectorySearch**](/windows/win32/Iads/nn-iads-idirectorysearch?branch=master)                   | Yes  | No    |



 

## Provider Support for IADsUser



| Property                                                    | LDAP          | WinNT         |
|-------------------------------------------------------------|---------------|---------------|
| [**AccountDisabled**](iadsuser-property-methods.md)        | Supported     | Supported     |
| [**AccountExpirationDate**](iadsuser-property-methods.md)  | Supported     | Supported     |
| [**BadLoginAddress**](iadsuser-property-methods.md)        | Unsupported   | Not supported |
| [**BadLoginCount**](iadsuser-property-methods.md)          | Supported     | Supported     |
| [**Department**](iadsuser-property-methods.md)             | Supported     | Unsupported   |
| [**Description**](iadsuser-property-methods.md)            | Supported     | Supported     |
| [**Division**](iadsuser-property-methods.md)               | Supported     | Unsupported   |
| [**EmailAddress**](iadsuser-property-methods.md)           | Supported     | Unsupported   |
| [**EmployeeID**](iadsuser-property-methods.md)             | Supported     | Unsupported   |
| [**FaxNumber**](iadsuser-property-methods.md)              | Supported     | Unsupported   |
| [**FirstName**](iadsuser-property-methods.md)              | Supported     | Unsupported   |
| [**FullName**](iadsuser-property-methods.md)               | Supported     | Supported     |
| [**GraceLoginsAllowed**](iadsuser-property-methods.md)     | Not Supported | Unsupported   |
| [**GraceLoginsRemaining**](iadsuser-property-methods.md)   | Not Supported | Unsupported   |
| [**HomeDirectory**](iadsuser-property-methods.md)          | Supported     | Supported     |
| [**HomePage**](iadsuser-property-methods.md)               | Supported     | Unsupported   |
| [**IsAccountLocked**](iadsuser-property-methods.md)        | Supported     | Supported     |
| [**Languages**](iadsuser-property-methods.md)              | Not Supported | Unsupported   |
| [**LastFailedLogin**](iadsuser-property-methods.md)        | Supported     | Unsupported   |
| [**LastLogin**](iadsuser-property-methods.md)              | Supported     | Supported     |
| [**LastLogoff**](iadsuser-property-methods.md)             | Supported     | Supported     |
| [**LastName**](iadsuser-property-methods.md)               | Supported     | Unsupported   |
| [**LoginHours**](iadsuser-property-methods.md)             | Supported     | Supported     |
| [**LoginScript**](iadsuser-property-methods.md)            | Supported     | Supported     |
| [**LoginWorkstations**](iadsuser-property-methods.md)      | Supported     | Supported     |
| [**Manager**](iadsuser-property-methods.md)                | Supported     | Unsupported   |
| [**MaxLogins**](iadsuser-property-methods.md)              | Unsupported   | Unsupported   |
| [**MaxStorage**](iadsuser-property-methods.md)             | Supported     | Supported     |
| [**NamePrefix**](iadsuser-property-methods.md)             | Supported     | Unsupported   |
| [**NameSuffix**](iadsuser-property-methods.md)             | Supported     | Unsupported   |
| [**OfficeLocations**](iadsuser-property-methods.md)        | Supported     | Unsupported   |
| [**OtherName**](iadsuser-property-methods.md)              | Supported     | Unsupported   |
| [**PasswordExpirationDate**](iadsuser-property-methods.md) | Unsupported   | Supported     |
| [**PasswordLastChanged**](iadsuser-property-methods.md)    | Supported     | Unsupported   |
| [**PasswordMinimumLength**](iadsuser-property-methods.md)  | Unsupported   | Supported     |
| [**PasswordRequired**](iadsuser-property-methods.md)       | Supported     | Supported     |
| [**Picture**](iadsuser-property-methods.md)                | Supported     | Unsupported   |
| [**PostalAddresses**](iadsuser-property-methods.md)        | Supported     | Unsupported   |
| [**PostalCodes**](iadsuser-property-methods.md)            | Supported     | Unsupported   |
| [**Profile**](iadsuser-property-methods.md)                | Supported     | Supported     |
| [**RequireUniquePassword**](iadsuser-property-methods.md)  | Unsupported   | Unsupported   |
| [**SeeAlso**](iadsuser-property-methods.md)                | Supported     | Unsupported   |
| [**TelephoneHome**](iadsuser-property-methods.md)          | Supported     | Unsupported   |
| [**TelephoneMobile**](iadsuser-property-methods.md)        | Supported     | Unsupported   |
| [**TelephoneNumber**](iadsuser-property-methods.md)        | Supported     | Unsupported   |
| [**TelephonePager**](iadsuser-property-methods.md)         | Supported     | Unsupported   |
| [**Title**](iadsuser-property-methods.md)                  | Supported     | Unsupported   |



 

## Provider Support for IADsComputer



| Properties                                     | LDAP                    | WinNT       |
|------------------------------------------------|-------------------------|-------------|
| [**ComputerID**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)             | Interface not supported | Unsupported |
| [**Department**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)             | Interface not supported | Unsupported |
| [**Description**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)            | Interface not supported | Unsupported |
| [**Division**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)               | Interface not supported | Supported   |
| [**Location**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)               | Interface not supported | Unsupported |
| [**MemorySize**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)             | Interface not supported | Unsupported |
| [**Model**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)                  | Interface not supported | Unsupported |
| [**NetAddresses**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)           | Interface not supported | Unsupported |
| [**OperatingSystem**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)        | Interface not supported | Supported   |
| [**OperatingSystemVersion**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master) | Interface not supported | Supported   |
| [**Owner**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)                  | Interface not supported | Supported   |
| [**PrimaryUser**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)            | Interface not supported | Unsupported |
| [**Processor**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)              | Interface not supported | Supported   |
| [**ProcessorCount**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)         | Interface not supported | Supported   |
| [**Role**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)                   | Interface not supported | Unsupported |
| [**Site**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)                   | Interface not supported | Unsupported |
| [**StorageCapacity**](/windows/win32/Iads/nn-iads-iadscomputer?branch=master)        | Interface not supported | Unsupported |



 

## Provider Support for IADsComputerOperations



| Property                                   | LDAP                    | WinNT           |
|--------------------------------------------|-------------------------|-----------------|
| [**Shutdown**](/windows/win32/Iads/nn-iads-iadscomputeroperations?branch=master) | Interface not supported | Not implemented |
| [**Status**](/windows/win32/Iads/nn-iads-iadscomputeroperations?branch=master)   | Interface not supported | Not implemented |



 

## Provider Support for IADsDomain



| Property                                         | LDAP                    | WinNT           |
|--------------------------------------------------|-------------------------|-----------------|
| [**IsWorkgroup**](/windows/win32/Iads/nn-iads-iadsdomain?branch=master)                | Interface not supported | Not implemented |
| [**MinPasswordLength**](/windows/win32/Iads/nn-iads-iadsdomain?branch=master)          | Interface not supported | Supported       |
| [**MinPasswordAge**](/windows/win32/Iads/nn-iads-iadsdomain?branch=master)             | Interface not supported | Supported       |
| [**MaxpasswordAge**](/windows/win32/Iads/nn-iads-iadsdomain?branch=master)             | Interface not supported | Supported       |
| [**MaxBadPasswordsAllowed**](/windows/win32/Iads/nn-iads-iadsdomain?branch=master)     | Interface not supported | Supported       |
| [**PasswordHistoryLength**](/windows/win32/Iads/nn-iads-iadsdomain?branch=master)      | Interface not supported | Supported       |
| [**PasswordAttributes**](/windows/win32/Iads/nn-iads-iadsdomain?branch=master)         | Interface not supported | Unsupported     |
| [**AutoUnlockInterval**](/windows/win32/Iads/nn-iads-iadsdomain?branch=master)         | Interface not supported | Supported       |
| [**LockoutObservationInterval**](/windows/win32/Iads/nn-iads-iadsdomain?branch=master) | Interface not supported | Supported       |



 

## Provider Support for IADsFileService



| Property                                | LDAP                    | WinNT     |
|-----------------------------------------|-------------------------|-----------|
| [**Description**](/windows/win32/Iads/nn-iads-iadsfileservice?branch=master)  | Interface not supported | Supported |
| [**MaxUserCount**](/windows/win32/Iads/nn-iads-iadsfileservice?branch=master) | Interface not supported | Supported |



 

## Provider Support for IADsGroup



| Property                         | LDAP      | WinNT     |
|----------------------------------|-----------|-----------|
| [**Description**](/windows/win32/Iads/nn-iads-iadsgroup?branch=master) | Supported | Supported |



 

## Provider Support for IADsClass



| Property                                   | LDAP               | WinNT           |
|--------------------------------------------|--------------------|-----------------|
| [**PrimaryInterface**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)      | Supported          | Supported       |
| [**CLSID**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)                 | Supported          | Supported       |
| [**OID**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)                   | Supported          | Supported       |
| [**Abstract**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)              | Supported          | Supported       |
| [**Auxiliary**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)             | Supported          | Supported       |
| [**MandatoryProperties**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)   | Supported          | Supported       |
| [**OptionalProperties**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)    | Supported          | Supported       |
| [**NamingProperties**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)      | Supported          | Not implemented |
| [**DerivedFrom**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)           | Supported          | Unsupported     |
| [**AuxDerivedFrom**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)        | Supported          | Unsupported     |
| [**PossibleSuperiors**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)     | Supported          | Supported       |
| [**Containment**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)           | Supported for read | Supported       |
| [**Container**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)             | Supported for read | Supported       |
| [**HelpFileName**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)          | Supported          | Supported       |
| [**HelpFileContext**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)       | Supported          | Supported       |
| Method                                     | LDAP               | WinNT           |
| [**Qualifiers**](/windows/win32/Iads/nf-iads-iadsclass-qualifiers?branch=master) | Not implemented    | Not implemented |



 

## Provider Support for IADsProperty



| Property                            | LDAP      | WinNT     |
|-------------------------------------|-----------|-----------|
| [**OID**](/windows/win32/Iads/nn-iads-iadsproperty?branch=master)         | Supported | Supported |
| [**Syntax**](/windows/win32/Iads/nn-iads-iadsproperty?branch=master)      | Supported | Supported |
| [**MaxRange**](/windows/win32/Iads/nn-iads-iadsproperty?branch=master)    | Supported | Supported |
| [**MinRange**](/windows/win32/Iads/nn-iads-iadsproperty?branch=master)    | Supported | Supported |
| [**Multivalued**](/windows/win32/Iads/nn-iads-iadsproperty?branch=master) | Supported | Supported |



 

## Provider Support for IADsSyntax



| Property                              | LDAP      | WinNT     |
|---------------------------------------|-----------|-----------|
| [**OleAutoDataType**](/windows/win32/Iads/nn-iads-iadssyntax?branch=master) | Supported | Supported |



 

## Provider Support for IADsContainer



| Property                        | LDAP            | WinNT           |
|---------------------------------|-----------------|-----------------|
| [**Count**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master)  | Not implemented | Not implemented |
| [**Hints**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master)  | Supported       | Not implemented |
| [**Filter**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master) | Supported       | Supported       |



 

## Provider Support for IADsNamespaces



| Property                                   | LDAP      | WinNT     |
|--------------------------------------------|-----------|-----------|
| [**defaultContainer**](/windows/win32/Iads/nn-iads-iadsnamespaces?branch=master) | Supported | Supported |



 

## Provider Support for IADsAccessControlEntry



| Property                                              | LDAP      | WinNT       |
|-------------------------------------------------------|-----------|-------------|
| [**AccessMask**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master)          | Supported | Unsupported |
| [**AccessType**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master)          | Supported | Unsupported |
| [**AccessFlags**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master)         | Supported | Unsupported |
| [**Flags**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master)               | Supported | Unsupported |
| [**ObjectType**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master)          | Supported | Unsupported |
| [**InheritedObjectType**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master) | Supported | Unsupported |
| [**Trustee**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master)             | Supported | Unsupported |



 

## Provider Support for IADsAccessControlList



| Property                                                       | LDAP      | WinNT       |
|----------------------------------------------------------------|-----------|-------------|
| [**AceCount**](/windows/win32/Iads/nn-iads-iadsaccesscontrollist?branch=master)                      | Supported | Unsupported |
| [**AceRevision**](/windows/win32/Iads/nn-iads-iadsaccesscontrollist?branch=master)                   | Supported | Unsupported |
| Method                                                         | LDAP      | WinNT       |
| [**AddAce**](/windows/win32/Iads/nf-iads-iadsaccesscontrollist-addace?branch=master)                 | Supported | Unsupported |
| [**CopyAccessList**](/windows/win32/Iads/nf-iads-iadsaccesscontrollist-copyaccesslist?branch=master) | Supported | Unsupported |
| [**RemoveAce**](/windows/win32/Iads/nf-iads-iadsaccesscontrollist-removeace?branch=master)           | Supported | Unsupported |
| [**get\_\_NewEnum**](/windows/win32/Iads/nf-iads-iadsaccesscontrollist-get__newenum?branch=master)   | Supported | Unsupported |



 

## Provider Support for IADsSecurityDescriptor



| Property                                                                        | LDAP      | WinNT       |
|---------------------------------------------------------------------------------|-----------|-------------|
| [**Control**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)                                       | Supported | Unsupported |
| [**DaclDefaulted**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)                                 | Supported | Unsupported |
| [**DiscretionaryAcl**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)                              | Supported | Unsupported |
| [**Group**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)                                         | Supported | Unsupported |
| [**GroupDefaulted**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)                                | Supported | Unsupported |
| [**Owner**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)                                         | Supported | Unsupported |
| [**OwnerDefaulted**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)                                | Supported | Unsupported |
| [**SaclDefaulted**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)                                 | Supported | Unsupported |
| [**SystemAcl**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)                                     | Supported | Unsupported |
| Method                                                                          | LDAP      | WinNT       |
| [**CopySecurityDescriptor**](/windows/win32/Iads/nf-iads-iadssecuritydescriptor-copysecuritydescriptor?branch=master) | Supported | Unsupported |



 

## Provider Support for IADsObjectOptions



| Method                                           | LDAP      | WinNT                   |
|--------------------------------------------------|-----------|-------------------------|
| [**GetOption**](/windows/win32/Iads/nf-iads-iadsobjectoptions-getoption?branch=master) | Supported | Interface not supported |
| [**SetOption**](/windows/win32/Iads/nf-iads-iadsobjectoptions-setoption?branch=master) | Supported | Interface not supported |



 

## Provider Support for IADsCollection



| Method                                                | LDAP                    | WinNT       |
|-------------------------------------------------------|-------------------------|-------------|
| [**Add**](/windows/win32/Iads/nf-iads-iadscollection-add?branch=master)                     | Interface not supported | Unsupported |
| [**get\_\_NewEnum**](/windows/win32/Iads/nf-iads-iadscollection-get__newenum?branch=master) | Interface not supported | Supported   |
| [**GetObject**](/windows/win32/Iads/nf-iads-iadscollection-getobject?branch=master)         | Interface not supported | Supported   |
| [**Remove**](/windows/win32/Iads/nf-iads-iadscollection-remove?branch=master)               | Interface not supported | Supported   |



 

## Provider Support for IADsMembers



| Property                                           | LDAP                                                      | WinNT       |
|----------------------------------------------------|-----------------------------------------------------------|-------------|
| [**Count**](/windows/win32/Iads/nn-iads-iadsmembers?branch=master)                       | Supported for GroupCollection, but not for UserCollection | Unsupported |
| [**Filter**](/windows/win32/Iads/nn-iads-iadsmembers?branch=master)                      | Supported                                                 | Supported   |
| Method                                             | LDAP                                                      | WinNT       |
| [**get\_\_NewEnum**](/windows/win32/Iads/nf-iads-iadsmembers-get__newenum?branch=master) | Supported                                                 | Supported   |



 

## Provider Support for IADsPathname



| Property                                                    | LDAP      | WinNT       |
|-------------------------------------------------------------|-----------|-------------|
| [**EscapedMode**](/windows/win32/Iads/nn-iads-iadspathname?branch=master)                         | Supported | Supported   |
| Method                                                      | LDAP      | WinNT       |
| [**Set**](/windows/win32/Iads/nf-iads-iadspathname-set?branch=master)                             | Supported | Supported   |
| [**SetDisplayType**](/windows/win32/Iads/nf-iads-iadspathname-setdisplaytype?branch=master)       | Supported | Supported   |
| [**Retrieve**](/windows/win32/Iads/nf-iads-iadspathname-retrieve?branch=master)                   | Supported | Supported   |
| [**GetNumElements**](/windows/win32/Iads/nf-iads-iadspathname-getnumelements?branch=master)       | Supported | Supported   |
| [**GetElement**](/windows/win32/Iads/nf-iads-iadspathname-getelement?branch=master)               | Supported | Supported   |
| [**GetEscapedElement**](/windows/win32/Iads/nf-iads-iadspathname-getescapedelement?branch=master) | Supported | Unsupported |
| [**RemoveLeafElement**](/windows/win32/Iads/nf-iads-iadspathname-removeleafelement?branch=master) | Supported | Supported   |
| [**CopyPath**](/windows/win32/Iads/nf-iads-iadspathname-copypath?branch=master)                   | Supported | Supported   |



 

## Provider Support for IADsPrintQueue



| Property                                     | LDAP        | WinNT       |
|----------------------------------------------|-------------|-------------|
| [**PrinterPath**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)        | Supported   | Unsupported |
| [**Model**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)              | Supported   | Supported.  |
| [**Datatype**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)           | Unsupported | Supported   |
| [**PrintProcessor**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)     | Unsupported | Supported   |
| [**Description**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)        | Supported   | Supported   |
| [**Location**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)           | Supported   | Supported   |
| [**StartTime**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)          | Supported   | Supported   |
| [**UntilTime**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)          | Supported   | Supported   |
| [**DefaultJobPriority**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master) | Unsupported | Supported   |
| [**Priority**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)           | Supported   | Supported   |
| [**BannerPage**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)         | Supported   | Supported   |
| [**PrintDevices**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)       | Supported   | Supported   |
| [**NetAddresses**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)       | Unsupported | Unsupported |



 

## Provider Support for IADsPrintQueueOperations



| Property                                                | LDAP      | WinNT      |
|---------------------------------------------------------|-----------|------------|
| [**Status**](/windows/win32/Iads/nn-iads-iadsprintqueueoperations?branch=master)              | Supported | Supported  |
| Method                                                  | LDAP      | WinNT      |
| [**Pause**](/windows/win32/Iads/nf-iads-iadsprintqueueoperations-pause?branch=master)         | Supported | Supported. |
| [**PrintJobs**](/windows/win32/Iads/nf-iads-iadsprintqueueoperations-printjobs?branch=master) | Supported | Supported  |
| [**Purge**](/windows/win32/Iads/nf-iads-iadsprintqueueoperations-purge?branch=master)         | Supported | Supported  |
| [**Resume**](/windows/win32/Iads/nf-iads-iadsprintqueueoperations-resume?branch=master)       | Supported | Supported  |



 

 

 




