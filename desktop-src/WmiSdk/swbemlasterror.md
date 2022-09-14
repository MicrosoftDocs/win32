---
description: The methods and properties of the SWbemLastError object contain and manipulate error objects.
ms.assetid: 11a652fa-29e8-437b-8e62-e28e56a8a38d
ms.tgt_platform: multiple
title: SWbemLastError object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemLastError
- Associators_
- AssociatorsAsync_
- Delete_
- DeleteAsync_
- ExecMethod_
- ExecMethodAsync_
- Instances_
- InstancesAsync_
- Put_
- PutAsync_
- References_
- ReferencesAsync_
- SpawnDerivedClass_
- SpawnInstance_
- Subclasses_
- SubclassesAsync_
- Derivation_
- get_Derivation_
- Methods_
- get_Methods_
- Qualifiers_
- get_Qualifiers_
- Security_
- get_Security_
- ISWbemLastError
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemLastError object

The methods and properties of the **SWbemLastError** object contain and manipulate error objects. The methods and properties of this object are exactly the same as those of the [**SWbemObject**](swbemobject.md) object, but are used to contain error information instead of WMI class information. This object can be created by the VBScript **CreateObject** call.

You can create an **SWbemLastError** error object to inspect the extended error information that is associated with a previous method call. If error information is not available, an attempt to create an error object will fail. If the call succeeds and an error object returns, the status of the object is reset. Further attempts to retrieve an error object will fail until a new error occurs. If you make an asynchronous call that fails, an **SWbemLastError** object may be returned to you by the [**SWbemSink.OnCompleted**](swbemsink-oncompleted.md) event in the *objWbemErrorObject* parameter.

## Members

The **SWbemLastError** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemLastError** object has these methods.



| Method                                                   | Description                                                                                  |
|:---------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| **Associators\_**                                        | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **AssociatorsAsync\_**                                   | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| [**Clone\_**](swbemlasterror-clone-.md)                 | Makes a copy of the current object.<br/>                                               |
| [**CompareTo\_**](swbemlasterror-compareto-.md)         | Tests two objects for equality.<br/>                                                   |
| **Delete\_**                                             | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **DeleteAsync\_**                                        | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **ExecMethod\_**                                         | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **ExecMethodAsync\_**                                    | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| [**GetObjectText\_**](swbemlasterror-getobjecttext-.md) | Retrieves the textual representation of the object written with MOF syntax.<br/>       |
| **Instances\_**                                          | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **InstancesAsync\_**                                     | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **Put\_**                                                | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **PutAsync\_**                                           | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **References\_**                                         | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **ReferencesAsync\_**                                    | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **SpawnDerivedClass\_**                                  | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **SpawnInstance\_**                                      | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **Subclasses\_**                                         | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |
| **SubclassesAsync\_**                                    | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/> |



 

### Properties

The **SWbemLastError** object has these properties.



| Property                                                      | Access type          | Description                                                                                                                                                   |
|:--------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Derivation\_**<br/>                                   | Read-only<br/> | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/>                                                                  |
| **Methods\_** <br/>                                     | Read-only<br/> | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/>                                                                  |
| [**Path\_**](swbemlasterror-path-.md)<br/>             | Read-only<br/> | Contains an [**SWbemObjectPath**](swbemobjectpath.md) object that represents the object path of the current class or instance.<br/>                    |
| [**Properties\_**](swbemlasterror-properties-.md)<br/> | Read-only<br/> | Represents the collection of properties of the **SWbemLastError** object. This property is an [**SWbemPropertySet**](swbempropertyset.md) object.<br/> |
| **Qualifiers\_**<br/>                                   | Read-only<br/> | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/>                                                                  |
| **Security\_**<br/>                                     | Read-only<br/> | Not used. The [**SWbemObject**](swbemobject.md) object provides the same method.<br/>                                                                  |



 

## Examples

The following VBScript sample demonstrates how to inspect error and error object information.


```VB
On Error Resume Next

'Ask for non-existent class to force error

Set t_Service = GetObject("winmgmts://./root/default")
Set t_Object = t_Service.Get("Nosuchclass000")

if Err = 0 Then
 WScript.Echo "Got a class"
Else
 WScript.Echo ""
 WScript.Echo "Err Information:"
 WScript.Echo ""
 WScript.Echo "  Source:", Err.Source
 WScript.Echo "  Description:", Err.Description
 WScript.Echo "  Number", "0x" & Hex(Err.Number)

 'Create the last error object
 set t_Object = CreateObject("WbemScripting.SWbemLastError")
 WScript.Echo ""
 WScript.Echo "WMI Last Error Information:"
 WScript.Echo ""
 WScript.Echo " Operation:", t_Object.Operation
 WScript.Echo " Provider:", t_Object.ProviderName

 strDescr = t_Object.Description
 strPInfo = t_Object.ParameterInfo
 strCode = t_Object.StatusCode

 if (strDescr <> nothing) Then
  WScript.Echo " Description:", strDescr  
 end if

 if (strPInfo <> nothing) Then
  WScript.Echo " Parameter Info:", strPInfo  
 end if

 if (strCode <> nothing) Then
  WScript.Echo " Status:", strCode  
 end if

 WScript.Echo ""
 Err.Clear
 set t_Object2 = CreateObject("WbemScripting.SWbemLastError")
 if Err = 0 Then
    WScript.Echo "Got the error object again - this shouldn't have happened!" 
 Else
    Err.Clear
    WScript.Echo "Couldn't get last error again - as expected"
 End if
End If

```



The following Perl sample demonstrates how to inspect error and error object information.


```
use strict;
use Win32::OLE;

my ( $t_Service, $t_Object, $t_Object2, $strDescr, $strPInfo, $strCode );

# Close STDERR file handle to eliminate redundant error message
close(STDERR);

# Ask for non-existent class to force error 
$t_Service = Win32::OLE->GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\default"); 
$t_Object = $t_Service->Get("Nosuchclass000");

if (defined $t_Object)
{
 print "Got a class\n"; 
}
else
{
 print "\nErr Information:\n\n";
 print Win32::OLE->LastError, "\n";

 # Create the last error object
 $t_Object = new Win32::OLE 'WbemScripting.SWbemLastError';
 print "\nWMI Last Error Information:\n\n";
 print " Operation: ", $t_Object->{Operation}, "\n";
 print " Provider: ", $t_Object->{ProviderName}, "\n";
 
 $strDescr = $t_Object->{Description};
 $strPInfo = $t_Object->{ParameterInfo};
 $strCode = $t_Object->{StatusCode};

 if (defined $strDescr)
 {
  print " Description: ", $strDescr, "\n";  
 }

 if (defined $strPInfo)
 {
  print " Parameter Info: ", $strPInfo, "\n";  
 }

 if (defined $strCode)
 {
  print " Status: ", $strCode, "\n";  
 }

 print "\n";

 $t_Object2 = new Win32::OLE 'WbemScripting.SWbemLastError';
 if (defined $t_Object2)
 {
  print "Got the error object again - this shouldn't have happened!\n";
 }
 else
 {
  print "Couldn't get last error again - as expected\n";
 }
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
| CLSID<br/>                    | CLSID\_SWbemLastError<br/>                                                        |
| IID<br/>                      | IID\_ISWbemLastError<br/>                                                         |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




