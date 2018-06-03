---
title: MSFT\_FSRMADRSettings class
description: Returns an object containing event settings as supplied by the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0ddadb89-7059-43bb-9b8b-e31976ce715a
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMADRSettings class File Server Resource Manager
- MSFT_FSRMADRSettings class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMADRSettings
- MSFT_FSRMADRSettings.Event
- MSFT_FSRMADRSettings.Enabled
- MSFT_FSRMADRSettings.DisplayMessage
- MSFT_FSRMADRSettings.EmailMessage
- MSFT_FSRMADRSettings.AllowRequests
- MSFT_FSRMADRSettings.MailToOwner
- MSFT_FSRMADRSettings.MailCCAdmin
- MSFT_FSRMADRSettings.MailTo
- MSFT_FSRMADRSettings.IncludeDeviceClaims
- MSFT_FSRMADRSettings.IncludeUserClaims
- MSFT_FSRMADRSettings.EventLog
- MSFT_FSRMADRSettings.DeviceTroubleShooting
- MSFT_FSRMADRSettings.SetByPolicy
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMADRSettings class

Returns an object containing event settings as supplied by the server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMADRSettings
{
  uint32  Event;
  boolean Enabled = False;
  string  DisplayMessage;
  string  EmailMessage;
  boolean AllowRequests = False;
  boolean MailToOwner = True;
  boolean MailCCAdmin = True;
  string  MailTo = "";
  boolean IncludeDeviceClaims = True;
  boolean IncludeUserClaims = True;
  boolean EventLog = True;
  boolean DeviceTroubleShooting = True;
  boolean SetByPolicy = False;
};
```

## Members

The **MSFT\_FSRMADRSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FSRMADRSettings** class has these properties.

<dl> <dt>

**AllowRequests**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional value that specifies whether users are allowed to request access by sending email. The default value is **False**.

</dd> <dt>

**DeviceTroubleShooting**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional value that specifies whether to show the user the offending device claims during the interaction. The default value is **True**.

</dd> <dt>

**DisplayMessage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional message sent to a user upon receiving the event. The length of the string must not exceed 10KB.

</dd> <dt>

**EmailMessage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional message sent to a user upon receiving the event. The length of the string must not exceed 10KB.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether to enable remediation for the event on this server. The default value is **False**.

</dd> <dt>

**Event**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Describes the type of failure handled by ADR.

<dt>

<span id="AccessDenied"></span><span id="accessdenied"></span><span id="ACCESSDENIED"></span>

<span id="AccessDenied"></span><span id="accessdenied"></span><span id="ACCESSDENIED"></span>**AccessDenied** (1)


</dt> <dd>

The failure was an access denied error.

</dd> <dt>

<span id="FileNotFound"></span><span id="filenotfound"></span><span id="FILENOTFOUND"></span>

<span id="FileNotFound"></span><span id="filenotfound"></span><span id="FILENOTFOUND"></span>**FileNotFound** (2)


</dt> <dd>

The failure was an file not found error.

</dd> </dl>

</dd> <dt>

**EventLog**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional value that specifies whether to create an Event Log entry for each access email sent. The default value is **True**.

</dd> <dt>

**IncludeDeviceClaims**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional value that specifies whether to include device claims in a request. The default value is **True**.

</dd> <dt>

**IncludeUserClaims**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional value that specifies whether to include user claims in a request. The default value is **True**.

</dd> <dt>

**MailCCAdmin**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional value that specifies whether the system administrator is included on the CC line when a request is sent. The default value is **True**.

</dd> <dt>

**MailTo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional semicolon-separated list of email addresses to which the request will be sent. The string is empty by default.

</dd> <dt>

**MailToOwner**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional value that specifies whether the data owner is contacted when a request is sent. The default value is **True**.

</dd> <dt>

**SetByPolicy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether these settings were set by group policy. The default value is **False**.

</dd> </dl>

## Remarks

Not all combinations of properties are supported. The **Name** property is always required. The **UpdateDerived** and **UpdateDerivedMatching** properties are mutually exclusive if one is provided then the other must not be set. Only one of **Description**, **Size**, **SoftLimit**, and **Threshold** must be provided. The table below indicates which combinations of properties in this class are supported.



Property

Valid combinations

**Name**

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

**Description**

Yes

Yes

No

No

No

No

No

No

**Size**

No

No

Yes

Yes

No

No

No

No

**SoftLimit**

No

No

No

No

Yes

Yes

No

No

**Threshold**

No

No

No

No

No

No

Yes

Yes

**UpdateDerived**

Yes

No

Yes

No

Yes

No

Yes

No

**UpdateDerivedMatching**

No

Yes

No

Yes

No

Yes

No

Yes



 

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[FSRM WMI Classes](fsrm-wmi-classes.md)
</dt> <dt>

[**IFsrmAccessDeniedRemediationClient**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmaccessdeniedremediationclient)
</dt> </dl>

 

 





