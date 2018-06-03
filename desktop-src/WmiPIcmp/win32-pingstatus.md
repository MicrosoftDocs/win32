---
title: Win32\_PingStatus class
description: Represents the values returned by the standard ping command.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4e271877-2f49-46cc-9c95-9e67ef5c9735
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_PingStatus class
- Win32_PingStatus class, described
topic_type:
- apiref
api_name:
- Win32_PingStatus
- Win32_PingStatus.Address
- Win32_PingStatus.BufferSize
- Win32_PingStatus.NoFragmentation
- Win32_PingStatus.PrimaryAddressResolutionStatus
- Win32_PingStatus.ProtocolAddress
- Win32_PingStatus.ProtocolAddressResolved
- Win32_PingStatus.RecordRoute
- Win32_PingStatus.ReplyInconsistency
- Win32_PingStatus.ReplySize
- Win32_PingStatus.ResolveAddressNames
- Win32_PingStatus.ResponseTime
- Win32_PingStatus.ResponseTimeToLive
- Win32_PingStatus.RouteRecord
- Win32_PingStatus.RouteRecordResolved
- Win32_PingStatus.SourceRoute
- Win32_PingStatus.SourceRouteType
- Win32_PingStatus.StatusCode
- Win32_PingStatus.Timeout
- Win32_PingStatus.TimeStampRecord
- Win32_PingStatus.TimeStampRecordAddress
- Win32_PingStatus.TimeStampRecordAddressResolved
- Win32_PingStatus.TimeStampRoute
- Win32_PingStatus.TimeToLive
- Win32_PingStatus.TypeofService
api_location:
- Wmipicmp.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_PingStatus class

The **Win32\_PingStatus** [WMI class](https://msdn.microsoft.com/library/aa393244) represents the values returned by the standard **ping** command. More information about **ping** can be found in cccccccccc[RFC 791](Http://go.microsoft.com/fwlink/p/?linkid=84404).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[dynamic, provider("WMIPingProvider"), AMENDMENT]
class Win32_PingStatus
{
  string  Address;
  uint32  BufferSize = 32;
  boolean NoFragmentation = FALSE;
  uint32  PrimaryAddressResolutionStatus;
  string  ProtocolAddress = "";
  string  ProtocolAddressResolved = "";
  uint32  RecordRoute = 0;
  boolean ReplyInconsistency;
  uint32  ReplySize;
  boolean ResolveAddressNames = FALSE;
  uint32  ResponseTime;
  uint32  ResponseTimeToLive;
  string  RouteRecord[];
  string  RouteRecordResolved[];
  String  SourceRoute = "";
  uint32  SourceRouteType = 0;
  uint32  StatusCode;
  uint32  Timeout = 1000;
  uint32  TimeStampRecord[];
  string  TimeStampRecordAddress[];
  string  TimeStampRecordAddressResolved[];
  uint32  TimeStampRoute = 0;
  uint32  TimeToLive = 80;
  uint32  TypeofService = 0;
};
```

## Members

The **Win32\_PingStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PingStatus** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Value of the address requested. The form of the value can be either the computer name ("wxyz1234"), IPv4 address ("192.168.177.124"), or IPv6 address ("2010:836B:4179::836B:4179").

</dd> <dt>

**BufferSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Buffer size sent with the **ping** command. The default value is 32.

</dd> <dt>

**NoFragmentation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

If **TRUE**, "Do not Fragment" is marked on the packets sent. The default is **FALSE**, not fragmented.

</dd> <dt>

**PrimaryAddressResolutionStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Status of the address resolution process. If successful, the value is 0 (zero). Any other value indicates an unsuccessful address resolution.

<dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

**Success** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other**


</dt> <dd>1 4294967295</dd> </dl>

</dd> <dt>

**ProtocolAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (4096)
</dt> </dl>

Address that the destination used to reply. The default is "".

</dd> <dt>

**ProtocolAddressResolved**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (4096)
</dt> </dl>

Resolved address corresponding to the **ProtocolAddress** property. The default is "".

</dd> <dt>

**RecordRoute**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

How many hops should be recorded while the packet is in route. The default is 0 (zero).

</dd> <dt>

**ReplyInconsistency**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Inconsistent reply data is reported.

</dd> <dt>

**ReplySize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Represents the size of the buffer returned.

</dd> <dt>

**ResolveAddressNames**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Command resolves address names of output address values. The default is **FALSE**, which indicates no resolution.

</dd> <dt>

**ResponseTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time elapsed to handle the request.

</dd> <dt>

**ResponseTimeToLive**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time to live from the moment the request is received.

</dd> <dt>

**RouteRecord**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Record of intermediate hops.

</dd> <dt>

**RouteRecordResolved**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Resolved address that corresponds to the **RouteRecord** value.

</dd> <dt>

**SourceRoute**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Comma-separated list of valid Source Routes. The default is "".

</dd> <dt>

**SourceRouteType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Type of source route option to be used on the host list specified in the **SourceRoute** property. If a value outside of the **ValueMap** is specified, then 0 (zero) is assumed. The default is 0 (zero).

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Loose_Source_Routing"></span><span id="loose_source_routing"></span><span id="LOOSE_SOURCE_ROUTING"></span>

**Loose Source Routing** (1)


</dt> <dd></dd> <dt>

<span id="Strict_Source_Routing"></span><span id="strict_source_routing"></span><span id="STRICT_SOURCE_ROUTING"></span>

**Strict Source Routing** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**StatusCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Ping** command status codes.

<dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

**Success** (0)


</dt> <dd></dd> <dt>

<span id="Buffer_Too_Small"></span><span id="buffer_too_small"></span><span id="BUFFER_TOO_SMALL"></span>

**Buffer Too Small** (11001)


</dt> <dd></dd> <dt>

<span id="Destination_Net_Unreachable"></span><span id="destination_net_unreachable"></span><span id="DESTINATION_NET_UNREACHABLE"></span>

**Destination Net Unreachable** (11002)


</dt> <dd></dd> <dt>

<span id="Destination_Host_Unreachable"></span><span id="destination_host_unreachable"></span><span id="DESTINATION_HOST_UNREACHABLE"></span>

**Destination Host Unreachable** (11003)


</dt> <dd></dd> <dt>

<span id="Destination_Protocol_Unreachable"></span><span id="destination_protocol_unreachable"></span><span id="DESTINATION_PROTOCOL_UNREACHABLE"></span>

**Destination Protocol Unreachable** (11004)


</dt> <dd></dd> <dt>

<span id="Destination_Port_Unreachable"></span><span id="destination_port_unreachable"></span><span id="DESTINATION_PORT_UNREACHABLE"></span>

**Destination Port Unreachable** (11005)


</dt> <dd></dd> <dt>

<span id="No_Resources"></span><span id="no_resources"></span><span id="NO_RESOURCES"></span>

**No Resources** (11006)


</dt> <dd></dd> <dt>

<span id="Bad_Option"></span><span id="bad_option"></span><span id="BAD_OPTION"></span>

**Bad Option** (11007)


</dt> <dd></dd> <dt>

<span id="Hardware_Error"></span><span id="hardware_error"></span><span id="HARDWARE_ERROR"></span>

**Hardware Error** (11008)


</dt> <dd></dd> <dt>

<span id="Packet_Too_Big"></span><span id="packet_too_big"></span><span id="PACKET_TOO_BIG"></span>

**Packet Too Big** (11009)


</dt> <dd></dd> <dt>

<span id="Request_Timed_Out"></span><span id="request_timed_out"></span><span id="REQUEST_TIMED_OUT"></span>

**Request Timed Out** (11010)


</dt> <dd></dd> <dt>

<span id="Bad_Request"></span><span id="bad_request"></span><span id="BAD_REQUEST"></span>

**Bad Request** (11011)


</dt> <dd></dd> <dt>

<span id="Bad_Route"></span><span id="bad_route"></span><span id="BAD_ROUTE"></span>

**Bad Route** (11012)


</dt> <dd></dd> <dt>

<span id="TimeToLive_Expired_Transit"></span><span id="timetolive_expired_transit"></span><span id="TIMETOLIVE_EXPIRED_TRANSIT"></span>

**TimeToLive Expired Transit** (11013)


</dt> <dd></dd> <dt>

<span id="TimeToLive_Expired_Reassembly"></span><span id="timetolive_expired_reassembly"></span><span id="TIMETOLIVE_EXPIRED_REASSEMBLY"></span>

**TimeToLive Expired Reassembly** (11014)


</dt> <dd></dd> <dt>

<span id="Parameter_Problem"></span><span id="parameter_problem"></span><span id="PARAMETER_PROBLEM"></span>

**Parameter Problem** (11015)


</dt> <dd></dd> <dt>

<span id="Source_Quench"></span><span id="source_quench"></span><span id="SOURCE_QUENCH"></span>

**Source Quench** (11016)


</dt> <dd></dd> <dt>

<span id="Option_Too_Big"></span><span id="option_too_big"></span><span id="OPTION_TOO_BIG"></span>

**Option Too Big** (11017)


</dt> <dd></dd> <dt>

<span id="Bad_Destination"></span><span id="bad_destination"></span><span id="BAD_DESTINATION"></span>

**Bad Destination** (11018)


</dt> <dd></dd> <dt>

<span id="Negotiating_IPSEC"></span><span id="negotiating_ipsec"></span><span id="NEGOTIATING_IPSEC"></span>

**Negotiating IPSEC** (11032)


</dt> <dd></dd> <dt>

<span id="General_Failure"></span><span id="general_failure"></span><span id="GENERAL_FAILURE"></span>

**General Failure** (11050)


</dt> <dd></dd> </dl>

</dd> <dt>

**Timeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Time-out value in milliseconds. If a response is not received in this time, no response is assumed. The default is 1000 milliseconds.

</dd> <dt>

**TimeStampRecord**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Record of time stamps for intermediate hops.

</dd> <dt>

**TimeStampRecordAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Intermediate hop that corresponds to the **TimeStampRecord** value.

</dd> <dt>

**TimeStampRecordAddressResolved**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Resolved address that corresponds to the **TimeStampRecordAddress** value.

</dd> <dt>

**TimeStampRoute**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

How many hops should be recorded with time stamp information while the packet is in route. A time stamp is the number of milliseconds that have passed since midnight Universal Time (UT). If the time is not available in milliseconds or cannot be provided with respect to midnight UT, then any time may be inserted as a time stamp, provided the high order bit of the **Timestamp** property is set to 1 (one) to indicate the use of a nonstandard value. The default is 0 (zero).

</dd> <dt>

**TimeToLive**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Life span of the **ping** packet in seconds. The value is treated as an upper limit. All routers must decrement this value by 1 (one). When this value becomes 0 (zero), the packet is dropped by the router. The default value is 80 seconds. The hops between routers rarely take this amount of time.

</dd> <dt>

**TypeofService**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Type of service that is used. The default value is 0 (zero).

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

Normal

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Minimize Monetary Cost

</dd> <dt>

<span id="4"></span>

<span id="4"></span>**4**


</dt> <dd>

Maximize Reliability

</dd> <dt>

<span id="8"></span>

<span id="8"></span>**8**


</dt> <dd>

Maximize Throughput

</dd> <dt>

<span id="16"></span>

<span id="16"></span>**16**


</dt> <dd>

Minimize Delay

</dd> </dl>

</dd> </dl>

## Remarks

This class does not support enumeration. For more information about implementing WMI enumeration in C++, see [Enumerating WMI](https://msdn.microsoft.com/library/aa390386). In scripting, **Win32\_PingStatus** does not support the enumeration calls [**SWbemServices.InstancesOf**](https://msdn.microsoft.com/library/aa393870) or [**SWbemObject.Instances**](https://msdn.microsoft.com/library/aa393778). It does support [**SWbemServices.ExecQuery**](https://msdn.microsoft.com/library/aa393866) and [SWbemServices.GetObject](http://go.microsoft.com/fwlink/p/?linkid=121322).

## Examples

The [Get computers ping status, IP, OS version, sp version, uptime and last boot gui](https://Gallery.TechNet.Microsoft.Com/scriptcenter/Display-computers-status-c8ff289d) PowerShell sample on TechNet Gallery retrieves a variety of information from a specified system, including the Ping status, and displays the information in a GUI.

The [Collect userprofile, recycle bin and selective folder size for remote servers](https://Gallery.TechNet.Microsoft.Com/f1634012-59e2-4f7e-9a3e-75e522fc0511) PowerShell sample on TechNet Gallery uses **Win32\_PingStatus** to check whether a server is reachable.

The following PowerShell code sample demonstrates the use of **Win32\_PingStatus**.


```PowerShell
[Cmdletbinding()]
param ( 
[Parameter(Position=0,mandatory=$false,ValueFromPipeline=$true)]
[string] $comp = "localhost")

### 
# Start of Script 
### 

Process {
# Display intput
"Computer to ping: $comp"

# Now ping the system
$ping = get-wmiobject -Query "select * from win32_pingstatus where Address='$comp'"

# Display Results
if ($ping.statuscode -eq 0) {
"Computer responded in: {0}ms" -f $ping.responsetime
}
else {
"Computer did not respond"
}
}
#
```



The following VBS code sample describes using Win32\_PingStatus to retrieve information about a remote web server.


```VB
strAddress = InputBox ("Specify an address to ping", WScript.ScriptFullName, "google.com")

If GetOsVersion < "5.01" Then
  MsgBox "Unsupported Operating System", _
         vbOKOnly  + vbExclamation, WScript.ScriptFullName
  WScript.Quit
End If

Set objPing = GetObject("winmgmts:").Get("Win32_PingStatus.Address='" & strAddress & "'")

With objPing
  Wscript.Echo "Address : " & .Address
  Wscript.Echo "Buffer size : " & .BufferSize
  Wscript.Echo "No Fragmentation : " & .NoFragmentation
  Wscript.Echo "PrimaryAddressResolutionStatus : " & .PrimaryAddressResolutionStatus
  Wscript.Echo "ProtocolAddress : " & .ProtocolAddress
  Wscript.Echo "ProtocolAddressResolved : " & .ProtocolAddressResolved
  Wscript.Echo "RecordRoute : " & .RecordRoute
  Wscript.Echo "ReplyInconsistency : " & .ReplyInconsistency
  Wscript.Echo "ReplySize : " & .ReplySize
  Wscript.Echo "ResolveAddressNames : " & .ResolveAddressNames
  Wscript.Echo "ResponseTime : " & .ResponseTime
  Wscript.Echo "ResponseTimeToLive : " & .ResponseTimeToLive
  If IsNull (.RouteRecord) Then
    Wscript.Echo "RouteRecord : Null"
  Else
    Wscript.Echo "RouteRecord : " & _
           Join (.RouteRecord, "; ")
  End If
  If IsNull (.RouteRecordResolved) Then
    Wscript.Echo "RouteRecordResolved : Null"
  Else
    Wscript.Echo "RouteRecordResolved : " & _
           Join (.RouteRecordResolved, "; ")
  End If
  Wscript.Echo "SourceRoute : " & .SourceRoute
  Wscript.Echo "SourceRouteType : " & GetSourceRouteType(.SourceRouteType)
  Wscript.Echo "Status code : " & GetStatusCode(.StatusCode)
  Wscript.Echo "Timeout : " & .TimeOut
  If IsNull (.TimeStampRecord) Then
    Wscript.Echo "TimeStampRecord : Null"
  Else
    Wscript.Echo "TimeStampRecord : " & _
           Join (.TimeStampRecord, "; ")
  End If
  If IsNull (.TimeStampRecordAddress) Then
    Wscript.Echo "TimeStampRecordAddress : Null"
  Else
    Wscript.Echo "TimeStampRecordAddress : " & _
           Join (.TimeStampRecordAddress, "; ")
  End If
  If IsNull (.TimeStampRecordAddressResolved) Then
    Wscript.Echo "TimeStampRecordAddressResolved : Null"
  Else
    Wscript.Echo "TimeStampRecordAddressResolved : " & _
           Join (.TimeStampRecordAddressResolved, "; ")
  End If
  Wscript.Echo "TimeStampRoute : " & .TimeStampRoute
  Wscript.Echo "TimeToLive : " & .TimeToLive
  Wscript.Echo "TypeOfService : " & GetTypeOfService(.TypeOfService)
End With

MsgBox "The END"

' ___________________
Function GetOsVersion
  Set objWMIService = GetObject("winmgmts:") 
  Set colItems = objWMIService.ExecQuery( _
    "SELECT * FROM Win32_OperatingSystem",,48) 
  For Each objItem In colItems
    WScript.Echo objItem.Version
    GetOsVersion = objItem.Version
  Next
  Set colItems = Nothing : Set objWMIService = Nothing
End Function

' ____________________________________________
Function GetSourceRouteType (intSourceRouteType)

  Dim strType

  Select Case intSourceRouteType
  case 1
    strType = "Loose Source Routing"
  case 2
    strType = "Strict Source Routing"
  case Else
    ' Default - 0 - or any other value.
    strType = intSourceRouteType & " - None"
  End Select
  GetSourceRouteType = strType

End Function

' ______________________________________
Function GetTypeOfService (intServiceType)

  Dim strType

  Select Case intServiceType
  case 2
    strType = "Minimize Monetary Cost"
  case 4
    strType = "Maximize Reliability"
  case 8
    strType = "Maximize Throughput"
  case 16
    strType = "Minimize Delay"
  Case Else
    ' Default - 0 - or any other value.
    strType = intServiceType & " - Normal"
  End Select
  GetTypeOfService = strType

End Function

' ____________________________
Function GetStatusCode (intCode)

  Dim strStatus
  Select Case intCode
  case  0
    strStatus = "Success"
  case  11001
    strStatus = "Buffer Too Small"
  case  11002
    strStatus = "Destination Net Unreachable"
  case  11003
    strStatus = "Destination Host Unreachable"
  case  11004
    strStatus = "Destination Protocol Unreachable"
  case  11005
    strStatus = "Destination Port Unreachable"
  case  11006
    strStatus = "No Resources"
  case  11007
    strStatus = "Bad Option"
  case  11008
    strStatus = "Hardware Error"
  case  11009
    strStatus = "Packet Too Big"
  case  11010
    strStatus = "Request Timed Out"
  case  11011
    strStatus = "Bad Request"
  case  11012
    strStatus = "Bad Route"
  case  11013
    strStatus = "TimeToLive Expired Transit"
  case  11014
    strStatus = "TimeToLive Expired Reassembly"
  case  11015
    strStatus = "Parameter Problem"
  case  11016
    strStatus = "Source Quench"
  case  11017
    strStatus = "Option Too Big"
  case  11018
    strStatus = "Bad Destination"
  case  11032
    strStatus = "Negotiating IPSEC"
  case  11050
    strStatus = "General Failure"
  case Else
    strStatus = intCode & " - Unknown"
  End Select
  GetStatusCode = strStatus

End Function
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipicmp.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipicmp.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> <dt>

[WMI Tasks: Networking](https://msdn.microsoft.com/library/aa394595)
</dt> </dl>

 

 





