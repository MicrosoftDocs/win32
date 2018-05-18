---
title: IMsgrUsers interface
description: Do not use.
ms.assetid: 'e5958281-d81b-41aa-b209-7445ba983a5c'
keywords: ["IMsgrUsers interface Windows Messenger", "IMsgrUsers interface Windows Messenger , described"]
topic_type:
- apiref
api_name:
- IMsgrUsers
api_location:
- Msmsgs.exe
api_type:
- COM
---

# IMsgrUsers interface

\[**IMsgrUsers** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **IMsgrUsers** interface provides methods and properties to handle the **Messenger User** object.

> [!Note]  
> The **IMsgrUsers** interface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**IMessengerContacts**](im-imessengercontacts.md) instead.

 

## Members

The **IMsgrUsers** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMsgrUsers** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMsgrUsers** interface has these methods.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Method</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>Add</strong>](im-imsgrusers-add.md)</td>
<td style="text-align: left;">Adds a <strong>MessengerUser</strong> object to a collection. <br/>
<blockquote>
[!Note]<br />
The [<strong>Add</strong>](im-imsgrusers-add.md) method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>Item</strong>](im-imsgrusers-item.md)</td>
<td style="text-align: left;">Retrieves a specific <strong>MessengerUser</strong> object by numeric index. <br/>
<blockquote>
[!Note]<br />
The [<strong>Item</strong>](im-imsgrusers-item.md) method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>Item</strong>](im-imessengercontacts-item.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Remove</strong>](im-imsgrusers-remove.md)</td>
<td style="text-align: left;">Removes a [<strong>MsgrObject</strong>](im-msgrobject.md) object from a collection. <br/>
<blockquote>
[!Note]<br />
The [<strong>Remove</strong>](im-imsgrusers-remove.md) method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>Remove</strong>](im-imessengercontacts-remove.md) instead.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **IMsgrUsers** interface has these properties.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Access type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>Count</strong>](im-imsgrusers-count.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Retrieves the number of <strong>MessengerUser</strong> objects in the collection. <br/>
<blockquote>
[!Note]<br />
The [<strong>Count</strong>](im-imsgrusers-count.md) property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>Count</strong>](im-imessengercontacts-count.md) instead.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Mdisp.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>Mdisp.idl</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Msmsgs.exe</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](c1accca9-971c-4435-8a5e-e25404a3fb25)
</dt> <dt>

[**IMsgrUsers**](im-imsgrusers.md)
</dt> </dl>

 

 





