---
title: Provider Support of ADSI Interfaces
description: The following table lists a brief description of the interfaces supported by the providers included with ADSI for Windows 2000 and DS Client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '8eb9a88c-cf18-4fe4-b256-1d6fcaf96c62'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Provider Support of ADSI Interfaces ADSI", "ADSI ADSI , service providers, interfaces supported by each provider", "Provider Support for IADsUser", "Provider Support for IADsComputer", "Provider Support for IADsComputerOperations", "Provider Support for IADsDomain", "Provider Support for IADsFileService", "Provider Support for IADsGroup", "Provider Support for IADsClass", "Provider Support for IADsProperty", "Provider Support for IADsSyntax", "Provider Support for IADsContainer", "Provider Support for IADsNamespaces", "Provider Support for IADsAccessControlEntry", "Provider Support for IADsAccessControlList", "Provider Support for IADsSecurityDescriptor", "Provider Support for IADsObjectOptions", "Provider Support for IADsCollection", "Provider Support for IADsMembers", "Provider Support for IADsPathname", "Provider Support for IADsPrintQueue", "Provider Support for IADsPrintQueueOperations"]
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
| [**IADs**](iads.md)                                           | Yes  | Yes   |
| [**IADsAccessControlEntry**](iadsaccesscontrolentry.md)       | Yes  | No    |
| [**IADsAccessControlList**](iadsaccesscontrollist.md)         | Yes  | No    |
| [**IADsAcl**](iadsacl.md)                                     | No   | No    |
| [**IADsBackLink**](iadsbacklink.md)                           | No   | No    |
| [**IADsCaseIgnoreList**](iadscaseignorelist.md)               | No   | No    |
| [**IADsClass**](iadsclass.md)                                 | Yes  | Yes   |
| [**IADsCollection**](iadscollection.md)                       | No   | Yes   |
| [**IADsComputer**](iadscomputer.md)                           | No   | Yes   |
| [**IADsComputerOperations**](iadscomputeroperations.md)       | No   | Yes   |
| [**IADsContainer**](iadscontainer.md)                         | Yes  | Yes   |
| [**IADsDeleteOps**](iadsdeleteops.md)                         | Yes  | No    |
| [**IADsDomain**](iadsdomain.md)                               | No   | Yes   |
| [**IADsEmail**](iadsemail.md)                                 | No   | No    |
| [**IADsExtension**](iadsextension.md)                         | Yes  | Yes   |
| [**IADsFaxNumber**](iadsfaxnumber.md)                         | No   | No    |
| [**IADsFileService**](iadsfileservice.md)                     | No   | Yes   |
| [**IADsFileServiceOperations**](iadsfileserviceoperations.md) | No   | Yes   |
| [**IADsFileShare**](iadsfileshare.md)                         | No   | Yes   |
| [**IADsGroup**](iadsgroup.md)                                 | Yes  | Yes   |
| [**IADsHold**](iadshold.md)                                   | No   | No    |
| [**IADsLargeInteger**](iadslargeinteger.md)                   | Yes  | No    |
| [**IADsLocality**](iadslocality.md)                           | Yes  | No    |
| [**IADsMembers**](iadsmembers.md)                             | Yes  | Yes   |
| [**IADsNamespaces**](iadsnamespaces.md)                       | Yes  | Yes   |
| [**IADsNetAddress**](iadsnetaddress.md)                       | No   | No    |
| [**IADsO**](iadso.md)                                         | Yes  | No    |
| [**IADsObjectOptions**](iadsobjectoptions.md)                 | Yes  | No    |
| [**IADsOctetList**](iadsoctetlist.md)                         | No   | No    |
| [**IADsOpenDSObject**](iadsopendsobject.md)                   | Yes  | Yes   |
| [**IADsOU**](iadsou.md)                                       | Yes  | No    |
| [**IADsPath**](iadspath.md)                                   | No   | No    |
| [**IADsPathName**](iadspathname.md)                           | Yes  | Yes   |
| [**IADsPostalAddress**](iadspostaladdress.md)                 | No   | No    |
| [**IADsPrintJob**](iadsprintjob.md)                           | No   | Yes   |
| [**IADsPrintJobOperations**](iadsprintjoboperations.md)       | No   | Yes   |
| [**IADsPrintQueue**](iadsprintqueue.md)                       | Yes  | Yes   |
| [**IADsPrintQueueOperations**](iadsprintqueueoperations.md)   | Yes  | Yes   |
| [**IADsProperty**](iadsproperty.md)                           | Yes  | Yes   |
| [**IADsPropertyEntry**](iadspropertyentry.md)                 | Yes  | Yes   |
| [**IADsPropertyList**](iadspropertylist.md)                   | Yes  | Yes   |
| [**IADsPropertyValue**](iadspropertyvalue.md)                 | Yes  | Yes   |
| [**IADsPropertyValue2**](iadspropertyvalue2.md)               | Yes  | Yes   |
| [**IADsReplicaPointer**](iadsreplicapointer.md)               | No   | No    |
| [**IADsResource**](iadsresource.md)                           | No   | Yes   |
| [**IADsSecurityDescriptor**](iadssecuritydescriptor.md)       | Yes  | No    |
| [**IADsService**](iadsservice.md)                             | No   | Yes   |
| [**IADsServiceOperations**](iadsserviceoperations.md)         | No   | Yes   |
| [**IADsSession**](iadssession.md)                             | No   | Yes   |
| [**IADsSyntax**](iadssyntax.md)                               | Yes  | Yes   |
| [**IADsTimestamp**](iadstimestamp.md)                         | No   | No    |
| [**IADsTypedName**](iadstypedname.md)                         | No   | No    |
| [**IADsUser**](iadsuser.md)                                   | Yes  | Yes   |
| [**IDirectoryObject**](idirectoryobject.md)                   | Yes  | No    |
| [**IDirectorySearch**](idirectorysearch.md)                   | Yes  | No    |



 

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
| [**ComputerID**](iadscomputer.md)             | Interface not supported | Unsupported |
| [**Department**](iadscomputer.md)             | Interface not supported | Unsupported |
| [**Description**](iadscomputer.md)            | Interface not supported | Unsupported |
| [**Division**](iadscomputer.md)               | Interface not supported | Supported   |
| [**Location**](iadscomputer.md)               | Interface not supported | Unsupported |
| [**MemorySize**](iadscomputer.md)             | Interface not supported | Unsupported |
| [**Model**](iadscomputer.md)                  | Interface not supported | Unsupported |
| [**NetAddresses**](iadscomputer.md)           | Interface not supported | Unsupported |
| [**OperatingSystem**](iadscomputer.md)        | Interface not supported | Supported   |
| [**OperatingSystemVersion**](iadscomputer.md) | Interface not supported | Supported   |
| [**Owner**](iadscomputer.md)                  | Interface not supported | Supported   |
| [**PrimaryUser**](iadscomputer.md)            | Interface not supported | Unsupported |
| [**Processor**](iadscomputer.md)              | Interface not supported | Supported   |
| [**ProcessorCount**](iadscomputer.md)         | Interface not supported | Supported   |
| [**Role**](iadscomputer.md)                   | Interface not supported | Unsupported |
| [**Site**](iadscomputer.md)                   | Interface not supported | Unsupported |
| [**StorageCapacity**](iadscomputer.md)        | Interface not supported | Unsupported |



 

## Provider Support for IADsComputerOperations



| Property                                   | LDAP                    | WinNT           |
|--------------------------------------------|-------------------------|-----------------|
| [**Shutdown**](iadscomputeroperations.md) | Interface not supported | Not implemented |
| [**Status**](iadscomputeroperations.md)   | Interface not supported | Not implemented |



 

## Provider Support for IADsDomain



| Property                                         | LDAP                    | WinNT           |
|--------------------------------------------------|-------------------------|-----------------|
| [**IsWorkgroup**](iadsdomain.md)                | Interface not supported | Not implemented |
| [**MinPasswordLength**](iadsdomain.md)          | Interface not supported | Supported       |
| [**MinPasswordAge**](iadsdomain.md)             | Interface not supported | Supported       |
| [**MaxpasswordAge**](iadsdomain.md)             | Interface not supported | Supported       |
| [**MaxBadPasswordsAllowed**](iadsdomain.md)     | Interface not supported | Supported       |
| [**PasswordHistoryLength**](iadsdomain.md)      | Interface not supported | Supported       |
| [**PasswordAttributes**](iadsdomain.md)         | Interface not supported | Unsupported     |
| [**AutoUnlockInterval**](iadsdomain.md)         | Interface not supported | Supported       |
| [**LockoutObservationInterval**](iadsdomain.md) | Interface not supported | Supported       |



 

## Provider Support for IADsFileService



| Property                                | LDAP                    | WinNT     |
|-----------------------------------------|-------------------------|-----------|
| [**Description**](iadsfileservice.md)  | Interface not supported | Supported |
| [**MaxUserCount**](iadsfileservice.md) | Interface not supported | Supported |



 

## Provider Support for IADsGroup



| Property                         | LDAP      | WinNT     |
|----------------------------------|-----------|-----------|
| [**Description**](iadsgroup.md) | Supported | Supported |



 

## Provider Support for IADsClass



| Property                                   | LDAP               | WinNT           |
|--------------------------------------------|--------------------|-----------------|
| [**PrimaryInterface**](iadsclass.md)      | Supported          | Supported       |
| [**CLSID**](iadsclass.md)                 | Supported          | Supported       |
| [**OID**](iadsclass.md)                   | Supported          | Supported       |
| [**Abstract**](iadsclass.md)              | Supported          | Supported       |
| [**Auxiliary**](iadsclass.md)             | Supported          | Supported       |
| [**MandatoryProperties**](iadsclass.md)   | Supported          | Supported       |
| [**OptionalProperties**](iadsclass.md)    | Supported          | Supported       |
| [**NamingProperties**](iadsclass.md)      | Supported          | Not implemented |
| [**DerivedFrom**](iadsclass.md)           | Supported          | Unsupported     |
| [**AuxDerivedFrom**](iadsclass.md)        | Supported          | Unsupported     |
| [**PossibleSuperiors**](iadsclass.md)     | Supported          | Supported       |
| [**Containment**](iadsclass.md)           | Supported for read | Supported       |
| [**Container**](iadsclass.md)             | Supported for read | Supported       |
| [**HelpFileName**](iadsclass.md)          | Supported          | Supported       |
| [**HelpFileContext**](iadsclass.md)       | Supported          | Supported       |
| Method                                     | LDAP               | WinNT           |
| [**Qualifiers**](iadsclass-qualifiers.md) | Not implemented    | Not implemented |



 

## Provider Support for IADsProperty



| Property                            | LDAP      | WinNT     |
|-------------------------------------|-----------|-----------|
| [**OID**](iadsproperty.md)         | Supported | Supported |
| [**Syntax**](iadsproperty.md)      | Supported | Supported |
| [**MaxRange**](iadsproperty.md)    | Supported | Supported |
| [**MinRange**](iadsproperty.md)    | Supported | Supported |
| [**Multivalued**](iadsproperty.md) | Supported | Supported |



 

## Provider Support for IADsSyntax



| Property                              | LDAP      | WinNT     |
|---------------------------------------|-----------|-----------|
| [**OleAutoDataType**](iadssyntax.md) | Supported | Supported |



 

## Provider Support for IADsContainer



| Property                        | LDAP            | WinNT           |
|---------------------------------|-----------------|-----------------|
| [**Count**](iadscontainer.md)  | Not implemented | Not implemented |
| [**Hints**](iadscontainer.md)  | Supported       | Not implemented |
| [**Filter**](iadscontainer.md) | Supported       | Supported       |



 

## Provider Support for IADsNamespaces



| Property                                   | LDAP      | WinNT     |
|--------------------------------------------|-----------|-----------|
| [**defaultContainer**](iadsnamespaces.md) | Supported | Supported |



 

## Provider Support for IADsAccessControlEntry



| Property                                              | LDAP      | WinNT       |
|-------------------------------------------------------|-----------|-------------|
| [**AccessMask**](iadsaccesscontrolentry.md)          | Supported | Unsupported |
| [**AccessType**](iadsaccesscontrolentry.md)          | Supported | Unsupported |
| [**AccessFlags**](iadsaccesscontrolentry.md)         | Supported | Unsupported |
| [**Flags**](iadsaccesscontrolentry.md)               | Supported | Unsupported |
| [**ObjectType**](iadsaccesscontrolentry.md)          | Supported | Unsupported |
| [**InheritedObjectType**](iadsaccesscontrolentry.md) | Supported | Unsupported |
| [**Trustee**](iadsaccesscontrolentry.md)             | Supported | Unsupported |



 

## Provider Support for IADsAccessControlList



| Property                                                       | LDAP      | WinNT       |
|----------------------------------------------------------------|-----------|-------------|
| [**AceCount**](iadsaccesscontrollist.md)                      | Supported | Unsupported |
| [**AceRevision**](iadsaccesscontrollist.md)                   | Supported | Unsupported |
| Method                                                         | LDAP      | WinNT       |
| [**AddAce**](iadsaccesscontrollist-addace.md)                 | Supported | Unsupported |
| [**CopyAccessList**](iadsaccesscontrollist-copyaccesslist.md) | Supported | Unsupported |
| [**RemoveAce**](iadsaccesscontrollist-removeace.md)           | Supported | Unsupported |
| [**get\_\_NewEnum**](iadsaccesscontrollist-get--newenum.md)   | Supported | Unsupported |



 

## Provider Support for IADsSecurityDescriptor



| Property                                                                        | LDAP      | WinNT       |
|---------------------------------------------------------------------------------|-----------|-------------|
| [**Control**](iadssecuritydescriptor.md)                                       | Supported | Unsupported |
| [**DaclDefaulted**](iadssecuritydescriptor.md)                                 | Supported | Unsupported |
| [**DiscretionaryAcl**](iadssecuritydescriptor.md)                              | Supported | Unsupported |
| [**Group**](iadssecuritydescriptor.md)                                         | Supported | Unsupported |
| [**GroupDefaulted**](iadssecuritydescriptor.md)                                | Supported | Unsupported |
| [**Owner**](iadssecuritydescriptor.md)                                         | Supported | Unsupported |
| [**OwnerDefaulted**](iadssecuritydescriptor.md)                                | Supported | Unsupported |
| [**SaclDefaulted**](iadssecuritydescriptor.md)                                 | Supported | Unsupported |
| [**SystemAcl**](iadssecuritydescriptor.md)                                     | Supported | Unsupported |
| Method                                                                          | LDAP      | WinNT       |
| [**CopySecurityDescriptor**](iadssecuritydescriptor-copysecuritydescriptor.md) | Supported | Unsupported |



 

## Provider Support for IADsObjectOptions



| Method                                           | LDAP      | WinNT                   |
|--------------------------------------------------|-----------|-------------------------|
| [**GetOption**](iadsobjectoptions-getoption.md) | Supported | Interface not supported |
| [**SetOption**](iadsobjectoptions-setoption.md) | Supported | Interface not supported |



 

## Provider Support for IADsCollection



| Method                                                | LDAP                    | WinNT       |
|-------------------------------------------------------|-------------------------|-------------|
| [**Add**](iadscollection-add.md)                     | Interface not supported | Unsupported |
| [**get\_\_NewEnum**](iadscollection-get--newenum.md) | Interface not supported | Supported   |
| [**GetObject**](iadscollection-getobject.md)         | Interface not supported | Supported   |
| [**Remove**](iadscollection-remove.md)               | Interface not supported | Supported   |



 

## Provider Support for IADsMembers



| Property                                           | LDAP                                                      | WinNT       |
|----------------------------------------------------|-----------------------------------------------------------|-------------|
| [**Count**](iadsmembers.md)                       | Supported for GroupCollection, but not for UserCollection | Unsupported |
| [**Filter**](iadsmembers.md)                      | Supported                                                 | Supported   |
| Method                                             | LDAP                                                      | WinNT       |
| [**get\_\_NewEnum**](iadsmembers-get--newenum.md) | Supported                                                 | Supported   |



 

## Provider Support for IADsPathname



| Property                                                    | LDAP      | WinNT       |
|-------------------------------------------------------------|-----------|-------------|
| [**EscapedMode**](iadspathname.md)                         | Supported | Supported   |
| Method                                                      | LDAP      | WinNT       |
| [**Set**](iadspathname-set.md)                             | Supported | Supported   |
| [**SetDisplayType**](iadspathname-setdisplaytype.md)       | Supported | Supported   |
| [**Retrieve**](iadspathname-retrieve.md)                   | Supported | Supported   |
| [**GetNumElements**](iadspathname-getnumelements.md)       | Supported | Supported   |
| [**GetElement**](iadspathname-getelement.md)               | Supported | Supported   |
| [**GetEscapedElement**](iadspathname-getescapedelement.md) | Supported | Unsupported |
| [**RemoveLeafElement**](iadspathname-removeleafelement.md) | Supported | Supported   |
| [**CopyPath**](iadspathname-copypath.md)                   | Supported | Supported   |



 

## Provider Support for IADsPrintQueue



| Property                                     | LDAP        | WinNT       |
|----------------------------------------------|-------------|-------------|
| [**PrinterPath**](iadsprintqueue.md)        | Supported   | Unsupported |
| [**Model**](iadsprintqueue.md)              | Supported   | Supported.  |
| [**Datatype**](iadsprintqueue.md)           | Unsupported | Supported   |
| [**PrintProcessor**](iadsprintqueue.md)     | Unsupported | Supported   |
| [**Description**](iadsprintqueue.md)        | Supported   | Supported   |
| [**Location**](iadsprintqueue.md)           | Supported   | Supported   |
| [**StartTime**](iadsprintqueue.md)          | Supported   | Supported   |
| [**UntilTime**](iadsprintqueue.md)          | Supported   | Supported   |
| [**DefaultJobPriority**](iadsprintqueue.md) | Unsupported | Supported   |
| [**Priority**](iadsprintqueue.md)           | Supported   | Supported   |
| [**BannerPage**](iadsprintqueue.md)         | Supported   | Supported   |
| [**PrintDevices**](iadsprintqueue.md)       | Supported   | Supported   |
| [**NetAddresses**](iadsprintqueue.md)       | Unsupported | Unsupported |



 

## Provider Support for IADsPrintQueueOperations



| Property                                                | LDAP      | WinNT      |
|---------------------------------------------------------|-----------|------------|
| [**Status**](iadsprintqueueoperations.md)              | Supported | Supported  |
| Method                                                  | LDAP      | WinNT      |
| [**Pause**](iadsprintqueueoperations-pause.md)         | Supported | Supported. |
| [**PrintJobs**](iadsprintqueueoperations-printjobs.md) | Supported | Supported  |
| [**Purge**](iadsprintqueueoperations-purge.md)         | Supported | Supported  |
| [**Resume**](iadsprintqueueoperations-resume.md)       | Supported | Supported  |



 

 

 




