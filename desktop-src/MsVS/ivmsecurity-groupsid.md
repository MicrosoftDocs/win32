---
title: IVMSecurity GroupSid property
description: The GroupSid property contains the SID string of the group.
ms.assetid: '0a483da0-542f-41db-ac2c-0cc1d8c0e29a'
keywords: ["GroupSid property Virtual Server", "GroupSid property Virtual Server , IVMSecurity interface", "IVMSecurity interface Virtual Server , GroupSid property", "GroupSid property Virtual Server , VMSecurity interface", "VMSecurity interface Virtual Server , GroupSid property"]
topic_type:
- apiref
api_name:
- IVMSecurity.GroupSid
- IVMSecurity.get_GroupSid
- IVMSecurity.put_GroupSid
- VMSecurity.GroupSid
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMSecurity::GroupSid property

The **GroupSid** property contains the SID string of the group.

This property is read/write.

## Syntax


```C++
HRESULT put_GroupSid(
  [in]  BSTR groupSid
);

HRESULT get_GroupSid(
  [out] BSTR *groupSid
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMSecurity.GroupSid( _
  ByRef groupSid, _
  ByVal groupSid _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The SID string of the group.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                  |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *groupSid* parameter was **NULL**.<br/>         |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *groupSid* parameter was invalid or empty.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred.<br/>                 |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSecurity**](ivmsecurity.md)
</dt> </dl>

 

 





