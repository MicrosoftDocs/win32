---
description: 'The event log contains the following standard logs as well as custom logs:'
ms.assetid: 87d860e3-2495-4e15-bb42-341e92935e55
title: Eventlog Key
ms.topic: article
ms.date: 05/31/2018
---

# Eventlog Key

The event log contains the following standard logs as well as custom logs:



| Log             | Description                                                                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Application** | Contains events logged by applications. For example, a database application might record a file error. The application developer decides which events to record.                                                                             |
| **Security**    | Contains events such as valid and invalid logon attempts, as well as events related to resource use such as creating, opening, or deleting files or other objects. An administrator can start auditing to record events in the security log. |
| **System**      | Contains events logged by system components, such as the failure of a driver or other system component to load during startup.                                                                                                               |
| *CustomLog*     | Contains events logged by applications that create a custom log. Using a custom log enables an application to control the size of the log or attach ACLs for security purposes without affecting other applications.                         |



 

The event logging service uses the information stored in the **Eventlog** registry key. The **Eventlog** key contains several subkeys, called *logs*. Each log contains information that the event logging service uses to locate resources when an application writes to and reads from the event log.

The structure of the **Eventlog** key is as follows:

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Services
            Eventlog
               Application
               Security
               System
               CustomLog
```

Note that domain controllers record events in the **Directory service** and **File Replication service** logs and DNS servers record events in the **DNS server**.

Each log can contain the following registry values.




| Registry value | Description | 
|----------------|-------------|
| <strong>CustomSD</strong> | Restricts access to the event log. This value is of type REG_SZ. The format used is <a href="/windows/desktop/SecAuthZ/security-descriptor-definition-language">Security Descriptor Definition Language</a> (SDDL). Construct an ACL that grants one or more of the following rights:<dl> Clear (0x0004)<br />Read (0x0001)<br />Write (0x0002)<br /></dl> To be a syntactically valid SDDL, the CustomSD value must specify an owner and a group owner (for example, O:BAG:SY), but the owner and group owner are not used. If CustomSD is set to a wrong value, an event is fired in the System event log when the event log service starts, and the event log gets a default security descriptor which is identical to the original CustomSD value for the Application log. SACLs are not supported.<br /> For more information, see <a href="event-logging-security.md">Event Logging Security</a>.<br /><strong>Windows Server 2003:</strong> SACLs are supported.<br /><strong>Windows XP/2000:</strong> This value is not supported.<br /><br /> | 
| <strong>DisplayNameFile</strong> | This value is not used. <strong>Windows Server 2003 and Windows XP/2000:  </strong> Name of the file that stores the localized name of the event log. The name stored in this file appears as the log name in Event Viewer. If this entry does not appear in the registry for an event log, Event Viewer displays the name of the registry subkey as the log name. This value is of type REG_EXPAND_SZ. The default value is %SystemRoot%\system32\els.dll.<br /> | 
| <strong>DisplayNameID</strong> | This value is not used. <strong>Windows Server 2003 and Windows XP/2000:  </strong> Message identification number of the log name string. This number indicates the message in which the localized display name appears. The message is stored in the file specified by the <strong>DisplayNameFile</strong> value. This value is of type REG_DWORD.<br /> | 
| <strong>File</strong> | Fully qualified path to the file where each event log is stored. This enables Event Viewer and other applications to find the log files. This value is of type REG_SZ or REG_EXPAND_SZ. This value is optional. If the value is not specified, it defaults to %SystemRoot%\system32\winevt\logs\ followed by a file name that is based on the event log registry key name.The specific event log file path should be set using the command line utility wevtutil.exe or by using the <a href="/windows/desktop/api/winevt/nf-winevt-evtsetchannelconfigproperty"><strong>EvtSetChannelConfigProperty</strong></a> function with EvtChannelLoggingConfigLogFilePath passed into the <em>PropertyId</em> parameter.<br /> If a specific file is set, make sure that the event log service has full permissions on the file.<br /> This value needs to be a valid file name for a file that is located on a local directory (not a remote computer, not a DOS device, not a floppy, and not a pipe). If the file setting is wrong, an event is fired in the System event log when the event log service starts.<br /> Do not use environment variables, in the path to the file, that cannot be expanded in the context of the event log service.<br /><strong>Windows Server 2003 and Windows XP/2000:</strong> This value defaults to %SystemRoot%\system32\config\ followed by a file name that is based on the event log registry key name. If the File setting is set to an invalid value, the log will either not be initialized properly, or all requests will silently go to the default log (Application).<br /> | 
| <strong>MaxSize</strong> | Maximum size, in bytes, of the log file. This value is of type REG_DWORD. The value must be set to a multiple of 64K for a System, Application, or Security log. The default value is 1MB.<strong>Windows Server 2003 and Windows XP/2000:</strong> The value is limited to 0xFFFFFFFF, and the default value is 512K.<br /> | 
| <strong>PrimaryModule</strong> | This value is not used.<strong>Windows Server 2003 and Windows XP/2000:</strong> This value is the name of the subkey that contains the default values for the entries in the subkey for the event source. This value is of type REG_SZ.<br /> | 
| <strong>Retention</strong> | This value is of type REG_DWORD. The default value is 0. If this value is 0, the records of events are always overwritten. If this value is 0xFFFFFFFF or any nonzero value, records are never overwritten. When the log file reaches its maximum size, you must clear the log manually; otherwise, new events are discarded. You must also clear the log before you can change its size.<strong>Windows Server 2003 and Windows XP/2000:  </strong> This value is the time interval, in seconds, that records of events are protected from being overwritten. When the age of an event reaches or exceeds this value, it can be overwritten.<br /> | 
| <strong>Sources</strong> | This value is not used. <strong>Windows Server 2003 and Windows XP/2000:  </strong> Names of the applications, services, or groups of applications that write events to this log. This value should only be read and not altered. The event log service maintains the list based on each program listed in a subkey under the log. This value is of type REG_MULTI_SZ.<br /> | 
| <strong>AutoBackupLogFiles</strong> | This value is of type REG_DWORD, and is used by the event log service to determine whether an event log should be automatically saved. The default value is 0, which disables auto-backup. The service will back up the log file only if the retention value is -1 (0xFFFFFFFF). Other values will be ignored.<strong>Windows Server 2003:  </strong> Retention can be set to -1 (0xFFFFFFFF) or 1 (0x00000001) for AutoBackupLogFiles to work. Other values will be ignored.<br /> | 
| <strong>RestrictGuestAccess</strong> | This value is not used. <strong>Windows XP/2000:  </strong> This value is of type REG_DWORD, and the default value is 1. When the value is set to 1, it restricts the Guest and Anonymous account access to the event log, and when this value is 0, it allows Guest account access to the event log.<br /> | 
| <strong>Isolation</strong> | Defines the default access permissions for the log. This value is of type REG_SZ. You can specify one of the following values:<ul><li><strong>Application</strong></li><li><strong>System</strong></li><li><strong>Custom</strong></li></ul>The default isolation is <strong>Application</strong>. The default permissions for <strong>Application</strong> are (shown using SDDL): <br /><pre class="syntax" data-space="preserve"><code>            L"O:BAG:SYD:"            L"(A;;0xf0007;;;SY)"                // local system               (read, write, clear)            L"(A;;0x7;;;BA)"                    // built-in admins            (read, write, clear)            L"(A;;0x7;;;SO)"                    // server operators           (read, write, clear)            L"(A;;0x3;;;IU)"                    // INTERACTIVE LOGON          (read, write)            L"(A;;0x3;;;SU)"                    // SERVICES LOGON             (read, write)            L"(A;;0x3;;;S-1-5-3)"               // BATCH LOGON                (read, write)            L"(A;;0x3;;;S-1-5-33)"              // write restricted service   (read, write)            L"(A;;0x1;;;S-1-5-32-573)";         // event log readers          (read) </code></pre>The default permissions for <strong>System</strong> are (shown using SDDL): <br /><pre class="syntax" data-space="preserve"><code>            L"O:BAG:SYD:"            L"(A;;0xf0007;;;SY)"                // local system             (read, write, clear)            L"(A;;0x7;;;BA)"                    // built-in admins          (read, write, clear)            L"(A;;0x3;;;BO)"                    // backup operators         (read, write)            L"(A;;0x5;;;SO)"                    // server operators         (read, clear)             L"(A;;0x1;;;IU)"                    // INTERACTIVE LOGON        (read)            L"(A;;0x3;;;SU)"                    // SERVICES LOGON           (read, write)            L"(A;;0x1;;;S-1-5-3)"               // BATCH LOGON              (read)            L"(A;;0x2;;;S-1-5-33)"              // write restricted service (write)            L"(A;;0x1;;;S-1-5-32-573)";         // event log readers        (read)</code></pre>The default permissions for <strong>Custom</strong> isolation is the same as Application.<br /><strong>Windows Server 2003 and Windows XP/2000:  </strong> This value is not available.<br /> | 




 

Each log also contains event sources. For more information, see [Event Sources](event-sources.md).

