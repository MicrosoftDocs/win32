---
title: IVMSecurity OwnerSid property
description: The OwnerSid property contains the SID string of the owner.
ms.assetid: 9374b8f1-0fb3-4f06-9b0a-d0963f35310e
keywords:
- OwnerSid property Virtual Server
- OwnerSid property Virtual Server , IVMSecurity interface
- IVMSecurity interface Virtual Server , OwnerSid property
- OwnerSid property Virtual Server , VMSecurity interface
- VMSecurity interface Virtual Server , OwnerSid property
topic_type:
- apiref
api_name:
- IVMSecurity.OwnerSid
- IVMSecurity.get_OwnerSid
- IVMSecurity.put_OwnerSid
- VMSecurity.OwnerSid
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMSecurity::OwnerSid property

The **OwnerSid** property contains the SID string of the owner.

This property is read/write.

## Syntax


```C++
HRESULT put_OwnerSid(
  [in]  BSTR inOwnerSid
);

HRESULT get_OwnerSid(
  [out] BSTR *outOwnerSid
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
<td><pre><code>VMSecurity.OwnerSid( _
  ByRef outOwnerSid, _
  ByVal inOwnerSid _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The SID string of the owner.

This property value is read/write.

## Error codes



| Name                                                                                           | Meaning                                                                                           |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>              | The operation was successful.<br/>                                                          |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *outOwnerSid* parameter was **NULL**.<br/>                                              |
| <dl> <dt>E\_INVALIDARG</dt> </dl>       | The *inOwnerSid* parameter was invalid or empty.<br/>                                       |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred. Other **HRESULT** error values may be returned as well.<br/> |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSecurity**](ivmsecurity.md)
</dt> </dl>

 

 





