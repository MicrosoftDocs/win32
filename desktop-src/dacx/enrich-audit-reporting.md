---
title: How to enrich audit reporting
description: Auditing reports can be enriched through parsing event records and accessing further details in the directory and file system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: DEE3B669-2BF2-407C-A52C-3E996602D8B0
ms.prod: windows-server-dev
ms.technology: dynamic-access-control
ms.tgt_platform: multiple
keywords:
- Dynamic Access Control developer extensibility DACx , audit reporting
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to enrich audit reporting

Auditing reports can be enriched through parsing event records and accessing further details in the directory and file system.

## What you need to know

### Technologies

-   [LDAP](https://msdn.microsoft.com/library/windows/desktop/aa367008.aspx)

    Provides programmable access to directory information.

-   [Windows PowerShell](https://technet.microsoft.com/library/bb978526.aspx)

    Provides programmable access to directory information.

### Prerequisites

The LDAP API documentation in the Microsoft Windows Software Development Kit (SDK) is intended for experienced C and C++ programmers and internet directory developers. A familiarity with directory services and the LDAP client/server model is necessary for development with the LDAP API.

PowerShell is a task-based command-line shell and scripting language designed especially for system administration. Built on the .NET Framework, PowerShell helps IT professionals and power users control and automate the administration of the Windows operating system and applications that run on Windows.

## Instructions

### Improving file access reporting

In Windows Server 2012 and Windows 8 the file access events (Event ID 4663 and 4656) have been updated to include file classification information. Audit event analysis and reporting tools can leverage this information to help answer questions such as, “Who accessed my *High Impact* data in the past month?” or “Show me all file access events for files belonging to the Finance department that contained PII”.

Following is an example of the file access event 4663 that was generated when user Joey accessed the file *MarchStmt.xls* which was classified as a *High Impact* document.

``` syntax
An attempt was made to access an object.

Subject:
 Security ID:  CONTOSODOM\joey
 Account Name:  joey
 Account Domain: CONTOSODOM
 Logon ID:  0x3e7

Object:
 Object Server: Security
 Object Type: File
 Object Name: C:\Finance Document Share\FinancialStatements\MarchStmt.xls
 Handle ID: 0x8e4
Resource Attributes: S:AI(RA;;;;;WD;("Department_88ce9e0e3cac9f52",TS,0x0,"Finance"))(RA;;;;;WD;("Impact_88ce9e0e4e78e57f",TI,0x0,1))


Process Information:
 Process ID: 0x200
 Process Name: C:\Program Files\Office\excel.exe

Access Request Information:
 Accesses: WRITE DATA   
 Access Mask: 0x2
```

The **Resource Attributes** field of this event displays the file classification information. This information is presented as an SDDL string which can be parsed programmatically to extract the file classification properties. Using an LDAP or PowerShell query, you can look up in Active Directory the display name of the attribute ID **Impact\_88ce9e0e4e78e57f** and **Department\_88ce9e0e3cac9f52** for your audit report. Using a similar query you can also look up the display name for the value (1) of the attribute **Impact\_88ce9e0e4e78e57f** which is “High”. For more information on querying AD, see the Remarks section.

In addition to the updates to the file access events, Windows Server 2012 and Windows 8 also introduce a new event (ID: 4626) to capture the user and device claim information associated with a user logon token. This event when correlated with the file access events (Event ID: 4656 or 4663) can provide information to answer questions such as, “Show me all attempts to access High Impact data by employees with a low security clearance”.

Following is an example of the event 4626 that was generated when Joey logged onto the file server that hosts the file *MarchStmt.xls*.

``` syntax
User / Device claims information.
Subject:
                Security ID:         SYSTEM
                Account Name:        FILESERVER$
                Account Domain:      CONTOSO
                Logon ID:            0x3E7

Logon Type:     10

New Logon:
                Security ID:         CONTOSO\Joey
                Account Name:        Joey
                Account Domain:      Contoso
                Logon ID:            0x3AA522

Event in sequence:   1 of 1

User Claims:    Department_88ce9e0e3cac9f52 <String> : "Finance"
                SecurityClearance_88ce9e0d334b000e <String> : "High"
                EmploymentStatus_88ce9e0e4e78e57f <String> : “Fulltime”

Device Claims:  -
```

The **User Claims** and **Device Claims** fields of this event contain the relevant information.

> [!Note]  
> the event in the previous example does not have device claims information.

 

Each line item in these fields is of the format *Attribute ID &lt;Data type&gt;: Value*. You can translate the attribute ID to its corresponding *Display name* using an LDAP or PowerShell query to look it up in Active Directory. For more information on querying AD, see the Remarks section.

The **Logon ID** field can be used to correlate this event to the corresponding file access events on the same file server.

> [!Note]  
> Event 4626 was introduced in Windows Server 2012 whereas events 4656 and 4663 are not new. All these events will be generated on the file server hosting the files that are being audited.

 

### Generating Staging reports – helping users deploy Dynamic Access Control Policies

Windows Server 2012/Windows 8 introduces the concept of *Staging* to help users test their Central Access Policies in the production environment. Each Central Access Policy has an *Effective Policy* which determines who gets access to what and a *Proposed/Staging Policy* which is the policy that is to be tested. Once deployed, special audit events are generated when there is a difference in the access granted by the *Effective Policy* and the *Proposed/Staging Policy*, thereby giving users an opportunity to understand the impact of the proposed policy changes. Audit event analysis and reporting tools can generate a special staging report to help users consume these events.

Following is an example of the staging event (ID: 4818) that was generated when the user Alice accessed the file *MarchStmt.xls* after a staging policy was added to the Central Access Rule named “Access to High Impact data”. The event was generated because the *Proposed/Staging Policy* does not grant Alice the same access rights as the *Effective Policy* (the Staging policy does not grant READ\_CONTROL and ReadAttributes rights to Alice)

``` syntax
Subject:
                Security ID:                  CONTOSODOM\alice
                Account Name:                 alice
                Account Domain:               CONTOSODOM
                Logon ID:                     0x26d20

Object:
                Object Server:                Security
                Object Type:                  File
                Object Name:                  C:\Finance Document Share\FinancialStatements\MarchStmt.xls
                Handle ID:                    0xaf0

Process Information:
                Process ID:                    0x314
                Process Name:                  D:\Windows\explorer.exe

Effective Central Access Policy Request Information:

                Access Reasons:                READ_CONTROL: Granted by Ownership
         ReadAttributes: Granted by D:(A;ID;FA;;;BA)
                                                                
Central Policy Staging Result:

                Staging Reasons:               READ_CONTROL: NOT Granted by CAPE “Access to High Impact Data (staging)”
                                               ReadAttributes: NOT Granted by CAPE “Access to High Impact Data (staging)”
```

## Remarks

For search examples, these LDAP samples would have been installed at the following default locations on your computer.

-   C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Samples\\netds\\adsi\\activedir\\attributes
-   C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Samples\\netds\\adsi\\activedir\\PropertyList

## Related topics

<dl> <dt>

[Dynamic Access Control developer extensibility](dynamic-access-control-developer-extensibility-roadmap.md)
</dt> <dt>

[FSRM Interfaces](https://msdn.microsoft.com/library/windows/desktop/bb625488.aspx)
</dt> <dt>

[Searching in Active Directory Domain Services](https://msdn.microsoft.com/library/windows/desktop/aa746427.aspx)
</dt> <dt>

[Introduction to System.DirectoryServices.Protocols: Search Operations](https://msdn.microsoft.com/library/bb332056.aspx#sdspintro-topic5)
</dt> </dl>

 

 




