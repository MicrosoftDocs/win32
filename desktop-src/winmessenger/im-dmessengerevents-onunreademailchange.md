---
title: DMessengerEvents OnUnreadEmailChange event
description: Indicates the number of unread e-mail messages in the Messenger client's correlated Outlook.com Inbox that have changed from the last count of previous OnUnreadEmailChange events or initial sign-in.
ms.assetid: 'f0e5e448-c635-4523-be6a-b0f526e6eb42'
keywords: ["OnUnreadEmailChange event Windows Messenger", "OnUnreadEmailChange event Windows Messenger , DMessengerEvents interface", "DMessengerEvents interface Windows Messenger , OnUnreadEmailChange event"]
topic_type:
- apiref
api_name:
- DMessengerEvents.OnUnreadEmailChange
api_location:
- Msgsc.dll
api_type:
- COM
---

# DMessengerEvents::OnUnreadEmailChange event

\[**OnUnreadEmailChange** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates the number of unread e-mail messages in the Messenger client's correlated Outlook.com Inbox that have changed from the last count of previous **OnUnreadEmailChange** events or initial sign-in.

## Syntax


```C++
void OnUnreadEmailChange(
  [in] MUAFOLDER    mFolder,
  [in] LONG         cUnreadEmail,
  [in] VARIANT_BOOL *pBoolfEnableDefault
);
```



## Parameters

<dl> <dt>*mFolder* \[in\]</dt> <dd> 

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>C++</strong></td>
<td>A value of the [<strong>MUAFOLDER</strong>](im-muafolder.md) enumeration. Allowed values are: 
<table>
<thead>
<tr class="header">
<th>Constant</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MUADFOLDER_INBOX</td>
<td>0</td>
<td>Unread mail count has changed in the Inbox.</td>
</tr>
<tr class="even">
<td>MUADFOLDER_ALL_OTHER_FOLDERS</td>
<td>1</td>
<td>Not currently implemented. Do not use.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td><strong>VB</strong></td>
<td>A value of the [<strong>MUAFOLDER</strong>](im-muafolder.md) enumeration.</td>
</tr>
</tbody>
</table>

 </dd> <dt>

*cUnreadEmail* \[in\]
</dt> <dd>

A **LONG** that contains the new number of unread e-mail messages in the Outlook.com Inbox.

</dd> <dt>*pBoolfEnableDefault* \[in\]</dt> <dd> 

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>C++</strong></td>
<td>A pointer to a <strong>VARIANT_BOOL</strong> (equivalent to a <strong>VARIANT</strong>) of type <strong>VT_BOOL</strong> that is used to specify whether new e-mail alerts should suppress the e-mail pop-up message in the Messenger client UI. Suppressing the e-mail pop-up message is useful if a client displays its own UI when new e-mail arrives.<br/>
<blockquote>
[!Note]<br />
Reserved. In the current implementation, the e-mail pop-up message cannot be suppressed.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><strong>VB</strong></td>
<td>A <strong>BOOL</strong> that is used to specify whether new e-mail alerts should suppress the e-mail pop-up message in the Messenger client UI. Suppressing the e-mail pop-up message is useful if a client displays its own UI when new e-mail arrives.
<blockquote>
[!Note]<br />
Reserved. In the current implementation, the e-mail pop-up message cannot be suppressed.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>

 </dd> </dl>

## Return value

This event does not return a value.

## Remarks

The **OnUnreadEmailChange** event is scriptable.

To use this event in Windows Messenger, you must install an add-in component that supports e-mail integration.

In most cases, this mail count mechanism applies only to the Outlook.com Inbox and therefore only to users signed in with Microsoft Outlook.com accounts or equivalent Outlook.com test domain accounts.

On the Microsoft Exchange Instant Messaging Service (IM) client, **OnUnreadEmailChange** indicates the changed unread e-mail count on the Exchange Inbox of the associated account.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter           | vaArgs\[x\] | Variant Type |
|---------------------|-------------|--------------|
| pBoolfEnableDefault | 0           | VT\_BOOL     |
| cUnreadEmail        | 1           | VT\_14       |
| mFolder             | 2           | VT\_I4       |



 

> [!Note]  
> This event is available for scripting languages.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.5<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**DMessengerEvents**](im-dmessengerevents.md)
</dt> <dt>

[**OpenInbox**](im-imessenger-openinbox.md)
</dt> <dt>

[**UnreadEmailCount**](im-imessenger-unreademailcount.md)
</dt> </dl>

 

 





