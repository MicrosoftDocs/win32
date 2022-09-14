---
title: Provider Support of ADSI Interfaces
description: The following table lists a brief description of the interfaces supported by the providers included with ADSI for Windows 2000 and DS Client.
ms.assetid: 8eb9a88c-cf18-4fe4-b256-1d6fcaf96c62
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
ms.topic: article
ms.date: 05/31/2018
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
| [**IADs**](/windows/desktop/api/Iads/nn-iads-iads)                                           | Yes  | Yes   |
| [**IADsAccessControlEntry**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry)       | Yes  | No    |
| [**IADsAccessControlList**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrollist)         | Yes  | No    |
| [**IADsAcl**](/windows/desktop/api/Iads/nn-iads-iadsacl)                                     | No   | No    |
| [**IADsBackLink**](/windows/desktop/api/Iads/nn-iads-iadsbacklink)                           | No   | No    |
| [**IADsCaseIgnoreList**](/windows/desktop/api/Iads/nn-iads-iadscaseignorelist)               | No   | No    |
| [**IADsClass**](/windows/desktop/api/Iads/nn-iads-iadsclass)                                 | Yes  | Yes   |
| [**IADsCollection**](/windows/desktop/api/Iads/nn-iads-iadscollection)                       | No   | Yes   |
| [**IADsComputer**](/windows/desktop/api/Iads/nn-iads-iadscomputer)                           | No   | Yes   |
| [**IADsComputerOperations**](/windows/desktop/api/Iads/nn-iads-iadscomputeroperations)       | No   | Yes   |
| [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer)                         | Yes  | Yes   |
| [**IADsDeleteOps**](/windows/desktop/api/Iads/nn-iads-iadsdeleteops)                         | Yes  | No    |
| [**IADsDomain**](/windows/desktop/api/Iads/nn-iads-iadsdomain)                               | No   | Yes   |
| [**IADsEmail**](/windows/desktop/api/Iads/nn-iads-iadsemail)                                 | No   | No    |
| [**IADsExtension**](/windows/desktop/api/Iads/nn-iads-iadsextension)                         | Yes  | Yes   |
| [**IADsFaxNumber**](/windows/desktop/api/Iads/nn-iads-iadsfaxnumber)                         | No   | No    |
| [**IADsFileService**](/windows/desktop/api/Iads/nn-iads-iadsfileservice)                     | No   | Yes   |
| [**IADsFileServiceOperations**](/windows/desktop/api/Iads/nn-iads-iadsfileserviceoperations) | No   | Yes   |
| [**IADsFileShare**](/windows/desktop/api/Iads/nn-iads-iadsfileshare)                         | No   | Yes   |
| [**IADsGroup**](/windows/desktop/api/Iads/nn-iads-iadsgroup)                                 | Yes  | Yes   |
| [**IADsHold**](/windows/desktop/api/Iads/nn-iads-iadshold)                                   | No   | No    |
| [**IADsLargeInteger**](/windows/desktop/api/Iads/nn-iads-iadslargeinteger)                   | Yes  | No    |
| [**IADsLocality**](/windows/desktop/api/Iads/nn-iads-iadslocality)                           | Yes  | No    |
| [**IADsMembers**](/windows/desktop/api/Iads/nn-iads-iadsmembers)                             | Yes  | Yes   |
| [**IADsNamespaces**](/windows/desktop/api/Iads/nn-iads-iadsnamespaces)                       | Yes  | Yes   |
| [**IADsNetAddress**](/windows/desktop/api/Iads/nn-iads-iadsnetaddress)                       | No   | No    |
| [**IADsO**](/windows/desktop/api/Iads/nn-iads-iadso)                                         | Yes  | No    |
| [**IADsObjectOptions**](/windows/desktop/api/Iads/nn-iads-iadsobjectoptions)                 | Yes  | No    |
| [**IADsOctetList**](/windows/desktop/api/Iads/nn-iads-iadsoctetlist)                         | No   | No    |
| [**IADsOpenDSObject**](/windows/desktop/api/Iads/nn-iads-iadsopendsobject)                   | Yes  | Yes   |
| [**IADsOU**](/windows/desktop/api/Iads/nn-iads-iadsou)                                       | Yes  | No    |
| [**IADsPath**](/windows/desktop/api/Iads/nn-iads-iadspath)                                   | No   | No    |
| [**IADsPathName**](/windows/desktop/api/Iads/nn-iads-iadspathname)                           | Yes  | Yes   |
| [**IADsPostalAddress**](/windows/desktop/api/Iads/nn-iads-iadspostaladdress)                 | No   | No    |
| [**IADsPrintJob**](/windows/desktop/api/Iads/nn-iads-iadsprintjob)                           | No   | Yes   |
| [**IADsPrintJobOperations**](/windows/desktop/api/Iads/nn-iads-iadsprintjoboperations)       | No   | Yes   |
| [**IADsPrintQueue**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)                       | Yes  | Yes   |
| [**IADsPrintQueueOperations**](/windows/desktop/api/Iads/nn-iads-iadsprintqueueoperations)   | Yes  | Yes   |
| [**IADsProperty**](/windows/desktop/api/Iads/nn-iads-iadsproperty)                           | Yes  | Yes   |
| [**IADsPropertyEntry**](/windows/desktop/api/Iads/nn-iads-iadspropertyentry)                 | Yes  | Yes   |
| [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist)                   | Yes  | Yes   |
| [**IADsPropertyValue**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue)                 | Yes  | Yes   |
| [**IADsPropertyValue2**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue2)               | Yes  | Yes   |
| [**IADsReplicaPointer**](/windows/desktop/api/Iads/nn-iads-iadsreplicapointer)               | No   | No    |
| [**IADsResource**](/windows/desktop/api/Iads/nn-iads-iadsresource)                           | No   | Yes   |
| [**IADsSecurityDescriptor**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)       | Yes  | No    |
| [**IADsService**](/windows/desktop/api/Iads/nn-iads-iadsservice)                             | No   | Yes   |
| [**IADsServiceOperations**](/windows/desktop/api/Iads/nn-iads-iadsserviceoperations)         | No   | Yes   |
| [**IADsSession**](/windows/desktop/api/Iads/nn-iads-iadssession)                             | No   | Yes   |
| [**IADsSyntax**](/windows/desktop/api/Iads/nn-iads-iadssyntax)                               | Yes  | Yes   |
| [**IADsTimestamp**](/windows/desktop/api/Iads/nn-iads-iadstimestamp)                         | No   | No    |
| [**IADsTypedName**](/windows/desktop/api/Iads/nn-iads-iadstypedname)                         | No   | No    |
| [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser)                                   | Yes  | Yes   |
| [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject)                   | Yes  | No    |
| [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch)                   | Yes  | No    |



 

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
| [**ComputerID**](/windows/desktop/api/Iads/nn-iads-iadscomputer)             | Interface not supported | Unsupported |
| [**Department**](/windows/desktop/api/Iads/nn-iads-iadscomputer)             | Interface not supported | Unsupported |
| [**Description**](/windows/desktop/api/Iads/nn-iads-iadscomputer)            | Interface not supported | Unsupported |
| [**Division**](/windows/desktop/api/Iads/nn-iads-iadscomputer)               | Interface not supported | Supported   |
| [**Location**](/windows/desktop/api/Iads/nn-iads-iadscomputer)               | Interface not supported | Unsupported |
| [**MemorySize**](/windows/desktop/api/Iads/nn-iads-iadscomputer)             | Interface not supported | Unsupported |
| [**Model**](/windows/desktop/api/Iads/nn-iads-iadscomputer)                  | Interface not supported | Unsupported |
| [**NetAddresses**](/windows/desktop/api/Iads/nn-iads-iadscomputer)           | Interface not supported | Unsupported |
| [**OperatingSystem**](/windows/desktop/api/Iads/nn-iads-iadscomputer)        | Interface not supported | Supported   |
| [**OperatingSystemVersion**](/windows/desktop/api/Iads/nn-iads-iadscomputer) | Interface not supported | Supported   |
| [**Owner**](/windows/desktop/api/Iads/nn-iads-iadscomputer)                  | Interface not supported | Supported   |
| [**PrimaryUser**](/windows/desktop/api/Iads/nn-iads-iadscomputer)            | Interface not supported | Unsupported |
| [**Processor**](/windows/desktop/api/Iads/nn-iads-iadscomputer)              | Interface not supported | Supported   |
| [**ProcessorCount**](/windows/desktop/api/Iads/nn-iads-iadscomputer)         | Interface not supported | Supported   |
| [**Role**](/windows/desktop/api/Iads/nn-iads-iadscomputer)                   | Interface not supported | Unsupported |
| [**Site**](/windows/desktop/api/Iads/nn-iads-iadscomputer)                   | Interface not supported | Unsupported |
| [**StorageCapacity**](/windows/desktop/api/Iads/nn-iads-iadscomputer)        | Interface not supported | Unsupported |



 

## Provider Support for IADsComputerOperations



| Property                                   | LDAP                    | WinNT           |
|--------------------------------------------|-------------------------|-----------------|
| [**Shutdown**](/windows/desktop/api/Iads/nn-iads-iadscomputeroperations) | Interface not supported | Not implemented |
| [**Status**](/windows/desktop/api/Iads/nn-iads-iadscomputeroperations)   | Interface not supported | Not implemented |



 

## Provider Support for IADsDomain



| Property                                         | LDAP                    | WinNT           |
|--------------------------------------------------|-------------------------|-----------------|
| [**IsWorkgroup**](/windows/desktop/api/Iads/nn-iads-iadsdomain)                | Interface not supported | Not implemented |
| [**MinPasswordLength**](/windows/desktop/api/Iads/nn-iads-iadsdomain)          | Interface not supported | Supported       |
| [**MinPasswordAge**](/windows/desktop/api/Iads/nn-iads-iadsdomain)             | Interface not supported | Supported       |
| [**MaxpasswordAge**](/windows/desktop/api/Iads/nn-iads-iadsdomain)             | Interface not supported | Supported       |
| [**MaxBadPasswordsAllowed**](/windows/desktop/api/Iads/nn-iads-iadsdomain)     | Interface not supported | Supported       |
| [**PasswordHistoryLength**](/windows/desktop/api/Iads/nn-iads-iadsdomain)      | Interface not supported | Supported       |
| [**PasswordAttributes**](/windows/desktop/api/Iads/nn-iads-iadsdomain)         | Interface not supported | Unsupported     |
| [**AutoUnlockInterval**](/windows/desktop/api/Iads/nn-iads-iadsdomain)         | Interface not supported | Supported       |
| [**LockoutObservationInterval**](/windows/desktop/api/Iads/nn-iads-iadsdomain) | Interface not supported | Supported       |



 

## Provider Support for IADsFileService



| Property                                | LDAP                    | WinNT     |
|-----------------------------------------|-------------------------|-----------|
| [**Description**](/windows/desktop/api/Iads/nn-iads-iadsfileservice)  | Interface not supported | Supported |
| [**MaxUserCount**](/windows/desktop/api/Iads/nn-iads-iadsfileservice) | Interface not supported | Supported |



 

## Provider Support for IADsGroup



| Property                         | LDAP      | WinNT     |
|----------------------------------|-----------|-----------|
| [**Description**](/windows/desktop/api/Iads/nn-iads-iadsgroup) | Supported | Supported |



 

## Provider Support for IADsClass



| Property                                   | LDAP               | WinNT           |
|--------------------------------------------|--------------------|-----------------|
| [**PrimaryInterface**](/windows/desktop/api/Iads/nn-iads-iadsclass)      | Supported          | Supported       |
| [**CLSID**](/windows/desktop/api/Iads/nn-iads-iadsclass)                 | Supported          | Supported       |
| [**OID**](/windows/desktop/api/Iads/nn-iads-iadsclass)                   | Supported          | Supported       |
| [**Abstract**](/windows/desktop/api/Iads/nn-iads-iadsclass)              | Supported          | Supported       |
| [**Auxiliary**](/windows/desktop/api/Iads/nn-iads-iadsclass)             | Supported          | Supported       |
| [**MandatoryProperties**](/windows/desktop/api/Iads/nn-iads-iadsclass)   | Supported          | Supported       |
| [**OptionalProperties**](/windows/desktop/api/Iads/nn-iads-iadsclass)    | Supported          | Supported       |
| [**NamingProperties**](/windows/desktop/api/Iads/nn-iads-iadsclass)      | Supported          | Not implemented |
| [**DerivedFrom**](/windows/desktop/api/Iads/nn-iads-iadsclass)           | Supported          | Unsupported     |
| [**AuxDerivedFrom**](/windows/desktop/api/Iads/nn-iads-iadsclass)        | Supported          | Unsupported     |
| [**PossibleSuperiors**](/windows/desktop/api/Iads/nn-iads-iadsclass)     | Supported          | Supported       |
| [**Containment**](/windows/desktop/api/Iads/nn-iads-iadsclass)           | Supported for read | Supported       |
| [**Container**](/windows/desktop/api/Iads/nn-iads-iadsclass)             | Supported for read | Supported       |
| [**HelpFileName**](/windows/desktop/api/Iads/nn-iads-iadsclass)          | Supported          | Supported       |
| [**HelpFileContext**](/windows/desktop/api/Iads/nn-iads-iadsclass)       | Supported          | Supported       |
| Method                                     | LDAP               | WinNT           |
| [**Qualifiers**](/windows/desktop/api/Iads/nf-iads-iadsclass-qualifiers) | Not implemented    | Not implemented |



 

## Provider Support for IADsProperty



| Property                            | LDAP      | WinNT     |
|-------------------------------------|-----------|-----------|
| [**OID**](/windows/desktop/api/Iads/nn-iads-iadsproperty)         | Supported | Supported |
| [**Syntax**](/windows/desktop/api/Iads/nn-iads-iadsproperty)      | Supported | Supported |
| [**MaxRange**](/windows/desktop/api/Iads/nn-iads-iadsproperty)    | Supported | Supported |
| [**MinRange**](/windows/desktop/api/Iads/nn-iads-iadsproperty)    | Supported | Supported |
| [**Multivalued**](/windows/desktop/api/Iads/nn-iads-iadsproperty) | Supported | Supported |



 

## Provider Support for IADsSyntax



| Property                              | LDAP      | WinNT     |
|---------------------------------------|-----------|-----------|
| [**OleAutoDataType**](/windows/desktop/api/Iads/nn-iads-iadssyntax) | Supported | Supported |



 

## Provider Support for IADsContainer



| Property                        | LDAP            | WinNT           |
|---------------------------------|-----------------|-----------------|
| [**Count**](/windows/desktop/api/Iads/nn-iads-iadscontainer)  | Not implemented | Not implemented |
| [**Hints**](/windows/desktop/api/Iads/nn-iads-iadscontainer)  | Supported       | Not implemented |
| [**Filter**](/windows/desktop/api/Iads/nn-iads-iadscontainer) | Supported       | Supported       |



 

## Provider Support for IADsNamespaces



| Property                                   | LDAP      | WinNT     |
|--------------------------------------------|-----------|-----------|
| [**defaultContainer**](/windows/desktop/api/Iads/nn-iads-iadsnamespaces) | Supported | Supported |



 

## Provider Support for IADsAccessControlEntry



| Property                                              | LDAP      | WinNT       |
|-------------------------------------------------------|-----------|-------------|
| [**AccessMask**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry)          | Supported | Unsupported |
| [**AccessType**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry)          | Supported | Unsupported |
| [**AccessFlags**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry)         | Supported | Unsupported |
| [**Flags**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry)               | Supported | Unsupported |
| [**ObjectType**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry)          | Supported | Unsupported |
| [**InheritedObjectType**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry) | Supported | Unsupported |
| [**Trustee**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry)             | Supported | Unsupported |



 

## Provider Support for IADsAccessControlList



| Property                                                       | LDAP      | WinNT       |
|----------------------------------------------------------------|-----------|-------------|
| [**AceCount**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrollist)                      | Supported | Unsupported |
| [**AceRevision**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrollist)                   | Supported | Unsupported |
| Method                                                         | LDAP      | WinNT       |
| [**AddAce**](/windows/desktop/api/Iads/nf-iads-iadsaccesscontrollist-addace)                 | Supported | Unsupported |
| [**CopyAccessList**](/windows/desktop/api/Iads/nf-iads-iadsaccesscontrollist-copyaccesslist) | Supported | Unsupported |
| [**RemoveAce**](/windows/desktop/api/Iads/nf-iads-iadsaccesscontrollist-removeace)           | Supported | Unsupported |
| [**get\_\_NewEnum**](/windows/desktop/api/Iads/nf-iads-iadsaccesscontrollist-get__newenum)   | Supported | Unsupported |



 

## Provider Support for IADsSecurityDescriptor



| Property                                                                        | LDAP      | WinNT       |
|---------------------------------------------------------------------------------|-----------|-------------|
| [**Control**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)                                       | Supported | Unsupported |
| [**DaclDefaulted**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)                                 | Supported | Unsupported |
| [**DiscretionaryAcl**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)                              | Supported | Unsupported |
| [**Group**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)                                         | Supported | Unsupported |
| [**GroupDefaulted**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)                                | Supported | Unsupported |
| [**Owner**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)                                         | Supported | Unsupported |
| [**OwnerDefaulted**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)                                | Supported | Unsupported |
| [**SaclDefaulted**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)                                 | Supported | Unsupported |
| [**SystemAcl**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)                                     | Supported | Unsupported |
| Method                                                                          | LDAP      | WinNT       |
| [**CopySecurityDescriptor**](/windows/desktop/api/Iads/nf-iads-iadssecuritydescriptor-copysecuritydescriptor) | Supported | Unsupported |



 

## Provider Support for IADsObjectOptions



| Method                                           | LDAP      | WinNT                   |
|--------------------------------------------------|-----------|-------------------------|
| [**GetOption**](/windows/desktop/api/Iads/nf-iads-iadsobjectoptions-getoption) | Supported | Interface not supported |
| [**SetOption**](/windows/desktop/api/Iads/nf-iads-iadsobjectoptions-setoption) | Supported | Interface not supported |



 

## Provider Support for IADsCollection



| Method                                                | LDAP                    | WinNT       |
|-------------------------------------------------------|-------------------------|-------------|
| [**Add**](/windows/desktop/api/Iads/nf-iads-iadscollection-add)                     | Interface not supported | Unsupported |
| [**get\_\_NewEnum**](/windows/desktop/api/Iads/nf-iads-iadscollection-get__newenum) | Interface not supported | Supported   |
| [**GetObject**](/windows/desktop/api/Iads/nf-iads-iadscollection-getobject)         | Interface not supported | Supported   |
| [**Remove**](/windows/desktop/api/Iads/nf-iads-iadscollection-remove)               | Interface not supported | Supported   |



 

## Provider Support for IADsMembers



| Property                                           | LDAP                                                      | WinNT       |
|----------------------------------------------------|-----------------------------------------------------------|-------------|
| [**Count**](/windows/desktop/api/Iads/nn-iads-iadsmembers)                       | Supported for GroupCollection, but not for UserCollection | Unsupported |
| [**Filter**](/windows/desktop/api/Iads/nn-iads-iadsmembers)                      | Supported                                                 | Supported   |
| Method                                             | LDAP                                                      | WinNT       |
| [**get\_\_NewEnum**](/windows/desktop/api/Iads/nf-iads-iadsmembers-get__newenum) | Supported                                                 | Supported   |



 

## Provider Support for IADsPathname



| Property                                                    | LDAP      | WinNT       |
|-------------------------------------------------------------|-----------|-------------|
| [**EscapedMode**](/windows/desktop/api/Iads/nn-iads-iadspathname)                         | Supported | Supported   |
| Method                                                      | LDAP      | WinNT       |
| [**Set**](/windows/desktop/api/Iads/nf-iads-iadspathname-set)                             | Supported | Supported   |
| [**SetDisplayType**](/windows/desktop/api/Iads/nf-iads-iadspathname-setdisplaytype)       | Supported | Supported   |
| [**Retrieve**](/windows/desktop/api/Iads/nf-iads-iadspathname-retrieve)                   | Supported | Supported   |
| [**GetNumElements**](/windows/desktop/api/Iads/nf-iads-iadspathname-getnumelements)       | Supported | Supported   |
| [**GetElement**](/windows/desktop/api/Iads/nf-iads-iadspathname-getelement)               | Supported | Supported   |
| [**GetEscapedElement**](/windows/desktop/api/Iads/nf-iads-iadspathname-getescapedelement) | Supported | Unsupported |
| [**RemoveLeafElement**](/windows/desktop/api/Iads/nf-iads-iadspathname-removeleafelement) | Supported | Supported   |
| [**CopyPath**](/windows/desktop/api/Iads/nf-iads-iadspathname-copypath)                   | Supported | Supported   |



 

## Provider Support for IADsPrintQueue



| Property                                     | LDAP        | WinNT       |
|----------------------------------------------|-------------|-------------|
| [**PrinterPath**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)        | Supported   | Unsupported |
| [**Model**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)              | Supported   | Supported.  |
| [**Datatype**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)           | Unsupported | Supported   |
| [**PrintProcessor**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)     | Unsupported | Supported   |
| [**Description**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)        | Supported   | Supported   |
| [**Location**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)           | Supported   | Supported   |
| [**StartTime**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)          | Supported   | Supported   |
| [**UntilTime**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)          | Supported   | Supported   |
| [**DefaultJobPriority**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue) | Unsupported | Supported   |
| [**Priority**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)           | Supported   | Supported   |
| [**BannerPage**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)         | Supported   | Supported   |
| [**PrintDevices**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)       | Supported   | Supported   |
| [**NetAddresses**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)       | Unsupported | Unsupported |



 

## Provider Support for IADsPrintQueueOperations



| Property                                                | LDAP      | WinNT      |
|---------------------------------------------------------|-----------|------------|
| [**Status**](/windows/desktop/api/Iads/nn-iads-iadsprintqueueoperations)              | Supported | Supported  |
| Method                                                  | LDAP      | WinNT      |
| [**Pause**](/windows/desktop/api/Iads/nf-iads-iadsprintqueueoperations-pause)         | Supported | Supported. |
| [**PrintJobs**](/windows/desktop/api/Iads/nf-iads-iadsprintqueueoperations-printjobs) | Supported | Supported  |
| [**Purge**](/windows/desktop/api/Iads/nf-iads-iadsprintqueueoperations-purge)         | Supported | Supported  |
| [**Resume**](/windows/desktop/api/Iads/nf-iads-iadsprintqueueoperations-resume)       | Supported | Supported  |



 

 

 




