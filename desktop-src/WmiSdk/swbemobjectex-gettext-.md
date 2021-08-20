---
description: Returns an XML representation of an object or instance. The text file is formatted in the XML format specified as shown in WbemObjectTextFormatEnum.
ms.assetid: 98961d94-8360-4ed7-b1b1-20b4fca45d45
ms.tgt_platform: multiple
title: SWbemObjectEx.GetText_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObjectEx.GetText_
- ISWbemObjectEx.GetText_
- ISWbemObjectEx.GetText_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObjectEx.GetText\_ method

The **GetText\_** method of the [**SWbemObjectEx**](swbemobjectex.md) object returns an XML representation of an object or instance. The text file is formatted in the XML format specified as shown in [**WbemObjectTextFormatEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemobjecttextformatenum).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
strObj = .GetText_( _
  ByVal iTextFormat, _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*iTextFormat* \[in\]
</dt> <dd>

Required. A value from [**WbemObjectTextFormatEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemobjecttextformatenum) that specifies the resulting XML format.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved operation flags. The default value is 0 (zero).

</dd> <dt>

*objWbemNamedValueSet* \[in, optional\]
</dt> <dd>

An [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that sets context for the operation. The default is null. For more information about the name/value pairs permitted, see Remarks below.

</dd> </dl>

## Return value

This method has no return values.

## Error codes

After completion of the **GetText\_** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

The requested format was not found.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

One of the parameters to the call is not correct.

</dd> <dt>

**wbemErrCriticalError** - 2147749898 (0x8004100A)
</dt> <dd>

An internal, critical, and unexpected error occurred. Report this error to Microsoft Technical Support.

</dd> </dl>

## Remarks

When constructing your [**SWbemNamedValueSet**](swbemnamedvalueset.md), only the following name/value pairs are permitted.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LocalOnly</td>
<td><strong>VT_BOOL</strong><br/> If <strong>TRUE</strong>, only locally defined properties and methods are present in the resulting XML. The default is <strong>FALSE</strong>.<br/></td>
</tr>
<tr class="even">
<td>IncludeQualifiers</td>
<td><strong>VT_BOOL</strong><br/> If <strong>TRUE</strong>, qualifiers of classes, instances, properties, and methods are included in the resulting XML. The default is <strong>FALSE</strong>.<br/></td>
</tr>
<tr class="odd">
<td>PathLevel</td>
<td><strong>VT-I4</strong><br/> Default is 0 (zero). Possible values are:<br/>
<ul>
<li>0: A <CLASS> or <INSTANCE> element is created depending on whether the object is a class or instance.</li>
<li>1: A <VALUE.NAMEDOBJECT> element is generated.</li>
<li>2: A <VALUE.OBJECTWITHLOCALPATH> element is generated.</li>
<li>3: A <VALUE.OBJECTWITHPATH> element is generated.</li>
</ul></td>
</tr>
<tr class="even">
<td>ExcludeSystemProperties</td>
<td><strong>VT-BOOL</strong><br/> If <strong>TRUE</strong>, system properties, like __NAMESPACE, are excluded from the output.<br/></td>
</tr>
<tr class="odd">
<td>IncludeClassOrigin</td>
<td><strong>VT_BOOL</strong><br/> If <strong>TRUE</strong>, the class origin attribute is set on the <PROPERTY> and <METHOD> elements. The default is <strong>FALSE</strong>.<br/></td>
</tr>
</tbody>
</table>



 

For more information about creating an [**SWbemNamedValueSet**](swbemnamedvalueset.md), see [**SWbemNamedValueSet.Add**](swbemnamedvalueset-add.md).

## Examples

The following script shows how to obtain an XML representation of the [**Win32\_Bios**](/windows/desktop/CIMWin32Prov/win32-bios) class definition. By specifying a particular instance of **Win32\_Bios**, you can obtain that object's data in XML.


```VB
' Connect to the default namespace (root\cimv2) with the default
' impersonation level ("impersonate") and obtain a Win32_Bios class
' object.
Set obj = GetObject("winmgmts:win32_bios")

' Use the value for the desired XML CIM DTD format. 
XMLDtd = 1
Text = obj.GetText_(XMLDtd)
wscript.echo Text
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



 

