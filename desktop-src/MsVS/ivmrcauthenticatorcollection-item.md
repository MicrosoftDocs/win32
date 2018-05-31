---
title: IVMRCAuthenticatorCollection Item property
description: The Item property contains the IVMRCAuthenticator object that corresponds to the given index in this collection.
ms.assetid: f725a966-08ce-4ef7-acd0-3cc73d90f709
keywords:
- Item property Virtual Server
- Item property Virtual Server , IVMRCAuthenticatorCollection interface
- IVMRCAuthenticatorCollection interface Virtual Server , Item property
- Item property Virtual Server , VMRCAuthenticatorCollection interface
- VMRCAuthenticatorCollection interface Virtual Server , Item property
topic_type:
- apiref
api_name:
- IVMRCAuthenticatorCollection.Item
- IVMRCAuthenticatorCollection.get_Item
- VMRCAuthenticatorCollection.Item
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

# IVMRCAuthenticatorCollection::Item property

The **Item** property contains the [**IVMRCAuthenticator**](ivmrcauthenticator.md) object that corresponds to the given index in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long               index,
        long               index,
  [out] IVMRCAuthenticator **authenticator
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
<td><pre><code>VMRCAuthenticatorCollection.Item( _
  ByVal index, _
  ByVal index, _
  ByRef authenticator _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains the [**VMRCAuthenticator**](ivmrcauthenticator.md) object at the given index.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                      |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *authenticator* parameter is **NULL**.<br/>                                         |
| <dl> <dt>DISP\_E\_BADINDEX</dt> </dl>  | The index of the requested item does not correspond to an item in this collection.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                                                      |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMRCAuthenticatorCollection**](ivmrcauthenticatorcollection.md)
</dt> </dl>

 

 





