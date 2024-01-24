---
title: Win32_TSSessionDirectory class
description: Defines the Remote Desktop Connection Broker (RD Connection Broker) configuration settings for the Win32\_TSSessionDirectorySetting class.
ms.assetid: ef9042c2-4a35-49e9-b195-fb37c0919068
ms.tgt_platform: multiple
keywords:
- Win32_TSSessionDirectory class Remote Desktop Services
- Win32_TSSessionDirectory class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSSessionDirectory
- Win32_TSSessionDirectory.Caption
- Win32_TSSessionDirectory.Description
- Win32_TSSessionDirectory.InstallDate
- Win32_TSSessionDirectory.Name
- Win32_TSSessionDirectory.Status
- Win32_TSSessionDirectory.SessionDirectoryLocation
- Win32_TSSessionDirectory.PolicySourceSessionDirectoryLocation
- Win32_TSSessionDirectory.SessionDirectoryActive
- Win32_TSSessionDirectory.PolicySourceSessionDirectoryActive
- Win32_TSSessionDirectory.SessionDirectoryExposeServerIP
- Win32_TSSessionDirectory.PolicySourceSessionDirectoryExposeServerIP
- Win32_TSSessionDirectory.SessionDirectoryClusterName
- Win32_TSSessionDirectory.PolicySourceLoadBalancing
- Win32_TSSessionDirectory.GetLoadBalancingState
- Win32_TSSessionDirectory.GetServerWeight
- Win32_TSSessionDirectory.PolicySourceSessionDirectoryClusterName
- Win32_TSSessionDirectory.SessionDirectoryIPAddress
- Win32_TSSessionDirectory.GetTSRedirectorMode
- Win32_TSSessionDirectory.PolicySourceTSRedirectorMode
api_location:
- TSCfgWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSSessionDirectory class

Defines the Remote Desktop Connection Broker (RD Connection Broker) configuration settings for the [**Win32\_TSSessionDirectorySetting**](win32-tssessiondirectorysetting.md) class.

> [!Note]  
> In Windows Server 2008 R2, the name of Terminal Services Session Broker (TS Session Broker) was changed to RD Connection Broker. These properties apply to all supported operating systems unless otherwise noted.

 

The following syntax is simplified from MOF code and includes all defined and inherited properties, in alphabetical order. For reference information about methods, see the table of methods later in this topic.

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_TSSESSIONDIRECTORY_Prov"), ClassContext("local|hkey_local_machine\\SYSTEM\\CurrentControlSet\\Control\\TerminalServer"), AMENDMENT]
class Win32_TSSessionDirectory : CIM_Setting
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  string   SessionDirectoryLocation;
  uint32   PolicySourceSessionDirectoryLocation;
  uint32   SessionDirectoryActive;
  uint32   PolicySourceSessionDirectoryActive;
  uint32   SessionDirectoryExposeServerIP;
  uint32   PolicySourceSessionDirectoryExposeServerIP;
  string   SessionDirectoryClusterName;
  uint32   PolicySourceLoadBalancing;
  uint32   GetLoadBalancingState;
  uint32   GetServerWeight;
  uint32   PolicySourceSessionDirectoryClusterName;
  string   SessionDirectoryIPAddress;
  uint32   GetTSRedirectorMode;
  uint32   PolicySourceTSRedirectorMode;
};
```

## Members

The **Win32\_TSSessionDirectory** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSSessionDirectory** class has these methods.



| Method                                                                                                  | Description                                                                                                  |
|:--------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|
| [**CreateUserDiskTemplate**](createuserdisktemplate-win32-tssessiondirectory.md)                       | Creates a user disk template.<br/>                                                                     |
| [**DisableUserVhd**](disableuservhd-win32-tssessiondirectory.md)                                       | Disables a user profile VHD.<br/>                                                                      |
| [**EnableUserVhd**](enableuservhd-win32-tssessiondirectory.md)                                         | Enables a user profile VHD on an RDSH server.<br/>                                                     |
| [**GetCurrentRedirectableAddresses**](getcurrentredirectableaddresses-win32-tssessiondirectory.md)     | Obtains the currently configured list of DNS eligible addresses, and the redirection type.<br/>        |
| [**GetRedirectableAddresses**](getredirectableaddresses-win32-tssessiondirectory.md)                   | Obtains the entire list of DNS eligible addresses.<br/>                                                |
| [**PingSessionDirectory**](pingsessiondirectory-win32-tssessiondirectory.md)                           | Checks whether the RD Connection Broker server is available.<br/>                                      |
| [**SetCurrentRedirectableAddresses**](setcurrentredirectableaddresses-win32-tssessiondirectory.md)     | Sets the configured list of DNS eligible addresses, and the redirection type.<br/>                     |
| [**SetLoadBalancingState**](setloadbalancingstate-win32-tssessiondirectory.md)                         | Sets the value to indicate if the server will participate in RD Connection Broker load balancing.<br/> |
| [**SetServerWeight**](setserverweight-win32-tssessiondirectory.md)                                     | Sets the server weight value for RD Connection Broker load balancing.<br/>                             |
| [**SetSessionDirectoryActive**](win32-tssessiondirectory-setsessiondirectoryactive.md)                 | Disables and enables the RD Connection Broker.<br/>                                                    |
| [**SetSessionDirectoryExposeServerIP**](win32-tssessiondirectory-setsessiondirectoryexposeserverip.md) | Sets the **SessionDirectoryExposeServerIP** property.<br/>                                             |
| [**SetSessionDirectoryProperty**](win32-tssessiondirectory-setsessiondirectoryproperty.md)             | Sets the **SessionDirectoryLocation** property or the **SessionDirectoryClusterName** property.<br/>   |
| [**SetTSRedirectorMode**](settsredirectormode-win32-tssessiondirectory.md)                             | This method is not available.<br/>                                                                     |



 

### Properties

The **Win32\_TSSessionDirectory** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Short description (one-line string) of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**GetLoadBalancingState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the server is configured to participate in RD Connection Broker load balancing.

<dt>

0
</dt> <dd>

The server is not configured to participate in RD Connection Broker load balancing.

</dd> <dt>

1
</dt> <dd>

The server is configured to participate in RD Connection Broker load balancing.

</dd> </dl>

</dd> <dt>

**GetServerWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the server weight value that is used in RD Connection Broker load balancing.

</dd> <dt>

**GetTSRedirectorMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the server is configured to act as a Remote Desktop Services redirector.

<dt>

0
</dt> <dd>

The server is configured to act as a Remote Desktop Services redirector.

</dd> <dt>

1
</dt> <dd>

The server is not configured to act as a Remote Desktop Services redirector.

</dd> </dl>

**Windows Server 2008:** This property is not available.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Mappingstrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The date the object was installed. A lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**PolicySourceLoadBalancing**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the **GetLoadBalancingState** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceSessionDirectoryActive**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the **SessionDirectoryActive** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceSessionDirectoryClusterName**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the **SessionDirectoryClusterName** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceSessionDirectoryExposeServerIP**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the **SessionDirectoryExposeServerIP** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceSessionDirectoryLocation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the **SessionDirectoryLocation** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceTSRedirectorMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not available.

**Windows Server 2008 R2:** Indicates if the **GetTSRedirectorMode** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**SessionDirectoryActive**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Specifies if Remote Desktop Services participates in the RD Connection Broker.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Remote Desktop Services participation in the RD Connection Broker is disabled.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Remote Desktop Services participation in the RD Connection Broker is enabled.

</dd> </dl>

</dd> <dt>

**SessionDirectoryClusterName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The virtual IP address of the cluster to which the RD Session Host server belongs.

</dd> <dt>

**SessionDirectoryExposeServerIP**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies if retrieval of the IP address of the RD Connection Broker is allowed.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Retrieval is denied.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Retrieval is allowed.

</dd> </dl>

</dd> <dt>

**SessionDirectoryIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IP address of the LAN adapter used by the session directory.

</dd> <dt>

**SessionDirectoryLocation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network DNS name or IP address of the server where the RD Connection Broker service is running.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10)
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

To connect to the \\\\root\\CIMV2\\TerminalServices namespace, the authentication level must include packet privacy. For C/C++ calls, this is an authentication level of **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**. For Visual Basic and scripting calls, this is an authentication level of **WbemAuthenticationLevelPktPrivacy** or "pktPrivacy", with a value of six.

The following Visual Basic Scripting Edition (VBScript) example shows how to connect to a remote computer with packet privacy.


```VB
strComputer = "RemoteServer1" 
Set objServices = GetObject( _
    "winmgmts:{authenticationLevel=pktPrivacy}!Root/CIMv2/TerminalServices")
```



In Windows Server 2008, the name of the Terminal Services Session Directory feature was changed to Terminal Services Session Broker.

In Windows Server 2008 R2, the name of the Terminal Services Session Broker feature was changed to Remote Desktop Connection Broker.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[**Win32\_TSSessionDirectorySetting**](win32-tssessiondirectorysetting.md)
</dt> </dl>

 

