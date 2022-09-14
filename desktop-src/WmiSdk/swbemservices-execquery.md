---
description: SWbemServices.ExecQuery method - Executes a query to retrieve objects.
ms.assetid: 06b9d4c9-cd72-49b2-92b0-d18d94dfbd9f
ms.tgt_platform: multiple
title: SWbemServices.ExecQuery method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServices.ExecQuery
- ISWbemServices.ExecQuery
- ISWbemServices.ExecQuery
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServices.ExecQuery method

The **ExecQuery** method of the [**SWbemServices**](swbemservices.md) object executes a query to retrieve objects. These objects are available through the returned [**SWbemObjectSet**](swbemobjectset.md) collection.

This method is called in the semisynchronous mode. For more information, see [Calling a Method](calling-a-method.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObjectSet = .ExecQuery( _
  ByVal strQuery, _
  [ ByVal strQueryLanguage ], _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*strQuery* 
</dt> <dd>

Required. String that contains the text of the query. This parameter cannot be blank. For more information on building WMI query strings, see [Querying with WQL](querying-with-wql.md) and the [WQL](wql-sql-for-wmi.md) reference.

</dd> <dt>

*strQueryLanguage* \[optional\]
</dt> <dd>

String that contains the query language to be used. If specified, this value must be "WQL".

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

Integer that determines the behavior of the query and determines whether this call returns immediately. The default value for this parameter is **wbemFlagReturnImmediately**. This parameter can accept the following values.

<dt>

<span id="wbemFlagForwardOnly"></span><span id="wbemflagforwardonly"></span><span id="WBEMFLAGFORWARDONLY"></span>

<span id="wbemFlagForwardOnly"></span><span id="wbemflagforwardonly"></span><span id="WBEMFLAGFORWARDONLY"></span>****wbemFlagForwardOnly**** (32 (0x20))


</dt> <dd>

Causes a forward-only enumerator to be returned. Forward-only enumerators are generally much faster and use less memory than conventional enumerators, but they do not allow calls to [**SWbemObject.Clone\_**](swbemobject-clone-.md).

</dd> <dt>

<span id="wbemFlagBidirectional"></span><span id="wbemflagbidirectional"></span><span id="WBEMFLAGBIDIRECTIONAL"></span>

<span id="wbemFlagBidirectional"></span><span id="wbemflagbidirectional"></span><span id="WBEMFLAGBIDIRECTIONAL"></span>****wbemFlagBidirectional**** (0 (0x0))


</dt> <dd>

Causes WMI to retain pointers to objects of the enumeration until the client releases the enumerator.

</dd> <dt>

<span id="wbemFlagReturnImmediately"></span><span id="wbemflagreturnimmediately"></span><span id="WBEMFLAGRETURNIMMEDIATELY"></span>

<span id="wbemFlagReturnImmediately"></span><span id="wbemflagreturnimmediately"></span><span id="WBEMFLAGRETURNIMMEDIATELY"></span>****wbemFlagReturnImmediately**** (16 (0x10))


</dt> <dd>

Causes the call to return immediately.

</dd> <dt>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>****wbemFlagReturnWhenComplete**** (0 (0x0))


</dt> <dd>

Causes this call to block until the query is complete. This flag calls the method in the synchronous mode.

</dd> <dt>

<span id="wbemQueryFlagPrototype"></span><span id="wbemqueryflagprototype"></span><span id="WBEMQUERYFLAGPROTOTYPE"></span>

<span id="wbemQueryFlagPrototype"></span><span id="wbemqueryflagprototype"></span><span id="WBEMQUERYFLAGPROTOTYPE"></span>****wbemQueryFlagPrototype**** (2 (0x2))


</dt> <dd>

Used for prototyping. This flag stops the query from happening and returns an object that looks like a typical result object.

</dd> <dt>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>****wbemFlagUseAmendedQualifiers**** (131072 (0x20000))


</dt> <dd>

Causes WMI to return class amendment data with the base class definition. For more information, see [Localizing WMI Class Information](localizing-wmi-class-information.md).

</dd> </dl> </dd> <dt>

*objWbemNamedValueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If no error occurs, this method returns an [**SWbemObjectSet**](swbemobjectset.md) object. This is an object collection that contains the result set of the query. The caller can examine the collection using the implementation of collections for the programming language you are using. For more information, see [Accessing a Collection](accessing-a-collection.md).

## Error codes

After the completion of the **ExecQuery** method, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object can contain one of the error codes in the following list.

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user does not have the permission to view the result set.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

Invalid parameter was specified.

</dd> <dt>

**wbemErrInvalidQuery** - 2147749911 (0x80041017)
</dt> <dd>

Query syntax is not valid.

</dd> <dt>

**wbemErrInvalidQueryType** - 2147749912 (0x80041018)
</dt> <dd>

Requested query language is not supported.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> </dl>

## Remarks

**ExecQuery** is one of the most commonly-used calls to retrieve WMI information. A standard call to **ExecQuery** looks like the following:


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")

Set colServices = objWMIService.ExecQuery ("Select * from Win32_Service where Name='Alerter'")
For Each objService in colServices
    Return = objService.StopService()
    If Return <> 0 Then
        Wscript.Echo "Failed " &VBNewLine & "Error code = " & Return 
    Else
       WScript.Echo "Succeeded"
    End If
Next
```



Note that you create the [**SWbemServices**](swbemservices.md) object with a moniker that represents the appropriate namespace and security, then make the **ExecQuery** call through the service. For a more complete discussion, see [Creating a WMI Script](creating-a-wmi-script.md) and [Enumerating WMI](enumerating-wmi.md).

Like the [**InstancesOf**](swbemservices-instancesof.md) method, the **ExecQuery** method always returns an [**SWbemObjectSet**](swbemobjectset.md) collection. Thus your WMI script must enumerate the collection ExecQuery returns in order to access each managed resource instance in the collection, as shown here:


```VB
strComputer = "."
Set objSWbemServices = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
Set colSWbemObjectSet = objSWbemServices.ExecQuery _
   ("SELECT * FROM Win32_Service")
For Each objSWbemObject In colSWbemObjectSet
    Wscript.Echo "Name: " & objSWbemObject.Name
Next
```



Other [**SWbemServices**](swbemservices.md) methods that return an [**SWbemObjectSet**](swbemobjectset.md) include [**AssociatorsOf**](swbemservices-associatorsof.md), [**ReferencesTo**](swbemservices-referencesto.md), and [**SubclassesOf**](swbemservices-subclassesof.md).

It is not an error for the query to return an empty result set. The **ExecQuery** method returns key properties whether or not the key property is requested in the *strQuery* argument. If an error occurs when executing this method and you do not use the **wbemFlagReturnImmediately** flag, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object is not set until you attempt to access the returned object set. However, if you use the **wbemFlagReturnWhenComplete** flag, the Err object is set when the **ExecQuery** method is called.

There are limits to the number of **AND** and **OR** keywords that can be used in WQL queries. Large numbers of WQL keywords that are used in a complex query can cause WMI to return the **WBEM\_E\_QUOTA\_VIOLATION** error code as an **HRESULT** value. The limit of WQL keywords depends on how complex the query is.

## Examples

The following VBScript code example locates all the disk drives on the local computer and displays the device ID and the type of the disk drive.


```VB
Set colDisks = GetObject( _
    "Winmgmts:").ExecQuery("Select * from Win32_LogicalDisk")
For Each objDisk in colDisks
 
    Select Case objDisk.DriveType
        Case 1
            Wscript.Echo "No root directory. Drive type could not be determined."
        Case 2
            Wscript.Echo "DeviceID= "& objDisk.DeviceID & "  DriveType = Removable drive" 
        Case 3
            Wscript.Echo "DeviceID= "& objDisk.DeviceID & "  DriveType = Local hard disk" 
        Case 4
            Wscript.Echo "DeviceID= "& objDisk.DeviceID & "  DriveType = Network disk" 
        Case 5
            Wscript.Echo "DeviceID= "& objDisk.DeviceID & "  DriveType = Compact disk" 
        Case 6
            Wscript.Echo "DeviceID= "& objDisk.DeviceID & "  DriveType = RAM disk" 
        Case Else
            Wscript.Echo "Drive type could not be determined."
    End Select
Next
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemServices<br/>                                                         |
| IID<br/>                      | IID\_ISWbemServices<br/>                                                          |



## See also

<dl> <dt>

[**SWbemServices**](swbemservices.md)
</dt> <dt>

[**SWbemServices.Get**](swbemservices-get.md)
</dt> <dt>

[Querying with WQL](querying-with-wql.md)
</dt> <dt>

[Creating a WMI Script](creating-a-wmi-script.md)
</dt> <dt>

[Enumerating WMI](enumerating-wmi.md)
</dt> </dl>

 

