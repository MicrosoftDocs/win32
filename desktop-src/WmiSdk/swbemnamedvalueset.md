---
description: An SWbemNamedValueSet object is a collection of SWbemNamedValue objects.
ms.assetid: 7d1c3a28-d0d3-4108-9628-74ad483e328e
ms.tgt_platform: multiple
title: SWbemNamedValueSet object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemNamedValueSet
- ISWbemNamedValueSet
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemNamedValueSet object

An **SWbemNamedValueSet** object is a collection of [**SWbemNamedValue**](swbemnamedvalue.md) objects. The methods and properties of **SWbemNamedValueSet** are used principally to send more information to providers when submitting certain calls to WMI. All calls in [**SWbemServices**](swbemservices.md), and some calls in [**SWbemObject**](swbemobject.md), take an optional parameter that is an object of this type. A client can add information to an **SWbemNamedValueSet** object, and send the **SWbemNamedValueSet** object with the call as one of the parameters. This object can be created by the VBScript **CreateObject** call.

For more information, see [Accessing a Collection](accessing-a-collection.md).

> [!Note]  
> Important - If possible, do not use this mechanism because it can break the uniform access model that is the basis of WMI. If a provider does use this mechanism, it is important that this mechanism is used as sparingly as possible. If a provider requires a large amount of highly specific context information to respond to a request, all clients must be coded to provide this information. This mechanism allows you to access such providers, if necessary.

 

An **SWbemNamedValueSet** object is a collection of [**SWbemNamedValue**](swbemnamedvalue.md) elements. These items are added to the collection using the [**SWbemNamedValueSet.Add**](swbemnamedvalueset-add.md) method. They are removed using the [**SWbemNamedValueSet.Remove**](swbemnamedvalueset-remove.md) method and retrieved using the [**SWbemNamedValueSet.Item**](swbemnamedvalueset-item.md) method. You can access the methods to fill in any context information that is required by a dynamic provider. After you call one of the [**SWbemServices**](swbemservices.md) methods, you can reuse the **SWbemNamedValueSet** object for another call.

The underlying provider determines the information that is contained in an **SWbemNamedValueSet** object. WMI makes no use of the information, but simply forwards it to the provider. Providers must publish the context information they require to service requests.

## Members

The **SWbemNamedValueSet** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemNamedValueSet** object has these methods.



| Method                                            | Description                                                                                                                              |
|:--------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](swbemnamedvalueset-add.md)             | Adds an [**SWbemNamedValue**](swbemnamedvalue.md) object to the collection.<br/>                                                  |
| [**Clone**](swbemnamedvalueset-clone.md)         | Makes a copy of this **SWbemNamedValueSet** collection.<br/>                                                                       |
| [**DeleteAll**](swbemnamedvalueset-deleteall.md) | Removes all items from the collection, making the **SWbemNamedValueSet** object empty.<br/>                                        |
| [**Item**](swbemnamedvalueset-item.md)           | Retrieves an [**SWbemNamedValue**](swbemnamedvalue.md) object from the collection. This is the default method of the object.<br/> |
| [**Remove**](swbemnamedvalueset-remove.md)       | Removes an [**SWbemNamedValue**](swbemnamedvalue.md) object from the collection.<br/>                                             |



 

### Properties

The **SWbemNamedValueSet** object has these properties.



| Property                                             | Access type          | Description                                       |
|:-----------------------------------------------------|:---------------------|:--------------------------------------------------|
| [**Count**](swbemnamedvalueset-count.md)<br/> | Read-only<br/> | The number of items in the collection.<br/> |



 

## Examples

The following VBScript sample demonstrates the manipulation of named value sets, in the case that the named value is an array type.


```VB
Set Context = CreateObject("WbemScripting.SWbemNamedValueSet")

On Error Resume Next

Context.Add "n1", Array (1, 2, 3)
str = "The initial value of n1 is {"
for x=LBound(Context("n1")) to UBound(Context("n1"))
 str = str & Context("n1")(x)
 if x <> UBound(Context("n1")) Then
  str = str & ", "
 End if
next
str = str & "}"
WScript.Echo str

WScript.Echo ""

' report the value of an element of the context value
v = Context("n1")
WScript.Echo "By indirection the first element of n1 has value:",v(0)

' report the value directly
WScript.Echo "By direct access the first element of n1 has value:", Context("n1")(0)

' set the value of a single named value element
Context("n1")(1) = 11 
WScript.Echo "After direct assignment the first element of n1 has value:", Context("n1")(1)

' set the value of a single named value element
Set v = Context("n1")
v(1) = 345
WScript.Echo "After indirect assignment the first element of n1 has value:", Context("n1")(1)

' set the value of an entire context value
Context("n1") = Array (5, 34, 178871)
WScript.Echo "After direct array assignment the first element of n1 has value:", Context("n1")(1)

str = "After direct assignment the entire value of n1 is {"
for x=LBound(Context("n1")) to UBound(Context("n1"))
 str = str & Context("n1")(x)
 if x <> UBound(Context("n1")) Then
  str = str & ", "
 End if
next
str = str & "}"
WScript.Echo str

if Err <> 0 Then
 WScript.Echo Err.Description
 Err.Clear
End if
```



The following Perl sample demonstrates the manipulation of named value sets, in the case that the named value is an array type.


```
use strict;
use Win32::OLE;

my ( $Context, $str, $x, @v);

eval {$Context = new Win32::OLE 'WbemScripting.SWbemNamedValueSet'; };
unless($@)
{
 $Context->Add("n1", [1, 2, 3]);
 $str = "The initial value of n1 is {";
 for ($x = 0; $x < @{$Context->Item("n1")->{Value}}; $x++)
 {
  $str = $str.@{$Context->Item("n1")->{Value}}[$x];
  if ($x != (@{$Context->Item("n1")->{Value}}) - 1 )
  {
   $str = $str.", ";
  }
 }
 $str = $str."}";
 print $str,"\n\n";

 # report the value of an element of the context value
 @v = @{$Context->Item("n1")->{Value}};
 print "By indirection the first element of n1 has value:", $v[0], "\n";

 # report the value directly
 print "By direct access the first element of n1 has value:", @{$Context->Item("n1")->{Value}}[0], "\n";

 # set the value of a single named value element
 @{$Context->Item("n1")->{Value}}[1] = 11;
 print "After direct assignment the first element of n1 has value:", 
       @{$Context->Item("n1")->{Value}}[1], "\n";

 # set the value of a single named value element
 @v = @{$Context->Item("n1")->{Value}};
 $v[1] = 345;
 print "After indirect assignment the first element of n1 has value:", 
    @{$Context->Item("n1")->{Value}}[1], "\n";

 # set the value of an entire context value
 $Context->Item("n1")->{Value} = [5, 34, 178871];
 print "After direct array assignment the first element of n1 has value:", 
   @{$Context->Item("n1")->{Value}}[1], "\n";

 $str = "After direct assignment the entire value of n1 is {";
 for ($x = 0; $x < @{$Context->Item("n1")->{Value}}; $x++)
 {
  $str = $str.@{$Context->Item("n1")->{Value}}[$x];
  if ($x != (@{$Context->Item("n1")->{Value}}) - 1 )
  {
   $str = $str.", ";
  }
 }
 $str = $str."}";
 print $str,"\n";
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
| CLSID<br/>                    | CLSID\_SWbemNamedValueSet<br/>                                                    |
| IID<br/>                      | IID\_ISWbemNamedValueSet<br/>                                                     |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




