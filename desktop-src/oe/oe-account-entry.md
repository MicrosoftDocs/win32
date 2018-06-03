---
title: New Handling for Account Data
description: New Handling for Account Data
ms.assetid: 0dab167b-78cd-4c56-a4fd-c339f74f8398
keywords:
- Windows Mail,account data
- Windows Mail,storage handling
- Outlook Express
- Windows Mail,account properties
- Windows Mail,examples
- Windows Mail,HTTPMail server types
- Windows Mail,IMAP properties
- Windows Mail,LDAP account properties
- Windows Mail,NNTP properties
- Windows Mail,POP3 properties
- Windows Mail,SMTP properties
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# New Handling for Account Data

-   [Disclaimer](#disclaimer)
-   [Introduction](#introduction)
-   [Understanding the Storage Handling Mechanism](#understanding-the-storage-handling-mechanism)
    -   [User Interface Scenario](#user-interface-scenario)
    -   [Pre-configured File Scenario](#pre-configured-file-scenario)
-   [Understanding the Account Property Data File](#understanding-the-account-property-data-file)
    -   [General Properties](#general-properties)
    -   [IMAP Properties](#imap-properties)
    -   [LDAP Properties](#ldap-properties)
    -   [NNTP Properties](#nntp-properties)
    -   [POP3 Properties](#pop3-properties)
    -   [SMTP Properties](#smtp-properties)
-   [Example Account Files](#example-account-files)
    -   [Example IMAP Mail Account File](#example-imap-mail-account-file)
    -   [Example NNTP News Account File](#example-nntp-news-account-file)
    -   [Template Account File](#template-account-file)

## Disclaimer

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

## Introduction

Windows Mail (formerly Outlook Express) for Windows Vista uses a new mechanism for storing mail, news, and directory service account data. The Windows registry no longer contains this account data; it is now stored in one or more files, each representing a user account.

Windows Mail does not support HTTPMail server types; this is a change from Microsoft Outlook Express.

## Understanding the Storage Handling Mechanism

Account property data files are located in subdirectories of the store root (%UserProfile%\\Local Settings\\Application Data\\Microsoft\\Windows Mail). Each data file has a unique name and an ".oeaccount" extension. For example, "account{4A18B81E-83CA-472A-8D7F-5301C0B97B8D}.oeaccount" could be the unique name of a news account data file located in a "Microsoft Help Groups" subdirectory of the store root. Note: a Post Office Protocol version 3 (POP3) .oeaccount file is always located in the "Local Folders" subdirectory of the store root.

There are two handling mechanisms by which an .oeaccount file could have arrived in its respective subdirectory: through the Windows Mail user interface and through the placement of pre-configured .oeaccount files in a monitored directory. The two following scenarios describe these mechanisms:

### User Interface Scenario

When a Windows Mail user adds accounts from the application's user interface, any mail, news, and directory service dialog field entries populate respective .oeaccount files for that user. Windows Mail creates and names the subdirectory into which each resulting .oeaccount file is placed. Note: .oeaccount files contain entries for only those dialog fields changed from their default values by the user.

### Pre-configured File Scenario

On system startup, Windows Mail monitors its store root for files that have an "account{XXX}.oeaccount" name and uses each such file to create a Windows Mail user account. Here, the "XXX" represents a unique string that Windows Mail uses as the name of the store root subdirectory into which the .oeaccount file is moved. Note: the exception to this subdirectory naming convention is that a POP3 .oeaccount file is always moved to the "Local Folders" subdirectory of the store root. Properties contained in the .oeaccount file populate dialog fields of that user account. When this process completes, the Windows Mail user fills in any final data, such as passwords.

Systems administrators will use this mechanism to supply correct Windows Mail account values for each user account.

See the section titled "Example Account Files" below for usage examples that illustrate this handling mechanism.

## Understanding the Account Property Data File

Accounts data entries are validated by the application using an internal array of data structures. An accounts data file contains a subset of those structure properties (name, data type, and value) in an XML form. An example data file entry is: &lt;Account\_Name type="SZ"&gt;mypop3account&lt;/Account\_Name&gt;.

The full list of accounts properties for all account types are described below:

-   Name - identifies the property. Notice that underscores are used to separate words.
-   Type - specifies the data type for this property: SZ, DWORD, or BINARY.
    -   An SZ is a string; a 0 or FALSE value represents an empty string.
    -   A DWORD is entered as a hex value with no 0x prepended to it. When a DWORD represents a true/false statement, 0 equals **FALSE** and 1 equals **TRUE**.
    -   A BINARY is a series of hexadecimal digit pairs, each representing a single character. 0 is the only valid entry for binary data within a .oeaccount file intended to be used to create a Windows Mail user account.
-   Default - specifies the default value for this property.
-   Comment - provides explanatory comments for this property.

### General Properties

The following general account property elements are defined:



| Name                       | Type  | Default | Comment                                                                              |
|----------------------------|-------|---------|--------------------------------------------------------------------------------------|
| "Account\_Name"            | SZ    | 0       | Specifies the account name. 256 character max. Required for account creation.        |
| "Temporary\_Account"       | DWORD | 0       | Specifies whether this is a temporary account.                                       |
| "Connection\_Type"         | DWORD | 0       | See [**Connection Types**](oe-connection-types.md) for possible values.             |
| "Connectoid"               | SZ    | 0       | Specifies the Remote Access Service (RAS) connection name to use. 256 character max. |
| "Connection\_Flags"        | DWORD | 0       | Specifies whether to automatically connect to server.                                |
| "Backup\_Connectoid"       | SZ    | 0       | Specifies the backup RAS connection name to use. 256 character max.                  |
| "Make\_Available\_Offline" | DWORD | 1       | Specifies whether to make account available offline.                                 |



 

### IMAP Properties

The following Internet Message Access Protocol (IMAP) account property elements are defined:



| Name                               | Type   | Default         | Comment                                                                              |
|------------------------------------|--------|-----------------|--------------------------------------------------------------------------------------|
| "IMAP\_Server"                     | SZ     | 0               | Specifies IMAP server name. 256 character max. Required for IMAP account creation.   |
| "IMAP\_User\_Name"                 | SZ     | 0               | Specifies IMAP user name. 256 character max.                                         |
| "IMAP\_Password2"                  | BINARY | 0               | Specifies IMAP password.                                                             |
| "IMAP\_Use\_Sicily"                | DWORD  | 0               | Specifies whether Secure Password Authentication (SPA) is used in authentication.    |
| "IMAP\_Port"                       | DWORD  | 8f              | Specifies TCP/IP port number. Maximum value is 0xffffffff.                           |
| "IMAP\_Secure\_Connection"         | DWORD  | 0               | Specifies whether to use a Secure Sockets Layer (SSL) connection to the IMAP server. |
| "IMAP\_Timeout"                    | DWORD  | 3c              | Specifies IMAP server timeout in seconds.                                            |
| "IMAP\_Root\_Folder"               | SZ     | 0               | Specifies user's root folder on IMAP server. 260 character max.                      |
| "IMAP\_Data\_Directory"            | SZ     | 0               | Specifies data directory for IMAP server. 260 character max.                         |
| "IMAP\_Use\_LSUB"                  | DWORD  | **TRUE**        | Specifies whether to list only subscribed mailboxes.                                 |
| "IMAP\_Polling"                    | DWORD  | **TRUE**        | Specifies whether to check periodically for messages.                                |
| "IMAP\_Svr-side\_Special\_Folders" | DWORD  | **TRUE**        | Specifies whether to store special folders on the IMAP server.                       |
| "IMAP\_Sent\_Items\_Folder"        | SZ     | "Sent Items"    | Specifies folder name. 260 character max.                                            |
| "IMAP\_Drafts\_Folder"             | SZ     | "Drafts"        | Specifies folder name. 260 character max.                                            |
| "IMAP\_Prompt\_for\_Password"      | DWORD  | **FALSE**       | Specifies whether to prompt for password.                                            |
| "IMAP\_Dirty"                      | DWORD  | 0               | See [**IMAP Dirty Flags**](oe-imap-dirty-flags.md) for valid values.                |
| "IMAP\_Poll\_All\_Folders"         | DWORD  | **TRUE**        | Specifies whether to check for new messages in all folders.                          |
| "IMAP\_Deleted\_Items\_Folder"     | SZ     | "Deleted Items" | Specifies folder name. 260 character max.                                            |
| "IMAP\_Junk\_E-mail\_Folder"       | SZ     | "Junk E-mail"   | Specifies folder name. 260 character max.                                            |



 

### LDAP Properties

The following Lightweight Directory Access Protocol (LDAP) account property elements are defined:



| Name                                 | Type   | Default | Comment                                                                                        |
|--------------------------------------|--------|---------|------------------------------------------------------------------------------------------------|
| "LDAP\_Server"                       | SZ     | 0       | Specifies LDAP server name. 256 character max. Required for LDAP account creation.             |
| "LDAP\_User\_Name"                   | SZ     | 0       | Specifies LDAP user name. 256 character max.                                                   |
| "LDAP\_Password2"                    | BINARY | 0       | Specifies LDAP password.                                                                       |
| "LDAP\_Authentication"               | DWORD  | 0       | See [**LDAP Authentication Types**](oe-ldap-authentication-types.md) for valid values.        |
| "LDAP\_Timeout"                      | DWORD  | 3c      | Specifies LDAP search timeout in seconds.                                                      |
| "LDAP\_Search\_Return"               | DWORD  | 0       | Specifies LDAP search max results returned.                                                    |
| "LDAP\_Search\_Base"                 | SZ     | 0       | Specifies LDAP search base, such as "US". 256 character max.                                   |
| "LDAP\_Server\_ID"                   | DWORD  | 0       | Specifies unique, ordered identifier for LDAP server.                                          |
| "LDAP\_Resolve\_Flag"                | DWORD  | 0       | Specifies whether LDAP server should be searched in name resolution.                           |
| "LDAP\_URL"                          | SZ     | 0       | Specifies the URL of the server's public home page. 256 character max.                         |
| "LDAP\_Port"                         | DWORD  | b9      | Specifies TCP/IP port number. Maximum value is 0xffffffff.                                     |
| "LDAP\_Secure\_Connection"           | DWORD  | 0       | Specifies whether an account requires a secure connection (SSL).                               |
| "LDAP\_Logo"                         | SZ     | 0       | Specifies path and file of image associated with server's public home page. 260 character max. |
| "LDAP\_Bind\_DN"                     | DWORD  | 0       | Specifies whether to check names against server when sending mail.                             |
| "LDAP\_Simple\_Search"               | DWORD  | 0       | Specifies whether to use the simple directory search filter.                                   |
| "LDAP\_Advanced\_Search\_Attributes" | SZ     | 0       | Specifies the search criteria for an advanced directory search. 260 character max.             |
| "LDAP\_Paged\_Result\_Support"       | DWORD  | 0       | See [**LDAP Paged Result Support Types**](oe-ldap-presult-types.md) for valid support values. |
| "LDAP\_NTDS"                         | DWORD  | 0       | See [**LDAP NTDS Types**](oe-ldap-ntds-types.md) for valid values.                            |



 

### NNTP Properties

The following Network News Transport Protocol (NNTP) account property elements are defined:



| Name                              | Type   | Default   | Comment                                                                                                         |
|-----------------------------------|--------|-----------|-----------------------------------------------------------------------------------------------------------------|
| "NNTP\_Server"                    | SZ     | 0         | Specifies NNTP server name. 256 character max. Required for NNTP account creation.                              |
| "NNTP\_User\_Name"                | SZ     | 0         | Specifies NNTP user name. 256 character max.                                                                    |
| "NNTP\_Password2"                 | BINARY | 0         | Specifies NNTP password.                                                                                        |
| "NNTP\_Use\_Sicily"               | DWORD  | 0         | Specifies whether SPA is used in authentication.                                                                |
| "NNTP\_Port"                      | DWORD  | 4d        | Specifies TCP/IP port number. Maximum value is 0xffffffff.                                                      |
| "NNTP\_Secure\_Connection"        | DWORD  | 0         | Specifies whether server requires a secure connection (SSL).                                                    |
| "NNTP\_Timeout"                   | DWORD  | 3c        | Specifies server timeout in seconds.                                                                            |
| "NNTP\_Display\_Name"             | SZ     | **FALSE** | Specifies user's display name; used for posting news.                                                           |
| "NNTP\_Organization\_Name"        | SZ     | **FALSE** | Specifies user's organization name.                                                                             |
| "NNTP\_Email\_Address"            | SZ     | **FALSE** | Specifies user's email address.                                                                                 |
| "NNTP\_Reply\_To\_Email\_Address" | DWORD  | **FALSE** | Specifies user's reply-to address.                                                                              |
| "Use\_Group\_Descriptions"        | DWORD  | **FALSE** | Specifies whether to get news group descriptions.                                                               |
| "NNTP\_Data\_Directory"           | SZ     | 0         | Specifies the data directory for the NNTP server connection. 260 character max.                                 |
| "NNTP\_Polling"                   | DWORD  | **FALSE** | Specifies whether to include this account when checking for new messages.                                       |
| "NNTP\_Posting"                   | DWORD  | 0         | See [**NNTP Post Format Types**](oe-nntp-post-format-types.md) for valid values.                               |
| "NNTP\_Signature"                 | SZ     | 0         | Specifies signature used by this account. 16 character max.                                                     |
| "NNTP\_Prompt\_for\_Password"     | DWORD  | **FALSE** | Specifies whether to prompt for password.                                                                       |
| "Communities"                     | DWORD  | 0         | Specifies whether Communities features are supported.                                                           |
| "Passport\_Member\_Name"          | SZ     | 0         | Specifies the Passport email address. 256 character max.                                                        |
| "Community\_Server\_Data"         | BINARY | 0         | Specifies non-persistent details (urls, etc.) of Communities web services for the session.                      |
| "Passport\_Session\_Data"         | BINARY | 0         | Specifies non-persistent details (Passport email address, identity handle, poster status, etc.) for a Passport. |
| "NNTP\_User\_Information\_Status" | DWORD  | 0         | See [**NNTP User Information Types**](oe-nntp-user-info-types.md) for valid values.                            |



 

### POP3 Properties

The following POP3 account property elements are defined:



| Name                          | Type   | Default   | Comment                                                                                   |
|-------------------------------|--------|-----------|-------------------------------------------------------------------------------------------|
| "POP3\_Server"                | SZ     | 0         | Specifies POP3 server name. 256 character max. Required for POP3 account creation.        |
| "POP3\_User\_Name"            | SZ     | 0         | Specifies POP3 user name. 256 character max.                                              |
| "POP3\_Password2"             | BINARY | 0         | Specifies POP3 password.                                                                  |
| "POP3\_Use\_Sicily"           | DWORD  | 0         | Specifies whether to log on using SPA.                                                    |
| "POP3\_Port"                  | DWORD  | 6e        | Specifies TCP/IP port number. Maximum value is 0xffffffff.                                |
| "POP3\_Secure\_Connection"    | DWORD  | 0         | Specifies whether server requires a secure connection (SSL).                              |
| "POP3\_Timeout"               | DWORD  | 3c        | Specifies server timeout in seconds.                                                      |
| "Leave\_Mail\_On\_Server"     | DWORD  | 0         | Specifies whether to leave mail on server.                                                |
| "Remove\_When\_Deleted"       | DWORD  | 0         | Specifies whether to delete mail from the server when it is deleted from the local store. |
| "Remove\_When\_Expired"       | DWORD  | 0         | Specifies whether to delete mail from the server when it expires.                         |
| "Expire\_Days"                | DWORD  | 0         | Specifies the number of days before mail expiration.                                      |
| "POP3\_Skip\_Account"         | DWORD  | **FALSE** | Specifies whether to not poll this server.                                                |
| "POP3\_Prompt\_for\_Password" | DWORD  | **FALSE** | Specifies whether to prompt for password. **FALSE** means remember password.              |



 

### SMTP Properties

The following Simple Mail Transport Protocol (SMTP) account property elements are defined:



| Name                              | Type   | Default   | Comment                                                                      |
|-----------------------------------|--------|-----------|------------------------------------------------------------------------------|
| "SMTP\_Server"                    | SZ     | 0         | Specifies SMTP server name. 256 character max.                               |
| "SMTP\_User\_Name"                | SZ     | 0         | Specifies SMTP user name. 256 character max.                                 |
| "SMTP\_Password2"                 | BINARY | 0         | Specifies SMTP password.                                                     |
| "SMTP\_Use\_Sicily"               | DWORD  | 0         | See [**SMTPAUTHTYPE**](oe-smtpauthtype.md) for valid values.                |
| "SMTP\_Port"                      | DWORD  | 19        | Specifies TCP/IP port number. Maximum value is 0xffffffff.                   |
| "SMTP\_Secure\_Connection"        | DWORD  | 0         | Specifies whether server requires a secure connection (SSL).                 |
| "SMTP\_Timeout"                   | DWORD  | 3c        | Specifies server timeout in seconds.                                         |
| "SMTP\_Display\_Name"             | SZ     | **FALSE** | Specifies user's display name; used for sending mail.                        |
| "SMTP\_Organization\_Name"        | SZ     | **FALSE** | Specifies user's organization name.                                          |
| "SMTP\_Email\_Address"            | SZ     | 0         | Specifies user's email address.                                              |
| "SMTP\_Reply\_To\_Email\_Address" | SZ     | **FALSE** | Specifies user's reply-to address.                                           |
| "SMTP\_Certificate"               | BINARY | 0         | Specifies signing certificate.                                               |
| "SMTP\_Signature"                 | SZ     | 0         | Specifies signature to use for this account. 16 character max.               |
| "SMTP\_Prompt\_for\_Password"     | DWORD  | **FALSE** | Specifies whether to prompt for password. **FALSE** means remember password. |
| "SMTP\_Encryption\_Certificate"   | BINARY | 0         | Specifies encryption certificate.                                            |
| "SMTP\_Encryption\_Algorithm"     | BINARY | 0         | Specifies encryption algorithm.                                              |



 

 

## Example Account Files

This section illustrates scenarios in which a systems administrator for Wingtip Toys provides setup files that simplify Windows Mail setup for an employee named Don Hall.

### Example IMAP Mail Account File

This example file is named "account{donhallimap}.oeaccount" and is placed in the store root, which is "%UserProfile%\\Local Settings\\Application Data\\Microsoft\\Windows Mail". On system startup, Windows Mail creates a "donhallimap" subdirectory in the store root, moves "account{donhallimap}.oeaccount" into that subdirectory, and creates an IMAP mail account for Don Hall.

Here, the systems administrator is supplying values for such properties as: incoming mail server, outgoing mail server, company-standard security settings and server message storage preferences, and port numbers.


```C++
<?xml version="1.0" encoding="utf-16" ?>
<MessageAccount>
    <Account_Name type="SZ">donhallimap</Account_Name>
    <Connection_Type type="DWORD">00000003</Connection_Type>
    <IMAP_Server type="SZ">mail.wingtiptoys.com</IMAP_Server>
    <IMAP_User_Name type="SZ">don</IMAP_User_Name>
    <IMAP_Use_Sicily type="DWORD">1</IMAP_Use_Sicily>
    <IMAP_Port type="DWORD">3e1</IMAP_Port>
    <IMAP_Secure_Connection type="DWORD">1</IMAP_Secure_Connection>
    <IMAP_Timeout type="DWORD">96</IMAP_Timeout>
    <IMAP_Root_Folder type="SZ">Inbox</IMAP_Root_Folder>
    <IMAP_Polling type="DWORD">1</IMAP_Polling>
    <IMAP_Svr-side_Special_Folders type="DWORD">1</IMAP_Svr-side_Special_Folders>
    <IMAP_Sent_Items_Folder type="SZ">Sent Items</IMAP_Sent_Items_Folder>
    <IMAP_Drafts_Folder type="SZ">Drafts</IMAP_Drafts_Folder>
    <IMAP_Prompt_for_Password type="DWORD">0</IMAP_Prompt_for_Password>
    <IMAP_Dirty type="DWORD">0</IMAP_Dirty>
    <IMAP_Poll_All_Folders type="DWORD">1</IMAP_Poll_All_Folders>
    <IMAP_Deleted_Items_Folder type="SZ">Deleted Items</IMAP_Deleted_Items_Folder>
    <IMAP_Junk_E-mail_Folder type="SZ">Junk E-mail</IMAP_Junk_E-mail_Folder>
    <Leave_Mail_On_Server type="DWORD">1</Leave_Mail_On_Server>
    <Remove_When_Deleted type="DWORD">1</Remove_When_Deleted>
    <Remove_When_Expired type="DWORD">1</Remove_When_Expired>
    <Expire_Days type="DWORD">5</Expire_Days>
    <SMTP_Server type="SZ">smtp.wingtiptoys.com</SMTP_Server>
    <SMTP_User_Name type="SZ">don</SMTP_User_Name>
    <SMTP_Use_Sicily type="DWORD">1</SMTP_Use_Sicily>
    <SMTP_Port type="DWORD">19</SMTP_Port>
    <SMTP_Secure_Connection type="DWORD">1</SMTP_Secure_Connection>
    <SMTP_Timeout type="DWORD">96</SMTP_Timeout>
    <SMTP_Display_Name type="SZ">Don Hall</SMTP_Display_Name>
    <SMTP_Organization_Name type="SZ">Wingtip Toys</SMTP_Organization_Name>
    <SMTP_Email_Address type="SZ">don@wingtiptoys.com</SMTP_Email_Address>
    <SMTP_Reply_To_Email_Address type="SZ">don@wingtiptoys.com</SMTP_Reply_To_Email_Address>
    <SMTP_Signature type="SZ">1</SMTP_Signature>
    <SMTP_Prompt_for_Password type="DWORD">0</SMTP_Prompt_for_Password>
</MessageAccount>
```



### Example NNTP News Account File

This example file is named "account{donhallnntp}.oeaccount" and is placed in the store root, which is "%UserProfile%\\Local Settings\\Application Data\\Microsoft\\Windows Mail". On system startup, Windows Mail creates a "donhallnntp" subdirectory in the store root, moves "account{donhallnntp}.oeaccount" into that subdirectory, and creates an NNTP news account for Don Hall.

Here, the systems administrator is supplying values for such properties as: company news server, company-standard security settings and community preferences, and port numbers.


```C++
<?xml version="1.0" encoding="utf-16" ?>
<MessageAccount>
    <Account_Name type="SZ">donhallnntp</Account_Name>
    <Connection_Type type="DWORD">00000003</Connection_Type>
    <NNTP_Server type="SZ">news.wingtiptoys.com</NNTP_Server>
    <NNTP_User_Name type="SZ">don</NNTP_User_Name>
    <NNTP_Use_Sicily type="DWORD">1</NNTP_Use_Sicily>
    <NNTP_Port type="DWORD">233</NNTP_Port>
    <NNTP_Secure_Connection type="DWORD">1</NNTP_Secure_Connection>
    <NNTP_Timeout type="DWORD">3c</NNTP_Timeout>
    <NNTP_Display_Name type="SZ">Don Hall</NNTP_Display_Name>
    <NNTP_Organization_Name type="SZ">Wingtip Toys</NNTP_Organization_Name>
    <NNTP_Email_Address type="SZ">don@wingtiptoys.com</NNTP_Email_Address>
    <NNTP_Reply_To_Email_Address type="DWORD">don@wingtiptoys.com</NNTP_Reply_To_Email_Address>
    <Use_Group_Descriptions type="DWORD">1</Use_Group_Descriptions>
    <NNTP_Polling type="DWORD">1</NNTP_Polling>
    <NNTP_Posting type="DWORD">2</NNTP_Posting>
    <NNTP_Signature type="SZ">0</NNTP_Signature>
    <NNTP_Prompt_for_Password type="DWORD">0</NNTP_Prompt_for_Password>
    <Communities type="DWORD">1</Communities>
    <Passport_Member_Name type="SZ">donh@wingtiptoysmail.com</Passport_Member_Name>
    <NNTP_User_Information_Status type="DWORD">3</NNTP_User_Information_Status>
</MessageAccount>
```



### Template Account File

This template example contains properties for all account types, with default values. It is supplied to aid you in creating your own .oeaccount files.


```C++
<?xml version="1.0" encoding="utf-16" ?>
<MessageAccount>
    <Account_Name type="SZ">0</Account_Name>
    <Temporary_Account type="DWORD">0</Temporary_Account>
    <Connection_Type type="DWORD">0</Connection_Type>
    <Connectoid type="SZ">0</Connectoid>
    <Connection_Flags type="DWORD">0</Connection_Flags>
    <Backup_Connectoid type="SZ">0</Backup_Connectoid>
    <Make_Available_Offline type="DWORD">1</Make_Available_Offline>
    <IMAP_Server type="SZ">0</IMAP_Server>
    <IMAP_User_Name type="SZ">0</IMAP_User_Name>
    <IMAP_Password2 type="BINARY">0</IMAP_Password2>
    <IMAP_Use_Sicily type="DWORD">0</IMAP_Use_Sicily>
    <IMAP_Port type="DWORD">8f</IMAP_Port>
    <IMAP_Secure_Connection type="DWORD">0</IMAP_Secure_Connection>
    <IMAP_Timeout type="DWORD">3c</IMAP_Timeout>
    <IMAP_Root_Folder type="SZ">0</IMAP_Root_Folder>
    <IMAP_Data_Directory type="SZ">0</IMAP_Data_Directory>
    <IMAP_Use_LSUB type="DWORD">TRUE</IMAP_Use_LSUB>
    <IMAP_Polling type="DWORD">TRUE</IMAP_Polling>
    <IMAP_Full_List type="DWORD">0</IMAP_Full_List>
    <IMAP_NOOP_Interval type="DWORD">0</IMAP_NOOP_Interval>
    <IMAP_Svr-side_Special_Folders type="DWORD">TRUE</IMAP_Svr-side_Special_Folders>
    <IMAP_Sent_Items_Folder type="SZ">Sent Items</IMAP_Sent_Items_Folder>
    <IMAP_Drafts_Folder type="SZ">Drafts</IMAP_Drafts_Folder>
    <IMAP_Prompt_for_Password type="DWORD">FALSE</IMAP_Prompt_for_Password>
    <IMAP_Dirty type="DWORD">0</IMAP_Dirty>
    <IMAP_Poll_All_Folders type="DWORD">TRUE</IMAP_Poll_All_Folders>
    <IMAP_Deleted_Items_Folder type="SZ">Deleted Items</IMAP_Deleted_Items_Folder>
    <IMAP_Junk_E-mail_Folder type="SZ">Junk E-mail</IMAP_Junk_E-mail_Folder>
    <LDAP_Server type="SZ">0</LDAP_Server>
    <LDAP_User_Name type="SZ">0</LDAP_User_Name>
    <LDAP_Password2 type="BINARY">0</LDAP_Password2>
    <LDAP_Authentication type="DWORD">0</LDAP_Authentication>
    <LDAP_Timeout type="DWORD">3c</LDAP_Timeout>
    <LDAP_Search_Return type="DWORD">0</LDAP_Search_Return>
    <LDAP_Search_Base type="SZ">0</LDAP_Search_Base>
    <LDAP_Server_ID type="DWORD">0</LDAP_Server_ID>
    <LDAP_Resolve_Flag type="DWORD">0</LDAP_Resolve_Flag>
    <LDAP_URL type="SZ">0</LDAP_URL>
    <LDAP_Port type="DWORD">b9</LDAP_Port>
    <LDAP_Secure_Connection type="DWORD">0</LDAP_Secure_Connection>
    <LDAP_Logo type="SZ">0</LDAP_Logo>
    <LDAP_Bind_DN type="DWORD">0</LDAP_Bind_DN>
    <LDAP_Simple_Search type="DWORD">0</LDAP_Simple_Search>
    <LDAP_Advanced_Search_Attributes type="SZ">0</LDAP_Advanced_Search_Attributes>
    <LDAP_Paged_Result_Support type="DWORD">0</LDAP_Paged_Result_Support>
    <LDAP_NTDS type="DWORD">0</LDAP_NTDS>
    <NNTP_Server type="SZ">0</NNTP_Server>
    <NNTP_User_Name type="SZ">0</NNTP_User_Name>
    <NNTP_Password2 type="BINARY">0</NNTP_Password2>
    <NNTP_Use_Sicily type="DWORD">0</NNTP_Use_Sicily>
    <NNTP_Port type="DWORD">4d</NNTP_Port>
    <NNTP_Secure_Connection type="DWORD">0</NNTP_Secure_Connection>
    <NNTP_Timeout type="DWORD">3c</NNTP_Timeout>
    <NNTP_Display_Name type="SZ">FALSE</NNTP_Display_Name>
    <NNTP_Organization_Name type="SZ">FALSE</NNTP_Organization_Name>
    <NNTP_Email_Address type="SZ">FALSE</NNTP_Email_Address>
    <NNTP_Reply_To_Email_Address type="DWORD">FALSE</NNTP_Reply_To_Email_Address>
    <Use_Group_Descriptions type="DWORD">FALSE</Use_Group_Descriptions>
    <NNTP_Data_Directory type="SZ">0</NNTP_Data_Directory>
    <NNTP_Polling type="DWORD">FALSE</NNTP_Polling>
    <NNTP_Posting type="DWORD">0</NNTP_Posting>
    <NNTP_Signature type="SZ">0</NNTP_Signature>
    <NNTP_Prompt_for_Password type="DWORD">FALSE</NNTP_Prompt_for_Password>
    <Communities type="DWORD">0</Communities>
    <Passport_Member_Name type="SZ">0</Passport_Member_Name>
    <Community_Server_Data type="BINARY">0</Community_Server_Data>
    <Passport_Session_Data type="BINARY">0</Passport_Session_Data>
    <NNTP_User_Information_Status type="DWORD">0</NNTP_User_Information_Status>
    <POP3_Server type="SZ">0</POP3_Server>
    <POP3_User_Name type="SZ">0</POP3_User_Name>
    <POP3_Password2 type="BINARY">0</POP3_Password2>
    <POP3_Use_Sicily type="DWORD">0</POP3_Use_Sicily>
    <POP3_Port type="DWORD">6e</POP3_Port>
    <POP3_Secure_Connection type="DWORD">0</POP3_Secure_Connection>
    <POP3_Timeout type="DWORD">3c</POP3_Timeout>
    <Leave_Mail_On_Server type="DWORD">0</Leave_Mail_On_Server>
    <Remove_When_Deleted type="DWORD">0</Remove_When_Deleted>
    <Remove_When_Expired type="DWORD">0</Remove_When_Expired>
    <Expire_Days type="DWORD">0</Expire_Days>
    <POP3_Skip_Account type="DWORD">FALSE</POP3_Skip_Account>
    <POP3_Prompt_for_Password type="DWORD">FALSE</POP3_Prompt_for_Password>
    <SMTP_Server type="SZ">0</SMTP_Server>
    <SMTP_User_Name type="SZ">0</SMTP_User_Name>
    <SMTP_Use_Sicily type="DWORD">0</SMTP_Use_Sicily>
    <SMTP_Port type="DWORD">19</SMTP_Port>
    <SMTP_Secure_Connection type="DWORD">0</SMTP_Secure_Connection>
    <SMTP_Timeout type="DWORD">3c</SMTP_Timeout>
    <SMTP_Display_Name type="SZ">FALSE</SMTP_Display_Name>
    <SMTP_Organization_Name type="SZ">FALSE</SMTP_Organization_Name>
    <SMTP_Email_Address type="SZ">0</SMTP_Email_Address>
    <SMTP_Reply_To_Email_Address type="SZ">FALSE</SMTP_Reply_To_Email_Address>
    <SMTP_Certificate type="BINARY">0</SMTP_Certificate>
    <SMTP_Signature type="SZ">0</SMTP_Signature>
    <SMTP_Prompt_for_Password type="DWORD">FALSE</SMTP_Prompt_for_Password>
    <SMTP_Encryption_Certificate type="BINARY">0</SMTP_Encryption_Certificate>
    <SMTP_Encryption_Algorithm type="BINARY">0</SMTP_Encryption_Algorithm>
</MessageAccount>
```



 

 




