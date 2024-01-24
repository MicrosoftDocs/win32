---
description: The following lists the qualifiers use to define View Provider classes.
ms.assetid: 31a6af2d-33da-44f2-86d7-c467dd2f3e00
ms.tgt_platform: multiple
title: Qualifiers Specific to the View Provider
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Qualifiers
api_type: 
- NA
api_location: 
---

# Qualifiers Specific to the View Provider

The following lists the qualifiers use to define View Provider classes.

> [!Note]  
> The View provider class only supports NetBIOS names when using remote references. If you use an IP address or a DNS name in a remote reference, then the connection fails with a 0x800706ba error.

 

<dt>

<span id="Direct"></span><span id="direct"></span><span id="DIRECT"></span>**Direct**
</dt> <dd>

Data type: **boolean**

Used with view association properties to prevent association references from being mapped to a view reference.

The following example defines the property **GroupComponent** as an association reference that is not mapped in the view reference.


```mof
[Direct, key, PropertySources
{"GroupComponent"}]
```



</dd> <dt>

<span id="HiddenDefault"></span><span id="hiddendefault"></span><span id="HIDDENDEFAULT"></span>**HiddenDefault**
</dt> <dd>

Data type: **boolean**

Default value for a view class property based on a source class property with a different default value. The underlying source class is implied by the view.

For example, the source class [**Win32\_ScheduledJob**](/windows/desktop/CIMWin32Prov/win32-scheduledjob) has a [boolean](boolean.md) property **RunRepeatedly** that indicates whether the job is to be carried out periodically or one time only. The default value of **RunRepeatedly** is not True for **Win32\_ScheduledJob**, but is True for the view class.


```mof
#pragma namespace("\\\\.\\root\\ns_view")
[Union,
ViewSources{"select * from Win32_ScheduledJob where RunRepeatedly=True"},
ViewSpaces{"\\\\.\\root\\cimv2"},
dynamic,provider("MS_VIEW_INSTANCE_PROVIDER")]
Class View_PeriodicJob
{
 [key, PropertySources{"JobId"}]
 uint32 JobId;
 [PropertySources{"Command"}]
 string Command;
 [HiddenDefault,PropertySources{"RunRepeatedly"}]
 boolean Repeat = True;
};
```



</dd> <dt>

<span id="JoinOn"></span><span id="joinon"></span><span id="JOINON"></span>**JoinOn**
</dt> <dd>

Data type: **string**

Defines how source class instances are joined in join view classes. The following example shows how to use the **JoinOn** qualifier to join two source classes.


```mof
JoinOn("Win32Perf_RawProcess.IDProcess = Win32Perf_RawThread.IDProcess")
```



</dd> <dt>

<span id="MethodSource"></span><span id="methodsource"></span><span id="METHODSOURCE"></span>**MethodSource**
</dt> <dd>

Data type: **string array**

Source method to execute for the view method. For similar syntax, see [PropertySources Qualifier](propertysources-qualifier.md). The signature of the method must match the signature of the source class exactly. Copy the method signature from the MOF file that defines the source class. The example below defines a method from the [**ClearEventLog**](/previous-versions/windows/desktop/eventlogprov/cleareventlog-method-in-class-win32-nteventlogfile) method of [**Win32\_NTEventlogFile**](/previous-versions/windows/desktop/legacy/aa394225(v=vs.85)):


```mof
[implemented, MethodSource
{"ClearEventlog"}]
  uint32   VClearEventlog([in] string ArchiveFileName);
```



This qualifier is only valid when it is used with union views.

</dd> <dt>

<span id="PostJoinFilter"></span><span id="postjoinfilter"></span><span id="POSTJOINFILTER"></span>[**PostJoinFilter**](postjoinfilter-qualifier.md)
</dt> <dd>

Data type: **string**

WQL query to filter instances after they have been joined in a join class.

</dd> <dt>

<span id="PropertySources"></span><span id="propertysources"></span><span id="PROPERTYSOURCES"></span>[**PropertySources**](propertysources-qualifier.md)
</dt> <dd>

Data type: **string array**

Source properties from which a view class property gets data.

</dd> <dt>

<span id="Union"></span><span id="union"></span><span id="UNION"></span>**Union**
</dt> <dd>

Data type: **boolean**

Indicates whether you are defining a union class. Union views contain instances based on the union of source instances. For example, you might declare the following:


```mof
Union, ViewSources{"SELECT Handle, Name, CreationDate FROM Win32_Process", 
                   "SELECT Caption, Name, ProcessHandle FROM Win32_Thread"}.
```



</dd> <dt>

<span id="ViewSources"></span><span id="viewsources"></span><span id="VIEWSOURCES"></span>[**ViewSources**](viewsources-qualifier.md)
</dt> <dd>

Data type: **string array**

Set of WMI Query Language (WQL) queries that define the source instances and properties used in a specific view class. Positional correspondence of all the array qualifiers is important.

</dd> <dt>

<span id="ViewSpaces"></span><span id="viewspaces"></span><span id="VIEWSPACES"></span>[**ViewSpaces**](viewspaces-qualifier.md)
</dt> <dd>

Data type: **string array**

Namespaces where the source instances are located.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



 

