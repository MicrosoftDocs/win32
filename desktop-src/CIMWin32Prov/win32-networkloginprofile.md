---
description: The Win32\_NetworkLoginProfile&\#8194;WMI class represents the network login information of a specific user on a computer system running Windows.
ms.assetid: e5a8e934-d5a7-43fa-b140-c3cca972590f
ms.tgt_platform: multiple
title: Win32_NetworkLoginProfile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkLoginProfile
- Win32_NetworkLoginProfile.Caption
- Win32_NetworkLoginProfile.Description
- Win32_NetworkLoginProfile.SettingID
- Win32_NetworkLoginProfile.AccountExpires
- Win32_NetworkLoginProfile.AuthorizationFlags
- Win32_NetworkLoginProfile.BadPasswordCount
- Win32_NetworkLoginProfile.CodePage
- Win32_NetworkLoginProfile.Comment
- Win32_NetworkLoginProfile.CountryCode
- Win32_NetworkLoginProfile.Flags
- Win32_NetworkLoginProfile.FullName
- Win32_NetworkLoginProfile.HomeDirectory
- Win32_NetworkLoginProfile.HomeDirectoryDrive
- Win32_NetworkLoginProfile.LastLogoff
- Win32_NetworkLoginProfile.LastLogon
- Win32_NetworkLoginProfile.LogonHours
- Win32_NetworkLoginProfile.LogonServer
- Win32_NetworkLoginProfile.MaximumStorage
- Win32_NetworkLoginProfile.Name
- Win32_NetworkLoginProfile.NumberOfLogons
- Win32_NetworkLoginProfile.Parameters
- Win32_NetworkLoginProfile.PasswordAge
- Win32_NetworkLoginProfile.PasswordExpires
- Win32_NetworkLoginProfile.PrimaryGroupId
- Win32_NetworkLoginProfile.Privileges
- Win32_NetworkLoginProfile.Profile
- Win32_NetworkLoginProfile.ScriptPath
- Win32_NetworkLoginProfile.UnitsPerWeek
- Win32_NetworkLoginProfile.UserComment
- Win32_NetworkLoginProfile.UserId
- Win32_NetworkLoginProfile.UserType
- Win32_NetworkLoginProfile.Workstations
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_NetworkLoginProfile class

The **Win32\_NetworkLoginProfile** [WMI class](../wmisdk/retrieving-a-class.md) represents the network login information of a specific user on a computer system running Windows. This includes, but is not limited to password status, access privileges, disk quotas, and logon directory paths.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), Privileges("SeRestorePrivilege"), UUID("{8502C4E7-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_NetworkLoginProfile : CIM_Setting
{
  string   Caption;
  string   Description;
  string   SettingID;
  datetime AccountExpires;
  uint32   AuthorizationFlags;
  uint32   BadPasswordCount;
  uint32   CodePage;
  string   Comment;
  uint32   CountryCode;
  uint32   Flags;
  string   FullName;
  string   HomeDirectory;
  string   HomeDirectoryDrive;
  datetime LastLogoff;
  datetime LastLogon;
  string   LogonHours;
  string   LogonServer;
  uint64   MaximumStorage;
  string   Name;
  uint32   NumberOfLogons;
  string   Parameters;
  datetime PasswordAge;
  datetime PasswordExpires;
  uint32   PrimaryGroupId;
  uint32   Privileges;
  string   Profile;
  string   ScriptPath;
  uint32   UnitsPerWeek;
  string   UserComment;
  uint32   UserId;
  string   UserType;
  string   Workstations;
};
```

## Members

The **Win32\_NetworkLoginProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NetworkLoginProfile** class has these properties.

<dl> <dt>

**AccountExpires**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_acct\_expires")
</dt> </dl>

Account will expire. This value is calculated from the number of seconds elapsed since 00:00:00, January 1, 1970, and is set in this format: yyyymmddhhmmss.mmmmmm sutc.

Example: 20521201000230.000000 000

</dd> <dt>

**AuthorizationFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_auth\_flags"), [**BitValues**](../wmisdk/standard-qualifiers.md) ("Printer", "Communication", "Server", "Accounts")
</dt> </dl>

Set of flags that specify the resources a user is authorized to use or modify.

<dt>

1 (0x1)
</dt> <dd>

Printer

</dd> <dt>

2 (0x2)
</dt> <dd>

Communication

</dd> <dt>

4 (0x4)
</dt> <dd>

Server

</dd> <dt>

8 (0x8)
</dt> <dd>

Accounts

</dd> </dl>

</dd> <dt>

**BadPasswordCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Functions\|NetUserEnum")
</dt> </dl>

Number of times the user enters a bad password when logging on to a computer system running Windows.

Example: 0

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64)
</dt> </dl>

Short textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**CodePage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_code\_page")
</dt> </dl>

Code page for the user's language of choice. A code page is the character set used.

</dd> <dt>

**Comment**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_comment")
</dt> </dl>

Comment or description for this logon profile.

</dd> <dt>

**CountryCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_country\_code")
</dt> </dl>

Country/region code for the user's language of choice.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_flags"), [**BitMap**](../wmisdk/standard-qualifiers.md) ("0", "1", "3", "4", "5", "6", "7", "8", "9", "11", "12", "13", "16", "17", "18", "19", "20", "21", "22", "23"), [**BitValues**](../wmisdk/standard-qualifiers.md) ("Script", "Account Disabled", "Home Dir Required", "Lockout", "Password Not Required", "Paswword Can't Change", "Encrypted Test Password Allowed", "Temp Duplicate Account", "Normal Account", "InterDomain Trust Account", "WorkStation Trust Account", "Server Trust Account", "Don't Expire Password", "MNS Logon Account", "Smartcard Required", "Trusted For Delegation", "Not Delegated", "Use DES Key Only", "Don't Require Preauthorization", "Password Expired")
</dt> </dl>

The properties available to this network profile.

Properties that can be set include:

<dt>

1 (0x1)
</dt> <dd>

Script

A logon script executed. This value must be set for LAN Manager 2.0.

</dd> <dt>

2 (0x2)
</dt> <dd>

Account Disabled

The user's account is disabled.

</dd> <dt>

8 (0x8)
</dt> <dd>

Home Directory Required

A home directory is required.

</dd> <dt>

16 (0x10)
</dt> <dd>

Lockout

The account is currently locked out. For [**NetUserSetInfo**](/windows/win32/api/lmaccess/nf-lmaccess-netusersetinfo), this value can be cleared to unlock a previously locked account. This value cannot be used to lock a previously unlocked account.

</dd> <dt>

32 (0x20)
</dt> <dd>

Password Not Required

No password is required.

</dd> <dt>

64 (0x40)
</dt> <dd>

Password Cannot Change

The user cannot change the password.

</dd> <dt>

128 (0x80)
</dt> <dd>

Encrypted Test Password Allowed

</dd> <dt>

256 (0x100)
</dt> <dd>

Temp Duplicate Account

An account for users whose primary account is in another domain. This account provides user access to this domain, but not to any domain that trusts this domain. The User Manager refers to this account type as a local user account.

</dd> <dt>

512 (0x200)
</dt> <dd>

Normal Account

Default account type that represents a typical user.

</dd> <dt>

2048 (0x800)
</dt> <dd>

Interdomain Trust Account

A permit to a trust account for a domain that trusts other domains.

</dd> <dt>

4096 (0x1000)
</dt> <dd>

Workstation Trust Account

A computer account for a Windows workstation or server that is a member of this domain.

</dd> <dt>

8192 (0x2000)
</dt> <dd>

Server Trust Account

A computer account for a backup domain controller that is a member of this domain.

</dd> <dt>

65536 (0x10000)
</dt> <dd>

Do Not Expire Password

</dd> <dt>

131072 (0x20000)
</dt> <dd>

MNS Logon Account

Majority Node Set (MNS) logon account type that represents an MNS user.

</dd> <dt>

262144 (0x40000)
</dt> <dd>

Smartcard Required

</dd> <dt>

524288 (0x80000)
</dt> <dd>

Trusted for Delegation

</dd> <dt>

1048576 (0x100000)
</dt> <dd>

Not Delegated

</dd> <dt>

2097152 (0x200000)
</dt> <dd>

Use DES Key Only

</dd> <dt>

4194304 (0x400000)
</dt> <dd>

Do Not Require Preauthorization

</dd> <dt>

8388608 (0x800000)
</dt> <dd>

Password Expired

Indicates that the password has expired.

</dd> </dl>

The following properties describe the account type. Only one value can be set:

-   UF\_NORMAL\_ACCOUNT
-   UF\_TEMP\_DUPLICATE\_ACCOUNT
-   UF\_WORKSTATION\_TRUST\_ACCOUNT
-   UF\_SERVER\_TRUST\_ACCOUNT
-   UF\_INTERDOMAIN\_TRUST\_ACCOUNT

</dd> <dt>

**FullName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_full\_name")
</dt> </dl>

Full name of the user belonging to the network login profile. This string can be empty if the user chooses not to associate a full name with a user name.

</dd> <dt>

**HomeDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_home\_dir")
</dt> </dl>

Path to the home directory of the user. This string may be empty if the user chooses not to specify a home directory.

Example:"\\HOMEDIR"

</dd> <dt>

**HomeDirectoryDrive**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_home\_dir\_drive")
</dt> </dl>

Drive letter assigned to the user's home directory for log on purposes.

Example: "C:"

</dd> <dt>

**LastLogoff**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_last\_logoff")
</dt> </dl>

User last logged off the system. This value is calculated from the number of seconds elapsed since 00:00:00, January 1, 1970. A value of " \*\*\*\*\*\*\*\*\*\*\*\*\*\*.\*\*\*\*\*\*+\*\*\* " means that the last logoff time is unknown. The format of this value is yyyymmddhhmmss.mmmmmm sutc. For information about translating this property into your local time, see [WMI Tasks: Dates and Times](../wmisdk/wmi-tasks--dates-and-times.md).

Example: 19521201000230.000000 000

</dd> <dt>

**LastLogon**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_last\_logon")
</dt> </dl>

User last logged on to the system. This value is calculated from the number of seconds elapsed since 00:00:00, January 1, 1970. The format of this value is yyyymmddhhmmss.mmmmmm sutc. For information about translating this property into your local time, see [WMI Tasks: Dates and Times](../wmisdk/wmi-tasks--dates-and-times.md).

Example: 19521201000230.000000 000

</dd> <dt>

**LogonHours**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (147), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_logon\_hours")
</dt> </dl>

Times during the week when the user can log on. Each bit represents a unit of time specified by the **UnitsPerWeek** property. For instance, if the unit of time is hourly, the first bit (bit 0, word 0) is Sunday, 0:00 to 0:59, the second bit (bit 1, word 0) is Sunday, 1:00 to 1:59, and so on. If this member is set to **NULL**, then there is no time restriction. The time is set to GMT and must be adjusted for other time zones (for example, GMT minus 8 hours for PST).

</dd> <dt>

**LogonServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_logon\_server")
</dt> </dl>

Name of the server to which logon requests are sent. Server names should be preceded by two backslashes (\\\\). A server name with an asterisk (\\\\\*) indicates that the logon request can be handled by any logon server. A null string indicates that requests are sent to the domain controller.

Example: "\\\\MyServer"

</dd> <dt>

**MaximumStorage**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_max\_storage"), [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Maximum amount of disk space available to the user. If MaximumStorage is set to USER\_MAXSTORAGE\_UNLIMITED, the user is allowed to use all of the available disk space.

Example: 10000000

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_name")
</dt> </dl>

User account on a particular domain or computer. The number of characters in the name cannot exceed the value of UNLEN.

Example: "somedomain\\johndoe"

</dd> <dt>

**NumberOfLogons**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_num\_logons")
</dt> </dl>

Number of successful times the user tried to log on to this account. A value of 0xFFFFFFFF indicates that the value is unknown. This property is maintained separately on each backup domain controller (BDC) in the domain. To get an accurate value, only the largest value from all BDCs should be used.

Example: 4

</dd> <dt>

**Parameters**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_parms")
</dt> </dl>

Space set aside for use by applications. This string can be null, or it can have any number of characters before the terminating null character. Microsoft products use this member to store user configuration information. Do not modify this information, because this value is specific to an application.

</dd> <dt>

**PasswordAge**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_password\_age")
</dt> </dl>

Length of time a password has been in effect. This value is measured from the number of seconds elapsed since the password was last changed.

Example: 00001201000230.000000 000

</dd> <dt>

**PasswordExpires**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_MODALS\_INFO\_0**](/windows/win32/api/lmaccess/ns-lmaccess-user_modals_info_0)\|usrmod0\_max\_passwd\_age")
</dt> </dl>

Date and time the password expires. The value is set in this format: yyyymmddhhmmss.mmmmmm sutc

Example: 19521201000230.000000 000

</dd> <dt>

**PrimaryGroupId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_primary\_group\_id")
</dt> </dl>

Relative identifier (RID) of the Primary Global Group for this user. The identifier verifies the primary group to which the user's profile belongs.

</dd> <dt>

**Privileges**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_priv")
</dt> </dl>

Level of privilege assigned to the **usri3\_name** property.

<dt>

<span id="Guest"></span><span id="guest"></span><span id="GUEST"></span>

**Guest** (0)


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** (1)


</dt> <dd></dd> <dt>

<span id="Administrator"></span><span id="administrator"></span><span id="ADMINISTRATOR"></span>

**Administrator** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**Profile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_profile")
</dt> </dl>

Path to the user's profile. This value can be a null string, a local absolute path, or a UNC path. A user profile contains settings that are customizable for each user such as the desktop colors.

Example: "C:\\Windows"

</dd> <dt>

**ScriptPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_script\_path")
</dt> </dl>

Directory path to the user's logon script. A logon script automatically executes a set of commands each time a user logs on to a system.

Example: "C:\\win\\profiles\\ThomasSteven"

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Identifier by which the current object is known.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**UnitsPerWeek**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_units\_per\_week")
</dt> </dl>

Number of time units the week is divided into. It is used with the **LogonHours** property to limit user access to the computer.

Example: 168 (hours per week)

</dd> <dt>

**UserComment**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_usr\_comment")
</dt> </dl>

User-defined comment or description for this profile.

</dd> <dt>

**UserId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_user\_id")
</dt> </dl>

RID of the user. The identifier verifies that the user exists and is unique to this domain.

</dd> <dt>

**UserType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_flags")
</dt> </dl>

Type of account to which the user has privileges.

The values are:

-   "Normal Account"
-   "Duplicate Account"
-   "Workstation Trust Account"
-   "Server Trust Account"
-   "Interdomain Trust Account"
-   "Unknown"

<dt>

<span id="Normal_Account"></span><span id="normal_account"></span><span id="NORMAL_ACCOUNT"></span>

**Normal Account** ("Normal Account")


</dt> <dd></dd> <dt>

<span id="Duplicate_Account"></span><span id="duplicate_account"></span><span id="DUPLICATE_ACCOUNT"></span>

**Duplicate Account** ("Duplicate Account")


</dt> <dd></dd> <dt>

<span id="Workstation_Trust_Account"></span><span id="workstation_trust_account"></span><span id="WORKSTATION_TRUST_ACCOUNT"></span>

**Workstation Trust Account** ("Workstation Trust Account")


</dt> <dd></dd> <dt>

<span id="Server_Trust_Account"></span><span id="server_trust_account"></span><span id="SERVER_TRUST_ACCOUNT"></span>

**Server Trust Account** ("Server Trust Account")


</dt> <dd></dd> <dt>

<span id="Interdomain_Trust_Account"></span><span id="interdomain_trust_account"></span><span id="INTERDOMAIN_TRUST_ACCOUNT"></span>

**Interdomain Trust Account** ("Interdomain Trust Account")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> </dl>

</dd> <dt>

**Workstations**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Network Management Structures\|[**USER\_INFO\_3**](/windows/win32/api/lmaccess/ns-lmaccess-user_info_3)\|usri3\_workstations")
</dt> </dl>

Names of workstations from which the user can log on. Up to eight workstations can be specified; the names must be separated by commas (,). A null string indicates no restrictions. To disable logons from all workstations to this account, set the UF\_ACCOUNTDISABLE in the **Flags** property of this class.

</dd> </dl>

## Remarks

The **Win32\_NetworkLoginProfile** class is derived from [**CIM\_Setting**](cim-setting.md).

The calling process that uses this class must have the **SE\_RESTORE\_NAME** privilege on the computer in which the registry resides. For more information, see [Executing Privileged Operations](../wmisdk/executing-privileged-operations.md).

## Examples

The [List Network Login Profiles](https://Gallery.TechNet.Microsoft.Com/4b84fb8a-964e-4811-98d2-de1009685a14) PowerShell sample returns network login information for all the users of a computer.

The following VBScript sample returns network login information.


```VB
On Error Resume Next 
 
strComputer = "." 
Set objWMIService = GetObject("winmgmts:" _ 
    & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
Set colItems = objWMIService.ExecQuery _ 
    ("Select * from Win32_NetworkLoginProfile") 
 
For Each objItem in colItems 
    dtmWMIDate = objItem.AccountExpires 
    strReturn = WMIDateStringToDate(dtmWMIDate) 
    Wscript.Echo "Account Expires: " & strReturn 
    Wscript.Echo "Authorization Flags: " & objItem.AuthorizationFlags 
    Wscript.Echo "Bad Password Count: " & objItem.BadPasswordCount 
    Wscript.Echo "Caption: " & objItem.Caption 
    Wscript.Echo "CodePage: " & objItem.CodePage 
    Wscript.Echo "Comment: " & objItem.Comment 
    Wscript.Echo "Country Code: " & objItem.CountryCode 
    Wscript.Echo "Description: " & objItem.Description 
    Wscript.Echo "Flags: " & objItem.Flags 
    Wscript.Echo "Full Name: " & objItem.FullName 
    Wscript.Echo "Home Directory: " & objItem.HomeDirectory 
    Wscript.Echo "Home Directory Drive: " & objItem.HomeDirectoryDrive 
    dtmWMIDate = objItem.LastLogoff 
    strReturn = WMIDateStringToDate(dtmWMIDate) 
    Wscript.Echo "Last Logoff: " & strReturn 
    dtmWMIDate = objItem.LastLogon 
    strReturn = WMIDateStringToDate(dtmWMIDate) 
    Wscript.Echo "Last Logon: " & strReturn 
    Wscript.Echo "Logon Hours: " & objItem.LogonHours 
    Wscript.Echo "Logon Server: " & objItem.LogonServer 
    Wscript.Echo "Maximum Storage: " & objItem.MaximumStorage 
    Wscript.Echo "Name: " & objItem.Name 
    Wscript.Echo "Number Of Logons: " & objItem.NumberOfLogons 
    Wscript.Echo "Password Age: " & objItem.PasswordAge 
    dtmWMIDate = objItem.PasswordExpires 
    strReturn = WMIDateStringToDate(dtmWMIDate) 
    Wscript.Echo "Password Expires: " & strReturn 
    Wscript.Echo "Primary Group ID: " & objItem.PrimaryGroupId 
    Wscript.Echo "Privileges: " & objItem.Privileges 
    Wscript.Echo "Profile: " & objItem.Profile 
    Wscript.Echo "Script Path: " & objItem.ScriptPath 
    Wscript.Echo "Setting ID: " & objItem.SettingID 
    Wscript.Echo "Units Per Week: " & objItem.UnitsPerWeek 
    Wscript.Echo "User Comment: " & objItem.UserComment 
    Wscript.Echo "User Id: " & objItem.UserId 
    Wscript.Echo "User Type: " & objItem.UserType 
    Wscript.Echo "Workstations: " & objItem.Workstations 
    Wscript.Echo 
Next 
  
Function WMIDateStringToDate(dtmWMIDate) 
    If Not IsNull(dtmWMIDate) Then 
    WMIDateStringToDate = CDate(Mid(dtmWMIDate, 5, 2) & "/" & _ 
         Mid(dtmWMIDate, 7, 2) & "/" & Left(dtmWMIDate, 4) _ 
             & " " & Mid (dtmWMIDate, 9, 2) & ":" & _ 
                 Mid(dtmWMIDate, 11, 2) & ":" & Mid(dtmWMIDate, 13, 2)) 
    End If 
End Function 
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[Operating System Classes](./operating-system-classes.md)
</dt> </dl>

 

 
