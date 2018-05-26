---
title: Win32\_ServiceSpecification class
description: The Win32\_ServiceSpecification WMI class represents a service that is to be installed with an associated package.
ms.assetid: 597dc119-bb58-4606-9fd2-b4f804c78175
keywords:
- Win32_ServiceSpecification class
- Win32_ServiceSpecification class, described
topic_type:
- apiref
api_name:
- Win32_ServiceSpecification
- Win32_ServiceSpecification.Caption
- Win32_ServiceSpecification.CheckID
- Win32_ServiceSpecification.CheckMode
- Win32_ServiceSpecification.Dependencies
- Win32_ServiceSpecification.Description
- Win32_ServiceSpecification.DisplayName
- Win32_ServiceSpecification.ErrorControl
- Win32_ServiceSpecification.ID
- Win32_ServiceSpecification.LoadOrderGroup
- Win32_ServiceSpecification.Name
- Win32_ServiceSpecification.Password
- Win32_ServiceSpecification.ServiceType
- Win32_ServiceSpecification.SoftwareElementID
- Win32_ServiceSpecification.SoftwareElementState
- Win32_ServiceSpecification.StartName
- Win32_ServiceSpecification.StartType
- Win32_ServiceSpecification.TargetOperatingSystem
- Win32_ServiceSpecification.Version
api_location:
- Msiprov.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_ServiceSpecification class

The **Win32\_ServiceSpecification** [WMI class](https://msdn.microsoft.com/library/aa393244) represents a service that is to be installed with an associated package.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ServiceSpecification : CIM_Check
{
  string  Caption;
  string  CheckID;
  Boolean CheckMode;
  string  Dependencies;
  string  Description;
  string  DisplayName;
  sint32  ErrorControl;
  string  ID;
  string  LoadOrderGroup;
  string  Name;
  string  Password;
  sint32  ServiceType;
  string  SoftwareElementID;
  uint16  SoftwareElementState;
  string  StartName;
  sint32  StartType;
  uint16  TargetOperatingSystem;
  string  Version;
};
```

## Members

The **Win32\_ServiceSpecification** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_ServiceSpecification** class has these methods.



| Method                                                              | Description                                                                                                                                                                                         |
|:--------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Invoke**](invoke-method-in-class-win32-servicespecification.md) | Evaluates a specific check. The details of how the method evaluates a specific check in a CIM context are described by the non-abstract [**CIM\_Check**](https://msdn.microsoft.com/library/aa387206) subclasses.<br/> |



 

### Properties

The **Win32\_ServiceSpecification** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the object a one-line string.

</dd> <dt>

**CheckID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier used together with other keys to uniquely identify the check.

</dd> <dt>

**CheckMode**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether or not the condition is expected to exist in the environment. When **TRUE**, the condition is expected to exist, for example, a file is expected to be on a system, so the [**Invoke**](invoke-method-in-class-win32-servicespecification.md) method is expected to return **TRUE**.

</dd> <dt>

**Dependencies**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of names of services or load ordering groups that the system must start before this service. Names in the list are separated by **null**s. If the service does not have dependencies, then **NULL** or an empty string is returned. Dependency on a group means that this service can run if at least one member of the group is running after an attempt to start all members of the group.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of an object.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Service identifier that the user interface programs use.

</dd> <dt>

**ErrorControl**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Action that the startup program takes if the service does not start during startup. One of the following error control flags must be specified. Add the value 0x08000 to the following flags to specify that the overall install fails if the service cannot be installed.



| Value                                                                                 | Meaning                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0x00000000</dt> </dl> | Logs the error and continues with the startup operation.<br/>                                                                                                                                          |
| <dl> <dt>0x00000001</dt> </dl> | Logs the error, displays a message box, and continues the startup operation.<br/>                                                                                                                      |
| <dl> <dt>0x00000003</dt> </dl> | Logs the error if it is possible, and the system is restarted with the last configuration that is known to be good. If the last good configuration is being started, the startup operation fails.<br/> |



 

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique key that identifies the service specification item within its product.

</dd> <dt>

**LoadOrderGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the load ordering group of which this service is a member.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name used to identify the software element.

</dd> <dt>

**Password**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Password associated with **StartName**.

</dd> <dt>

**ServiceType**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bit flags that specify the type of service. One of the following service types must be specified.



| Value                                                                                                                                                                                                                                                                     | Meaning                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SERVICE_WIN32_OWN_PROCESS"></span><span id="service_win32_own_process"></span><dl> <dt>**SERVICE\_WIN32\_OWN\_PROCESS**</dt> <dt>0x00000010</dt> </dl>       | Windows service that runs its own process.<br/>                                                                                            |
| <span id="SERVICE_WIN32_SHARE_PROCESS"></span><span id="service_win32_share_process"></span><dl> <dt>**SERVICE\_WIN32\_SHARE\_PROCESS**</dt> <dt>0x00000020</dt> </dl> | Windows service that shares a process.<br/>                                                                                                |
| <span id="SERVICE_INTERACTIVE_PROCESS"></span><span id="service_interactive_process"></span><dl> <dt>**SERVICE\_INTERACTIVE\_PROCESS**</dt> <dt>0x00000100</dt> </dl>  | Windows service that interacts with the desktop. This value cannot be used alone, and must be added to one of the two previous types.<br/> |



 

The following types of service are unsupported.



| Value                                                                                                                                                                                                                                                                  | Meaning                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| <span id="SERVICE_KERNEL_DRIVER"></span><span id="service_kernel_driver"></span><dl> <dt>**SERVICE\_KERNEL\_DRIVER**</dt> <dt>0x00000001</dt> </dl>                 | Driver service.<br/>             |
| <span id="SERVICE_FILE_SYSTEM_DRIVER"></span><span id="service_file_system_driver"></span><dl> <dt>**SERVICE\_FILE\_SYSTEM\_DRIVER**</dt> <dt>0x00000002</dt> </dl> | File system driver service.<br/> |



 

</dd> <dt>

**SoftwareElementID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier for the software element.

</dd> <dt>

**SoftwareElementState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

State of a software element.



| Value                                                                        | Meaning                |
|------------------------------------------------------------------------------|------------------------|
| <dl> <dt>1</dt> </dl> | Deployable<br/>  |
| <dl> <dt>2</dt> </dl> | Installable<br/> |
| <dl> <dt>3</dt> </dl> | Executable<br/>  |
| <dl> <dt>4</dt> </dl> | Running<br/>     |



 

</dd> <dt>

**StartName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Account name used to start this service.

</dd> <dt>

**StartType**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bit flags that specify when to start a service. One of the following types of service start must be specified.



| Value                                                                                                                                                                                                                                               | Meaning                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <span id="SERVICE_AUTO_START"></span><span id="service_auto_start"></span><dl> <dt>**SERVICE\_AUTO\_START**</dt> <dt>0x00000002</dt> </dl>       | Service starts during startup of the system.<br/>                                     |
| <span id="SERVICE_DEMAND_START"></span><span id="service_demand_start"></span><dl> <dt>**SERVICE\_DEMAND\_START**</dt> <dt>0x00000003</dt> </dl> | Service starts when the service control manager calls the StartService function.<br/> |
| <span id="SERVICE_DISABLED"></span><span id="service_disabled"></span><dl> <dt>**SERVICE\_DISABLED**</dt> <dt>0x00000004</dt> </dl>              | Service that cannot be started.<br/>                                                  |



 

The following types of service starts are valid only for driver services.



| Value                                                                                                                                                                                                                                               | Meaning                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="SERVICE_BOOT_START"></span><span id="service_boot_start"></span><dl> <dt>**SERVICE\_BOOT\_START**</dt> <dt>0x00000000</dt> </dl>       | Device driver started by the operating system loader.<br/>       |
| <span id="SERVICE_SYSTEM_START"></span><span id="service_system_start"></span><dl> <dt>**SERVICE\_SYSTEM\_START**</dt> <dt>0x00000001</dt> </dl> | Device driver started by the system initialization process.<br/> |



 

</dd> <dt>

**TargetOperatingSystem**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Target operating system of the software element. The possible values for this property are the following:



| Value                                                                         | Meaning                     |
|-------------------------------------------------------------------------------|-----------------------------|
| <dl> <dt>0</dt> </dl>  | Unknown<br/>          |
| <dl> <dt>1</dt> </dl>  | Other<br/>            |
| <dl> <dt>2</dt> </dl>  | MACOS<br/>            |
| <dl> <dt>3</dt> </dl>  | ATTUNIX<br/>          |
| <dl> <dt>4</dt> </dl>  | DGUX<br/>             |
| <dl> <dt>5</dt> </dl>  | DECNT<br/>            |
| <dl> <dt>6</dt> </dl>  | Digital Unix<br/>     |
| <dl> <dt>7</dt> </dl>  | OpenVMS<br/>          |
| <dl> <dt>8</dt> </dl>  | HPUX<br/>             |
| <dl> <dt>9</dt> </dl>  | AIX<br/>              |
| <dl> <dt>10</dt> </dl> | MVS<br/>              |
| <dl> <dt>11</dt> </dl> | OS400<br/>            |
| <dl> <dt>12</dt> </dl> | OS/2<br/>             |
| <dl> <dt>13</dt> </dl> | JavaVM<br/>           |
| <dl> <dt>14</dt> </dl> | MSDOS<br/>            |
| <dl> <dt>15</dt> </dl> | WIN3x<br/>            |
| <dl> <dt>16</dt> </dl> | WIN95<br/>            |
| <dl> <dt>17</dt> </dl> | WIN98<br/>            |
| <dl> <dt>18</dt> </dl> | WINNT<br/>            |
| <dl> <dt>19</dt> </dl> | WINCE<br/>            |
| <dl> <dt>20</dt> </dl> | NCR3000<br/>          |
| <dl> <dt>21</dt> </dl> | NetWare<br/>          |
| <dl> <dt>22</dt> </dl> | OSF<br/>              |
| <dl> <dt>23</dt> </dl> | DC/OS<br/>            |
| <dl> <dt>24</dt> </dl> | Reliant UNIX<br/>     |
| <dl> <dt>25</dt> </dl> | SCO UnixWare<br/>     |
| <dl> <dt>26</dt> </dl> | SCO OpenServer<br/>   |
| <dl> <dt>27</dt> </dl> | Sequent<br/>          |
| <dl> <dt>28</dt> </dl> | IRIX<br/>             |
| <dl> <dt>29</dt> </dl> | Solaris<br/>          |
| <dl> <dt>30</dt> </dl> | SunOS<br/>            |
| <dl> <dt>31</dt> </dl> | U6000<br/>            |
| <dl> <dt>32</dt> </dl> | ASERIES<br/>          |
| <dl> <dt>33</dt> </dl> | TandemNSK<br/>        |
| <dl> <dt>34</dt> </dl> | TandemNT<br/>         |
| <dl> <dt>35</dt> </dl> | BS2000<br/>           |
| <dl> <dt>36</dt> </dl> | LINUX<br/>            |
| <dl> <dt>37</dt> </dl> | Lynx<br/>             |
| <dl> <dt>38</dt> </dl> | XENIX<br/>            |
| <dl> <dt>39</dt> </dl> | VM/ESA<br/>           |
| <dl> <dt>40</dt> </dl> | Interactive UNIX<br/> |
| <dl> <dt>41</dt> </dl> | BSDUNIX<br/>          |
| <dl> <dt>42</dt> </dl> | FreeBSD<br/>          |
| <dl> <dt>43</dt> </dl> | NetBSD<br/>           |
| <dl> <dt>44</dt> </dl> | GNU Hurd<br/>         |
| <dl> <dt>45</dt> </dl> | OS9<br/>              |
| <dl> <dt>46</dt> </dl> | MACH Kernel<br/>      |
| <dl> <dt>47</dt> </dl> | Inferno<br/>          |
| <dl> <dt>48</dt> </dl> | QNX<br/>              |
| <dl> <dt>49</dt> </dl> | EPOC<br/>             |
| <dl> <dt>50</dt> </dl> | IxWorks<br/>          |
| <dl> <dt>51</dt> </dl> | VxWorks<br/>          |
| <dl> <dt>52</dt> </dl> | MiNT<br/>             |
| <dl> <dt>53</dt> </dl> | BeOS<br/>             |
| <dl> <dt>54</dt> </dl> | HP MPE<br/>           |
| <dl> <dt>55</dt> </dl> | NextStep<br/>         |
| <dl> <dt>56</dt> </dl> | PalmPilot<br/>        |
| <dl> <dt>57</dt> </dl> | Rhapsody<br/>         |



 

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version of a software element. Values should be in the form \[Major\].\[Minor\].\[Revision\] or \[Major\].\[Minor\]\[letter\]\[revision\].

</dd> </dl>

## Remarks

The **Win32\_ServiceSpecification** class is derived from [**CIM\_Check**](https://msdn.microsoft.com/library/aa387206).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





