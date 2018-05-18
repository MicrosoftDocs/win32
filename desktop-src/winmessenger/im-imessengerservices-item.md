---
title: IMessengerServices Item method
description: Retrieves a specific service by index.
ms.assetid: '5743e9f3-a01f-4897-9f55-4856f50cc828'
keywords: ["Item method Windows Messenger", "Item method Windows Messenger , IMessengerServices interface", "IMessengerServices interface Windows Messenger , Item method"]
topic_type:
- apiref
api_name:
- IMessengerServices.Item
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerServices::Item method

\[**Item** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a specific service by index.

## Syntax


```C++
HRESULT Item(
  [in]          LONG      Index,
  [out, retval] IDispatch **ppService
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **LONG**

**LONG** that specifies the index of the desired [**MessengerServices**](im-messengerservices.md) object in the collection.

</dd> <dt>

*ppService* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

Address of a pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerServices**](im-messengerservices.md) object requested with *Index*. The object can now be accessed through the [**IMessengerServices**](im-imessengerservices.md) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values. 



| Return code                                                                                               | Description                                                                                  |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Success. <br/>                                                                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>                    | Invalid collection or index number provided exceeds the length of the collection.<br/> |
| <dl> <dt>**RPC\_X\_NULL\_REF\_POINTER**</dt> </dl> | *ppService* is a **NULL** pointer.<br/>                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>              | *Index* is not a positive integer.<br/>                                                |



 

## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                            |
|------------|------------------------------------------------------------------------------------|
| 0x80004005 | Invalid collection, or index number provided exceeds the length of the collection. |
| 0x80070057 | *Index* is not a positive integer.                                                 |



 

If you know the name for that specific service, you can get the [**MessengerServices**](im-messengerservices.md) object by creating an object for it explicitly by calling [**ServiceName**](im-imessengerservice-servicename.md). Even if that service is already present in a list, the same pointer is returned (as it would have been by retrieving that object from an existing collection).

> [!Note]  
> This method is available for scripting languages.

 

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
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





