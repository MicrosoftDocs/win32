---
description: Use the methods and properties of the SWbemObjectPath object to construct and validate an object path. This object can be created by the VBScript CreateObject call.
ms.assetid: f2cf489d-d2a9-4926-84cf-fb33fe3d726a
ms.tgt_platform: multiple
title: SWbemObjectPath object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObjectPath
- ISWbemObjectPath
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObjectPath object

Use the methods and properties of the **SWbemObjectPath** object to construct and validate an object path. This object can be created by the VBScript **CreateObject** call.

## Members

The **SWbemObjectPath** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemObjectPath** object has these methods.



| Method                                                   | Description                                                     |
|:---------------------------------------------------------|:----------------------------------------------------------------|
| [**SetAsClass**](swbemobjectpath-setasclass.md)         | Forces the path to address a WMI class.<br/>              |
| [**SetAsSingleton**](swbemobjectpath-setassingleton.md) | Forces the path to address a singleton WMI instance.<br/> |



 

### Properties

The **SWbemObjectPath** object has these properties.



| Property                                                              | Access type           | Description                                                                                                                                                                          |
|:----------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Authority**](swbemobjectpath-authority.md)<br/>             | Read/write<br/> | String that defines the Authority component of the object path.<br/>                                                                                                           |
| [**Class**](swbemobjectpath-class.md)<br/>                     | Read/write<br/> | Name of the class that is part of the object path.<br/>                                                                                                                        |
| [**DisplayName**](swbemobjectpath-displayname.md)<br/>         | Read/write<br/> | String that contains the path in a form that can be used as a moniker display name. See [Creating a WMI Application or Script](creating-a-wmi-application-or-script.md).<br/> |
| [**IsClass**](swbemobjectpath-isclass.md)<br/>                 | Read-only<br/>  | Boolean value that indicates if this path represents a class. This is analogous to the [\_\_Genus](wmi-system-properties.md) property in the COM API.<br/>                    |
| [**IsSingleton**](swbemobjectpath-issingleton.md)<br/>         | Read-only<br/>  | Boolean value that indicates if this path represents a singleton instance.<br/>                                                                                                |
| [**Keys**](swbemobjectpath-keys.md)<br/>                       | Read-only<br/>  | An [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that contains the key value bindings.<br/>                                                                          |
| [**Locale**](swbemobjectpath-locale.md)<br/>                   | Read/write<br/> | String that contains the locale for this object path.<br/>                                                                                                                     |
| [**Namespace**](swbemobjectpath-namespace.md)<br/>             | Read/write<br/> | Name of the namespace that is part of the object path. This is the same as the [\_\_Namespace](wmi-system-properties.md) property in the COM API.<br/>                        |
| [**ParentNamespace**](swbemobjectpath-parentnamespace.md)<br/> | Read-only<br/>  | Name of the parent of the namespace that is part of the object path.<br/>                                                                                                      |
| [**Path**](swbemobjectpath-path.md)<br/>                       | Read/write<br/> | Contains the absolute path. This is the same as the [\_\_Path](wmi-system-properties.md) system property in the COM API. This is the default property of this object.<br/>    |
| [**Relpath**](swbemobjectpath-relpath.md)<br/>                 | Read/write<br/> | Contains the relative path. This is the same as the [\_\_Relpath](wmi-system-properties.md) system property in the COM API.<br/>                                              |
| [**Security\_**](swbemobjectpath-security-.md)<br/>            | Read-only<br/>  | Used to read or change the security settings.<br/>                                                                                                                             |
| [**Server**](swbemobjectpath-server.md)<br/>                   | Read/write<br/> | Name of the server. This is the same as the [\_\_Server](wmi-system-properties.md) system property in the COM API.<br/>                                                       |



 

## Examples

The following VBScript code sample demonstrates how to build object paths.


```VB
on error resume next 
Set ObjectPath = CreateObject("WbemScripting.SWbemObjectPath")
ObjectPath.Server = "dingle"
ObjectPath.Namespace = "root/default/something"
ObjectPath.Class = "ho"
ObjectPath.Keys.Add "fred1", 10
ObjectPath.Keys.Add "fred2", -34
ObjectPath.Keys.Add "fred3", 65234654
ObjectPath.Keys.Add "fred4", "Wahaay"
ObjectPath.Keys.Add "fred5", -786186777

if err <> 0 then 
 WScript.Echo err.number
end if 

WScript.Echo "Pass 1:"
WScript.Echo ObjectPath.Path
WScript.Echo ObjectPath.DisplayName
WScript.Echo ""

ObjectPath.Security_.ImpersonationLevel = 3

WScript.Echo "Pass 2:"
WScript.Echo ObjectPath.Path
WScript.Echo ObjectPath.DisplayName
WScript.Echo ""

ObjectPath.Security_.AuthenticationLevel = 5

WScript.Echo "Pass 3:"
WScript.Echo ObjectPath.Path
WScript.Echo ObjectPath.DisplayName
WScript.Echo ""

Set Privileges = ObjectPath.Security_.Privileges
if err <> 0 then
 WScript.Echo Hex(Err.Number), Err.Description
end if
Privileges.Add 8
Privileges.Add 20, false

WScript.Echo "Pass 4:"
WScript.Echo ObjectPath.Path
WScript.Echo ObjectPath.DisplayName
WScript.Echo ""

ObjectPath.DisplayName = "winmgmts:{impersonationLevel=impersonate,authenticationLevel=pktprivacy,(Debug,!IncreaseQuota, CreatePagefile ) }!//fred/root/blah"

WScript.Echo "Pass 5:"
WScript.Echo ObjectPath.Path
WScript.Echo ObjectPath.DisplayName
WScript.Echo ""
```



The following Perl code sample demonstrates how to build object paths.


```
use strict;
use Win32::OLE;
use constant FALSE=>"false";

my ( $ObjectPath, $Privileges );

eval { $ObjectPath = new Win32::OLE 'WbemScripting.SWbemObjectPath'; };
unless($@)
{
 eval
 {
  $ObjectPath->{Server} = "dingle";
  $ObjectPath->{Namespace} = "root/default/something";
  $ObjectPath->{Class} = "ho";
  $ObjectPath->{Keys}->Add("fred1", 10);
  $ObjectPath->{Keys}->Add("fred2", -34);
  $ObjectPath->{Keys}->Add("fred3", 65234654);
  $ObjectPath->{Keys}->Add("fred4", "Wahaay");
  $ObjectPath->{Keys}->Add("fred5", -786186777);
 };
 unless($@)
 {
  print "\n";
  print "Pass 1:\n";
  print $ObjectPath->{Path}, "\n";
  print $ObjectPath->{DisplayName} , "\n\n";

  $ObjectPath->{Security_}->{ImpersonationLevel} = 3 ;

  print "Pass 2:\n";
  print $ObjectPath->{Path}, "\n";
  print $ObjectPath->{DisplayName} , "\n\n";

  $ObjectPath->{Security_}->{AuthenticationLevel} = 5 ;

  print "Pass 3:\n";
  print $ObjectPath->{Path}, "\n";
  print $ObjectPath->{DisplayName} , "\n\n";

  eval { $Privileges = $ObjectPath->{Security_}->{Privileges}; };
  unless($@)
  {
   $Privileges->Add(8);
   $Privileges->Add(20,FALSE);

   print "Pass 4:\n";
   print $ObjectPath->{Path}, "\n";
   print $ObjectPath->{DisplayName} , "\n\n";

   $ObjectPath->{DisplayName} = "winmgmts:{impersonationLevel=impersonate,authenticationLevel=pktprivacy,(Debug,!IncreaseQuota, CreatePagefile ) }!//fred/root/blah";

   print "Pass 5:\n";
   print $ObjectPath->{Path}, "\n";
   print $ObjectPath->{DisplayName} , "\n";
  }
  else
  {
   print STDERR Win32::OLE->LastError, "\n";
  }
 }
 else
 {
  print STDERR Win32::OLE->LastError, "\n";
 }
}
else
{
 print STDERR Win32::OLE->LastError, "\n";
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemObjectPath<br/>                                                       |
| IID<br/>                      | IID\_ISWbemObjectPath<br/>                                                        |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




