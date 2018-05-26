---
title: IMessengerServices Count property
description: Retrieves the number of MessengerServices objects in the collection.
ms.assetid: 1f57bd67-ac66-45d2-a77c-540d4f877995
keywords:
- Count property Windows Messenger
- Count property Windows Messenger , IMessengerServices interface
- IMessengerServices interface Windows Messenger , Count property
topic_type:
- apiref
api_name:
- IMessengerServices.Count
- IMessengerServices.get_Count
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMessengerServices::Count property

\[**Count** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the number of [**MessengerServices**](im-messengerservices.md) objects in the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out, retval] LONG *pcServices
);
```



## Property value

Pointer to a **LONG** that provides the number of [**MessengerServices**](im-messengerservices.md) objects in the collection.

## Error codes

Returns one of the following values. 



| Name                                                                                                  | Meaning                                        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                           |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pcServices* is a **NULL** pointer.<br/> |



## Remarks

This property does not return any error codes.

If there are no active [**MessengerServices**](im-messengerservices.md) objects, *pcServices* will return zero.

If this method is called while the client is offline, the method call will not fail.

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrServices As MessengerAPI.IMessengerServices

Private Sub btnServicesCount_Click()
    On Error Resume Next
    MsgBox("Services Count= " & CStr(MsgrServices.Count))
    ErrorTrap ("MsgrServices.Count")    'Error handling routine
End Sub
```



## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessengerServices**](im-imessengerservices.md)
</dt> <dt>

[**Item**](im-imessengerservices-item.md)
</dt> </dl>

 

 





