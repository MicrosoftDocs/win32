---
description: Returns an SWbemPropertySet object that contains the collection of WMI System Properties that apply to the object.
ms.assetid: e95c325a-8851-4f55-a99d-4346d064e308
ms.tgt_platform: multiple
title: SWbemObjectEx.SystemProperties_ property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObjectEx.SystemProperties_
- ISWbemObjectEx.SystemProperties_
- ISWbemObjectEx.get_SystemProperties_
- ISWbemObjectEx.put_SystemProperties_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObjectEx.SystemProperties\_ property

The **SystemProperties\_** property of the [**SWbemObjectEx**](swbemobjectex.md) object returns an [**SWbemPropertySet**](swbempropertyset.md) object that contains the collection of [WMI System Properties](wmi-system-properties.md) that apply to the object.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemObjectEx.SystemProperties_ As Object
```



## Property value

## Examples

The following code sample retrieves the property values for the Win32\_Process class.


```VB
Set objWmi = GetObject ("winmgmts:root\cimv2")
Set objClass = objWmi.Get("Win32_Process")

' SWbemObjectEx.SystemProperties_ returns 
' an SWbemPropertySet object that contains the collection
' of sytem properties for Win32_Process class

For Each objProperty In objClass.SystemProperties_

    WScript.Echo vbCrLf & objProperty.Name & ":"

    ' Have to take into account that
    ' __Derivation is an array

    If Not objProperty.IsArray Then
        WScript.Echo vbTab & objProperty.Value
    Else
        For Each strValue In objProperty.Value
            WScript.Echo vbTab & strValue
        Next
    End If

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
| CLSID<br/>                    | CLSID\_SWbemObjectEx<br/>                                                         |
| IID<br/>                      | IID\_ISWbemObjectEx<br/>                                                          |



## See also

<dl> <dt>

[**SWbemObjectEx**](swbemobjectex.md)
</dt> </dl>

 

 




