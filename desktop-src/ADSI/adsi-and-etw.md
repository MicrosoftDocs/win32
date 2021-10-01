---
title: Event Tracing in ADSI
description: Windows Server 2008 and Windows Vista introduce Event Tracing in Active Directory Service Interfaces (ADSI).
ms.assetid: 743aeeba-5b48-47c7-aaf5-0e9b48e206db
ms.tgt_platform: multiple
keywords:
- event tracing ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Event Tracing in ADSI

Windows Server 2008 and Windows Vista introduce [Event Tracing](/windows/desktop/ETW/event-tracing-portal) in [Active Directory Service Interfaces](active-directory-service-interfaces-adsi.md) (ADSI). Certain areas of the ADSI LDAP Provider have an underlying implementation that is complex or that involves a sequence of steps that makes it difficult to diagnose problems. To help application developers troubleshoot, Event Tracing has been added to the following areas:

## Schema Parsing and Downloading

The IADs interface in ADSI requires that the LDAP schema be cached on the client so that attributes can be marshaled correctly (as described in the [ADSI Schema Model](adsi-schema-model.md)). To achieve this, ADSI loads the schema for each process (and for each LDAP server/domain) into memory either from a schema (.sch) file that is saved on the local disk or by downloading it from the LDAP server. Different processes on the same client machine use the cached schema on disk if it is available and applicable.

If the schema cannot be obtained from the disk or the server, ADSI uses a hardcoded default schema. When this occurs, attributes that are not part of this default schema cannot be marshaled and ADSI returns an error while retrieving these attributes. A number of factors could cause this to happen, including problems in parsing the schema, and insufficient privileges to download the schema. It is often difficult to determine why a certain default schema is being used. Using Event Tracing in this area will help to more quickly diagnose the problem and fix it.

## Changing and Setting the Password

[**ChangePassword**](/windows/desktop/api/Iads/nf-iads-iadsuser-changepassword) and [**SetPassword**](/windows/desktop/api/Iads/nf-iads-iadsuser-setpassword) employ more than one mechanism to perform the requested operation based on the available configuration (as described in [Setting and Changing User Passwords with the LDAP Provider](setting-user-passwords-for-ldap-providers.md)). When **ChangePassword** and **SetPassword** fail, it can be difficult to determine exactly why, and Event Tracing will help to troubleshoot problems with these methods.

## ADSI Bind Cache

ADSI internally tries to reuse LDAP connections whenever possible (see [Connection Caching](connection-caching.md)). When troubleshooting, it is useful to trace whether a new connection was opened for communication with the server or whether an existing connection was used. It can also be useful to trace the lifecycle of the connection cache (sometimes referred to as the bind cache) and its creation or closure, and whether a connection referral took place. In the case of a [serverless bind](/windows/desktop/AD/serverless-binding-and-rootdse), ADSI calls the DC locator to select a server for the domain of the user's context. ADSI then maintains a cache of the domain-server mapping for subsequent connections. Event Tracing helps to trace the selection of the DC, and is therefore helpful in troubleshooting connection-related issues.

## Enabling Tracing and Starting a Tracing Session

To turn on ADSI tracing, create the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**adsi**\\**Tracing**\\***ProcessName***

*ProcessName* is the full name of the process that you want to trace, including its extension (for example, "Svchost.exe"). In addition, you can place an optional value of type **DWORD** named PID in this key. It is highly recommended that you set this value and thereby trace only a particular process. Otherwise, all instances of the application specified by *ProcessName* will be traced.

Then execute the following command:

**tracelog.exe -start** *sessionname* **-guid \#***provider\_guid* **-f** *filename* **-flag** *traceFlags* **-level** *traceLevel*

*sessionname* is simply an arbitrary identifier that is used to label the tracing session (you will need to refer to this session name later when you stop the tracing session). The GUID for the ADSI tracking provider is "7288c9f8-d63c-4932-a345-89d6b060174d". *filename* specifies the logfile to which events will be written. *traceFlags* should be one of the following values:



|         Flag                        |         Value              |
|---------------------------------|-----------------------|
| **DEBUG\_SCHEMA**<br/>    | 0x00000001<br/> |
| **DEBUG\_CHANGEPWD**<br/> | 0x00000002<br/> |
| **DEBUG\_SETPWD**<br/>    | 0x00000004<br/> |
| **DEBUG\_BINDCACHE**<br/> | 0x00000008<br/> |



 

These flags determine which [ADSI](active-directory-service-interfaces-adsi.md) methods will be traced, according to the following table:




| 
|
| <strong>DEBUG_SCHEMA</strong><br /> | <ul><li>LdapGetSchema</li><li>GetSchemaInfoTime</li><li>LdapReadSchemaInfoFromServer</li><li>ProcessSchemaInfo</li><li>HelperReadLdapSchemaInfo</li><li>ProcessClassInfoArray</li><li>ReadSchemaInfoFromRegistry</li><li>StoreSchemaInfoFromRegistry</li><li>AttributeTypeDescription</li><li>ObjectClassDescription</li><li>DITContentRuleDescription</li><li>DirectoryString</li><li>DirectoryStrings</li><li>DITContentRuleDescription</li></ul><br /> | 
| <strong>DEBUG_CHANGEPWD</strong><br /> | <ul><li>CADsUser::ChangePassword</li></ul><br /> | 
| <strong>DEBUG_SETPWD</strong><br /> | <ul><li>CADsUser::SetPassword</li></ul><br /> | 
| <strong>DEBUG_BINDCACHE</strong><br /> | <ul><li>GetServerBasedObject</li><li>GetServerLessBasedObject</li><li>GetGCDomainName</li><li>GetDefaultDomainName</li><li>GetUserDomainFlatName</li><li>BindCacheLookup</li><li>EquivalentPortNumbers</li><li>CanCredentialsBeReused</li><li>BindCacheAdd</li><li>BindCacheAddRef</li><li>AddReferralLink</li><li>CommonRemoveEntry</li><li>BindCacheDerefHelper</li><li>NotifyNewConnection</li><li>QueryForConnection</li><li>LdapOpenBindWithCredentials</li><li>LdapOpenBindWithDefaultCredentials</li></ul><br /> | 




 

You can combine flags by combining the appropriate bits in the *traceFlags* argument. For example, to specify the **DEBUG\_SCHEMA** and **DEBUG\_BINDCACHE** flags, the appropriate *traceFlags* value would be 0x00000009.

Finally, the *traceLevel* flag should be one of the following values:



|      Flag                                    |       Value                |
|------------------------------------------|-----------------------|
| **TRACE\_LEVEL\_ERROR**<br/>       | 0x00000002<br/> |
| **TRACE\_LEVEL\_INFORMATION**<br/> | 0x00000004<br/> |



 

**TRACE\_LEVEL\_INFORMATION** causes the tracing process to record all events, whereas **TRACE\_LEVEL\_ERROR** causes the tracing process to record only error events.

To terminate tracing, run the following command:

**tracelog.exe -stop** *sessionname*

In the previous example, *sessionname* is the same name as the one that was provided with the command that started the tracing section.

## Remarks

It is more effective to trace only specific processes by specifying a particular PID than to trace all processes on a computer. If you do need to trace multiple applications on the same machine, there might be a performance impact; there is substantial debugging output in performance-oriented sections of the code. Also, administrators must be careful to properly set the permissions of the log files when tracing multiple processes; otherwise, any user might be able to read the tracing logs, and other users will be able to trace processes that contain secure information.

For example, presume the administrator sets up tracing for an application "Test.exe", and does not specify a PID in the registry to trace multiple instances of the process. Now another user wants to trace the application "Secure.exe". If the tracing log files are not properly restricted, all that user needs to do is rename "Secure.exe" to "Test.exe", and it will be traced. In general, it is best to trace only specific processes while troubleshooting, and to remove the tracing registry key as soon as troubleshooting is done.

Since enabling Event Tracing will produce extra log files, administrators should carefully monitor log file sizes; lack of disk space on the local computer can cause a denial-of-service.

## Example Scenarios

Scenario 1: The administrator sees an unexpected error in an application that sets passwords for user accounts, so they would take the following steps to fix the problem using Event Tracing.

1.  Write a script that reproduces the problem, and create the registry key

    **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**adsi**\\**Tracing**\\**cscript.exe**

2.  Start a tracing session, setting *traceFlags* to 0x2 (**DEBUG\_CHANGEPASSWD**) and *traceLevel* to 0x4 (**TRACE\_LEVEL\_INFORMATION**), using the following command:

    **tracelog.exe -start scripttrace -guid \#7288c9f8-d63c-4932-a345-89d6b060174d -f .\\adsi.etl -flag 0x2 -level 0x4**

3.  Run cscript.exe with their test script to reproduce the problem, and then terminate the tracing session:

    **tracelog.exe -stop scripttrace**

4.  Delete the registry key

    **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**adsi**\\**Tracing**\\**cscript.exe**

5.  Run the ETW tool Tracerpt.exe to parse the tracing information from the log:

    **tracelog.exe -start scripttrace -guid \#7288c9f8-d63c-4932-a345-89d6b060174d -f .\\adsi.etl -flag 0x2 -level 0x4**

Scenario 2: The administrator wants to trace the schema parsing and download operations in an [ASP](https://msdn.microsoft.com/asp.net/default.aspx) application named w3wp.exe that is already running. To do this, the administrator would take the following steps:

1.  Create the registry key

    **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**adsi**\\**Tracing**\\**w3wp.exe**

    and inside that key, create a value of type DWORD that is named PID and set it to the process ID of the instance of w3wp.exe that is currently running on the local computer.

2.  Then they create a tracing session, setting *traceFlags* to 0x1 (**DEBUG\_SCHEMA**) and *traceLevel* to 0x4 (**TRACE\_LEVEL\_INFORMATION**):

    **tracelog.exe -start w3wptrace -guid \#7288c9f8-d63c-4932-a345-89d6b060174d -f .\\w3wp.etl -flag 0x1 -level 0x4**

3.  Reproduce the operation that needs troubleshooting.
4.  Terminate the tracing session:

    **tracelog.exe -stop w3wptrace**

5.  Delete the registry key **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**adsi**\\**Tracing**\\**w3wp.exe**.
6.  Run the ETW tool tracerpt.exe to parse the tracing information from the log:

    **tracerpt.exe .\\w3wp.etl -o -report**

 

