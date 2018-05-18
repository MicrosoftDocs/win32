---
title: Windows Contact Schema Overview
description: This topic defines how the contact schema is used to read and write contact properties using IContactProperties.
ms.assetid: 'c2dfb974-3c79-4656-bd63-30bfb881bd92'
keywords: ["Windows Contacts,schema", "Windows Contacts,property categories", "Windows Contacts,single-value property type", "Windows Contacts,hierarchical property type", "Windows Contacts,property extensibility", "Windows Contacts,using labels", "Windows Contacts,contacts API programming", "Windows Contacts,element definitions", "Windows Contacts,standard labels", "Windows Contacts,labels", "single-value property type", "hierarchical property type"]
---

# Windows Contact Schema Overview

This topic defines how the contact schema is used to read and write contact properties using [**IContactProperties**](-wincontacts-icontactproperties.md).

New applications should not use these interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

This topic contains the following sections:

-   [Contact Property Categories](#contact-property-categories)
-   [Contact Property Extensibility](#contact-property-extensibility)
-   [Windows Contact Schema Element Definitions](#windows-contact-schema-element-definitions)
    -   [Single-Value Properties](#single-value-properties)
    -   [Hierarchical Properties](#hierarchical-properties)
    -   [Standard Labels for Contact Properties](#standard-labels-for-contact-properties)

## Contact Property Categories

Contact properties fit into one of two categories:

-   Single-value: This property type has a single value for any contact. Birthdays are an example; a contact has only one birthday.
-   Hierarchical: This property type has multiple values for any contact and require labeling to differentiate individual values. A phone number is an example; a contact can have one or more phone numbers (home, work, and mobile phone).

## Contact Property Extensibility

Applications that use contacts may want contact data that the application-supplied schema does not provide. [**IContactProperties**](-wincontacts-icontactproperties.md) supports two approaches to extend the base contact schema:

-   *Using Labels*: For hierarchical properties, application-supplied contact array nodes can be differentiated by applying labels (arbitrary strings) to each node. For example, a phone number can be labeled with *Voice* or *Pager*. You can create custom labels or use one from the base schema. See [Standard Labels for Contact Properties](#standard-labels-for-contact-properties) below. Custom labels must be created in the form of Uniform Resource Identifiers (URIs). For more information, see [Programming Windows Contacts](-wincontacts-example-entry.md) for a code example that uses [**IContactProperties**](-wincontacts-icontactproperties.md) to set a unique label on an existing property. **IContactProperties** also provides methods to manipulate labels and to filter data to obtain a desired [**IContactPropertyCollection**](-wincontacts-icontactpropertycollection.md).
-   *Contacts API programming*: For single-value and hierarchical properties, an outside application can define new contact properties and array nodes (see [**CreateArrayNode**](-wincontacts-icontactproperties-createarraynode.md)). The data contained in these new properties can be enumerated by [**IContactProperties**](-wincontacts-icontactproperties.md) from other applications. For an example of this, see [Programming Windows Contacts](-wincontacts-example-entry.md).
    > [!Note]  
    > Developers must prefix a unique namespace (in brackets) to these new contact properties to avoid conflicts.

     

## Windows Contact Schema Element Definitions

The following elements are defined for the base schema:

### Single-Value Properties



| Property                       | Value           | Description                                                |
|--------------------------------|-----------------|------------------------------------------------------------|
| CONTACTPROP\_PUB\_GENDER       | L"Gender"       | Choose one of L"Male", L"Female", L"Unspecified" (default) |
| CONTACTPROP\_PUB\_NOTES        | L"Notes"        | Free text content in which to write notes                  |
| CONTACTPROP\_PUB\_MAILER       | L"Mailer"       | The contact's e-mail program                               |
| CONTACTPROP\_PUB\_PROGID       | L"ProgID"       | The ProgID of mailer                                       |
| CONTACTPROP\_PUB\_CREATIONDATE | L"CreationDate" | The date and time the contact was created in the system    |



 

### Hierarchical Properties

These properties contain many values differentiated by labels. To access the heirarchical properties through [**GetString**](-wincontacts-icontactproperties-getstring.md), [**GetDate**](-wincontacts-icontactproperties-getdate.md), and [**GetBinary**](-wincontacts-icontactproperties-getbinary.md) you need to provide an index (1 based). For example, a parameter in the form of L"NameCollection/Name\[1\]/Title" returns the Title string of the first Name property in the contact.



Property

Value

Description

CONTACTPROP\_PUB\_L1\_CONTACTIDS

L"ContactIDCollection"

A collection of ContactIDs associated with this contact

CONTACTPROP\_PUB\_L2\_CONTACTID

L"/ContactID"

An entry in the collection of IDs

CONTACTPROP\_PUB\_L3\_VALUE

L"/Value"

One of the unique identifiers for this contact (as a string)

CONTACTPROP\_PUB\_L1\_NAMECOLLECTION

L"NameCollection"

A collection of names associated with this contact

CONTACTPROP\_PUB\_L2\_NAME

L"/Name"

An entry in the collection of names

CONTACTPROP\_PUB\_L3\_FORMATTEDNAME

L"/FormattedName"

The name as displayed, such as "John H. Smith III"

CONTACTPROP\_PUB\_L3\_PHONETIC

L"/Phonetic""

Name as pronounced

CONTACTPROP\_PUB\_L3\_PREFIX

L"/Prefix""

A prefix to the contact name, such as "Ms."

CONTACTPROP\_PUB\_L3\_TITLE

L"/Title"

A person's title, such as "Dr."

CONTACTPROP\_PUB\_L3\_GIVENNAME

L"/GivenName"

A person's first name

CONTACTPROP\_PUB\_L3\_FAMILYNAME

L"/FamilyName"

A person's last name

CONTACTPROP\_PUB\_L3\_MIDDLENAME

L"/MiddleName"

A person's middle name

CONTACTPROP\_PUB\_L3\_GENERATION

L"/Generation"

A person's family name generation, such as "III" or "Jr."

CONTACTPROP\_PUB\_L3\_SUFFIX

L"/Suffix"

A person's credentials, such as "PhD"

CONTACTPROP\_PUB\_L3\_NICKNAME

L"/NickName"

A person's nickname, such as "Ace"

CONTACTPROP\_PUB\_L1\_POSITIONCOLLECTION

L"PositionCollection"

Collection of positions that a contact holds

CONTACTPROP\_PUB\_L2\_POSITION

L"/Position"

An entry in the collection of names

CONTACTPROP\_PUB\_L3\_ORGANIZATION

L"/Organization"

The contact's organization, such as "IEEE"

CONTACTPROP\_PUB\_L3\_COMPANY

L"/Company"

The contact's company, such as "Microsoft"

CONTACTPROP\_PUB\_L3\_DEPARTMENT

L"/Department"

The department, such as "Accounting"

CONTACTPROP\_PUB\_L3\_OFFICE

L"/Office"

The office number, such as "10/1234"

CONTACTPROP\_PUB\_L3\_JOB\_TITLE

L"/JobTitle"

Any job title, such as "Software Engineer"

CONTACTPROP\_PUB\_L3\_PROFESSION

L"/Profession"

The line of work, such as "Plumber"

CONTACTPROP\_PUB\_L3\_ROLE

L"/Role"

The role in the organization, such as "Quality Assurance"

CONTACTPROP\_PUB\_L1\_PERSONCOLLECTION

L"PersonCollection"

Collection of people associated with the contact

CONTACTPROP\_PUB\_L2\_PERSON

L"/Person"

Entry in the collection

CONTACTPROP\_PUB\_L3\_FORMATTEDNAME

L"/FormattedName"

The person's formatted (display) name

CONTACTPROP\_PUB\_L3\_PERSONID

L"/PersonID"

Unique ID for this person, which may be a ContactID from another [**IContact**](-wincontacts-icontact.md) entry

CONTACTPROP\_PUB\_L1\_DATECOLLECTION

L"DateCollection"

Collection of dates associated with the contact

CONTACTPROP\_PUB\_L2\_DATE

L"/Date"

Entry in the collection

CONTACTPROP\_PUB\_L3\_VALUE

L"/Value"

Value for this date, as a DateTime

CONTACTPROP\_PUB\_L1\_EMAILADDRESSCOLLECTION

L"EmailAddressCollection"

Collection of email addresses

CONTACTPROP\_PUB\_L2\_EMAILADDRESS

L"/EmailAddress"

Entry in the collection

CONTACTPROP\_PUB\_L3\_ADDRESS

L"/Address"

The address, such as example@microsoft.com

CONTACTPROP\_PUB\_L3\_TYPE

L"/Type"

Type of address (for example, SMTP or x509)

CONTACTPROP\_PUB\_L1\_CERTIFICATECOLLECTION

L"CertificateCollection"

Collection of certificate data and thumbprints

CONTACTPROP\_PUB\_L2\_CERTIFICATE

L"/Certificate"

Entry in the collection

CONTACTPROP\_PUB\_L3\_VALUE

L"/Value"

Certificate value

CONTACTPROP\_PUB\_L3\_THUMBPRINT

L"/ThumbPrint"

Thumbprint value

CONTACTPROP\_PUB\_L1\_PHONENUMBERCOLLECTION

L"PhoneNumberCollection"

Collection of phone numbers

CONTACTPROP\_PUB\_L2\_PHONENUMBER

L"/PhoneNumber"

Entry in the collection

CONTACTPROP\_PUB\_L3\_NUMBER

L"/Number"

Normal number to display (as string)

CONTACTPROP\_PUB\_L3\_ALTERNATE

L"/Alternate"

Alternate number (as string)

CONTACTPROP\_PUB\_L1\_PHYSICALADDRESSCOLLECTION

L"PhysicalAddressCollection"

Collection of physical addresses

CONTACTPROP\_PUB\_L2\_PHYSICALADDRESS

L"/PhysicalAddress"

Entry in the collection

CONTACTPROP\_PUB\_L3\_ADDRESSLABEL

L"/AddressLabel"

The exact data that a mailing label contains

CONTACTPROP\_PUB\_L3\_STREET

L"/Street"

Number and street

CONTACTPROP\_PUB\_L3\_LOCALITY

L"/Locality"

City or urban district

CONTACTPROP\_PUB\_L3\_REGION

L"/Region"

State or Province

CONTACTPROP\_PUB\_L3\_POSTALCODE

L"/PostalCode"

Zip or PostalCode

CONTACTPROP\_PUB\_L3\_COUNTRY

L"/Country"

The country, territory, or nation

CONTACTPROP\_PUB\_L3\_POBOX

L"/POBox"

Any POBox number

CONTACTPROP\_PUB\_L3\_EXTENDEDADDRESS

L"/ExtendedAddress"

Any extra information

CONTACTPROP\_PUB\_L1\_IMADDRESSCOLLECTION

L"IMAddressCollection"

Instant Messaging Service (IM) addresses and protocols

CONTACTPROP\_PUB\_L2\_IMADDRESSENTRY

L"/IMAddress"

Entry in the collection

CONTACTPROP\_PUB\_L3\_VALUE

L"/Value"

The identifing data (for example, username@microsoft.com)

CONTACTPROP\_PUB\_L3\_PROTOCOL

L"/Protocol"

The protocol as a string (for example, Messenger Protocol)

CONTACTPROP\_PUB\_L1\_URLCOLLECTION

L"UrlCollection"

Collection of URLs associated with this contact

CONTACTPROP\_PUB\_L2\_URL

L"/Url"

An entry in the collection of url

CONTACTPROP\_PUB\_L3\_VALUE

L"/Value"

The actual URL data (as a string)

CONTACTPROP\_PUB\_L1\_PHOTOCOLLECTION

L"PhotoCollection"

Collection of images associated with this contact

CONTACTPROP\_PUB\_L2\_PHOTO

L"/Photo"

An entry in the collection of photos

CONTACTPROP\_PUB\_L3\_VALUE

L"/Value"

Image that represents the contact (binary with MIME type)

CONTACTPROP\_PUB\_L3\_URL

L"/Url"

A URL for retrieving the image (as a string)



 

### Standard Labels for Contact Properties

These labels differentiate second level (L2) entries. For example, a company address is created by labelling a CONTACTPROP\_PUB\_L2\_PHYSICALADDRESS property as *Business*.

### Common Contact Labels



| Label                        | Value        | Description                                                      |
|------------------------------|--------------|------------------------------------------------------------------|
| CONTACTLABEL\_PUB\_PREFERRED | L"Preferred" | Note: many entries in a set may have this "Preferred" label set. |
| CONTACTLABEL\_PUB\_PERSONAL  | L"Personal"  | Home-related data                                                |
| CONTACTLABEL\_PUB\_BUSINESS  | L"Business"  | Work-related data                                                |
| CONTACTLABEL\_PUB\_OTHER     | L"Other"     | Some other label (but not a URI substitute for a label)          |



 

### PhoneNumber Labels

The following labels can be associated with PhoneNumber elements.



| Label                       | Value       | Description                               |
|-----------------------------|-------------|-------------------------------------------|
| CONTACTLABEL\_PUB\_VOICE    | L"Voice"    | A number that supports voice conversation |
| CONTACTLABEL\_PUB\_MOBILE   | L"Mobile"   | A mobile phone number                     |
| CONTACTLABEL\_PUB\_PCS      | L"PCS"      | PCS support                               |
| CONTACTLABEL\_PUB\_CELLULAR | L"Cellular" | A cell phone support                      |
| CONTACTLABEL\_PUB\_CAR      | L"Car"      | A number for travel                       |
| CONTACTLABEL\_PUB\_PAGER    | L"Pager"    | A pager number                            |
| CONTACTLABEL\_PUB\_TTY      | L"TTY"      | A tty machine                             |
| CONTACTLABEL\_PUB\_FAX      | L"Fax"      | A fax machine number                      |
| CONTACTLABEL\_PUB\_VIDEO    | L"Video"    | number supports video conversation        |
| CONTACTLABEL\_PUB\_MODEM    | L"Modem"    | A number for modem connection             |
| CONTACTLABEL\_PUB\_BBS      | L"BBS"      | A number for BBS connection               |
| CONTACTLABEL\_PUB\_ISDN     | L"ISDN"     | A number for ISDN                         |



 

### Person Labels

The following labels can be associated with Person elements. Some of these labels are specific to the Windows Address Book (WAB).



| Label                        | Value            | Description                                             |
|------------------------------|------------------|---------------------------------------------------------|
| CONTACTLABEL\_PUB\_AGENT     | L"Agent"         | This person is allowed to work on behalf of the contact |
| CONTACTLABEL\_WAB\_SPOUSE    | L"wab:Spouse"    | The contact's spouse                                    |
| CONTACTLABEL\_WAB\_CHILD     | L"wab:Child"     | A child of the contact                                  |
| CONTACTLABEL\_WAB\_MANAGER   | L"wab:Manager"   | The contact's manager                                   |
| CONTACTLABEL\_WAB\_ASSISTANT | L"wab:Assistant" | The contact's personal assistant                        |



 

### PhysicalAddress Labels

The following labels can be associated with PhysicalAddress elements.



| Label                            | Value            | Description                                   |
|----------------------------------|------------------|-----------------------------------------------|
| CONTACTLABEL\_PUB\_DOMESTIC      | L"Domestic"      | A domestic mailing address                    |
| CONTACTLABEL\_PUB\_INTERNATIONAL | L"International" | An international mailing address              |
| CONTACTLABEL\_PUB\_POSTAL        | L"Postal"        | A mailing address which accepts incoming mail |
| CONTACTLABEL\_PUB\_PARCEL        | L"Parcel"        | A mailing address that accepts packages       |



 

### Photo Labels

The following labels can be associated with Photo elements.



| Label                       | Value       | Description                                                   |
|-----------------------------|-------------|---------------------------------------------------------------|
| CONTACTLABEL\_PUB\_USERTILE | L"UserTile" | An image used to represent the contact                        |
| CONTACTLABEL\_PUB\_LOGO     | L"Logo"     | A logo (for example, to represent the contact's organization) |



 

### Date Labels

The following labels can be associated with Date elements. These labels are specific to WAB.



| Label                          | Value              | Description                  |
|--------------------------------|--------------------|------------------------------|
| CONTACTLABEL\_WAB\_BIRTHDAY    | L"wab:Birthday"    | The contact's birth date     |
| CONTACTLABEL\_WAB\_ANNIVERSARY | L"wab:Anniversary" | A date of an important event |



 

### Url Labels

The following labels can be associated with Url elements. These labels are specific to WAB.



| Label                            | Value                | Description                            |
|----------------------------------|----------------------|----------------------------------------|
| CONTACTLABEL\_WAB\_SOCIALNETWORK | L"wab:SocialNetwork" | A link to an online community          |
| CONTACTLABEL\_WAB\_SCHOOL        | L"wab:School"        | The site of an educational institution |
| CONTACTLABEL\_WAB\_WISHLIST      | L"wab:WishList"      | A page of bookmarked items             |



 

 

 




