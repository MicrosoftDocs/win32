---
title: HTTPCONTACTINFO structure
description: Contains the response information for the ListContactInfos method.
ms.assetid: 8cca7f04-da40-40a9-b58f-5393fc84cf21
keywords:
- HTTPCONTACTINFO structure Windows Mail (formerly Outlook Express)
- LPHTTPCONTACTINFO structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPCONTACTINFO
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# HTTPCONTACTINFO structure

\[**HTTPCONTACTINFO** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response information for the [**ListContactInfos**](oe-ihttpmailtransport-listcontactinfos.md) method.

## Syntax


```C++
typedef struct tagHTTPCONTACTINFO {
  LPSTR               pszHref;
  LPSTR               pszId;
  HTTPMAILCONTACTTYPE tyContact;
  LPSTR               pszModified;
  LPSTR               pszDisplayName;
  LPSTR               pszGivenName;
  LPSTR               pszSurname;
  LPSTR               pszNickname;
  LPSTR               pszEmail;
  LPSTR               pszHomeStreet;
  LPSTR               pszHomeCity;
  LPSTR               pszHomeState;
  LPSTR               pszHomePostalCode;
  LPSTR               pszHomeCountry;
  LPSTR               pszCompany;
  LPSTR               pszWorkStreet;
  LPSTR               pszWorkCity;
  LPSTR               pszWorkState;
  LPSTR               pszWorkPostalCode;
  LPSTR               pszWorkCountry;
  LPSTR               pszHomePhone;
  LPSTR               pszHomeFax;
  LPSTR               pszWorkPhone;
  LPSTR               pszWorkFax;
  LPSTR               pszMobilePhone;
  LPSTR               pszOtherPhone;
  LPSTR               pszBday;
  LPSTR               pszPager;
} HTTPCONTACTINFO, *LPHTTPCONTACTINFO;
```



## Members

<dl> <dt>

**pszHref**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the URL to this contact.

</dd> <dt>

**pszId**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the contact ID.

</dd> <dt>

**tyContact**
</dt> <dd>

Type: **[**HTTPMAILCONTACTTYPE**](oe-httpmailcontacttype.md)**

</dd> <dd>

Contains an [**HTTPMAILCONTACTTYPE**](oe-httpmailcontacttype.md) value that indicates the type of contact.

</dd> <dt>

**pszModified**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the date this contact was last updated.

</dd> <dt>

**pszDisplayName**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the display name of the contact.

</dd> <dt>

**pszGivenName**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the name of the contact.

</dd> <dt>

**pszSurname**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the surname of the contact.

</dd> <dt>

**pszNickname**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the nickname of the contact.

</dd> <dt>

**pszEmail**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the email address of the contact.

</dd> <dt>

**pszHomeStreet**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the home street address of the contact.

</dd> <dt>

**pszHomeCity**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the home city of the contact.

</dd> <dt>

**pszHomeState**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the home state or province of the contact.

</dd> <dt>

**pszHomePostalCode**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the home postal code of the contact.

</dd> <dt>

**pszHomeCountry**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the home country/region of the contact.

</dd> <dt>

**pszCompany**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the company name for the contact.

</dd> <dt>

**pszWorkStreet**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the work street address of the contact.

</dd> <dt>

**pszWorkCity**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the work city of the contact.

</dd> <dt>

**pszWorkState**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the work state or province of the contact.

</dd> <dt>

**pszWorkPostalCode**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the work postal code of the contact.

</dd> <dt>

**pszWorkCountry**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the work country/region of the contact.

</dd> <dt>

**pszHomePhone**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the home phone number of the contact.

</dd> <dt>

**pszHomeFax**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the home fax number of the contact.

</dd> <dt>

**pszWorkPhone**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the work phone number of the contact.

</dd> <dt>

**pszWorkFax**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the work fax number of the contact.

</dd> <dt>

**pszMobilePhone**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the mobile phone number of the contact.

</dd> <dt>

**pszOtherPhone**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the alternate phone number of the contact.

</dd> <dt>

**pszBday**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the birthday of the contact.

</dd> <dt>

**pszPager**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the pager number of the contact.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





